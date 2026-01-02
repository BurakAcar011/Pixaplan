from tkinter import *
import modules.themeColor as themeColor
import json

from modules.theme import themeUI
from modules.logIn import logInUI
from modules.settingsDeafultGraph import deafultGraphUI
THEMECOLOR = themeColor.updateTheme()
FOREGROUND = themeColor.updateForeground()

class SettingsUI():
    def showYourself():
        window = Tk()
        window.title("Pixaplan - Settings")
        window.config(bg=THEMECOLOR, padx=50, pady=50)

        grandTitle = Label(window, text="Settings", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 24, "bold"))
        grandTitle.pack(pady=10)

        changeDeafultAccountButton = Button(window, text="Deafult Account", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=logInUI.showYourself)
        changeDeafultAccountButton.pack()

        changeDeafultGraphButton = Button(window, text="Deafult Graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=deafultGraphUI.showYourself)
        changeDeafultGraphButton.pack()

        themeButton = Button(window, text="Change Theme", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=themeUI.showYourself)
        themeButton.pack()
