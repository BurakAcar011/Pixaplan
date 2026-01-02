def graphCreate(paramdict):
    import requests
    from tkinter import messagebox
    import json
    from pathlib import Path
    scriptdir = Path(__file__).parent

    def saveInfo():
        with open(scriptdir / "graphData.json", "w") as file:
            json.dump(paramdict, file)
    
    with open(scriptdir / "accountData.json", "r") as file:
        header = {
            "X-USER-TOKEN": json.load(file)["token"]
        }

    # print(paramdict)

    with open(scriptdir / "accountData.json", "r") as file:
        graphEndpoint = f"https://pixe.la/v1/users/{json.load(file)["username"]}/graphs/"
        request = requests.post(graphEndpoint, headers=header, json=paramdict)
        jsonrequest = request.json()

        if jsonrequest.get("isSuccess", True):
            messagebox.showinfo("Success", "Graph created successfully!")
            saveInfo()
        else:
            messagebox.showerror("Error", jsonrequest.get("message", "Unknown error"))