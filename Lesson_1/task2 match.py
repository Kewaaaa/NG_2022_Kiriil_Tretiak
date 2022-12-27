firstNumberForCalc = int(input("Enter first number: "))
secondNumberForCalc = int(input("Enter second number: "))
symbolForCalc = input("Which operation u want: ")
match symbolForCalc:
    case "+":
        print("Result: " + str(firstNumberForCalc + secondNumberForCalc))
    case "-":
        print("Result: " + str(firstNumberForCalc - secondNumberForCalc))
    case "*":
        print("Result: " + str(firstNumberForCalc * secondNumberForCalc))
    case "^":
        print("Result: " + str(firstNumberForCalc ** secondNumberForCalc))
    case "/":
        print("Result: " + str(firstNumberForCalc / secondNumberForCalc))
    case "&":
        print("Result " + str(firstNumberForCalc ** (1 / secondNumberForCalc)))
