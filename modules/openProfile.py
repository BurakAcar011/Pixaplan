def openProfile():
    import webbrowser
    import json
    from pathlib import Path
    scriptdir = Path(__file__).parent

    with open(scriptdir / "accountData.json", "r") as file:
        username = json.load(file)["username"]
        webbrowser.open(f"https://pixe.la/@{username}")