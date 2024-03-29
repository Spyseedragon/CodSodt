from tkinter import *
import string
import random
import pyperclip


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)


'''def reset():
    choice.set(0)
    passwordField.config(text="")'''


root=Tk()
root.title("Password generator")
root.config(bg='aliceblue')
choice=IntVar()
choice.set(0)
Font=('Times',13,'bold')

passwordLabel=Label(root,text='Password Generator',font=('Helvetica',20,'bold'),bg='aliceblue',fg='black')
passwordLabel.grid(pady=10)

weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font='Helvetica')
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font='Helvetica')
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font='Helvetica')
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text='Password Length',font='Helvetica',bg='aliceblue',fg='white')
lengthLabel.grid(pady=5)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font='Helvetica')
length_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font='Helvetica',command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font='Helvetica')
passwordField.grid()

copyButton=Button(root,text='Copy',font='Helvetica',command=copy)
copyButton.grid(pady=5)

'''resetButton=Button(root,text='Reset',font='Helvetica',command=reset)
resetButton.grid(pady=5)'''

root.mainloop()
