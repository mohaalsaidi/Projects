state = input("Enter F (female) or M (male) : ")
age = int(input("Enter your age: "))

if(30>=age>=24):
    if (state.upper() == "M"):
        print("Accepted!")
    else:
        print("Rejected:You are not male.")
else:
    print("Rejected:You are not in accepted age")