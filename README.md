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

### Unlimited Keyword Args - `kwargs`

The keyword args provided creates a dictionary which can be looped through or access a specific arg.

```py
class Test:
    def __init__(self, **kwargs) -> None:
        self.tester = kwargs["tester"] # Might cause err if arg is not present
        self.name = kwargs.get("name") # If arg not specified, its = Null


test = Test(name="Test 1", tester="A")

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
window.config(padx=10, pady=10, bg='#fff')

window.mainloop()
```

### Tkinter Layout Managers

1. Pack => Arrangement in center by default, 1 over another. Use `side` to specify either `top`, `left`...

   ```py
    btn.pack()
   ```

2. Place => Requires coordinates: x & y for precise positioning.

   ```py
    btn.place(x=10, y=30)
   ```

3. Grid => Requires the `column` & `row` numbers to place an item relative to other placed items.

   ```py
    btn.grid(column=1, row=2)
   ```

## Here Comes JSON

```py
import json

# Read a json file
with open('my.json', 'r') as my_json:
    info = json.load(my_json)

my_dict = {
    'key': {
        'val1': 'Ans',
        'val2': 'Ans 2',
    }
}

# Write to a json file
with open('my.json', 'w') as my_json:
    # what & where
    json.dump(my_dict, my_json, indent=2)

# Update => Read, update, write
with open('my.json', 'r') as my_json:
    # Read
    info = json.load(my_json)
    # Update
    info.update(new_dict)

with open('my.json', 'w') as my_json:
    json.dump(info, my_json, indent=2)

```
