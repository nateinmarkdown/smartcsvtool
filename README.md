
# SmartCSVTool

A python package for working with CSV files.

## Installation

```phyton
pip install smartcsvtool
```

## Usage

### Reading CSV files

```phyton
import smartcsvtool
data = smartcsvtool.read_csv('example.csv')
```

The `read_csv()` function reads a CSV file and returns a list of dictionaries, where each dictionary represents a row in the CSV file.

### Reading CSV files as list

```phyton
import smartcsvtool
data = smartcsvtool.read_csv_as_list('example.csv')
```

The `read_csv_as_list()` function reads a CSV file and returns a list of lists, where each list represents a row in the CSV file.

### Removing duplicates

```phyton
import smartcsvtool
data = smartcsvtool.read_csv('example.csv')
no_duplicates = smartcsvtool.remove_duplicates(data, 'id')
```

The `remove_duplicates()` function takes a list of dictionaries and removes any duplicates based on a specified key.

### Filtering data

```phyton
import smartcsvtool
data = smartcsvtool.read_csv('example.csv')
filtered_data = smartcsvtool.filter_data(data, 'age', 25)
```

The `filter_data()` function filters a list of dictionaries based on a specified key-value pair.

### Sorting data

```phyton
import smartcsvtool
data = smartcsvtool.read_csv('example.csv')
sorted_data = smartcsvtool.sort_data(data, 'name')
```

The `sort_data()` function sorts a list of dictionaries based on a specified key.
