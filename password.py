import random
from tkinter import *
import string

def generate_password():
    password=[]
    for i in range(5):
        beta=random.choice(string.ascii_letters)
        symbol=random.choice(string.punctuation)
        numbers=random.choice(string.digits)
        password.append(beta)
        password.append(symbol)
        password.append(numbers)
        
    y="".join(str(x)for x in password)
    lbl.config(text=y)
        

root=Tk()
root.geometry("300x200")
btn=Button(root,text="generate password" ,command=generate_password)
btn.grid(row=8,column=5)
lbl=Label(root,font=("times",15,"bold"))
lbl.grid(row=5,column=3)
root.mainloop()