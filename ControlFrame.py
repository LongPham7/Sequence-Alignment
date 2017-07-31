from tkinter import *
from tkinter import ttk
from Bio import pairwise2

class ControlFrame(object):

    def __init__(self, master, result):
        self.master = master
        self.result = result

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

        self.label1 = ttk.Label(self.master, text = 'Specify two DNA sequences with bases A, T, G, and C')
        self.label2 = ttk.Label(self.master, text = 'First sequence')
        self.label3 = ttk.Label(self.master, text = 'Second sequence')
        self.label4 = ttk.Label(self.master, text = 'Match score')
        self.label5 = ttk.Label(self.master, text = 'Mismatch score')
        self.label6 = ttk.Label(self.master, text = 'Gap oepning')
        self.label7 = ttk.Label(self.master, text = 'Gap extension')

        self.button1 = ttk.Button(self.master, text = 'Global alignment', command = self.global_alignment)
        self.button2 = ttk.Button(self.master, text = 'Local alignment', command = self.local_alignment)

        self.entry1 = ttk.Entry(self.master, textvariable = self.first_seq)
        self.entry2 = ttk.Entry(self.master, textvariable = self.second_seq)
        self.entry3 = ttk.Entry(self.master, textvariable = self.match_score)
        self.entry4 = ttk.Entry(self.master, textvariable = self.mismatch_score)
        self.entry5 = ttk.Entry(self.master, textvariable = self.gap_opening)
        self.entry6 = ttk.Entry(self.master, textvariable = self.gap_extension)

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

    def global_alignment(self):
        """Align two sequences globally"""
        first = self.first_seq.get()
        second = self.second_seq.get()
        alignments = pairwise2.align.globalms(first, second, \
            self.match_score.get(), self.mismatch_score.get(), self.gap_opening.get(), \
            self.gap_extension.get(), one_alignment_only = True)
        text = pairwise2.format_alignment(*alignments[0])
        self.result.text.delete(1.0, END)
        self.result.text.insert(1.0, text)

    def local_alignment(self):
        """Align two sequences locally"""
        first = self.first_seq.get()
        second = self.second_seq.get()
        alignments = pairwise2.align.localms(first, second, \
            self.match_score.get(), self.mismatch_score.get(), self.gap_opening.get(), \
            self.gap_extension.get(), one_alignment_only = True)
        text = pairwise2.format_alignment(*alignments[0])
        self.result.text.delete(1.0, END)
        self.result.text.insert(1.0, text)