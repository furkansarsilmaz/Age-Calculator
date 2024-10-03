from datetime import datetime

name = str(input("Enter your name : "))
today = datetime.now()
loop = True

while loop :
    try:
        birthdate = input("Enter your birthdate (YY-MM-DD) : ")
        formated_birthdate = datetime.strptime(birthdate,'%Y-%m-%d')
        age = today.year - formated_birthdate.year
        print(f"{name}, you are {age} years old")
        loop = False
    except ValueError:
        print("Invalid format. Please enter as YYYY-MM-DD ")