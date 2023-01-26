import json

def to_json(data):
    """
    Convert a list of dictionaries to a JSON string.

    :param data: List of dictionaries to convert.
    :return: JSON string representation of the data.
    """
    json_string = json.dumps(data)
    return json_string

def to_dict(data):
    """
    Convert a list of lists to a dictionary.

    :param data: List of lists to convert.
    :return: Dictionary representation of the data.
    """
    keys = data[0]
    dict_data = [dict(zip(keys, row)) for row in data[1:]]
    return dict_data
