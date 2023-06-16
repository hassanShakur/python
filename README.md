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
