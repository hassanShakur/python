# Python

## OOP Basics

```py
class House:
    # Constructor
    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location
        self.cars = 3

    def emptyMethod(self):
        pass


home = House("home", "China")
```

- Inheritance

  ```py
    class Mansion(House):
        def __init__(self) -> None:
            super().__init__()

  ```

- Overriding

  ```py
    class Mansion(House):
        def __init__(self) -> None:
            super().__init__()

        def some_method_override:
            super().some_method_override() # To execute what parent method does
            # Extra specialized implementation
            print('Other stuff')
  ```

## Files & Directories

You can read, write, append etc to a file with the syntax:

```py
# Read
with open(file='text.txt', mode='r') as file:
    content = file.read()
    print(content)

# Write
with open(file='text.txt', mode='w') as file:
    file.write('Some text')
```

`append` will have the mode `a`. To create a new file, use mode `w` and the file name should not be exixting in the target directory.

## Pandas

```py
import pandas

# Reading csvs
data = pandas.read_csv('path/to/csv') # DataFrame - Table like struct

# Access a column
col = data['columnName'] # Series - 1D col
# Or
col = data.columnName

# Accessing a row based on a filter value
row = data[data.colName == 'col_value_for_that_row']

# Create DataFrame from dictionary
df = pandas.DataFrame(dict)

# df to csv and save in a file
df.to_csv('file_to_save_to.csv')
```
