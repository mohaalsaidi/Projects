n = int(input("Enter n: "))
list = ['bleed', 'cat' , 'careless', 'three']
new_list=[]
for i in list:
    if len(i) > n:
        new_list.append(i)
print(new_list)