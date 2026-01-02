from tkinter import *
from tkinter import messagebox
from modules.themeColor import updateTheme, updateForeground
from pathlib import Path
import datetime as dt
import json
from modules.editRecordingEngine import record
scriptdir = Path(__file__).parent
THEMECOLOR = updateTheme()
FOREGROUND = updateForeground()

class editRecordingUI():
    def showYourself():
        month = str(dt.datetime.now().month)
        day = str(dt.datetime.now().day)
        year = str(dt.datetime.now().year)
        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        
        window = Tk()
        window.title("Pixaplan - Edit Recording")
        window.config(bg=THEMECOLOR, padx=10, pady=10)

        grandTitle = Label(window, text="Edit Recording", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 24, "bold"))
        grandTitle.grid(row=0, column=1, pady=5)

        subtitle = Label(window, text="month, day, year", font=("Arial", 12), bg=THEMECOLOR, fg=FOREGROUND)
        subtitle.grid(row=1, column=1)

        monthEntry = Entry(window, font=("Arial", 24), width=2)
        monthEntry.insert(0, month)
        monthEntry.grid(row=2, column=0)

        dayEntry = Entry(window, font=("Arial", 24), width=2)
        dayEntry.insert(0, day)
        dayEntry.grid(row=2, column=1)

        yearEntry = Entry(window, font=("Arial", 24), width=4)
        yearEntry.insert(0, year)
        yearEntry.grid(row=2, column=2)

        textforpadding = Label(window, text=" ", bg=THEMECOLOR, fg=FOREGROUND)
        textforpadding.grid(row=3, column=1, pady=10)

        subtitle = Label(window, text="username, password, graph ID", font=("Arial", 12), bg=THEMECOLOR, fg=FOREGROUND)
        subtitle.grid(row=3, column=1)

        usernameEntry  = Entry(window, font=("Arial", 24), width=20)
        usernameEntry.grid(row=4, column=1)
        with open(scriptdir / "accountData.json", "r") as file:
            username = json.load(file)["username"]
            usernameEntry.insert(0, username)


        passwordEntry = Entry(window, font=("Arial", 24), width=20)
        passwordEntry.grid(row=5, column=1)
        with open(scriptdir / "accountData.json", "r") as file:
            password = json.load(file)["token"]
            passwordEntry.insert(0, password)

        graphEntry = Entry(window, font=("Arial", 24), width=20)
        graphEntry.grid(row=7, column=1)
        with open(scriptdir / "graphData.json", "r") as file:
            graph = json.load(file)["id"]
            graphEntry.insert(0, graph)
        
        graphEntry.grid(row=6, column=1)
        textforpadding = Label(window, text=" ", bg=THEMECOLOR, fg=FOREGROUND)
        textforpadding.grid(row=7, column=1, pady=10)


        quantityEntry = Entry(window, font=("Arial", 24), width=20)
        quantityEntry.grid(row=9, column=1)
        quantityEntry.insert(0, "How much?")
        subtitle = Label(window, text="Only number, don't include the unit.", font=("Arial", 12), bg=THEMECOLOR, fg=FOREGROUND)
        subtitle.grid(row=10, column=1)

        def updateFunct():
            record(usernameEntry.get(), passwordEntry.get(), graphEntry.get(), monthEntry.get(), dayEntry.get(), yearEntry.get(), quantityEntry.get())
        updateButton = Button(window, text="Update", font=("Arial", 12), bg=THEMECOLOR, fg=FOREGROUND, command=updateFunct)
        updateButton.grid(row=11, column=1, pady=10)