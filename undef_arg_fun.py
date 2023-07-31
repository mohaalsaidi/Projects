def manyArgs(*arg):
    sum = 0
    print(len(arg), "arguments:", arg)
    for i in arg:
        sum+=i
    return sum



print("sum of arguments = ",manyArgs(1,2,3,4))
