from Log import Log


def check_for_maximum_word_count(log, configuration_item, attribute: str, word_count: int):
    if count_words_in_string(attribute) <= int(word_count):
        return True
    else:
        log.list_of_log_entries.append(f"\t * Provided {configuration_item.name} is too long.\n")
        Log.generate_log_entry_by_failure(log, configuration_item, attribute)
        return False


# strip removes whitespace at the beginning and the end of a string
def count_words_in_string(string: str) -> int:
    # Corner-case - otherwise will return 1 for some reason
    if string == "":
        return 0
    return len(string.strip().split(" "))
