from tkinter import *
from tkinter import messagebox
import modules.themeColor as themeColor
from modules.createAccountEngine import accountCreate
import modules.themeColor as themeColor
THEMECOLOR = themeColor.updateTheme()
FOREGROUND = themeColor.updateForeground()

class CreateAccountUI():
    def showYourself():
        window = Tk()
        window.title("Pixaplan - Create Account")
        window.config(bg=THEMECOLOR, padx=100, pady=100)

        title = Label(window, text="Create Account", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 24, "bold"))
        title.pack(pady=10)

        usernameEntry = Entry(window, width=30, font=("Arial", 12))
        usernameEntry.insert(0, "Username")
        usernameEntry.pack(pady=5)

        passwordEntry = Entry(window, width=30, font=("Arial", 12))
        passwordEntry.insert(0, "Password")
        passwordEntry.pack(pady=5)

        def startMakeAccount():
            accountCreate(usernameEntry.get(), passwordEntry.get())
        submitButton = Button(window, text="Create Account", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=startMakeAccount)
        submitButton.pack(pady=10)

        finePrint = Label(window, text="By creating an account you agree to the Terms of Service of Pixela", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 7))
        finePrint.pack()
        finePrintcont = Label(window, text="and agree that you are either not a minor or you have parental consent to use Pixaplan and Pixela", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 7))
        finePrintcont.pack()