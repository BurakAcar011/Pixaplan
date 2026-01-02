def accountCreate(username, token):
    import requests
    from tkinter import messagebox
    from pathlib import Path
    import json
    scriptdir = Path(__file__).parent
    prompt = messagebox.askokcancel(title="Pixaplan - Account Creation", message="Store your password safely; you will need it from this point on. \n \n If you already created an account on this device, the deafult account will be replaced with this one, if sucessful. \n \n Continue?")
    if prompt:
        pixela_endpoint = "https://pixe.la/v1/users"
        userParams = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
        }

        response = requests.post(url=pixela_endpoint, json=userParams)
        jsonresponse = response.json()
        if not jsonresponse["isSuccess"]:
            messagebox.showerror(title="Info", message=jsonresponse["message"])
        else: #If account was created sucessfully:
            messagebox.showinfo(title="Pixaplan - Account Creation", message="Account created successfully!")
            
            with open(scriptdir / "accountData.json", "w") as file:
                initialData = {
                    "username": username,
                    "token": token,
                    "agreeTermsOfService": "yes",
                    "notMinor": "yes",
                }
                json.dump(initialData, file)


    else: #If cancel button is pressed
        messagebox.showinfo(title="Pixaplan - Account Creation", message="Account creation cancelled.")