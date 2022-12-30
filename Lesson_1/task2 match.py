firstNumberForCalc = int(input("Enter first number: "))
secondNumberForCalc = int(input("Enter second number: "))
symbolForCalc = input("Which operation u want: ")
result = "Result: "
match symbolForCalc:
    case "+":
        print(result + str(firstNumberForCalc + secondNumberForCalc))
    case "-":
        print(result + str(firstNumberForCalc - secondNumberForCalc))
    case "*":
        print(result + str(firstNumberForCalc * secondNumberForCalc))
    case "^":
        print(result + str(firstNumberForCalc ** secondNumberForCalc))
    case "/":
        print(result + str(firstNumberForCalc / secondNumberForCalc))
    case "&":
        print(result + str(firstNumberForCalc ** (1 / secondNumberForCalc)))
