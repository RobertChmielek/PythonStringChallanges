FirstName=input("Enter your first name")
if len(FirstName) < 5:
    Surname=input("Enter your surname")
    FullName =FirstName+Surname
    print(FullName.upper())
else:
    print(FirstName.lower())