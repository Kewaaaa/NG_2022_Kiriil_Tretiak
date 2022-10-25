firstNumberForCalc = int(input("Enter first number: "))
secondNumberForCalc = int(input("Enter second number: "))
symbolForCalc = input("Which operation u want: ")

if symbolForCalc == "+":
    result = firstNumberForCalc + secondNumberForCalc
elif symbolForCalc == "-":
    result = firstNumberForCalc - secondNumberForCalc
elif symbolForCalc == "*":
    result = firstNumberForCalc * secondNumberForCalc
elif symbolForCalc == "/":
    if secondNumberForCalc == 0:
        result = ("you can't!")
    else:
        result = firstNumberForCalc / secondNumberForCalc
elif symbolForCalc == "^":
    result = firstNumberForCalc ** secondNumberForCalc
elif symbolForCalc == "&":
    result = firstNumberForCalc ** (1 / secondNumberForCalc)
    if firstNumberForCalc < 0:
        result = ("you can't!")
print("Result: " + str(result))
