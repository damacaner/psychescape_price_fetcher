import urllib.request

import requests
import json
import os

global chaos_ex_ratio
import sys
from os.path import exists
from urllib.request import Request, urlopen, URLopener
from PIL import Image

'''
CRAFTING ECONOMY
CRAFTING
Base Types
Fossils
Resonators
Helmet Enchants ( I WILL NOT IMPLEMENT HELMET ENCHANTS )
Beasts
Essences
Vials
'''
response_API = requests.get("https://poe.ninja/api/data/currencyoverview?league=Scourge&type=Currency")
data = response_API.text
parse_json = json.loads(data)
for i in parse_json["lines"]:
    if i["currencyTypeName"] == ("Exalted Orb"):
        chaos_ex_ratio = i["receive"]["value"]


class SearchEssences(list):

    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("essences.txt", "r") as f:
            lines = f.readlines()  ## Read all the lines
        i = 0
        for line in lines:
            i += 1
            item = line.strip()  ## Strip \n from the lines
            parsed = json.loads(item)[0]  ## Load the i'th line with json
            name_list = parsed["name"]  ## Extract the name_list
            if searchvar in name_list:  ## If searched term is in searchvar go through
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type.lower())
                return exalted_value, chaos_value, curr_type
            elif searchvar.title() in name_list:
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type.lower())
                return exalted_value, chaos_value, curr_type
            else:
                pass


class EssenceValues:
    exportfunction = SearchEssences()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Essence_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/itemoverview?league=Scourge&type=Essence")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("essences.txt", "w") as file:
            file.write(" ")
        j = 0
        for i in parse_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.currType = "Exalted Orb"
                exportlist.append(self)
                self.exportfunction.append(self)
                os.chdir(
                    r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\icons")
                img_name = (i["name"] + ".jpg")
                file_exists = os.path.exists(img_name)
                if file_exists == True:
                    pass
                else:
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
                    urllib.request.install_opener(opener)
                    urllib.request.urlretrieve(i["icon"], img_name)
            else:
                self.name = i["name"]
                self.chaosValue = i["chaosValue"]
                self.currType = "Chaos Orb"
                exportlist.append(self)
                self.exportfunction.append(self)
                os.chdir(
                    r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\icons")
                img_name = (i["name"] + ".jpg")
                file_exists = os.path.exists(img_name)
                if file_exists == True:
                    pass
                else:
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
                    urllib.request.install_opener(opener)
                    urllib.request.urlretrieve(i["icon"], img_name)
            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            result = json.dumps(exportlist, default=lambda o: o.__dict__)
            with open("essences.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()

    def Check_Incus(self):
        pass
        # TODO Get every incubators on character's stash. PoE still didnt give me an authorization key.


class SearchFossils(list):

    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("fossils.txt", "r") as f:
            lines = f.readlines()  ## Read all the lines
        i = 0
        for line in lines:
            i += 1
            item = line.strip()  ## Strip \n from the lines
            parsed = json.loads(item)[0]  ## Load the i'th line with json
            name_list = parsed["name"]  ## Extract the name_list
            if searchvar in name_list:  ## If searched term is in searchvar go through
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            elif searchvar.title() in name_list:
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            else:
                pass


class FossilVals:
    exportfunction = SearchFossils()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Fossil_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/itemoverview?league=Scourge&type=Fossil")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("fossils.txt", "w") as file:
            file.write(" ")
        for i in parse_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.currType = "Exalted Orb"
                os.chdir(
                    r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\icons")
                img_name = (i["name"] + ".jpg")
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(i["icon"], img_name)
                exportlist.append(self)
                self.exportfunction.append(self)
                os.chdir(
                    r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\icons")
                img_name = (i["name"] + ".jpg")
                file_exists = os.path.exists(img_name)
                if file_exists == True:
                    pass
                else:
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
                    urllib.request.install_opener(opener)
                    urllib.request.urlretrieve(i["icon"], img_name)
            else:
                self.name = i["name"]
                self.chaosValue = i["chaosValue"]
                self.currType = "Chaos Orb"
                exportlist.append(self)
                self.exportfunction.append(self)
                os.chdir(
                    r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\icons")
                img_name = (i["name"] + ".jpg")
                file_exists = os.path.exists(img_name)
                if file_exists == True:
                    pass
                else:
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
                    urllib.request.install_opener(opener)
                    urllib.request.urlretrieve(i["icon"], img_name)
            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            result = json.dumps(exportlist, default=lambda o: o.__dict__)
            with open("fossils.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


class SearchResonators(list):

    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("resonators.txt", "r") as f:
            lines = f.readlines()  ## Read all the lines
        i = 0
        for line in lines:
            i += 1
            item = line.strip()  ## Strip \n from the lines
            parsed = json.loads(item)[0]  ## Load the i'th line with json
            name_list = parsed["name"]  ## Extract the name_list
            if searchvar in name_list:  ## If searched term is in searchvar go through
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            elif searchvar.title() in name_list:
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            else:
                pass


class ResoValues:
    exportfunction = SearchResonators()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" ", ):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Reso_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/itemoverview?league=Scourge&type=Resonator")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("resonators.txt", "w") as file:
            file.write(" ")
        j = 0
        for i in parse_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.currType = "Exalted Orb"
                exportlist.append(self)
                self.exportfunction.append(self)
                os.chdir(
                    r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\icons")
                img_name = (i["name"] + ".jpg")
                file_exists = os.path.exists(img_name)
                if file_exists == True:
                    pass
                else:
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
                    urllib.request.install_opener(opener)
                    urllib.request.urlretrieve(i["icon"], img_name)
            else:
                self.name = i["name"]
                self.chaosValue = i["chaosValue"]
                self.currType = "Chaos Orb"
                exportlist.append(self)
                ## DOWNLOAD ICONS (WILL BE USEFUL LATER)
                os.chdir(
                    r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\icons")
                img_name = (i["name"] + ".jpg")
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(i["icon"], img_name)
                j = j + 1
                ## WRITE ICON DATA TO IMG NAME
                self.exportfunction.append(self)
                j = j + 1
            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            result = json.dumps(exportlist, default=lambda o: o.__dict__)
            with open("resonators.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


class SearchBeast(list):

    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("beast.txt", "r") as f:
            lines = f.readlines()  ## Read all the lines
        i = 0
        for line in lines:
            i += 1
            item = line.strip()  ## Strip \n from the lines
            parsed = json.loads(item)[0]  ## Load the i'th line with json
            name_list = parsed["name"]  ## Extract the name_list
            if searchvar in name_list:  ## If searched term is in searchvar go through
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            elif searchvar.title() in name_list:
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            else:
                pass


class BeastValues:
    exportfunction = SearchResonators()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Beast_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/ItemOverview?league=Scourge&type=Beast&language=en")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("beast.txt", "w") as file:
            file.write(" ")
        j = 0
        for i in parse_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.currType = "Exalted Orb"
                exportlist.append(self)
                self.exportfunction.append(self)
            else:
                self.name = i["name"]
                self.chaosValue = i["chaosValue"]
                self.currType = "Chaos Orb"
                exportlist.append(self)
                self.exportfunction.append(self)
                self.exaltedValue = 0
            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            result = json.dumps(exportlist, default=lambda o: o.__dict__)
            with open("beast.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


def main():
    print("Are you sure this is gonna be the main function?")
    sys.exit(0)


if __name__ == "__main__":
    main()
