from tkinter import *
from tkinter import messagebox
from pathlib import Path
from modules.themeColor import updateTheme, updateForeground
import json
import webbrowser
import requests
THEMECOLOR = updateTheme()
FOREGROUND = updateForeground()
scriptdir = Path(__file__).parent

class goToGraphUI():
    def showYourself():
        window = Tk()
        window.title("Go To Graph")
        window.config(bg=THEMECOLOR, padx=10, pady=10)

        grandTitle = Label(window, text="Go to Graph", font=("Arial", 24), bg=THEMECOLOR, fg=FOREGROUND)
        grandTitle.pack(pady=10)

        subtitle = Label(window, text="username, graph ID", font=("Arial", 12), bg=THEMECOLOR, fg=FOREGROUND)
        subtitle.pack(pady=1)

        usernameEntry = Entry(window, font=("Arial", 24))
        with open(scriptdir / "accountData.json", "r") as file:
            username = json.load(file)["username"]
            usernameEntry.insert(0, username)
        usernameEntry.pack()

        # passwordEntry = Entry(window, font=("Arial", 24))
        # with open(scriptdir / "accountData.json", "r") as file:
        #     password = json.load(file)["token"]
        #     passwordEntry.insert(0, password)
        # passwordEntry.pack()

        graphEntry = Entry(window, font=("Arial", 24))
        with open(scriptdir / "graphData.json", "r") as file:
            graphID = json.load(file)["id"]
            graphEntry.insert(0, graphID)
        graphEntry.pack()

        def goFunct():
            # header = {
            #     "X-USER-TOKEN": passwordEntry.get(),
            # }

            webbrowser.open(f"https://pixe.la/v1/users/{usernameEntry.get()}/graphs/{graphEntry.get()}.html")
            # sgraphEndpoint = f"https://pixe.la/v1/users/{usernameEntry.get()}/graphs/{graphEntry.get()}/graph-def"
            # request = requests.get(sgraphEndpoint, headers=header).json()
            # newDeafultGraph = {
            #     "id": graphEntry.get(),
            #     "name": request["name"],
            #     "unit": request["unit"],
            #     "type": request["type"],
            #     "color": request["color"],
            # }

            # with open(scriptdir / "graphData.json", "w") as file:
            #     json.dump(newDeafultGraph, file)
        goButton = Button(window, text="Go to Graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=goFunct)
        goButton.pack()