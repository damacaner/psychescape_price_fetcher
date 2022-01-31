import requests
import json
import os
from modules import scarabvals, skillgems, general, crafting, uniques
from poemodules import stashid
headers = {
    "User-Agent": "Mozilla/5.0",
    "Authorization": "Censored till I learn .gitignore",
    "Cookie": "Same as above"
}


class GetStash():
    def __init__(self, stackSize=0, note=" ", x=" ", y=" ", inventoryId=" ", typeline=" ", sglvl="", sgqual=" "):
        self.stacksize = stackSize
        self.note = note
        self.x = x
        self.y = y
        self.inventoryID = inventoryId
        self.typeLine = typeline
        self.sglvl = sglvl
        self.sgqual = sgqual

    def StashNotes(self):
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\poemodules")
        with open("stashid.txt", "r") as file:
            stashiddata = file.readlines()
        for lines in stashiddata:
            lines_json = json.loads(lines)
            url = ("https://api.pathofexile.com/stash/Scourge/" + str(lines_json[0]["id"]))
            raw_data = requests.get(url, headers=headers)
            data_r = raw_data.text
            data = json.loads(data_r)
            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\stashvalues")
            folder = (
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\stashvalues")
            stashtxt = (str(lines_json[0]["name"])).replace("~b/o", "buyout") + ".txt"
            with open(stashtxt, "w") as file:
                file.write(" ")
            for i in data["stash"]:
                if "items" in i:
                    for j in (data["stash"]["items"]):
                        if "properties" in j:
                            for z in j["properties"]:
                                if z["name"] == "Level":
                                    self.sglvl = (z["values"][0][0])
                                if z["name"] == "Quality":
                                    self.sgqual = (z["values"][0][0])
                        else:
                            self.sglvl = None
                            self.sgqual = None
                        exportlist = []
                        os.chdir(
                            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\stashvalues")
                        self.x = j["x"]
                        self.y = j["y"]
                        self.inventoryID = j["inventoryId"]
                        if "note" in j:
                            self.note = j["note"]
                        else:
                            searchvar = j["typeLine"]
                            print(searchvar)
                            search = SearchUnknown()
                            if self.sgqual == None:
                                returnoutput = search.Search(searchvar, self.sglvl, 0)
                                if returnoutput == None:
                                    self.note = "Unknown"
                                else:
                                    exalted_value, chaos_value, curr_type = returnoutput
                                    if exalted_value == 0:
                                        conc = str(chaos_value) + " " + str(curr_type.lower()).replace("orb", "")
                                        print(conc)
                                        self.note = conc
                                    else:
                                        conc = str(exalted_value) + " " + str(curr_type.lower()).replace("orb", "")
                                        print(conc)
                                        self.note = conc
                            else:
                                returnoutput = search.Search(searchvar, self.sglvl, self.sgqual)
                                if returnoutput == None:
                                    self.note = "Unknown"
                                else:
                                    exalted_value, chaos_value, curr_type = returnoutput
                                    if exalted_value == 0:
                                        conc = str(chaos_value) + " " + str(curr_type.lower()).replace("orb", "")
                                        print(conc)
                                        self.note = conc
                                    else:
                                        # .split(".")[0]
                                        conc = str(exalted_value) + " " + str(curr_type.lower()).replace("orb", "")
                                        print(conc)
                                        self.note = conc
                        self.typeLine = j["typeLine"]
                        exportlist.append(self)
                        result = json.dumps(exportlist, default=lambda o: o.__dict__)
                        os.chdir(folder)
                        with open(stashtxt, "r") as file:
                            if str(result) in file.read():
                                # print("We already priced {} !".format(self.typeLine))
                                file.close()
                            else:
                                file.close()
                                with open(stashtxt, "a") as file2:
                                    file2.write(str(result))
                                    file2.write("\n")
                                    file2.close()
                else:
                    pass

'''
CLUSTERFUCK OF NESTED IF'S AHEAD PROCEED WITH CAUTION
I DIDNT COMMENT ANYTHING
BE WARY
'''


class SearchUnknown():
    def Search(self, searchvar, gemlvl, gemqual):
        ## First iteration
        search = scarabvals.SearchScarab()
        returnoutput = search.search(searchvar)
        if returnoutput is None:
            ## Second Iteration
            search = general.SearchOil()
            returnoutput = search.search(searchvar)
            if returnoutput is None:
                ## Third Iteration
                search = general.SearchIncus()
                returnoutput = search.search(searchvar)
                if returnoutput is None:
                    ## Fourth Iteration
                    search = general.DivSearch()
                    returnoutput = search.search(searchvar)
                    if returnoutput is None:
                        ## Fifth Iteration
                        search = general.ArtifactSearch()
                        returnoutput = search.search(searchvar)
                        if returnoutput is None:
                            ## Sixth Iteration
                            search = general.SearchFrags()
                            returnoutput = search.search(searchvar)
                            if returnoutput is None:
                                ## Seventh Iteration, finished searching on general values passing to crafting economy.
                                search = crafting.SearchBeast()
                                returnoutput = search.search(searchvar)
                                if returnoutput is None:
                                    search = crafting.SearchFossils()
                                    returnoutput = search.search(searchvar)
                                    if returnoutput is None:
                                        ## 8th Iteration, fuck this shit
                                        search = crafting.SearchEssences()
                                        returnoutput = search.search(searchvar)
                                        if returnoutput is None:
                                            ## 9th Iteration
                                            search = crafting.SearchResonators()
                                            returnoutput = search.search(searchvar)
                                            if returnoutput is None:
                                                ## 10th Iteration, search on skill gems.
                                                search = skillgems.SearchSG()
                                                returnoutput = search.search(searchvar, gemlvl, gemqual)
                                                if returnoutput is None:
                                                    ## 11th Iteration, unique item values.
                                                    search = uniques.UArmourSearch()
                                                    returnoutput = search.search(searchvar)
                                                    if returnoutput is None:
                                                        search = uniques.UWeaponSearch()
                                                        returnoutput = search.search(searchvar)
                                                        if returnoutput is None:
                                                            search = uniques.UAccessorySearch()
                                                            returnoutput = search.search(searchvar)
                                                            if returnoutput is None:
                                                                search = uniques.UJewelSearch()
                                                                returnoutput = search.search(searchvar)
                                                                if returnoutput is None:
                                                                  search = general.SearchRatio()
                                                                  returnoutput = search.search(searchvar)
                                                                  if returnoutput is None:
                                                                     pass
                                                                  else:
                                                                      exval, chval, currtype = returnoutput
                                                                      return exval, chval, currtype
                                                                else:
                                                                  exval, chval, currtype = returnoutput
                                                                  return exval, chval, currtype
                                                            else:
                                                                exval, chval, currtype = returnoutput
                                                                return exval, chval, currtype

                                                        else:
                                                            exval, chval, currtype = returnoutput
                                                            return exval, chval, currtype
                                                    else:
                                                        exval, chval, currtype = returnoutput
                                                        return exval, chval, currtype
                                                else:
                                                    exval, chval, currtype = returnoutput
                                                    return exval, chval, currtype
                                            else:
                                                exval, chval, currtype = returnoutput
                                                return exval, chval, currtype
                                        else:
                                            print(returnoutput)
                                            exval, chval, currtype = returnoutput
                                            print(exval, chval, currtype)
                                            return exval, chval, currtype
                                else:
                                    exval, chval, currtype = returnoutput
                                    return exval, chval, currtype
                            else:
                                exval, chval, currtype = returnoutput
                                return exval, chval, currtype
                        else:
                            exval, chval, currtype = returnoutput
                            return exval, chval, currtype
                    else:
                        exval, chval, currtype = returnoutput
                        return exval, chval, currtype
                else:
                    exval, chval, currtype = returnoutput
                    return exval, chval, currtype
            else:
                exval, chval, currtype = returnoutput
                return exval, chval, currtype
        else:
            exval, chval, currtype = returnoutput
            return exval, chval, currtype
