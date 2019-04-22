from tkinter import * #from xxx import all

#create window
window = Tk()

#functions : 
def Kg_convert():
    #print(e1_value.get())
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.delete("1.0" , END)
    t1.insert(END, grams)
    t2.delete("1.0" , END)
    t2.insert(END, pounds)
    t3.delete("1.0" , END)
    t3.insert(END, ounces)
    
#add widgets
l1 = Label(window , text = "Kg")
l1.grid(row = 0 , column = 0 )

e1_value = StringVar()
e1 = Entry(window , textvariable = e1_value )
e1.grid(row = 0 , column = 1)

b1 = Button(window , text = "Convert" , command = Kg_convert )
b1.grid(row = 0 , column = 2 )

t1 = Text(window , height = 1 , width = 20)
t1.grid(row =1 , column = 0)

t2 = Text(window , height = 1 , width = 20)
t2.grid(row =1 , column = 1)

t3 = Text(window , height = 1 , width = 20)
t3.grid(row =1 , column = 2)

window.mainloop()