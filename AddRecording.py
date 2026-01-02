import datetime as dt
import json
from time import sleep
from modules.recordHabitEngine import record
from pathlib import Path
scriptdir = Path(__file__).parent


month = str(dt.datetime.now().month)
day = str(dt.datetime.now().day)
year = str(dt.datetime.now().year)
if len(month) == 1:
    month = "0" + month
if len(day) == 1:
    day = "0" + day

date = f"{year}{month}{day}"

with open(scriptdir / "modules" / "accountData.json", "r") as file:
    username = json.load(file)["username"]
with open(scriptdir / "modules" / "accountData.json", "r") as file:
    password = json.load(file)["token"]

with open(scriptdir / "modules" /"graphData.json", "r") as file:
    graphID = json.load(file)["id"]

quantity = input("How much? (number only, don't include units) ")

record(username, password, graphID, month, day, year, quantity)