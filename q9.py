myList = [23, 54, 76, 12, 90]
for i in range(len(myList)):
    if i<(len(myList)-1):
        print(myList[i], end= "| " )
    else:
        print(myList[i])