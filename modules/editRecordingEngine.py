def record(username, password, graphID, month, day, year, quantity):
    import requests
    from tkinter import messagebox
    
    header = {
        "X-USER-TOKEN": password
    }

    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    
    date = f"{year}{month}{day}"
    params = {
        "quantity": quantity
    }

    request = requests.post(f"https://pixe.la/v1/users/{username}/graphs/{graphID}/{date}", json=params, headers=header)
    jsonrequest = request.json()

    # print(jsonrequest)
    if jsonrequest.get("isSuccess", True):
        messagebox.showinfo("Success", "Recording updated successfully")
    else:
        if "isRejected" in jsonrequest and jsonrequest["isRejected"]:
            messagebox.showerror("Request Denied", "Pixaplan uses Pixela to graph your habits. Because you are not a Pixela supporter, your requests will be denied 25% of the time. Please try recording the habit again.")
        else:
            messagebox.showerror("Error", jsonrequest.get("message"))