from View import View
from Dijkstra_Algorithm import Dijkstra
from Network import Network


class Presenter(tk.Frame):
    __dijkstra: Dijkstra
    __view: View

    def __init__(self):
        super().__init__(None)
        self.pack()

        self.__network = Network("DistanzenNeu.csv")
        self.__dijkstra = Dijkstra(self.__network)
        self.__view = View(self)

        self.master.title("Dijkstra Algorithm")
        self.master.maxsize(1000, 400)

        self.__view.button.bind("<Button-1>", self.button_event_handler)
        self.mainloop()

    def button_event_handler(self, event):
        start_point = self.__view.start_point.get()
        end_point = self.__view.end_point.get()


presenter = Presenter()
