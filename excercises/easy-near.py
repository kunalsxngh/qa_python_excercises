def near(string1, string2):
    if((len(string2) + 1) != len(string1)):
        return False
    i = 0
    while(i < len(string1)):
        testString = string1[:i] + string1[i+1:]
        if testString == string2:
                return True
        i += 1
    
    return False

if(near("sleet", "lets") == True):
     print("true")
else: 
    print("false")