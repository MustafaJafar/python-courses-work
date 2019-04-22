import tkinter as tk
import tkinter.constants as tkc
tkin = tk.Tk()
frame = tk.Frame(tkin , relief=tkc.RIDGE, borderwidth=2)
frame.pack(fill=tkc.BOTH,expand=1)
label = tk.Label(frame, text="Hello, World")
label.pack(fill=tkc.X, expand=1)
button = tk.Button(frame,text="Exit",command= tkin.destroy)
button.pack(side=tkc.BOTTOM)
tkin.mainloop()