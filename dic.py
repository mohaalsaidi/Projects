contacts = {"Fred":7235591,
            "Mary":3841212,
            "Bob":3841212,
            "Sarah":2213278}
oldContact = dict(contacts)
if "Mary" in contacts:
    print("Mary's number is",contacts["Mary"])
else:
    print("Mary is not in mycontact list.")

number = contacts.get("Sarah","Error:(not in mycontact list)")
print("Dial "+str(number))

contacts["John"] = 2228102
fredsnum = contacts.pop("Fred")
print(contacts)
print("my contacts")
for keys in sorted(contacts):
    print(keys,contacts[keys])
print("--"*20)
print("my contacts")
for item in sorted(contacts.items()):
    print(item[0],item[1])