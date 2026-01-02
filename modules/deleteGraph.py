from tkinter import *
from tkinter import messagebox
from modules.themeColor import updateTheme, updateForeground
import modules.deleteGraphEngine as deleteGraphEngine
import json
from pathlib import Path
scriptdir = Path(__file__).parent
THEMECOLOR = updateTheme()
FOREGROUND = updateForeground()

class deleteGraphUI():
    def showYourself():
        window = Tk()
        window.title("Delete Graph")
        window.config(bg=THEMECOLOR, padx=10, pady=10)

        grandTitle = Label(window, text="Delete Graph", font=("Arial", 24), bg=THEMECOLOR, fg=FOREGROUND)
        grandTitle.pack(pady=10)

        subtitle = Label(window, text="username, password, graph ID", font=("Arial", 12), bg=THEMECOLOR, fg=FOREGROUND)
        subtitle.pack(pady=1)

        usernameEntry = Entry(window, width=30, font=("Arial", 14))
        with open(scriptdir / "accountData.json", "r") as file:
            username = json.load(file)["username"]
            usernameEntry.insert(0, username)
        usernameEntry.pack()

        passwordEntry = Entry(window, width=30, font=("Arial", 14))
        with open(scriptdir / "accountData.json", "r") as file:
            password = json.load(file)["token"]
            passwordEntry.insert(0, password)
        passwordEntry.pack()

        graphEntry = Entry(window, width=30, font=("Arial", 14))
        graphEntry.insert(0, "Graph ID")
        graphEntry.pack()

        def deletefunct():
            deleteGraphEngine.deleteGraph(graphEntry.get(), usernameEntry.get(), passwordEntry.get())
        deleteButton = Button(window, text="Delete", font=("Arial", 14), bg=THEMECOLOR, fg=FOREGROUND, command=deletefunct)
        deleteButton.pack(pady=10)