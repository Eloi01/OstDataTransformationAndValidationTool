import LODValidator
import CoordinateValidator
import DateValidator
import NormVocab
import InputItem
import WordCountValidation
from Log import Log
import Configuration

"""Couple of methods which are used in the general validation process."""


def check_for_string_type(log, configuration_item, element_name, attribute):
    if type(attribute) is str:
        return True
    else:
        log.list_of_log_entries.append(f"\t Provided Element {element_name} is not a String.\n")
        Log.generate_log_entry_by_failure(log, configuration_item, attribute)
        return False


def check_if_dict_is_empty(json_dict: dict) -> bool:
    check = bool(json_dict)
    return check


def check_validation_rules_from_configuration_fields(input_item, configuration_item, log):
    """Coordinates the validation process of an input-Item for one given configuration.

    Stores the result in a provided log.

    :parameter input_item: Input-Item which shall be validated.
    :parameter log: Log-Representation of the findings in the transformation and validation process.
    :parameter configuration_item: A single Configuration-Item by which it containes information will be applied
    the the Input-Item.
    :return: true - If Validation process was successful."""
    # stores the state of the validation
    has_failure = False
    contains_attribute = hasattr(input_item, configuration_item.name)

    # checks if the field is required and if the input file has such an attribute
    if configuration_item.required == "True" and contains_attribute is False:
        Log.generate_log_entry_by_missing_required_field(log, configuration_item)
        return False
    # cornerCase: Field is allowed to be empty String. If that matches no further validation is needed.
    if configuration_item.empty_string == "True" and contains_attribute is True and \
            len(getattr(input_item, configuration_item.name)) == 0:
        return True
    # if previous validation succeeds
    else:
        # if input-item does not contain attribute but it is also not required
        if contains_attribute is False:
            return True
        if check_related_required_element(input_item, configuration_item, log) is False:
            has_failure = True
        if check_word_count_validation(input_item, configuration_item, log) is False:
            has_failure = True
        if check_lod_validation(input_item, configuration_item, log) is False:
            has_failure = True
        if check_coordinates_validation(input_item, configuration_item, log) is False:
            has_failure = True
        if check_internal_normvocabulary_validation(input_item, configuration_item, log) is False:
            has_failure = True
        if check_external_normvocabulary_validation(input_item, configuration_item, log) is False:
            has_failure = True
        if check_date_validation(input_item, configuration_item, log) is False:
            has_failure = True
        # Check the result of the validation process
        if has_failure is True:
            return False
        return True


def check_word_count_validation(input_item, configuration_item, log):
    """Coordinates the word-count-validation."""
    word_count = configuration_item.wordcount
    if word_count != "null":
        attribute = getattr(input_item, configuration_item.name)
        return WordCountValidation.check_for_maximum_word_count(log, configuration_item, attribute, word_count)
    else:
        return True


def check_related_required_element(input_item, configuration_item, log):
    """Coordinates the related-required-element coordination."""
    related_required_element = configuration_item.required_element
    if related_required_element != "null":
        if hasattr(input_item, related_required_element) is False:
            Log.generate_log_entry_by_missing_related_required_field(log, configuration_item)
            return False
        else:
            return True
    return True


def check_lod_validation(input_item, configuration_item, log):
    """Extracts LOD-Links from Input-Item according to the set Option.
       Transforms the option to a list and checks every given option
       stores the results in a result list and returns it after every given option
       is evaluated."""
    configuration_lod = configuration_item.lod
    attribute = getattr(input_item, configuration_item.name)
    if configuration_lod == "null":
        return True
    else:
        lod_list = configuration_lod.lower().replace(" ", "").split(",")
        result_list = []
        for lod in lod_list:
            if lod == 'gnd':
                context = LODValidator.LODContext(LODValidator.GNDStrategy())
                if context.execute(input_item, configuration_item, log) is not None:
                    result_list.append(LODValidator.extract_gnd_link(attribute))
            if lod == 'viaf':
                context = LODValidator.LODContext(LODValidator.VIAFStrategy())
                if context.execute(input_item, configuration_item, log) is not None:
                    result_list.append(LODValidator.extract_viaf_link(attribute))
            if lod == 'orcid':
                context = LODValidator.LODContext(LODValidator.OrcidStrategy())
                if context.execute(input_item, configuration_item, log) is not None:
                    result_list.append(LODValidator.extract_orcid_link(attribute))
            if lod == 'ror':
                context = LODValidator.LODContext(LODValidator.RORStrategy())
                if context.execute(input_item, configuration_item, log) is not None:
                    result_list.append(LODValidator.extract_ror_link(attribute))
        if len(result_list) == 0:
            lod = getattr(input_item, configuration_item.name)
            log.list_of_log_entries.append(f"\t * Provided {configuration_item.name} could not be extracted. \n")
            Log.generate_log_entry_by_failure(log, configuration_item, lod)
            return False
        else:
            return setattr(input_item, configuration_item.name, result_list)


