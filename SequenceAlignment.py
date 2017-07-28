from tkinter import *
from tkinter import ttk

def global_alignment():
    pass

def local_alignment():
    pass

root = Tk()
root.title('Sequence Alignment')
controlFrame = ttk.Frame(root, borderwidth = 10, padding = 10)
resultFrame = ttk.Frame(root)

label1 = ttk.Label(controlFrame, text = 'Specify two DNA sequences with bases A, T, G, and C')
label2 = ttk.Label(controlFrame, text = 'First sequence')
label3 = ttk.Label(controlFrame, text = 'Second sequence')
label4 = ttk.Label(controlFrame, text = 'Match score')
label5 = ttk.Label(controlFrame, text = 'Mismatch score')
label6 = ttk.Label(controlFrame, text = 'Gap oepning')
label7 = ttk.Label(controlFrame, text = 'Gap extension')

button1 = ttk.Button(controlFrame, text = 'Global alignment', command = global_alignment)
button2 = ttk.Button(controlFrame, text = 'Local alignment', command = local_alignment)

first_seq = StringVar()
second_seq = StringVar()
match_score  = StringVar()
mismatch_score = StringVar()
gap_opening = StringVar()
gap_extension = StringVar()

entry1 = ttk.Entry(controlFrame, textvariable = first_seq)
entry2 = ttk.Entry(controlFrame, textvariable = second_seq)
entry3 = ttk.Entry(controlFrame, textvariable = match_score)
entry4 = ttk.Entry(controlFrame, textvariable = mismatch_score)
entry5 = ttk.Entry(controlFrame, textvariable = gap_opening)
entry6 = ttk.Entry(controlFrame, textvariable = gap_extension)

controlFrame.grid(column = 0, row = 0)
resultFrame.grid(column = 0, row = 0)

label1.grid(column = 0, row = 0, columnspan = 2)
label2.grid(column = 0, row = 1, sticky = W)
label3.grid(column = 0, row = 2, sticky = W)
label4.grid(column = 0, row = 3, sticky = W)
label5.grid(column = 0, row = 4, sticky = W)
label6.grid(column = 0, row = 5, sticky = W)
label7.grid(column = 0, row = 6, sticky = W)

button1.grid(column = 2, row = 5, sticky = (N, S, E, W))
button2.grid(column = 2, row = 6, sticky = (N, S, E, W))

entry1.grid(column = 1, row = 1)
entry2.grid(column = 1, row = 2)
entry3.grid(column = 1, row = 3)
entry4.grid(column = 1, row = 4)
entry5.grid(column = 1, row = 5)
entry6.grid(column = 1, row = 6)

for child in controlFrame.winfo_children(): 
    child.grid_configure(padx = 3, pady = 3)

root.mainloop()