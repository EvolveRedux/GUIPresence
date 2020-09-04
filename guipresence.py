# Created by EvolveRedux
import tkinter as tk
import tkinter.messagebox
from pypresence import Presence
import time
root = tk.Tk()

root.title('GUIPresence 1.0')
canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()


entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)
label1 = tk.Label(root, text="Bottom Text:")
canvas1.create_window(60, 140, window=label1)
entry2 = tk.Entry(root)
canvas1.create_window(200, 100, window=entry2)
label2 = tk.Label(root, text="Title Text:")
canvas1.create_window(60, 100, window=label2)

entry3 = tk.Entry(root)
canvas1.create_window(200, 60, window=entry3)
label3 = tk.Label(root, text="Client ID:")
canvas1.create_window(60, 60, window=label3)



def getSquareRoot():
    clientid = entry3.get()
    title = entry1.get()
    subtitle = entry2.get()
    client_id = clientid
    RPC = Presence(client_id)
    RPC.connect()
    if len(title) < 2:
        tkinter.messagebox.showinfo("Alert", "Text needs to be longer than 1 character.")
        alert = 1
    if len(subtitle) < 2:
        if alert == 1:
            pass
        else:
            tkinter.messagebox.showinfo("Alert", "Text needs to be longer than 1 character.")
    if len(clientid) < 2:
        tkinter.messagebox.showinfo("Alert", "You must enter a client ID.")
    else:
        RPC.update(state=title, details=subtitle)
        tkinter.messagebox.showinfo("Alert", "Status updated successfully.")

button1 = tk.Button(text='Set Status', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()