vowels = ['a', 'e', 'o', 'u', 'i', 'y']


def actionsOfMenu():
    global strng
    strng = input("Enter some words: ")
    global choiseOfNumber
    print("What do u want:\n1.Sorting\n2.Count elements\n3.Show vowels or consonants\n4.Change words from end to start\n5.Choose a word in place u want\n6.Print string again\n")
    choiseOfNumber = input("Choose an action: ")
    global strngList
    strngList = strng.split(", ")


def printList():
    print("Your string: " + strng)


def sortingString():
    strngList.sort()
    return strngList


def countElement():
    print(len(strngList))


def vowelsLetters():
    result = []
    for letters in strng:
        if letters in vowels:
            result.append(letters)
    return result


def consonantsLetters():
    result = []
    for letters in strng:
        if letters not in vowels:
            result.append(letters)
    return result


def reversWord():
    result = []
    for i in range(len(strngList)):
        for j in range(len(strngList)):
            strngList[i] = strngList[j + 1]
        result.append(strngList)
    printList()
    return result


def wordPlace(word):
    return strngList[word - 1]


def choice():
    if choiseOfNumber == "1":
        print(sortingString())
        printList()
    if choiseOfNumber == "2":
        countElement()
        printList()
    if choiseOfNumber == "3":
        choise = input("Choose a vowels(v) or consonants(c): ")
        if choise == "v":
            print(vowelsLetters())
        if choise == "c":
            print(consonantsLetters())
        printList()
    if choiseOfNumber == "4":
        print(reversWord())
    if choiseOfNumber == "5":
        position = int(input("Choose the word place: "))
        print(wordPlace(position))
        printList()
    if choiseOfNumber == "6":
        actionsOfMenu()


choice()
