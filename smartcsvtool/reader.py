import csv

def read_csv(filename, delimiter=','):
    """
    Read data from a CSV file and return as a list of dictionaries.

    :param filename: Name of the file to read from.
    :param delimiter: Delimiter used in the file. Default is ','.
    :return: List of dictionaries representing the data in the file.
    """
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        data = [row for row in reader]
    return data

def read_csv_as_list(filename, delimiter=','):
    """
    Read data from a CSV file and return as a list of lists.

    :param filename: Name of the file to read from.
    :param delimiter: Delimiter used in the file. Default is ','.
    :return: List of lists representing the data in the file.
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter)
        data = [row for row in reader]
    return data
