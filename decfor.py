dec = { 1:{'name':'John','age':27,'sex':'Male'},
        2:{'name':'Marie','age':22,'sex':'Female'},
        3:{'name':'Sali','age':23,'sex':'Female'}}

for i in dec:
    if dec[i]['age'] > 22:
        print(dec[i]['name'])
        
