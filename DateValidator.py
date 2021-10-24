import re


def extract_date_format(string: str) -> [str]:
    """Extracts dates containing in a provided String.

    :parameter string: String which shall be investigated.
    :return List of Matches (String) which could be extracted from the provided String."""

    list_of_results = []
    # YYYY-MM-TT
    pattern1 = r"^\d{4}-d{2}-\d{2}$"
    # YYYY-MM
    pattern2 = r"^\d{4}-[0-1]\d$"
    # YYYY
    pattern3 = r"^\d{4}$"
    if re.findall(pattern1, string):
        result = re.findall(pattern1, string)
        return result[0]
    if re.findall(pattern2, string):
        result = re.findall(pattern2, string)
        return result[0]
    if re.findall(pattern3, string):
        result = re.findall(pattern3, string)
        return result[0]
    return False


def check_date_duration_format(string: str) -> [str]:
    """Extracts date in duration format, which are contained in a provided String.

    :parameter string: String which shall be investigated.
    :return List of Matches (String) which could be extracted from the provided String."""

    list_of_results = []
    # YYYY-MM-TT/YYYY-MM-TT
    pattern1 = r"^\d{4}-\d{2}-\d{2}/\d{4}-\d{2}-\d{2}$"
    # YYYY-MM/YYYY-MM
    pattern2 = r"^\d{4}-\d{2}/\d{4}-\d{2}$"
    # YYYY/YYYY
    pattern3 = r"^\d{4}/\d{4}$"
    if re.findall(pattern1, string):
        result = re.findall(pattern1, string)
        return result[0]
    if re.findall(pattern2, string):
        result = re.findall(pattern2, string)
        return result[0]
    if re.findall(pattern3, string):
        result = re.findall(pattern3, string)
        return result[0]
    return False



