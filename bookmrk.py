import tkinter as tk
import webbrowser

def doorbell(event):
    print("DING DONG!")

def open_cp(event):
    webbrowser.open_new_tab('https://reactiongifs.me/rub-face/')

window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Check these buttons out")
alabel.grid(column=0, row=0)


button = tk.Button(window, text="Doorbell")
button.grid(column=1, row=0)


button2 = tk.Button(window, text="Look what I can do")
button2.grid(column=1, row=1)

button.bind("<Button-1>", doorbell)
button2.bind("<Button-1>", open_cp)

window.mainloop()


