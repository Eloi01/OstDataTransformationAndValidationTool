import FileWriter
import InputItem
import FileReader
import InputStandartization
import Log
import Validator


def start_tool(input_path, configuration_path, output_path, log_output_path, log_failed_items_path):
    """Coordinates the process of the Tool.

    :parameter input_path: path of the file of datasets which should be processed.
    :parameter configuration_path: path of the configuration file.
    :parameter output_path: path in which the result file shall be written.
    :parameter log_output_path: path in which the corresponding log file shall be written.
    :parameter log_failed_items_path: path in which the corresponding log file shall be written which only document failed datasets."""

    list_of_transformed_objects = []
    list_of_logs = []
    object_id = 0
    configuration_list = FileReader.read_configuration_file_to_configuration_object_list(configuration_path)
    input_list = FileReader.read_input(input_path)
    for input_dict in input_list:
        object_id = object_id + 1
        log = Log.Log()
        log.file_id = object_id
        if Validator.check_if_dict_is_empty(input_dict):
            InputStandartization.standardize_dict(input_dict, log)
            input_item = InputItem.create_input_item_from_input(input_dict, configuration_list, log)
            if Validator.validate_input_item(input_item, log, configuration_list) is False:
                list_of_logs.append(log)
                continue
            list_of_transformed_objects.append(input_item)
            list_of_logs.append(log)
    FileWriter.write_list_to_json(list_of_transformed_objects, output_path)
    FileWriter.write_log_list_to_file(list_of_logs, log_output_path, input_path, configuration_path,
                                      len(list_of_transformed_objects))
    FileWriter.write_log_of_failed_items(list_of_logs, log_failed_items_path)
