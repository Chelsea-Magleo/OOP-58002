from tkinter import*
class MyWindow:
    def __init__(self, win):
        self.t1 = Entry()
        self.t1.place(x=130, y=50)
        self.t1.place(width=150, height=50)



window = Tk()
mywin = MyWindow(window)
window.title('Text field')
window.geometry("400x300+10+10")
window.mainloop()
