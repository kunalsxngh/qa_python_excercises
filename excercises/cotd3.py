def zip(string1, string2):
    returnString = ""
    if len(string1) == len(string2):
        i = 0
        while(i < len(string1)):
            returnString += string1[i] + string2[i]
            i += 1

    return returnString
