def plus(num1, num2, result):
    result = num1 + num2
    return result


def minus(num1, num2, result):
    result = num1 - num2
    return result


def multiply(num1, num2, result):
    result = num1 * num2
    return result


def devide(num1, num2, result):
    result = num1 / num2
    return result


num1 = int(input("Enter 1 number: "))
num2 = int(input("Enter 2 number: "))
symbol = input("Choose an action: ")
if symbol == "+":
    print(plus(num1, num2, symbol))
elif symbol == "-":
    print(minus(num1, num2, symbol))
elif symbol == "*":
    print(multiply(num1, num2, symbol))
elif symbol == "/":
    print(devide(num1, num2, symbol))
