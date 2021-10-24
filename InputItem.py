from Log import Log
from dataclasses import dataclass


@dataclass
class InputItem:
    """Blank default class for the Input-Item. The Object will dynamicaly built by the create_input_item-Form_input- method"""
    def __init__(self):
        pass


def create_input_item_from_input(input_dict, configuration_list, log):
    """Creates a new InputItem according to the input dictionary and the configuration list.

    Searches in the given dictionary for the element names and compares them with the thesauri of the configuration-file.
    If it finds a fitting element in the thesauri, it sets its attributes to the element name of the item.

    :parameter input_dict: dictionary representation of a dataset.
    :parameter configuration_list: list of configuration objects.
    :parameter log: log-object in which any result will be documented.

    :returns: InputItem: the created Input-Item."""

    input_item = InputItem()
    list_of_field_names = list(input_dict.keys())
    Log.generate_log_entry_by_start_of_transformation(log)
    list_of_matched_field_names = []
    for field_name in list_of_field_names:
        for configuration in configuration_list:
            # if the field name from the input file is the same as the configuration name for a target schema field
            if field_name == configuration.name:
                setattr(input_item, configuration.name, input_dict[field_name])
                list_of_matched_field_names.append(field_name)
                continue
            # if the field name from the input file is the same as an altLabel from the target schema configuration element
            for thesaurus_alt in configuration.list_of_alt_labels:
                if field_name == thesaurus_alt:
                    setattr(input_item, configuration.name, input_dict[field_name])
                    list_of_matched_field_names.append(field_name)
                    Log.generate_log_entry_by_alt_configuration_label(log, field_name, configuration.name)

    # Compare the lists of input fields and matched field name and save the difference
    # difference are the field names which could not be matched
    list_of_not_matched_field_names = set(list_of_field_names) - set(list_of_matched_field_names)
    if len(list_of_not_matched_field_names) != 0:
        Log.generate_log_entry_for_not_matched_fields_from_input(log, list_of_not_matched_field_names)
    return input_item
