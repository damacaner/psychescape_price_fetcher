import requests
import json
import os
import time
from ratelimiter import RateLimiter
from ratelimit import limits, RateLimitException, sleep_and_retry
max_hit = 15
period = 30
headers = {
    "censor"
}
class StashIDFetch():
    def __init__(self,id = " ", name = " ", index=0):
        self.id = id
        self.name = name
        self.index = index
    @limits(calls=max_hit, period=period)
    def StashID(self):
     raw_data = requests.get("https://api.pathofexile.com/stash/Standard", headers=headers)
     time.sleep(10)  ## Rate the API. Yeah.
     data_r = raw_data.text
     data = json.loads(data_r)
     os.chdir(
         r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\poemodules")
     with open("stashid.txt", "w") as file:
         file.write(" ")
     for i in data["stashes"]:
         exportlist = []
         self.name = i["name"]
         self.id = i["id"]
         self.index = i["index"]
         exportlist.append(self)
         with open("stashid.txt", "a") as file:
             result = json.dumps(exportlist, default=lambda o: o.__dict__)
             file.write(result)
             file.write("\n")
