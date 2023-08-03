input_file = open("input.txt", "r")
sum1=0
values = []

for i in input_file:
        print(i)
        sum1 +=float(i)
        values.append(i)
average = sum1 /(len(values))
print("--"*10)
print("Total: ",sum1)
print("Average: ",average)



