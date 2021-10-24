import re
from Log import Log


def check_for_empty_lists(input_element: str):
    """Checks a provided dataset-element if its empty.

     :parameter input_element: Element which shall be evaluated.

     :return: the modified element."""
    pattern = "(\\[\\])+"
    if re.match(input_element, pattern):
        input_element = "null"
        return input_element
    return input_element


def convert_to_string(input_element, element_name, log) -> str:
    """Converts a provided dataset-element in a string.

    :parameter input_element: element to be evaluated.
    :parameter element_name: name of the element.
    :parameter log: log-object in which the result will be documented.

    :returns: the input element in a string-type."""
    if type(input_element) is not str:
        Log.generate_log_entry_by_standardization_change(log, element_name, input_element, str(input_element))
        return str(input_element)
    else:
        return input_element


def check_for_incorrect_date_format(input_attribute: str, element_name, log):
    """Checks a given Element if it contains a wrong formatted date.
    If matched it transforms the date in a ISO conform format.

    Checks for the following patterns:
    YYYY:MM:DD
    YYYY:MM
    YYYYMMDD

    :parameter input_attribute: element which shall be evaluated.
    :parameter element_name: name of the element which shall be evaluated.
    :parameter log: log-object in which the results shall be documented if a transformation takes place.

    :returns: the evaluated and modified element"""
    # YYYY-MM-TT
    pattern1 = "\\d{4}:\\d{2}:\\d{2}"
    # YYYY-MM
    pattern2 = "\\d{4}:\\d{2}"
    # No seperation of Digits
    pattern3 = "(\\d{8}){1}"

    if re.match(pattern1, input_attribute):
        new_attribute = input_attribute.replace(":", "-")
        Log.generate_log_entry_by_standardization_change(log, element_name, input_attribute, new_attribute)
        return new_attribute
    if re.match(pattern2, input_attribute):
        new_attribute = input_attribute.replace(":", "-")
        Log.generate_log_entry_by_standardization_change(log, element_name, input_attribute, new_attribute)
        return new_attribute
    if re.match(pattern3, input_attribute):
        new_attribute = input_attribute[:4] + ":" + input_attribute[4:]
        new_attribute = new_attribute[:7] + ":" + new_attribute[7:]
        Log.generate_log_entry_by_standardization_change(log, element_name, input_attribute, new_attribute)
        return new_attribute
    return input_attribute


def standardize_input(input_element, element_name, log):
    """Coordinates the standardisation process for a single Input-Element"""
    input_element = convert_to_string(input_element, element_name, log)
    input_element = check_for_incorrect_date_format(input_element, element_name, log)

    return input_element


def standardize_dict(input_dict, log):
    """Coordinates the standardisation process for a dictionary.

    :parameter input_dict: dictionary which shall be standardised
    :parameter log: log-object in which the results of the standardisation shall be documented."""
    Log.generate_log_entry_by_start_of_standardization(log)
    for element in input_dict:
        standardized_input = standardize_input(input_dict[element], element, log)
        input_dict[element] = standardized_input
    return input_dict
