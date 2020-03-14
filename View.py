import tkinter as tk
from tkinter import Label, Button, Entry


class View(tk.Frame):
    button: Button
    text_field: Entry

    def __init__(self, **kw):
        super().__init__(**kw)
        self.pack()

        self.master.title("Dijkstra Algorithmus")
        self.master.maxsize(1000, 400)

        text = Label(self, text="Dijkstra Algorithmus")
        text.pack()

        start_text = Label(self, text="Start Ort:")
        start_text.pack()
        self.start_text = Entry(self)
        self.start_text.pack()

        ziel_text = Label(self, text="Ziel Ort:")
        ziel_text.pack()
        self.destination_text = Entry(self)
        self.destination_text.pack()

        blank = Label(self, text="")
        blank.pack()
        self.button = Button(self, text="Start!")
        self.button.pack()
