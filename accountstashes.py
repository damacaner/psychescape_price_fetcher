import requests
import json
import os
from modules import scarabvals, skillgems, general, crafting, uniques

raw_data = requests.get("https://api.pathofexile.com/stash")
headers = {
    "User-Agent": "Mozilla/5.0",
    "Authorization": "censored for github",
    "Cookie": "censored for github"
}


class StashIDs():
    def __init__(self, name=" ", id=" ", index=" ", typeline=" "):
        self.name = name
        self.id = id
        self.index = index
        self.typeLine = typeline

    def stashids(self):
        raw_data = requests.get("https://api.pathofexile.com/stash/Scourge", headers=headers)
        data_r = raw_data.text
        data = json.loads(data_r)
        print(data)
        with open("stashid.txt", "w") as file:
            file.write(" ")
        for i in data["stashes"]:
            exportlist = []
            print("Stash tab> {}".format(i["index"] + 1))
            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            self.name = i["name"]
            self.id = i["id"]
            self.index = i["index"]
            exportlist.append(self)
            result = json.dumps(exportlist, default=lambda o: o.__dict__)
            with open("stashid.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


class GetStash():
    def __init__(self, stackSize=0, note=" ", x=" ", y=" ", inventoryId=" ", typeline=" ", sglvl = "", sgqual = " "):
        self.stacksize = stackSize
        self.note = note
        self.x = x
        self.y = y
        self.inventoryID = inventoryId
        self.typeLine = typeline
        self.sglvl = sglvl
        self.sgqual = sgqual

    def StashNotes(self):
        raw_data = requests.get("https://api.pathofexile.com/stash/Scourge/378f3aa85a", headers=headers)
        data_r = raw_data.text
        data = json.loads(data_r)
        print(data)
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        with open("getstash.txt", "w") as file:
            file.write(" ")
        for i in data["stash"]:
            for j in (data["stash"]["items"]):
                if "properties" in j:
                    for  z in j["properties"]:
                        if z["name"] == "Level":
                            self.sglvl = (z["values"][0][0])
                        if z["name"] == "Quality":
                            self.sgqual = (z["values"][0][0])
                else:
                    self.sglvl = None
                    self.sgqual = None
                exportlist = []
                os.chdir(
                    r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
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
                       returnoutput = search.Search(searchvar,self.sglvl,0)
                       if returnoutput == None:
                           self.note = "Unknown"
                       else:
                           exalted_value, chaos_value, curr_type = returnoutput
                           if exalted_value == 0:
                               conc = str(chaos_value).split(".")[0] + " " + str(curr_type.lower())
                               print(conc)
                               self.note = conc
                           else:
                               conc = str(exalted_value).split(".")[0] + " " + str(curr_type.lower())
                               print(conc)
                               self.note = conc
                    else:
                       returnoutput = search.Search(searchvar, self.sglvl, self.sgqual)
                       if returnoutput == None:
                           self.note = "Unknown"
                       else:
                           exalted_value, chaos_value, curr_type = returnoutput
                           if exalted_value == 0:
                               conc = str(chaos_value).split(".")[0] + " " + str(curr_type.lower())
                               print(conc)
                               self.note = conc
                           else:
                               conc = str(exalted_value).split(".")[0] + " " + str(curr_type.lower())
                               print(conc)
                               self.note = conc
                self.typeLine = j["typeLine"]
                exportlist.append(self)
                result = json.dumps(exportlist, default=lambda o: o.__dict__)
                with open("getstash.txt", "r") as file:
                    if str(result) in file.read():
                        # print("We already priced {} !".format(self.typeLine))
                        file.close()
                    else:
                        file.close()
                        with open("getstash.txt", "a") as file2:
                            file2.write(str(result))
                            file2.write("\n")
                            file2.close()


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
