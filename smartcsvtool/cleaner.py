def remove_duplicates(data, key):
    """
    Remove duplicate rows from a list of dictionaries based on a specified key.

    :param data: List of dictionaries to remove duplicates from.
    :param key: Key to use for determining duplicates.
    :return: List of dictionaries with duplicates removed.
    """
    seen = set()
    no_duplicates = []
    for row in data:
        if row[key] not in seen:
            seen.add(row[key])
            no_duplicates.append(row)
    return no_duplicates

def filter_data(data, key, value):
    """
    Filter a list of dictionaries based on a specified key-value pair.

    :param data: List of dictionaries to filter.
    :param key: Key to use for filtering.
    :param value: Value to filter on.
    :return: List of dictionaries that match the specified key-value pair.
    """
    filtered_data = [row for row in data if row[key] == value]
    return filtered_data

def sort_data(data, key, reverse=False):
    """
    Sort a list of dictionaries by a specified key.

    :param data: List of dictionaries to sort.
    :param key: Key to use for sorting.
    :param reverse: Set to True to sort in descending order. Default is False.
    :return: List of dictionaries sorted by the specified key.
    """
    sorted_data = sorted(data, key=lambda k: k[key], reverse=reverse)
    return sorted_data

