from tkinter import *
from tkinter import ttk



##crear la funcion calcular
def calculate(*args):
  try:
    value=float(feet.get())
    meters.set(int(0.3048*value*10000.0+0.5)/10000)
  except ValueError:
    pass



root =Tk()
root.title("Feet to Meters")



##create the frame widget
mainframe=ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

##creating the entry widget
feet=StringVar()
feet_entry=ttk.Entry(mainframe,width=15, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W,E))
etiquetapies= Label(mainframe, text="pies").grid(column=3,row=1, sticky=(W,E))

##creating the remaining widgets
meters=StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2,row=2,sticky=(W,E))
etiquetametros= Label(mainframe, text="metros").grid(column=3,row=2, sticky=(W,E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4,row=1,sticky=W)
ttk.Button(mainframe, text="Exit", command=exit).grid(column=4, row=2,sticky=W)

##extras
for child in mainframe.winfo_children():
  child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()