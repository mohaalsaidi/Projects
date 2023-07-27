h1 = int(input("Enter first hour: "))
m1 = int(input("Enter first minutes: "))
h2 = int(input("Enter second hour: "))
m2 = int(input("Enter second minutes: "))

if h1 < h2:
    print("first time comes first")
    
elif h1==h2:
        if m1<=m2:
            print("first time comes first")
        else:
            print("second time comes first")
    
else:
    print("second time comes first")
    

    
    
