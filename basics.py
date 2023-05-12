name = input("Enter your name: ") 
print("Hello " + name)

# Conversions
str(123)
float("400")
int("7")

# Functions
len('abcd')
type(name)

# Methods
"tEXt".lower()
'name'.count('a') # How many times 'a' occurs


# Mathematics
print(8 / 2) # FLoat result
print(8 // 2) # int result

round(1.456, 5) # Decimal places precision
print("{:.2f}".format(1.4)) # Add 0 to the end to fit num of decimal places

# F-string - formatted string
print(f"Your name is {name}")

# Conditions
if name or 1:
    print('🫡✅')
elif 1 == 1 and 3 == 3:
    print('🟰')
elif not 2 < 3:
    print('Used not')
else:
    print('❌')
