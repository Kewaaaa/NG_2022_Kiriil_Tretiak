firstNumberForCalc = int(input("Enter first number: "))
secondNumberForCalc = int(input("Enter second number: "))
symbolForCalc = input("Which operation u want: ")
match symbolForCalc:
    case "+":
        result = firstNumberForCalc + secondNumberForCalc
    case "-":
        result = firstNumberForCalc - secondNumberForCalc
    case "*":
        result = firstNumberForCalc * secondNumberForCalc
    case "^":
        result = firstNumberForCalc ^ secondNumberForCalc
    case "/":
        result = firstNumberForCalc / secondNumberForCalc
    case "&":
        result = firstNumberForCalc ** (1/secondNumberForCalc)
print("Result: " + str(result))
