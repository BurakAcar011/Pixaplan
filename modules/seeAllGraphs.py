import requests
from tkinter import messagebox
from tkinter import *
import json
from modules.themeColor import updateTheme, updateForeground
from pathlib import Path
scriptdir = Path(__file__).parent
BACKGROUND = updateTheme()
FOREGROUND = updateForeground()

class seeAllGraphsUI():
    def showYourself():
        window = Tk()
        window.title("Pixaplan - See All Graphs")
        window.config(bg=BACKGROUND, padx=50, pady=50)

        grandTitle = Label(window, text="Pixaplan - See All Graphs", bg=BACKGROUND, fg=FOREGROUND, font=("Arial", 24, "bold"))
        grandTitle.pack(pady=10)

        with open(scriptdir / "accountData.json", "r") as file:
            usernamee = json.load(file)["username"]
        with open(scriptdir / "accountData.json", "r") as file:
            passwordd = json.load(file)["token"]

        usernameEntry = Entry(window, font=("Arial", 24), width=20)
        usernameEntry.pack()
        usernameEntry.insert(0, usernamee)

        passwordEntry = Entry(window, font=("Arial", 24), width=20)
        passwordEntry.pack()
        passwordEntry.insert(0, passwordd)

        header = {
            "X-USER-TOKEN": passwordEntry.get()
        }

        request = requests.get(f"https://pixe.la/v1/users/{usernameEntry.get()}/graphs", headers=header)
        jsonrequest = request.json()

        def seeGraphs():
            print(jsonrequest)  # Debugging: Print the API response to inspect its structure

            # Check if the request was successful
            if jsonrequest.get("isSuccess", False):
                # Retrieve the list of graphs
                graphs = jsonrequest.get("graphs", [])
                if not graphs:
                    messagebox.showinfo("No Graphs", "No graphs found for this user.")
                    return

                # Build a single string with all graph details
                graph_details = ""
                for graph in graphs:
                    graphID = graph.get("id", "Unknown ID")
                    graphName = graph.get("name", "Unknown Name")
                    graph_details += f"ID: {graphID}, Name: {graphName}\n"

                # Display all graphs in a single messagebox
                messagebox.showinfo("All Graphs", graph_details)
            else:
                # Handle errors or rejections
                if "isRejected" in jsonrequest and jsonrequest["isRejected"]:
                    messagebox.showerror(
                        "Request Denied",
                        "Pixaplan uses Pixela to graph your habits. Because you are not a Pixela supporter, your requests will be denied 25% of the time. Please try performing the action again."
                    )
                else:
                    messagebox.showerror("Error", jsonrequest.get("message", "An unknown error occurred."))

        graphButton = Button(window, text="See Graphs", bg=BACKGROUND, fg=FOREGROUND, font=("Arial", 12), padx=20, pady=10, command=seeGraphs)
        graphButton.pack(pady=5)
        
        window.mainloop()
