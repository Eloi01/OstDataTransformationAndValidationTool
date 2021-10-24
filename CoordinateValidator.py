import re
from Log import Log


class CoordinateContext:
    """Applied Strategy-Pattern for Coordinate-Validation."""

    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, input_item, configuration_item, log):
        return self.strategy(input_item, configuration_item, log)


class LongitudeStrategy:
    """Defines the Strategy for Longitude-Validation.
       Firstly evaluates if a coordinate can be extracted.
       Secondly validates the extracted coordinate.
    """

    def __call__(self, input_item, configuration_item, log):
        attribute = getattr(input_item, configuration_item.name)
        if extract_geo_coordinates(attribute) is not None:
            this_longitude = extract_geo_coordinates(attribute)
            if validate_longitude(this_longitude):
                setattr(input_item, configuration_item.name, this_longitude)
                Log.generate_log_entry_by_change(log, configuration_item, attribute, this_longitude)
                return True
            else:
                # Generates Log Entry by failed validation
                log.list_of_log_entries.append(f"\t * Provided {configuration_item.name} is not a valid Longitude. \n")
                Log.generate_log_entry_by_failure(log, configuration_item, attribute)
                return False
        else:
            # Generates Log-Entry if no Latitude can be extracted
            log.list_of_log_entries.append(f"\t * Provided {configuration_item.name} could not be extracted. \n")
            Log.generate_log_entry_by_failure(log, configuration_item, attribute)
            return False


class LatitudeStrategy:
    """Defines the Strategy for Latitude-Validation.
       Firstly evaluates if a coordinate can be extracted.
       Secondly validates the extracted coordinate.
    """

    def __call__(self, input_item, configuration_item, log):
        attribute = getattr(input_item, configuration_item.name)
        if extract_geo_coordinates(attribute) is not None:
            this_latitude = extract_geo_coordinates(attribute)
            if validate_latitude(this_latitude):
                setattr(input_item, configuration_item.name, this_latitude)
                Log.generate_log_entry_by_change(log, configuration_item, attribute, this_latitude)
                return True
            else:
                # Generates Log Entry by failed validation
                log.list_of_log_entries.append(f"\t * Provided {configuration_item.name} could not be extracted. \n")
                Log.generate_log_entry_by_failure(log, configuration_item, attribute)
                return False
        else:
            # Generates Log-Entry if no latitude can be extracted
            log.list_of_log_entries.append(f"\t * Provided {configuration_item.name} could not be extracted. \n")
            Log.generate_log_entry_by_failure(log, configuration_item, attribute)
            return False


class PointStrategy:
    """Defines the Strategy for Point-Validation."""
    def __call__(self, input_item, configuration_item, log):
        attribute = getattr(input_item, configuration_item.name)
        if validate_point(attribute):
            this_point = extract_geo_point(attribute)
            setattr(input_item, configuration_item.name, this_point)
            Log.generate_log_entry_by_change(log, configuration_item, attribute, this_point)
            return True
        else:
            # Generates a Log-Entry if given Point can not be validated.
            log.list_of_log_entries.append(f"\t * Provided {configuration_item.name} is not a Point.\n")
            Log.generate_log_entry_by_failure(log, configuration_item, attribute)
            return False


class BoxStrategy:
    """Defines the Strategy for Box-Validation."""

    def __call__(self, input_item, configuration_item, log):
        attribute = getattr(input_item, configuration_item.name)
        if extract_geo_point(attribute):
            point_list = extract_geo_point(attribute)
            setattr(input_item, configuration_item.name, point_list)
            Log.generate_log_entry_by_change(log, configuration_item, attribute, point_list)
            return True
        else:
            # Generates a Log-Entry if given Box can not be validated.
            log.list_of_log_entries.append(f"\t * Provided {configuration_item.name} is not a valid Box.\n")
            Log.generate_log_entry_by_failure(log, configuration_item, attribute)
            return False