def check_coordinates_validation(input_item, configuration_item, log):
    thesaurus_coordinate = configuration_item.coordinate
    if thesaurus_coordinate == "null":
        return True
    else:
        if thesaurus_coordinate == "Longitude":
            context = CoordinateValidator.CoordinateContext(CoordinateValidator.LongitudeStrategy())
            return context.execute(input_item, configuration_item, log)

        if thesaurus_coordinate == "Latitude":
            context = CoordinateValidator.CoordinateContext(CoordinateValidator.LatitudeStrategy())
            return context.execute(input_item, configuration_item, log)

        if thesaurus_coordinate == "Polygon":
            context = CoordinateValidator.CoordinateContext(CoordinateValidator.PolygonStrategy())
            return context.execute(input_item, configuration_item, log)

        if thesaurus_coordinate == "Point":
            context = CoordinateValidator.CoordinateContext(CoordinateValidator.PointStrategy())
            return context.execute(input_item, configuration_item, log)

        if thesaurus_coordinate == "Box":
            context = CoordinateValidator.CoordinateContext(CoordinateValidator.BoxStrategy())
            return context.execute(input_item, configuration_item, log)
        else:
            return False


def check_internal_normvocabulary_validation(input_item, configuration_item, log):
    internal_normvocab = configuration_item.internal_norm_vocabulary
    if internal_normvocab == "null":
        return True
    else:
        input_attribute = getattr(input_item, configuration_item.name)
        input_attribute = input_attribute.lower()
        normvocab_list = internal_normvocab.lower().replace(" ", "").split(",")
        if input_attribute in normvocab_list:
            return True
        else:
            Log.generate_log_entry_by_failure(log, configuration_item, input_attribute)
            return False


def check_external_normvocabulary_validation(input_item, configuration_item, log):
    external_normvocab = configuration_item.external_norm_vocabulary
    if external_normvocab == "null":
        return True
    else:
        item_normvocab = getattr(input_item, configuration_item.name)
        normvocab_list = getattr(NormVocab, external_normvocab)
        if item_normvocab in normvocab_list:
            return True
        else:
            Log.generate_log_entry_by_failure(log, configuration_item, item_normvocab)
            return False


def check_date_validation(input_item, configuration_item, log):
    """Coordinates the date-validation-process."""

    if configuration_item.date == "null":
        return True
    else:
        if configuration_item.date == "Duration":
            if DateValidator.check_date_duration_format(getattr(input_item, configuration_item.name)):
                return True
            else:
                Log.generate_log_entry_by_failure(log, configuration_item, getattr(input_item, configuration_item.name))
                return False
        if configuration_item.date == "Date":
            if DateValidator.extract_date_format(getattr(input_item, configuration_item.name)):
                return True
            else:
                Log.generate_log_entry_by_failure(log, configuration_item, getattr(input_item, configuration_item.name))
                return False


def validate_input_item(input_item: InputItem.InputItem, log, configuration_list: [Configuration.Configuration]):
    """Coordinates the validation process of a given Input-Item by evoking the validation method for each single
       Configuration-Item which is contained in a separate given list of configuration items.
        Returns the result of the Validation process.

        :parameter input_item: item which shall be validated.
        :parameter log: Log-Representation of the findings in the transformation and validation process.
        :parameter configuration_list: List of all configuration Objects.

        :return: true - If Validation-process was successful. """

    # checks if any validation returns false
    # ensures that the whole item will be validated even if one validation returns false
    has_failure = False

    if hasattr(input_item, "Titel"):
        log.object_title = getattr(input_item, "Titel")
    else:
        log.object_title = log.file_id
    Log.generate_log_entry_by_start_of_validation(log)

    # Checks each configuration_item in configuration_list and validates according to the specified rules
    for configuration_item in configuration_list:
        if check_validation_rules_from_configuration_fields(input_item, configuration_item, log):
            continue
        else:
            has_failure = True
            continue

    if has_failure is True:
        Log.generate_log_entry_for_failed_validation(log)
        return False
    log.passed = True
    Log.generate_log_entry_for_successful_validation(log)
    return True
