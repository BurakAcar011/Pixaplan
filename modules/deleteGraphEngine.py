def deleteGraph(id, usernamee, password):
    import requests
    import json
    from pathlib import Path
    from tkinter import messagebox
    scriptdir = Path(__file__).parent

    usernamefile = open(scriptdir / "accountData.json", "r")
    username = json.load(usernamefile)["username"]
    tokenfile = open(scriptdir / "accountData.json", "r")
    header = {
        "X-USER-TOKEN": password
    }
    response = requests.delete(f"https://pixe.la/v1/users/{usernamee}/graphs/{id}", headers=header)
    jsonresponse = response.json()

    if jsonresponse.get("isSuccess", True):
        messagebox.showinfo("Success", f"{id} has been terminated")
    else:
        if "isRejected" in jsonresponse and jsonresponse["isRejected"]:
            messagebox.showerror("Request Denied", "Pixaplan uses Pixela to graph your habits. Because you are not a Pixela supporter, your requests will be denied 25% of the time. Please try deleting the graph again.")
        else:
            messagebox.showerror("Error", jsonresponse.get("message"))