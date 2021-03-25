import tkinter as tk
from tkinter import ttk
from time import sleep


class StarSign:
    def __init__(self):
        self.canvas_width = 500
        self.canvas_height = 200
        self.app = tk.Tk()
        self.app.geometry("300x200")
        self.app.title('StarSign')
        self.labelTop = tk.Label(self.app,
                                 text="Choose your birth month", background="yellow", foreground="Black",
                                 font = ("Bahnschrift", 20))
        self.labelTop.pack()

        self.pb = ttk.Progressbar(self.app)

        self.Combo = ttk.Combobox(self.app, values=[
            "January",
            "February",
            "March",
            "April"],
                                  state="readonly")

        self.Combo.pack()
        self.Combo.current(0)
        self.Button = ttk.Button(self.app, text="Submit", command=self.submit)
        self.Button.pack()
        self.app2 = tk.Tk()
        self.app2.title('Paint')
        self.c = tk.Canvas(self.app2, width=self.canvas_width, height=self.canvas_height)
        self.app.mainloop()

    def submit(self):
        self.pb.pack()
        for i in range(101):
            sleep(0.002)
            self.pb.config(value=i)
            self.pb.update()

        print(self.Combo.get())
        answer = self.Combo.get()
        self.star(answer)

    def star(self, answer):
        labelBottom = ttk.Label(self.app)
        labelBottom.pack()

        if answer == "January":
            labelBottom.config(text="Capricorn or Aquarius")
        elif answer == "February":
            labelBottom.config(text="Aquarius or Pisces")
        elif answer == "March":
            labelBottom.config(text="Pisces or Aries")
        elif answer == "April":
            labelBottom.config(text="Aries or Taurus")
        self.castCanvas()

    def castCanvas(self):

        label3 = ttk.Label(self.app2, text=" Draw your given starsign", background="Green", foreground="White", font = ("Bahnschrift", 20))
        label3.pack()
        self.c.pack(fill='both', expand=1)
        self.c.bind('<B1-Motion>', self.paint)


    def paint(self, event):
        self.event = event
        x1 = self.event.x - 1
        y1 = self.event.y - 1
        x2 = self.event.x + 1
        y2 = self.event.y + 1
        self.c.create_line(x1, y1, x2, y2, fill="Blue")


a = StarSign()
