import re
from Log import Log


class LODContext:
    """Applied Strategy-Pattern. Defines the Context for the LOD-Validation"""

    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, input_item, configuration_item, log):
        return self.strategy(input_item, configuration_item, log)


class GNDStrategy:
    """Defines the Strategy for GND-Validation"""

    def __call__(self, input_item, configuration_item, log):
        lod = getattr(input_item, configuration_item.name)
        if extract_gnd_link(lod):
            extracted_lod = extract_gnd_link(lod)
            Log.generate_log_entry_by_change(log, configuration_item, lod, extracted_lod)
            return extracted_lod
        else:
            pass


class VIAFStrategy:
    """Defines the Strategy for VIAF-Validation"""

    def __call__(self, input_item, configuration_item, log):
        lod = getattr(input_item, configuration_item.name)
        if extract_viaf_link(lod):
            extracted_lod = extract_viaf_link(lod)
            Log.generate_log_entry_by_change(log, configuration_item, lod, extracted_lod)
            return extracted_lod
        else:
            pass


class RORStrategy:
    """Defines the Strategy for ROR-Validation"""

    def __call__(self, input_item, configuration_item, log):
        lod = getattr(input_item, configuration_item.name)
        if extract_ror_link(lod):
            extracted_lod = extract_ror_link(lod)
            Log.generate_log_entry_by_change(log, configuration_item, lod, extracted_lod)
            return extracted_lod
        else:
            pass


class OrcidStrategy:
    """Defines the Strategy for Orcid-Validation"""

    def __call__(self, input_item, configuration_item, log):
        lod = getattr(input_item, configuration_item.name)
        if extract_orcid_link(lod):
            extracted_lod = extract_orcid_link(lod)
            Log.generate_log_entry_by_change(log, configuration_item, lod, extracted_lod)
            return extracted_lod
        else:
            pass


class AllLodStrategy:
    def __call__(self, input_item, configuration_item, log):
        lod = getattr(input_item, configuration_item.name)
        if check_contains_lod(lod):
            extracted_lod = extract_lod(lod)
            setattr(input_item, configuration_item.name, extracted_lod)
            Log.generate_log_entry_by_change(log, configuration_item, lod, extracted_lod)
            return True
        else:
            return False


def extract_gnd_link(string: str) -> [str]:
    """Extracts the GND-Substrings of a given String and returns the matches as a List."""

    string_result_list = re.findall(r"http[s]?://d-nb\.info/gnd/\d+-{0,1}\d*\b", string)
    return string_result_list


def extract_viaf_link(string: str) -> [str]:
    """Extracts the VIAF-Substrings of a given String and returns the matches as a List."""

    string_result_list = re.findall(r"http[s]?://viaf\.org/viaf/[\d]+\b", string)
    return string_result_list


# a valid orcid id contains 4x4 digits separated by a '-' Last Character is allowed to be numeral or a 'X'
def extract_orcid_link(string: str) -> [str]:
    """Extracts the Orcid-Substrings of a given String and returns the matches as a List."""

    string_result = re.match(r"(http[s]?://orcid\.org/(\d{4}-){3}(\d{3}){1}[\d|X]{1}\b)+", string)
    # if regex does not match string result is None. In that chase there is the following workaround.
    if string_result is None:
        empty_list = []
        return empty_list
    string_result_list = [string_result.group()]
    return string_result_list


def extract_ror_link(string: str) -> [str]:
    """Extracts the ROR-Substrings of a given String and returns the matches as a List."""

    string_result = re.findall(r"http[s]?://ror\.org/0[^ILO]{6}\d{2}\b", string)
    return string_result


def check_contains_lod(string: str) -> bool:
    """Checks if a given String contains"""
    if extract_gnd_link(string) or extract_viaf_link(string) or extract_viaf_link(string) or extract_ror_link(string):
        return True


def extract_lod(string: str) -> [str]:
    """Extracts any contained LOD in a given String and returns them in a list"""
    lod_list = []
    for item in extract_gnd_link(string):
        lod_list.append(item)
    for item in extract_viaf_link(string):
        lod_list.append(item)
    for item in extract_orcid_link(string):
        lod_list.append(item)
    for item in extract_ror_link(string):
        lod_list.append(item)
    return lod_list


