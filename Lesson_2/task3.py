size = int(input("Input size: "))

for i in range(0, size):
    for j in range(size, 0, -1):

        print(j, end=" ")
    size -= 1
    print("\n")
print(i, size, j)
