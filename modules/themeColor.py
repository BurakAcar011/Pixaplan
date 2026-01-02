# def updateTheme():
#     import json
#     from pathlib import Path
#     scriptdir = Path(__file__).parent
#     with open(scriptdir / "theme.json", "r") as file:
#         return json.load(file)["color"]

def updateTheme():
    import json
    from pathlib import Path
    scriptdir = Path(__file__).parent
    theme_file = scriptdir / "theme.json"

    try:
        with open(theme_file, "r") as file:
            return json.load(file)["color"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        # Handle missing file, invalid JSON, or missing "color" key
        return "#375362"  # Default color
    
def updateForeground():
    import json
    from pathlib import Path
    scriptdir = Path(__file__).parent
    theme_file = scriptdir / "theme.json"

    try:
        with open(theme_file, "r") as file:
            return json.load(file)["foreground"]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        # Handle missing file, invalid JSON, or missing "foreground" key
        return "white"  # Default foreground color