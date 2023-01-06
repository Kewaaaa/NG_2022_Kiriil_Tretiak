def sorting(stringList):
    stringList.sort()
    return stringList


def countElements(stringList):
    return len(stringList)


def vowelsLetters(string):
    result = []
    vowels = ['a', 'e', 'o', 'u', 'i', 'y']
    for letters in string:
        if letters in vowels:
            result.append(letters)
    return result


def consonantsLetters(string):
    result = []
    vowels = ['a', 'e', 'o', 'u', 'i', 'y']
    for letters in string:
        if letters not in vowels:
            result.append(letters)
    return result


def reversString(stringList):
    lst = []
    for i in range(len(stringList), 0, -1):
        for j in range(len(stringList)):
            result = stringList[i-1]
        lst.append(result)
    return lst


def askString(string):
    return input(string)


def askAction(choise):
    return input(choise)


def printString(stringList):
    return stringList


def wordPosition(position, stringList):
    return stringList[position-1]


def main():
    string = askString("Enter some words: ")
    stringList = string.split(", ")
    print("What do u want: \n1.Sorting\n2.Count elements\n3.Show vowels or consonants\n4.Change words from end to start\n5.Choose a word in place u want\n6.Print string again\n7.Exit\n")
    choise = askAction("Choose an action: ")
    if choise == "1":
        print(printString(stringList))
        print(sorting(stringList))
    elif choise == "2":
        print(printString(stringList))
        print(str(countElements(stringList)) + " elements")
    elif choise == "3":
        choose = input("Choose a vowels(v) or consonants(c): ")
        if choose == "v":
            print(printString(stringList))
            print(vowelsLetters(string))
        else:
            print(printString(stringList))
            print(consonantsLetters(string))
    elif choise == "4":
        print("Before: " + str(printString(stringList)))
        print("After: " + str(reversString(stringList)))
    elif choise == "5":
        print(printString(stringList))
        position = int(input("Choose a position of word: "))
        print(wordPosition(position, stringList))
    elif choise == "6":
        while choise == "6":
            main()
            if choise != "6":
                break
    elif choise == "7":
        while True:
            break


main()
