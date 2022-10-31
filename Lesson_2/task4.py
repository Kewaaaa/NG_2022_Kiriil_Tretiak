number = int(input("Enter variable: "))
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(factorial)
