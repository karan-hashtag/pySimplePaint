import Tkinter as tk
from tkColorChooser import askcolor


class Paint:
    #Attributes
    button1 = "up"
    colour = "black"
    xold, yold = None, None
    root = tk.Tk()
    canvas = tk.Canvas(root)
    toolbar = tk.Frame(root)
    tk.Label(toolbar, text="Toolbar").pack(side=tk.TOP)
    colourchooser = tk.Button(toolbar, text="Choose Colour")

    # Binding events to respective functions
    def __init__(self):
        self.colourchooser["command"] = self.choosecolour
        self.colourchooser.pack()
        self.toolbar.pack(side=tk.LEFT)
        self.canvas.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
        self.canvas.bind("<ButtonPress-1>", self.togglebutton)
        self.canvas.bind("<ButtonRelease-1>", self.togglebutton)
        self.canvas.bind("<Motion>", self.motion)
    def choosecolour(self):
        colour = askcolor()
        rgb, self.colour = colour
        self.colourchooser["bg"] = self.colour
    # Events->Funtions
    def togglebutton(self, event):
        self.button1 = "down" if (self.button1=="up") else "up"
        if(self.button1 == "up"):
            self.xold, self.yold = None, None
    def motion(self, event):
        if(self.button1 == "down"):
            event.widget.create_line(self.xold, self.yold, event.x, event.y,
                                    fill=self.colour, smooth=True)
        self.xold = event.x
        self.yold = event.y
    # Run the program
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Paint()
    app.run()