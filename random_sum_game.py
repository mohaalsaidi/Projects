import random

ans = ""
while (ans != "done"):
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    c_ans = str(num1+num2)
    print(num1," + ",num2)
    ans = input("what is your answer? ")
    if ans == c_ans:
        print("your are correct!!")
    elif ans =="done":
        print("goodbye!")    
    else:
        print("wrong, try again.")
