from tkinter import *
from tkinter import ttk
from Bio import pairwise2

def global_alignment():
    """Align two sequences globally"""
    first = first_seq.get()
    second = second_seq.get()
    alignments = pairwise2.align.globalms(first, second, \
        match_score.get(), mismatch_score.get(), gap_opening.get(), \
        gap_extension.get(), one_alignment_only = True)
    text = pairwise2.format_alignment(*alignments[0])
    result.delete(1.0, END)
    result.insert(1.0, text)

def local_alignment():
    """Align two sequences locally"""
    first = first_seq.get()
    second = second_seq.get()
    alignments = pairwise2.align.localms(first, second, \
        match_score.get(), mismatch_score.get(), gap_opening.get(), \
        gap_extension.get(), one_alignment_only = True)
    text = pairwise2.format_alignment(*alignments[0])
    result.delete(1.0, END)
    result.insert(1.0, text)

root = Tk()
root.title('Sequence Alignment')
controlFrame = ttk.Frame(root, padding = 5, relief = 'solid')
resultFrame = ttk.Frame(root, padding = 5, relief = 'solid')

first_seq = StringVar()
second_seq = StringVar()
match_score  = DoubleVar()
mismatch_score = DoubleVar()
gap_opening = DoubleVar()
gap_extension = DoubleVar()
score = StringVar()

# Default scoring scheme for sequence alignment
match_score.set(3.0)
mismatch_score.set(1.0)
gap_opening.set(-1.0)
gap_extension.set(-0.5)
score.set("Alignment score:")

label1 = ttk.Label(controlFrame, text = 'Specify two DNA sequences with bases A, T, G, and C')
label2 = ttk.Label(controlFrame, text = 'First sequence')
label3 = ttk.Label(controlFrame, text = 'Second sequence')
label4 = ttk.Label(controlFrame, text = 'Match score')
label5 = ttk.Label(controlFrame, text = 'Mismatch score')
label6 = ttk.Label(controlFrame, text = 'Gap oepning')
label7 = ttk.Label(controlFrame, text = 'Gap extension')

label8 = ttk.Label(resultFrame, text = 'Result of sequence alignment:')

button1 = ttk.Button(controlFrame, text = 'Global alignment', command = global_alignment)
button2 = ttk.Button(controlFrame, text = 'Local alignment', command = local_alignment)

result = Text(resultFrame, width = 40, height = 10)

entry1 = ttk.Entry(controlFrame, textvariable = first_seq)
entry2 = ttk.Entry(controlFrame, textvariable = second_seq)
entry3 = ttk.Entry(controlFrame, textvariable = match_score)
entry4 = ttk.Entry(controlFrame, textvariable = mismatch_score)
entry5 = ttk.Entry(controlFrame, textvariable = gap_opening)
entry6 = ttk.Entry(controlFrame, textvariable = gap_extension)

controlFrame.grid(column = 0, row = 0)
resultFrame.grid(column = 0, row = 1)

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

label8.grid(column = 0, row = 0, sticky = W)
result.grid(column = 0, row = 1, columnspan = 2)

# Add padding to all widgets in the control frame.
for child in controlFrame.winfo_children(): 
    child.grid_configure(padx = 3, pady = 3)

# Add padding to all widgets in the result frame.
for child in resultFrame.winfo_children(): 
    child.grid_configure(padx = 3, pady = 3)

# Add padding to all widgets in the root.
for child in root.winfo_children(): 
    child.grid_configure(padx = 3, pady = 3)

root.mainloop()