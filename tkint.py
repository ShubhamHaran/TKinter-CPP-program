import tkinter as tk
import subprocess

top = tk.Tk()
top.title("Mesh generation")
V1=tk.StringVar()
V2=tk.StringVar()
V3=tk.StringVar()
V4=tk.StringVar()
V5=tk.StringVar()
V6=tk.StringVar()
def submit():
   print('bridging...')
   subprocess.call(["g++","hello_world.cpp"])
   subprocess.call(["./a.out",E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get()])
   V1.set("")
   V2.set("")
   V3.set("")
   V4.set("")
   V5.set("")
   V6.set("")
L1 = tk.Label(top, text="Dimension along x axis in mm")
L1.pack()
E1 = tk.Entry(top)
E1.pack()
L2 = tk.Label(top, text="Dimension along y axis in mm")
L2.pack()
E2 = tk.Entry(top)
E2.pack()
L3 = tk.Label(top, text="Points along x axis")
L3.pack()
E3 = tk.Entry(top)
E3.pack()
L4 = tk.Label(top, text="Points along y axis")
L4.pack()
E4 = tk.Entry(top)
E4.pack()
L5 = tk.Label(top, text="X index of the cell")
L5.pack()
E5 = tk.Entry(top)
E5.pack()
L6 = tk.Label(top, text="Y index of the cell")
L6.pack()
E6 = tk.Entry(top)
E6.pack()
b=tk.Button(top,text="Submit",bg="red",command=submit)
b.pack()

top.mainloop()
