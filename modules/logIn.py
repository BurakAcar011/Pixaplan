import json
from tkinter import *
from tkinter import messagebox
from pathlib import Path
import modules.themeColor as themeColor
THEMECOLOR = themeColor.updateTheme()
FOREGROUND = themeColor.updateForeground()
scriptdir = Path(__file__).parent

class logInUI():
    def showYourself():
        window = Tk()
        window.title("Pixaplan - Log In")
        window.config(bg=THEMECOLOR, padx=50, pady=50)

        grandTitle = Label(window, text="Change Deafult Account", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 24, "bold"))
        grandTitle.pack(pady=10)
        subtitle = Label(window, text="This will be the account that will be used throughout the app.", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12))
        subtitle1 = Label(window, text="This has to be an already existing account.", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12))
        subtitle.pack()
        subtitle1.pack()

        usernamee = Entry(window, text="Username", width=30)
        usernamee.insert(0, "Username")
        usernamee.pack(pady=10)
        password = Entry(window, text="Password", width=30)
        password.insert(0, "Password")
        password.pack(pady=10)

        def Apply():
            with open(scriptdir / "accountData.json", "w") as file:
                initialData = {
                    "username": usernamee.get(),
                    "token": password.get(),
                    "agreeTermsOfService": "yes",
                    "notMinor": "yes",
                }
                json.dump(initialData, file)
                messagebox.showinfo("Success", "Account data saved successfully! If the data entered is wrong, the app functions will not work.")
                window.destroy()
        ApplyButton = Button(window, text="Apply", command=Apply)
        ApplyButton.pack(pady=10)

        finePrint = Label(window, text="By pressing Apply you agree that the account entered follows Pixela's Terms of Service", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 7))
        finePrint.pack()
        finePrintcont = Label(window, text="and that the account holder is either not a minor or has parental consent.", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 7))
        finePrintcont.pack()