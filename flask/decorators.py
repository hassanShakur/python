def communicate(adder):
    def wrapper(*args):
        print("Addition operation")
        
        [num1, num2] = args
        if type(num1) == str or type(num2) == str:
            return print("Cannot add strings")

        adder(num1, num2)

    return wrapper


@communicate
def add(num1, num2):
    return print(num1 + num2)


add(1, '1')