class PolygonStrategy:
    """Strategy Pattern used when the other Strategies dont aply."""
    def __call__(self, input_item, configuration_item, log):
        attribute = getattr(input_item, configuration_item.name)
        if extract_polygon(attribute):
            this_coordinates = extract_polygon(attribute)
            setattr(input_item, configuration_item.name, this_coordinates)
            Log.generate_log_entry_by_change(log, configuration_item, attribute, this_coordinates)
            return True
        else:
            log.list_of_log_entries.append(
                f"\t * Provided {configuration_item.name} does not contain valid Coordinates.\n")
            Log.generate_log_entry_by_failure(log, configuration_item, attribute)
            return False


def extract_geo_coordinates(string: str) -> [str]:
    """Extracts Geo-Coordinates from a provided String.

    :parameter string: String which shall be investigated.
    :returns: List of Matches (String) which could be extracted."""
    # It's not the best way to extract a GeoCoordinate
    # Does not cut invalid Formats like '-12.'or'12.222.222'
    pattern = r"(-?\d{1,3}(\.\d+)?)+"
    if re.search(pattern, string):
        coordinate_list = re.search(pattern, string)
        return coordinate_list.group()
    else:
        return False


def validate_longitude(string: str) -> bool:
    """Validation for longitude. Checks if a given value is inside in a permitted interval ((-)90-90).

    :parameter string: String which shall be investigated.
    :returns: True - if provided String is in permitted interval. False - if not."""

    longitude = float(string)
    if -90 <= longitude <= 90:
        return True
    else:
        return False


def validate_latitude(string: str) -> bool:
    """Validation for latitude. Checks if a given value is inside in a permitted interval ((-)180-180).

    :parameter string: String which shall be investigated.
    :returns: True - if provided String is in permitted interval. False - if not."""

    latitude = float(string)
    if -180 <= latitude <= 180:
        return True
    else:
        return False


def validate_point(point: str) -> bool:
    """Validates a given Point by its formal structure.
    Validates is a given String contains elements which can be identified as a Point.
    Assumes a Point is provided in the format (Coordinate, Coordinate).

    :parameter point: String which shall be validated.
    :return: True - if provided String is a valid point. False - if not."""

    if extract_geo_point(point):
        list_of_points_tmp = point.split(",")
        list_of_points = []
        for point in list_of_points_tmp:
            list_of_points.append(extract_geo_coordinates(point))
        if len(list_of_points) == 2:
            return True
        else:
            return False


def extract_geo_point(point: str) -> [str]:
    """Extracts the containing points in a provided String.
    Assumes the provided Point is in the format of (Coordinate, Coordinate).

    :parameter point: String which shall be investigated.
    :returns: List of Matches (Strings) which could be extracted. If no Point could be extracted returns false."""

    list_of_points_tmp = point.split(",")
    list_of_points = []
    for point in list_of_points_tmp:
        list_of_points.append(extract_geo_coordinates(point))
    if len(list_of_points) == 0 or (len(list_of_points) % 2) != 0:
        return False
    else:
        return list_of_points


def extract_polygon(point: str) -> [str]:
    """Extracts the containing polygon in a provided String.
    Assumes the provided Polygon is in the format of (Coordinate, Coordinate,...).

    :parameter point: String which shall be investigated.
    :returns: List of Matches (Strings) which could be extracted. If no Polygon could be extracted returns false."""
    list_of_coordinates_tmp = point.split(",")
    list_of_points_tmp = []
    list_of_points = []
    # extracts coordinates
    for point_tmp in list_of_coordinates_tmp:
        list_of_points.append(extract_geo_coordinates(point_tmp))
    # extracts points
    for point in list_of_points_tmp:
        list_of_points.append(extract_geo_point(point))
    length_of_list = len(list_of_points)
    if length_of_list == 0 or (list_of_points[0] != list_of_points[length_of_list-2] and
                               list_of_points[1] != list_of_points[length_of_list-1]):
        return False
    else:
        return list_of_points
