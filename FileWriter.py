import json


def write_list_to_json(list_of_object, output_path):
    """Writes the given list_of_object into an JSON-File.

    :parameter list_of_object: List of Objects which shall be written.
    :parameter output_path: path of the to be written file."""

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write("[")
        for output_object in list_of_object:
            json.dump(output_object.__dict__, output_file, ensure_ascii=False, indent=4, sort_keys=False)
            if list_of_object.index(output_object) <= len(list_of_object) - 2:
                output_file.write(",")
        output_file.write("]")


def write_log_list_to_file(list_of_logs, log_output_path, input_path, config_file_path, count_of_passed_objects):
    """Writes the Log-File, beginning with a disclaimer and subsequently the Log-Information for each processed Item.

    :parameter list_of_logs: List of Logs which shall be written.
    :parameter log_output_path: Path for the to be written Log-File.
    :parameter input_path: Path of File which contains the Datasets which are proceeded.
    :parameter config_file_path: Path of the used Configuration-File.
    :parameter count_of_passed_objects: Count of Elements which passed the transformation and validation Process."""

    with open(log_output_path, "w", encoding="utf-8") as log_output_file:
        log_output_file.write("This is the Log-File for the OstData transformation and validation tool\n"
                              "Transformation and Validation were proceeded according to the Configuration-File\n"
                              f"located at: {config_file_path}\n"
                              "The files are sequentially transformed in the order they are received\n"
                              "The ID marks the order in which the datasets are transformed, starting with 0\n"
                              "Empty objects will not be considered.\n"
                              f"This Log-File represents the findings for the File located at {input_path}.\n"
                              "++++++++++++++++++++++++++++++++++++++++++\n\n"
                              f"Total of objects investigated: {len(list_of_logs)}\n"
                              f"Total of objects passed:{count_of_passed_objects}\n\n"
                              f"++++++++++++++++++++++++++++++++++++++++++\n\n")
        for log in list_of_logs:
            log_output_file.write(f"ID: {log.file_id}\n"
                                  f"Titel: {log.object_title}\n"
                                  f"Passed: {log.passed}\n\n")
            for log_entry in log.list_of_log_entries:
                log_output_file.write(log_entry)


def write_log_of_failed_items(list_of_logs, output_path):
    """Writes a separate Log-File only containing items in which a Error occurred.

    :parameter list_of_logs: List of Logs which documented the transformation and validation process.
    :parameter output_path: Path in which the Log-File shall be written."""

    with open(output_path, "w", encoding="utf-8") as log_of_failed_items:
        log_of_failed_items.write("This Log lists all failed items from the transformation and validation process.\n")
        for log in list_of_logs:
            if not log.passed:
                log_of_failed_items.write(f"ID: {log.file_id}\n"
                                          f"Titel: {log.object_title}\n")
                for log_entry in log.list_of_log_entries:
                    log_of_failed_items.write(log_entry)
