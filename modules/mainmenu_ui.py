from tkinter import *
from modules.donationEngine import donate
import modules.themeColor as themeColor
from modules.createAccount import CreateAccountUI
from modules.logIn import logInUI
from modules.settings import SettingsUI
from modules.createGraph import createGraphUI
import webbrowser
import json
from pathlib import Path
from modules.deleteGraph import deleteGraphUI
import modules.openProfile as openProfile
from modules.goToGraph import goToGraphUI
from modules.settingsDeafultGraph import deafultGraphUI
from modules.recordHabit import recordHabitUI
from modules.editRecording import editRecordingUI
scriptdir = Path(__file__).parent
THEMECOLOR = themeColor.updateTheme()
FOREGROUND = themeColor.updateForeground()

class ui():
    def __init__(self):
        window = Tk()
        window.title("Pixaplan - Main Menu")
        window.config(bg=THEMECOLOR, padx=50, pady=50)

        grandTitle = Label(window, text="Pixaplan", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 24, "bold"))
        grandTitle.pack(pady=10)

        createAccountButton = Button(window, text="Create Account", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=CreateAccountUI.showYourself)
        createAccountButton.pack()

        # logInButton = Button(window, text="Switch Deafult Account", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=logInUI.showYourself)
        # logInButton.pack()

        createGraphButton = Button(window, text="Create Graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=createGraphUI.showYourself)
        createGraphButton.pack()

        recordHabitButton = Button(window, text="Add Recording", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=recordHabitUI.showYourself)
        recordHabitButton.pack()

        # editPixelButton = Button(window, text="Edit Recording", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=editRecordingUI.showYourself)
        # editPixelButton.pack()

        def goToGraph():
            with open(scriptdir / "graphData.json", "r") as file:
                usernamefile = open(scriptdir / "accountData.json", "r")
                username = json.load(usernamefile)["username"]
                webbrowser.open(f"https://pixe.la/v1/users/{username}/graphs/{json.load(file)["id"]}.html")
        goToGraphButton = Button(window, text="Go to Graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=goToGraphUI.showYourself)
        goToGraphButton.pack()

        deleteGraphButton = Button(window, text="Delete Graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=deleteGraphUI.showYourself)
        deleteGraphButton.pack()

        openProfileButton = Button(window, text="Open Profile", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=openProfile.openProfile)
        openProfileButton.pack()

        settingsButton = Button(window, text="Settings", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=SettingsUI.showYourself)
        settingsButton.pack()

        donateButton = Button(window, text="Donate", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=donate)
        donateButton.pack()

        quitButton = Button(window, text="Quit", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=window.quit)
        quitButton.pack()



        window.mainloop()