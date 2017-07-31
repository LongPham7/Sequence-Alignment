from tkinter import *
from tkinter import ttk

class ResultFrame(object):

    def __init__(self, master):
        self.master = master

        self.label = ttk.Label(master, text = 'Result of sequence alignment:')
        self.text = Text(master, width = 40, height = 10)

        self.label.grid(column = 0, row = 0, sticky = W)
        self.text.grid(column = 0, row = 1, columnspan = 2)