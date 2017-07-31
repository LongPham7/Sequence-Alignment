from tkinter import *
from tkinter import ttk
from Bio import pairwise2

class AppFrame(object):
    
    def __init__(self, master):
        self.master = master
        self.master.title("Sequence Alignment")
        self.controlFrame = ttk.Frame(self.master, padding = 5, relief = 'solid')
        self.resultFrame = ttk.Frame(self.master, padding = 5, relief = 'solid')

        self.first_seq = StringVar()
        self.second_seq = StringVar()
        self.match_score  = DoubleVar()
        self.mismatch_score = DoubleVar()
        self.gap_opening = DoubleVar()
        self.gap_extension = DoubleVar()
        self.score = StringVar()

        # Default scoring scheme for sequence alignment
        self.match_score.set(3.0)
        self.mismatch_score.set(1.0)
        self.gap_opening.set(-1.0)
        self.gap_extension.set(-0.5)
        self.score.set("Alignment score:")

        self.label1 = ttk.Label(self.controlFrame, text = 'Specify two DNA sequences with bases A, T, G, and C')
        self.label2 = ttk.Label(self.controlFrame, text = 'First sequence')
        self.label3 = ttk.Label(self.controlFrame, text = 'Second sequence')
        self.label4 = ttk.Label(self.controlFrame, text = 'Match score')
        self.label5 = ttk.Label(self.controlFrame, text = 'Mismatch score')
        self.label6 = ttk.Label(self.controlFrame, text = 'Gap oepning')
        self.label7 = ttk.Label(self.controlFrame, text = 'Gap extension')

        self.label8 = ttk.Label(self.resultFrame, text = 'Result of sequence alignment:')

        self.button1 = ttk.Button(self.controlFrame, text = 'Global alignment', command = self.global_alignment)
        self.button2 = ttk.Button(self.controlFrame, text = 'Local alignment', command = self.local_alignment)

        self.result = Text(self.resultFrame, width = 40, height = 10)

        self.entry1 = ttk.Entry(self.controlFrame, textvariable = self.first_seq)
        self.entry2 = ttk.Entry(self.controlFrame, textvariable = self.second_seq)
        self.entry3 = ttk.Entry(self.controlFrame, textvariable = self.match_score)
        self.entry4 = ttk.Entry(self.controlFrame, textvariable = self.mismatch_score)
        self.entry5 = ttk.Entry(self.controlFrame, textvariable = self.gap_opening)
        self.entry6 = ttk.Entry(self.controlFrame, textvariable = self.gap_extension)

        self.controlFrame.grid(column = 0, row = 0)
        self.resultFrame.grid(column = 0, row = 1)

        self.label1.grid(column = 0, row = 0, columnspan = 2)
        self.label2.grid(column = 0, row = 1, sticky = W)
        self.label3.grid(column = 0, row = 2, sticky = W)
        self.label4.grid(column = 0, row = 3, sticky = W)
        self.label5.grid(column = 0, row = 4, sticky = W)
        self.label6.grid(column = 0, row = 5, sticky = W)
        self.label7.grid(column = 0, row = 6, sticky = W)

        self.button1.grid(column = 2, row = 5, sticky = (N, S, E, W))
        self.button2.grid(column = 2, row = 6, sticky = (N, S, E, W))

        self.entry1.grid(column = 1, row = 1)
        self.entry2.grid(column = 1, row = 2)
        self.entry3.grid(column = 1, row = 3)
        self.entry4.grid(column = 1, row = 4)
        self.entry5.grid(column = 1, row = 5)
        self.entry6.grid(column = 1, row = 6)

        self.label8.grid(column = 0, row = 0, sticky = W)
        self.result.grid(column = 0, row = 1, columnspan = 2)

        # Add padding to all widgets in the control frame.
        for child in self.controlFrame.winfo_children(): 
            child.grid_configure(padx = 3, pady = 3)

        # Add padding to all widgets in the result frame.
        for child in self.resultFrame.winfo_children(): 
            child.grid_configure(padx = 3, pady = 3)

    def global_alignment(self):
        """Align two sequences globally"""
        first = self.first_seq.get()
        second = self.second_seq.get()
        alignments = pairwise2.align.globalms(first, second, \
            self.match_score.get(), self.mismatch_score.get(), self.gap_opening.get(), \
            self.gap_extension.get(), one_alignment_only = True)
        text = pairwise2.format_alignment(*alignments[0])
        self.result.delete(1.0, END)
        self.result.insert(1.0, text)

    def local_alignment(self):
        """Align two sequences locally"""
        first = self.first_seq.get()
        second = self.second_seq.get()
        alignments = pairwise2.align.localms(first, second, \
            self.match_score.get(), self.mismatch_score.get(), self.gap_opening.get(), \
            self.gap_extension.get(), one_alignment_only = True)
        text = pairwise2.format_alignment(*alignments[0])
        self.result.delete(1.0, END)
        self.result.insert(1.0, text)

def main():
    root = Tk()
    app = AppFrame(root)
    # Add padding to all widgets in the root.
    for child in root.winfo_children(): 
        child.grid_configure(padx = 3, pady = 3)
    root.mainloop()

if __name__ == '__main__':
    main()