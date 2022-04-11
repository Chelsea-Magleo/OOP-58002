from tkinter import*
class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Enter your fullname:', fg='Red')
        self.lbl1.place(x=20, y=70)
        self.t1 = Entry()
        self.t1.place(x=150, y=70)
        self.t1.place(width=120, height=20)
        self.t2 = Entry()
        self.t2.place(x=150, y=100)
        self.t2.place(width=120, height=20)
        btn = Button(win, text="Click to display your fullname", fg='Red')
        btn.place(x=5, y=100)



window = Tk()
mywin = MyWindow(window)
window.title('Midterm Examination')
window.geometry("400x300+10+10")
window.mainloop()