import glob
import shutil
import os
import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()
apps = []
apps2 = []

# if os.path.isfile('save.txt'):
#     with open('save.txt', 'r') as f:
#         tempApps = f.read()
#         tempApps = tempApps.split(',')
#         apps = [x for x in tempApps if x.strip()]
#         print(apps)


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askdirectory(
        initialdir="/", title="Search folder")
    apps.append(filename)
    print(apps)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def addApp2():

    for widget in frame.winfo_children():
        widget.destroy()

    filename2 = filedialog.askdirectory(
        initialdir="/", title="Destination folder")
    apps2.append(filename2)
    print(apps2)
    for app in apps2:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    stra1 = ""
    strb = ""
    stra2 = ""

    for app in apps:
        stra1 += app+"/*"
    for app in apps2:
        strb += app
    for jpgfile in glob.iglob(os.path.join(stra1, "*.jpg")):
        shutil.copy(jpgfile, strb)
    
    for app in apps:
        stra2 += app
    for jpgfile in glob.iglob(os.path.join(stra2, "*.jpg")):
        shutil.copy(jpgfile, strb)


canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

openFile = tk.Button(root, text="Search folder", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addApp)
openFile.pack()

openFile2 = tk.Button(root, text="Destination folder", padx=25,
                     pady=10, fg='white', bg="#263D42", command=addApp2)
openFile2.pack()

runApps = tk.Button(root, text="Copy photos", padx=25,
                    pady=10, fg='white', bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()


# with open('save.txt', 'w') as f:
#     for app in apps:
#         f.write(app + ',')


