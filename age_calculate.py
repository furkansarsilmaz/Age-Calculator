from tkinter import *
from datetime import datetime
import re
from tkinter import messagebox

class calculator():
    def __init__(self,root):
        self.root = root
        self.root.geometry("300x200")
        self.root.title("Age Calculator")
        self.root.configure(background="gray")
        self.name_text = Text(self.root,width=15,height=1)
        self.name_text.pack(pady=5)

        self.birthdate_text = Text(self.root,width=15,height=1)
        self.birthdate_text.pack(pady=5)

        self.calc_button = Button(self.root,text="Calculate",width=7,height=2,command=self.calculate)
        self.calc_button.pack()

        self.today = datetime.now()

    def calculate(self):
        name = self.name_text.get("1.0",END).strip()
        birthdate = self.birthdate_text.get("1.0",END).strip()
        try:
            formated_birthdate = datetime.strptime(birthdate,'%Y-%m-%d')
            age = self.today.year - formated_birthdate.year
            messagebox.showinfo("Succeed",f"{name}, you are {age} old.")
        except ValueError:
            messagebox.showerror("Error","Use YYYY-MM-DD format ")
            self.name_text.delete("1.0",END)
            self.birthdate_text.delete("1.0",END)
            return
        
if __name__ == "__main__":
    root = Tk()
    calculator(root)
    root.mainloop()