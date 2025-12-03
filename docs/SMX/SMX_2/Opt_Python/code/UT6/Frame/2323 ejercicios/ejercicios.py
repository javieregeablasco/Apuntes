from tkinter import Tk, Frame

root = Tk()
root.geometry("300x300")

Frame(root, bg="red", height=50).pack(side="top", fill="x")
Frame(root, bg="green", height=100).pack(side="top", fill="x")
Frame(root, bg="blue", height=150).pack(side="top", fill="x")

root.mainloop()

# ej 2
# from tkinter import *

# root = Tk()
# root.geometry("400x200")

# frame1 = Frame(root, bg="yellow", width=100)
# frame1.pack(side="left", fill="y")

# frame2 = Frame(root, bg="orange", width=150) 
# frame2.pack(side="left", fill="y")  

# frame3 = Frame(root, bg="purple", width=150)
# frame3.pack(side="left", fill="y")
# root.mainloop()


# from tkinter import Tk, Frame

# root = Tk()
# root.geometry("400x300+400+300")

# frame_sup = Frame(root, bg="yellow", height=100)
# frame_inf = Frame(root, bg="orange")

# frame_sup.pack(fill="x")
# frame_inf.pack(fill="both", expand=True)

# subframe1= Frame(frame_inf, bg="green")
# subframe1.config(highlightbackground="blue", highlightthickness=5)
# subframe1.pack(side="left", fill="both", expand=True, padx=20, pady=20)

# subframe1= Frame(frame_inf, bg="red")
# subframe1.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# root.mainloop()
