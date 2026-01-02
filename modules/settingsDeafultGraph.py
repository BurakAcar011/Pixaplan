from tkinter import *
from tkinter import messagebox
from pathlib import Path
import json
from modules.themeColor import updateTheme, updateForeground
import requests
THEMECOLOR = updateTheme()
FOREGROUND = updateForeground()

class deafultGraphUI():
    def showYourself():
        window = Tk()
        window.title("Deafult Graph")
        window.config(bg=THEMECOLOR, padx=10, pady=10)
        scriptdir = Path(__file__).parent
        grandTitle = Label(window, text="Deafult Graph", font=("Arial", 24), bg=THEMECOLOR, fg=FOREGROUND)
        grandTitle.pack(pady=10)

        subtitle = Label(window, text="username, password, graph ID", font=("Arial", 12), bg=THEMECOLOR, fg=FOREGROUND)
        subtitle.pack(pady=1)

        usernameEntry = Entry(window, font=("Arial", 24))
        with open(scriptdir / "accountData.json", "r") as file:
            username = json.load(file)["username"]
            usernameEntry.insert(0, username)
        usernameEntry.pack()

        passwordEntry = Entry(window, font=("Arial", 24))
        with open(scriptdir / "accountData.json", "r") as file:
            password = json.load(file)["token"]
            passwordEntry.insert(0, password)
        passwordEntry.pack()


        graphEntry = Entry(window, font=("Arial", 24))
        with open(scriptdir / "graphData.json", "r") as file:
            graphID = json.load(file)["id"]
            graphEntry.insert(0, graphID)
        graphEntry.pack()


        def goFunct():
            header = {
                "X-USER-TOKEN": passwordEntry.get(),
            }
            sgraphEndpoint = f"https://pixe.la/v1/users/{usernameEntry.get()}/graphs/{graphEntry.get()}/graph-def"
            initrequest = requests.get(sgraphEndpoint, headers=header)
            request = initrequest.json()
            # print(request)
            newDeafultGraph = {
                "id": graphEntry.get(),
                "name": request["name"],
                "unit": request["unit"],
                "type": request["type"],
                "color": request["color"],
            }

            with open(scriptdir / "graphData.json", "w") as file:
                json.dump(newDeafultGraph, file)

        goButton = Button(window, text="Change Deafult Graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=goFunct)
        goButton.pack()