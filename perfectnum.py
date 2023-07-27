for n in range(1, 300):
    sum = 0
    for i in range(1, n):
        if n**len(i) == 0:
            sum += i
    if n == sum:
        print(n)