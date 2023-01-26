import csv

def write_csv(data, filename, delimiter=','):
    """
    Write data to a CSV file.

    :param data: List of dictionaries to write to the file.
    :param filename: Name of the file to write to.
    :param delimiter: Delimiter to use in the file. Default is ','.
    """
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to {filename}")

def write_csv_from_list(data, filename, delimiter=','):
    """
    Write list of lists to a CSV file.

    :param data: List of lists to write to the file.
    :param filename: Name of the file to write to.
    :param delimiter: Delimiter to use in the file. Default is ','.
    """
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=delimiter)
        writer.writerows(data)
    print(f"Data written to {filename}")
