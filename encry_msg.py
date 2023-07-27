msg = input("please enter message: ")

for l in msg:
    ascii = int(ord(l)-3)
    print(chr(ascii), end="")