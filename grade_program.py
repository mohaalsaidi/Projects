grade = int(input("enter grade in numbers: "))


if grade >90:
    print("Your grade is A")
elif 80< grade <=90:
    print("Your grade is B")
elif 60<= grade <=80:
    print("Your grade is C")
elif  grade <60:
    print("Your grade is D")
else:
    print("invalid grade please enter 0-100")