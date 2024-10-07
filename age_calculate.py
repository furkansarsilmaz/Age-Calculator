from datetime import datetime
from tkinter import * 
from tkinter import messagebox
class calculator:
    def __init__(self,name):
        self.name = name
        self.today = datetime.now()
        self.loop = True
    def calculate(self):
        while self.loop:
            try:
                birthdate = input("Enter your birthdate (YY-MM-DD) : ")
                formated_birthdate = datetime.strptime(birthdate,'%Y-%m-%d')
                age = self.today.year - formated_birthdate.year
                print(f"{name}, you are {age} years old")
                self.loop = False
            except ValueError:
                print("Invalid format. Please enter as YYYY-MM-DD ")

if __name__ == "__main__":
    name = input("Enter your name : ")
    calc = calculator(name)
    calc.calculate()
