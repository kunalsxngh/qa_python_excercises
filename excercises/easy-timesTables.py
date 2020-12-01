number = int(input("Please input a number: "))

i = 1
while(i < number+1):
    j = 1
    while (j < number+1):
        print (j * i, end = "   ")
        j += 1
        
    i += 1
    print()