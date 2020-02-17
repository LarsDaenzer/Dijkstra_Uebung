import tkinter as tk

from Network import Network
from View import View
from Dijkstra_Algorithm import Dijkstra


class Presenter(tk.Frame):
    __dijkstra: Dijkstra
    __view: View

    def __init__(self):
        super().__init__(None)
        self.pack()

        self.__network = Network("DistanzenNeu.csv")
        self.__dijkstra = Dijkstra(self.__network)
        self.__view = View(self)

        self.__view.button.bind("<Button-1>", self.button_event_handler)

        self.mainloop()

    def button_event_handler(self, event):
        start = self.__view.start_point.get()
        destination = self.__view.end_point.get()
        print("running algorithm. From: " + start + " To: " + destination)


presenter = Presenter()