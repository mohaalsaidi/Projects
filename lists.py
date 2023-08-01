mylist = [10,20,30,90]
limit = 90
pos = 0
found = False
while pos < len(mylist) and not found :
    if mylist[pos] == limit :
        found = True
    else :
        pos = pos + 1
if found:
    print("Found at position:" , pos)
else:
    print("Not found")