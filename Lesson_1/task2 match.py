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
match secondNumberForCalc:
    case 0:
        print("you can't")
    case "/":
        print("Result: " + str(firstNumberForCalc / secondNumberForCalc))
if firstNumberForCalc < 0:
    firstNumberForCalc = 0
match firstNumberForCalc:
    case 0:
        print("you can't")
    case "&":
        print("Result " + str(firstNumberForCalc / (1 / secondNumberForCalc)))
