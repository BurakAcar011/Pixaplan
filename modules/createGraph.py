# from tkinter import *
# from tkinter import messagebox
# from themeColor import updateTheme, updateForeground
# import createGraphEngine

# THEMECOLOR = updateTheme()
# FOREGROUND = updateForeground()

# class createGraphUI():
#     def showYourself():
#         window = Tk()
#         window.title("Pixaplan - Create Graph")
#         window.config(bg=THEMECOLOR, padx=50, pady=50)
        
#         grandTitle = Label(window, text="Create Graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 24, "bold"))
#         grandTitle.pack(pady=0)

#         entryNote = Label(window, text="Enter a unique ID for your graph. Make sure you remember it.", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 10))
#         entryNote.pack(pady=0)
#         idEntry = Entry(window, width=30)
#         idEntry.insert(0, "Graph ID (eg. graph1)")
#         idEntry.pack(pady=5) #Only for the ID. The other entries will not have a note

#         nameEntry = Entry(window, width=30)
#         nameEntry.insert(0, "Graph Name (eg. cycling)")
#         nameEntry.pack(pady=5)

#         unitEntry = Entry(window, width=30)
#         unitEntry.insert(0, "Graph Unit (eg. miles)")
#         unitEntry.pack(pady=5)

#         measurementType = StringVar()
#         measurementType.set("float")

#         integerRadio = Radiobutton(window, text="Integer (my measurement will not be a decimal)", variable=measurementType, value="int", bg=THEMECOLOR, fg=FOREGROUND, selectcolor=THEMECOLOR)
#         integerRadio.pack(pady=1)

#         floatRadio = Radiobutton(window, text="Float (my measurement will be a decimal)", variable=measurementType, value="float", bg=THEMECOLOR, fg=FOREGROUND, selectcolor=THEMECOLOR)
#         floatRadio.pack(pady=1)

#         paddingText = Label(window, text="", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 10))
#         paddingText.pack(pady=2)

#         colorLabel = Label(window, text="Select a color for your graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 10))
#         colorLabel.pack(pady=0)

#         colorOptions = ["shibafu (green)", "momiji (red)", "sora (blue)", "ichou (yellow)", "ajisai (purple)", "kuro (black)"]
#         colorVariable = StringVar(window)
#         colorVariable.set(colorOptions[0])  # Set the default value to the first color option
#         colorMenu = OptionMenu(window, colorVariable, *colorOptions)
#         colorMenu.config(bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 10))
#         colorMenu.pack(pady=5)


#         def createGraphFunct():
#             params = {
#             "id": idEntry.get(),
#             "name": nameEntry.get(),
#             "unit": unitEntry.get(),
#             "type": measurementType.get(),
#             "color": colorVariable.get().split(" ")[0]
#         }
#             createGraphEngine.graphCreate(params)
#         createGraphButton = Button(window, text="Create Graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=createGraphFunct)
#         createGraphButton.pack(pady=30)

from tkinter import *
from tkinter import messagebox
from modules.themeColor import updateTheme, updateForeground
import modules.createGraphEngine as createGraphEngine

THEMECOLOR = updateTheme()
FOREGROUND = updateForeground()

class createGraphUI():
    def showYourself():
        window = Tk()
        window.title("Pixaplan - Create Graph")
        window.config(bg=THEMECOLOR, padx=50, pady=50)
        
        grandTitle = Label(window, text="Create Graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 24, "bold"))
        grandTitle.pack(pady=0)

        entryNote = Label(window, text="Enter a unique ID for your graph. Make sure you remember it.", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 10))
        entryNote.pack(pady=0)
        idEntry = Entry(window, width=30)
        idEntry.insert(0, "Graph ID (eg. graph1)")
        idEntry.pack(pady=5)

        nameEntry = Entry(window, width=30)
        nameEntry.insert(0, "Graph Name (eg. cycling)")
        nameEntry.pack(pady=5)

        unitEntry = Entry(window, width=30)
        unitEntry.insert(0, "Graph Unit (eg. miles)")
        unitEntry.pack(pady=5)

        # Ensure measurementType is assigned correctly
        measurementType = StringVar()
        measurementType.set("float")  # Default value

        integerRadio = Radiobutton(window, text="Integer (my measurement will not be a decimal)", variable=measurementType, value="int", bg=THEMECOLOR, fg=FOREGROUND, selectcolor=THEMECOLOR, command=lambda: measurementType.set("int"))
        integerRadio.pack(pady=1)

        floatRadio = Radiobutton(window, text="Float (my measurement will be a decimal)", variable=measurementType, value="float", bg=THEMECOLOR, fg=FOREGROUND, selectcolor=THEMECOLOR, command=lambda: measurementType.set("float"))
        floatRadio.pack(pady=1)

        textForPadding = Label(window, text="", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 10))
        textForPadding.pack(pady=2)

        colorLabel = Label(window, text="Select a color for your graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 10))
        colorLabel.pack(pady=0)

        colorOptions = ["shibafu (green)", "momiji (red)", "sora (blue)", "ichou (yellow)", "ajisai (purple)", "kuro (black)"]
        colorVariable = StringVar(window)
        colorVariable.set(colorOptions[0])  
        colorMenu = OptionMenu(window, colorVariable, *colorOptions)
        colorMenu.config(bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 10))
        colorMenu.pack(pady=5)

        def createGraphFunct():
            # print("Measurement Type:", measurementType.get())  # Debugging line
            params = {
                "id": idEntry.get(),
                "name": nameEntry.get(),
                "unit": unitEntry.get(),
                "type": measurementType.get(),  # This should now correctly update
                "color": colorVariable.get().split(" ")[0]
            }
            createGraphEngine.graphCreate(params)

        createGraphButton = Button(window, text="Create Graph", bg=THEMECOLOR, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=createGraphFunct)
        createGraphButton.pack(pady=30)

        window.mainloop()
