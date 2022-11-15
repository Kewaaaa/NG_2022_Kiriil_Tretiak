value = list(input('Enter a variable: '))
print("Lenght: " + str(len(value)))
uniq = set(value)
for element in value:
    print(element, end="")
print("\n")
l = list(uniq)
l.sort()
for element in l:
    print(element + " - " + str(value.count(element)))
