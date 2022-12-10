value = list(input('Enter a variable: '))
print("Lenght: " + str(len(value)))
uniq = set(value)
for element in value:
    print(element, end="")
print("\n")
lst = list(uniq)
lst.sort()
for element in lst:
    print(element + " - " + str(value.count(element)))
