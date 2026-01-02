from tkinter import *
import modules.themeColor as themeColor
import json
from pathlib import Path
import os
import sys
from time import sleep
THEMECOLOR = themeColor.updateTheme()
from modules.themeColor import updateForeground
FOREGROUND = updateForeground()
scriptdir = Path(__file__).parent


class themeUI():
    def showYourself():
        window = Tk()
        window.title("Pixaplan - Settings")
        window.config(bg=THEMECOLOR, padx=50, pady=50)

        grandTitle = Label(window, text="Settings", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 24, "bold"))
        grandTitle.pack(pady=10)

        #Theme
        themeTitle = Label(window, text="Theme", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 18, "bold"))
        themeTitle.pack(pady=10)


        def restart_program():
            os.execv(sys.executable, ['python'] + sys.argv)

        def deafultTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#375362",
                    "foreground": "white"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()

            restart_program()
        def redTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#FF0000",
                    "foreground": "white"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()
            restart_program()
        def blueTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#2596BE",
                    "foreground": "white"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()
            restart_program()
        def greenTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#00FF00",
                    "foreground": "black"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()
            restart_program()
        def purpleTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#800080",
                    "foreground": "white"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()
            restart_program()
        def yellowTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#FFFF00",
                    "foreground": "black"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()
            restart_program()
        def pinkTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#FFC0CB",
                    "foreground": "black"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()
            restart_program()
        def orangeTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#FFA500",
                    "foreground": "black"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()
            restart_program()
        def greyTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#808080",
                    "foreground": "white"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()
            restart_program()
        def blackTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#000000",
                    "foreground": "white"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()
            restart_program()
        def whiteTheme():
            with open(scriptdir / "theme.json", "w") as file:
                newTheme = {
                    "color": "#FFFFFF",
                    "foreground": "black"
                }
                json.dump(newTheme, file)
                themeColor.updateTheme()
            restart_program()
        
        DeafultTheme = Button(window, text="Default Theme", bg="#375362", fg="white", font=("Arial", 12), command=deafultTheme)
        RedTheme = Button(window, text="Red", bg="#FF0000", fg="white", font=("Arial", 12), command=redTheme)
        BlueTheme = Button(window, text="Blue", bg="#2596BE", fg="white", font=("Arial", 12), command=blueTheme)
        GreenTheme = Button(window, text="Green", bg="#00FF00", fg="black", font=("Arial", 12), command=greenTheme)
        PurpleTheme = Button(window, text="Purple", bg="#800080", fg="white", font=("Arial", 12), command=purpleTheme)
        YellowTheme = Button(window, text="Yellow", bg="#FFFF00", fg="black", font=("Arial", 12), command=yellowTheme)
        PinkTheme = Button(window, text="Pink", bg="#FFC0CB", fg="black", font=("Arial", 12), command=pinkTheme)
        OrangeTheme = Button(window, text="Orange", bg="#FFA500", fg="black", font=("Arial", 12), command=orangeTheme)
        GreyTheme = Button(window, text="Grey", bg="#808080", fg="white", font=("Arial", 12), command=greyTheme)
        BlackTheme = Button(window, text="Black", bg="#000000", fg="white", font=("Arial", 12), command=blackTheme)
        WhiteTheme = Button(window, text="White", bg="#FFFFFF", fg="black", font=("Arial", 12), command=whiteTheme)
        DeafultTheme.pack()
        RedTheme.pack()
        BlueTheme.pack()
        GreenTheme.pack()
        PurpleTheme.pack()
        YellowTheme.pack()
        PinkTheme.pack()
        OrangeTheme.pack()
        GreyTheme.pack()
        BlackTheme.pack()
        WhiteTheme.pack()