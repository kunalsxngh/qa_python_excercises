def numberOfCases(sentence):
    upperCase = 0
    lowerCase = 0
    for x in sentence:
        if x.isupper():
            upperCase += 1
        elif x.islower():
            lowerCase += 1

    return "UPPER CASE " + str(upperCase) + "\nLOWER CASE " + str(lowerCase)

print(numberOfCases("Hello world!"))