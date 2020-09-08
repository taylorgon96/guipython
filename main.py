import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
apps = []



def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    file = filedialog.askopenfile(initialdir="/", title="Select File",
                                  filetypes=(("executables", "*.*"), ("all files", "*.py")))


    apps.append(file.name)
    print(file.name)
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()

def runApps():
    for app in apps:
        os.system(app)


canvas = tk.Canvas(root, height=700, width= 700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="blue", bg="#263D42", command=addApp)

openFile.pack()

runApps= tk.Button(root, text="Run Apps", padx=10,
                     pady=5, fg="red", bg="#263D42", command=runApps)

runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
