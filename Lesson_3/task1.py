firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
action = input("Enter an actions(+, -, *, /, ^): ")


def actions(action):
    if action == "+":
        return firstNumber + secondNumber
    elif action == "-":
        return firstNumber - secondNumber
    elif action == "*":
        return firstNumber * secondNumber
    elif action == "/":
        try:
            return firstNumber / secondNumber
        except ZeroDivisionError:
            return "Infinity"
    elif action == "^":
        return firstNumber ** secondNumber


print(actions(action))
