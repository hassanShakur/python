# Python

## Intros

### List Comprehension

Making a new lists out of python `sequences` like list, string, tuple & range, without loops.

```py
# New list where each item is increased by 3
old_list = [1, 2, 3]
new_list = [old_val + 3 for old_val in old_list]
```

The comprehension can be conditional, i.e only if a test is passed. Just add an if statement at the end.

```py
new = [x for x in old if x === 'test']
```

### Dictionary comprehension

The resulting structure is a `dictionary`.

```py
# From a sequence eg list
new_dict = {my_key: my_value for x in iterableSequence}

# From another dict
new_dict = {my_key: my_value for (key, val) in old_dict.items()}

# Adding a condition
new_dict = {my_key: my_value for (key, val) in old_dict.items() if val > 3}
```

### Unlimited Positional Args

```py
def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


add(1,2,3)
```

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

## Turtle

```py
# Load image - only supports gifs
import turtle

screen = turtle.Screen()

img = 'path_to_image.gif'
screen.addshape(img)
turtle.shape(img)

# Click on screen but do not exit
turtle.mainloop()
```

```py
# Prompt for input
screen.textinput(title='title', prompt='prompt')
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
dict = {
    "Name": ["Hs", "Hn", "Gl"],
    "age": [1, 2, 3]
}

df = pandas.DataFrame(dict)

# df to csv and save in a file
df.to_csv('file_to_save_to.csv')

```

You can also loop through each row in a `df` using `iterrow()`:

```py
import pandas

df = pandas.DataFrame('some.csv')

for (index, row) in df.iterrows():
    print(row)
```

## Tkinter

Basic window:

```py
import tkinter

window = tkinter.Tk()
window.title('Tk Basics')
window.minsize(width=300, height=200)

window.mainloop()
```
