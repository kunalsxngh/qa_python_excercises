isbn = input("Please input an ISBN: ")
isbn = isbn.replace('-', '')
isbn = isbn.replace('?', '')
print(isbn)
checksum = int(isbn[0])

index = 1
while(index < len(isbn)):

    if index % 2 == 0:
        checksum += int(isbn[index])
    else:
        checksum += int(isbn[index]) * 3
    
    index += 1

checksum = 10 - (checksum % 10)
print(checksum)