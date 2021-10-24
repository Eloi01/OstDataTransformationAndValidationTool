from dataclasses import dataclass


@dataclass
class Log:
    def __init__(self):
        """Represents the Log for one single element."""
        self.file_id: str = "null"
        self.list_of_log_entries: [str] = []
        self.object_title: str = "null"
        self.passed: bool = False

    def generate_log_entry_by_alt_configuration_label(self, field_name: str, configuration_name: str):
        self.list_of_log_entries.append(
            f"\t * Changed the elements field name from:\n"
            f"\t   {field_name} to {configuration_name}.\n\n")

    def generate_log_entry_by_failure(self, configuration_item, provided_element):
        self.list_of_log_entries.append(f"\t  * Failed Validation for Schema-Element : {configuration_item.name}\n"
                                        f"\t    Provided: {provided_element}\n"
                                        f"\t    The Specification for Schema ID {configuration_item.id} is: \n"
                                        f"\t    {configuration_item.note}\n\n")

    def generate_log_entry_by_change(self, configuration_item, old_version, new_version):
        """Checks prior to creating the according log entry, if the string representation of both versions is the
        same This is used to avoid Log-Entry's which document type-changes in data, which will be not present in the
        final file """
        if str(old_version) == str(new_version):
            pass
        else:
            self.list_of_log_entries.append(
                f"\t * Schema ID: {configuration_item.id}  {configuration_item.name}-Element has been changed from\n"
                f"\t  \"{old_version}\" to \"{new_version}\"\n\n")

    def generate_log_entry_by_standardization_change(self, element_name, old_version, new_version):
        self.list_of_log_entries.append(f"\t * Changed {element_name}\n"
                                        f"\t   from {old_version} to {new_version}\n\n")

    def generate_log_entry_by_missing_required_field(self, configuration_item):
        self.list_of_log_entries.append(f"\t * {configuration_item.name}: This required Item is not set!\n"
                                        f"\t   The whole Item will therefore not be transformed.\n"
                                        f"\t   Schema-Specification for {configuration_item.id}. {configuration_item.name} is:\n"
                                        f"\t   {configuration_item.note}\n\n")

    def generate_log_entry_by_missing_related_required_field(self, configuration_item):
        self.list_of_log_entries.append(f"\t * Missing related field {configuration_item.required_element}!\n"
                                        f"\t  When {configuration_item.name} is set, {configuration_item.required_element} has also to be set.\n"
                                        f"\t  The whole Item will therefore not be transformed.\n"
                                        f"\t  Schema-Specification for {configuration_item.id}. {configuration_item.name} is:\n"
                                        f"\t  {configuration_item.note}\n\n")

    def generate_log_entry_for_not_matched_fields_from_input(self, element_list):
        self.list_of_log_entries.append("\t * Following Fields from Input could not be matched:\n"
                                        f"\t   {element_list}\n\n")

    def generate_log_entry_by_start_of_validation(self):
        self.list_of_log_entries.append("\t ------------------------------------\n"
                                        + "\t Start of Validation\n"
                                        + "\t ------------------------------------\n\n")

    def generate_log_entry_by_start_of_standardization(self):
        self.list_of_log_entries.append("\t ------------------------------------\n"
                                        + "\t Start of Standardization\n"
                                        + "\t ------------------------------------\n\n")

    def generate_log_entry_by_start_of_transformation(self):
        self.list_of_log_entries.append("\t ------------------------------------\n"
                                        + "\t Start of Transformation\n"
                                        + "\t ------------------------------------\n\n")

    def generate_log_entry_by_check_of_required_elements(self):
        self.list_of_log_entries.append("\t ------------------------------------\n"
                                        + "\t Start of Check of required Elements\n"
                                        + "\t ------------------------------------\n\n")

    def generate_log_entry_for_successful_validation(self):
        self.list_of_log_entries.append("\t ++++++++++++++++++++++++\n"
                                        "\t +Validation successful!+\n"
                                        "\t ++++++++++++++++++++++++\n\n")

    def generate_log_entry_for_failed_validation(self):
        self.list_of_log_entries.append("\t ++++++++++++++++++++\n"
                                        "\t +Validation failed!+\n"
                                        "\t ++++++++++++++++++++\n\n")

    def generate_log_entry_for_passing_required_elements_test(self):
        self.list_of_log_entries.append("\t All required Elements are given!\n\n")
