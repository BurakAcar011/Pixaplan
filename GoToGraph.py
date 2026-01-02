import webbrowser
import json
from pathlib import Path
scriptdir = Path(__file__).parent

with open(scriptdir / "modules" / "accountData.json", "r") as file:
    username = json.load(file)["username"]
with open(scriptdir / "modules" / "accountData.json", "r") as file:
    password = json.load(file)["token"]
with open(scriptdir / "modules" / "graphData.json", "r") as file:
    graphID = json.load(file)["id"]


webbrowser.open(f"https://pixe.la/v1/users/{username}/graphs/{graphID}.html")