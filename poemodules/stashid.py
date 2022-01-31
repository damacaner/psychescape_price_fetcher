import requests
import json
headers = {
    "User-Agent": "Mozilla/5.0",
    "Authorization": "Bearer dc87aed8472e9917d62cb644abc576cb6923078d",
    "Cookie": "POESESSID=232f3a4e11b6e55f98feab1b21b3621c"
}
class StashIDFetch():
    def __init__(self,id = " ", name = " "):
        self.id = id
        self.name = name
    def StashID(self):
     raw_data = requests.get("https://api.pathofexile.com/stash/Scourge", headers=headers)
     data_r = raw_data.text
     data = json.loads(data_r)
     with open("stashid.txt", "w") as file:
         file.write(" ")
     for i in data["stashes"]:
         exportlist = []
         self.name = i["name"]
         self.id = i["id"]
         exportlist.append(self)
         with open("stashid.txt", "a") as file:
             result = json.dumps(exportlist, default=lambda o: o.__dict__)
             file.write(result)
             file.write("\n")