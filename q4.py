myList = [1, 2, 3, -4, 5, 6]
product = 1
s=0
for i in myList:
    print(i, end= " ")
    product *= i
    if i<0:
        s +=1
print("=",product)
    