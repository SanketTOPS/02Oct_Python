import tkinter
from tkinter import ttk


screen=tkinter.Tk()
screen.title("MyApp")
screen.geometry("400x500")
screen.config(bg='lightblue')

#tkinter.Label(text="Firstname:").pack()
#tkinter.Label(text="Lastname:").pack()

#tkinter.Label(text="Firstname:").place(x=0,y=0)
#tkinter.Label(text="Lastname:").place(x=0,y=30)

tkinter.Label(text="Firstname:",bg='lightblue',fg='red',font='Elephant 12').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Lastname:",bg='lightblue',fg='red',font='Elephant 12').grid(row=1,column=0,sticky='w')

tkinter.Entry().grid(row=0,column=1,sticky='w')
tkinter.Entry().grid(row=1,column=1,sticky='w')

tkinter.Radiobutton(value=0, text='Male',bg='lightblue',fg='red',font='Elephant 12').grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text='Female',bg='lightblue',fg='red',font='Elephant 12').grid(row=2,column=1,sticky='w')

tkinter.Checkbutton(text="Gujarati",bg='lightblue',fg='red',font='Elephant 12').grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="Hindi",bg='lightblue',fg='red',font='Elephant 12').grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="English",bg='lightblue',fg='red',font='Elephant 12').grid(row=5,column=0,sticky='w')

city=['Rajkot','Ahmedabad','Baroda','Surat','Jamnagar']
ttk.Combobox(values=city).grid(row=6,column=0)

def btnclick():
    print("Button clicked!")

tkinter.Button(text="Submit",font='Elephant 12',command=btnclick).place(x=160,y=250)


screen.mainloop()