try:
    # What to try to do
    file = open("some_file.txt")
    print("a" + 9)
except FileNotFoundError:
    # The todo didn't happen
    file = open("some_file.txt", mode="w")
    file.write("A simple poem...")
except TypeError as message:
    print(f"Error ❌: {message}")
else:
    # The todo happened
    info = file.read()
    print(info)
finally:
    # Always executed
    file.close()

# Raise own exception
# raise TypeError

# Or with a message
raise FileExistsError("The file exists but I won't give it to you 🙂")
