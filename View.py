from tkinter import Frame, Label, Button, Entry


class View:
    __frame: Frame
    button: Button
    text_field: Entry

    def __init__(self, frame: Frame):
        self.__frame = frame

        text = Label(frame, text="Dijkstra Algorithmus")
        text.pack()

        self.start_point = Entry(Frame)
        self.start_point.pack()

        self.end_point = Entry(Frame)
        self.end_point.pack()

        self.button = Button(frame, text="Start")
