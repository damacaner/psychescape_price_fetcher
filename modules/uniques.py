import urllib.request

import requests
import json
import os

global chaos_ex_ratio
import sys

response_API = requests.get("https://poe.ninja/api/data/currencyoverview?league=Scourge&type=Currency")
data = response_API.text
parse_json = json.loads(data)
for i in parse_json["lines"]:
    if i["currencyTypeName"] == ("Exalted Orb"):
        chaos_ex_ratio = i["receive"]["value"]


class UWeaponSearch(list):
    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("uniqueweapon.txt", "r") as f:
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
                links = parsed["links"]
                if "levelRequired" in parsed:
                    lvlreq = parsed["levelRequired"]
                    curr_type = parsed["currType"]
                else:
                    lvlreq = 0
                print("----------------")
                print("We have found the >", name)
                print("Linked sockets >", links)
                print("Level Required to Wear >", lvlreq)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return name
            elif searchvar.title() in name_list:
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                links = parsed["links"]
                if "levelRequired" in parsed:
                    lvlreq = parsed["levelRequired"]
                    curr_type = parsed["currType"]
                else:
                    lvlreq = 0
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Linked sockets >", links)
                print("Level Required to Wear >", lvlreq)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return name
            else:
                pass


class UWeaponValues():
    exportfunction = UWeaponSearch()

    def __init__(self, name=" ", links=0, lvlreq=0, chaosValue=0, exaltedValue=0, ):
        self.name = name
        self.links = links
        self.lvlreq = lvlreq
        self.chaosValue = chaosValue
        self.exaltedValue = exaltedValue

    def UniqueWeapons(self):
        raw_data = requests.get("https://poe.ninja/api/data/ItemOverview?league=Scourge&type=UniqueWeapon&language=en")
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        data = raw_data.text
        data_json = json.loads(data)
        with open("uniqueweapon.txt", "w") as f:
            f.write(" ")
        for i in data_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.currType = "Exalted Orb"
                self.chaosValue = 0
                if "links" in i:
                    self.links = i["links"]
                else:
                    self.links = 0
                if "levelRequired" in i:
                    self.lvlreq = i["levelRequired"]
                else:
                    self.lvlreq = 0
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
                self.exaltedValue = 0
                self.currType = "Chaos Orb"
                if "links" in i:
                    self.links = i["links"]
                else:
                    self.links = 0
                if "levelRequired" in i:
                    self.lvlreq = i["levelRequired"]
                else:
                    self.lvlreq = 0
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
            with open("uniqueweapon.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


class UArmourSearch(list):
    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("uniquearmour.txt", "r") as f:
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
                links = parsed["links"]
                curr_type = parsed["currType"]
                if "levelRequired" in parsed:
                    lvlreq = parsed["levelRequired"]
                else:
                    lvlreq = 0
                print("----------------")
                print("We have found the >", name)
                print("Linked sockets >", links)
                print("Level Required to Wear >", lvlreq)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            elif searchvar.title() in name_list:
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                links = parsed["links"]
                if "levelRequired" in parsed:
                    lvlreq = parsed["levelRequired"]
                    curr_type = parsed["currType"]
                else:
                    lvlreq = 0
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Linked sockets >", links)
                print("Level Required to Wear >", lvlreq)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            else:
                pass


class UArmourValues():
    exportfunction = UArmourSearch()

    def __init__(self, name=" ", links=0, lvlreq=0, chaosValue=0, exaltedValue=0, ):
        self.name = name
        self.links = links
        self.lvlreq = lvlreq
        self.chaosValue = chaosValue
        self.exaltedValue = exaltedValue

    def UniqueArmours(self):
        raw_data = requests.get("https://poe.ninja/api/data/ItemOverview?league=Scourge&type=UniqueArmour&language=en")
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        data = raw_data.text
        data_json = json.loads(data)
        with open("uniquearmour.txt", "w") as f:
            f.write(" ")
        for i in data_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.currType = "Exalted Orb"
                self.chaosValue = 0
                if "links" in i:
                    self.links = i["links"]
                else:
                    self.links = 0
                if "levelRequired" in i:
                    self.lvlreq = i["levelRequired"]
                else:
                    self.lvlreq = 0
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
                self.exaltedValue = 0
                self.currType = "Chaos Orb"
                if "links" in i:
                    self.links = i["links"]
                else:
                    self.links = 0
                if "levelRequired" in i:
                    self.lvlreq = i["levelRequired"]
                else:
                    self.lvlreq = 0
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
            with open("uniquearmour.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


class UAccessorySearch(list):
    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("uniqueaccessory.txt", "r") as f:
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
                if "levelRequired" in parsed:
                    lvlreq = parsed["levelRequired"]
                else:
                    lvlreq = 0
                print("----------------")
                print("We have found the >", name)
                print("Level Required to Wear >", lvlreq)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            elif searchvar.title() in name_list:
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                if "levelRequired" in parsed:
                    lvlreq = parsed["levelRequired"]
                    curr_type = parsed["currType"]
                else:
                    lvlreq = 0
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Level Required to Wear >", lvlreq)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            else:
                pass


class UAccessoryValues():
    exportfunction = UAccessorySearch()

    def __init__(self, name=" ", lvlreq=0, chaosValue=0, exaltedValue=0, ):
        self.name = name
        self.lvlreq = lvlreq
        self.chaosValue = chaosValue
        self.exaltedValue = exaltedValue

    def UniqueAccessory(self):
        raw_data = requests.get(
            "https://poe.ninja/api/data/ItemOverview?league=Scourge&type=UniqueAccessory&language=en")
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        data = raw_data.text
        data_json = json.loads(data)
        with open("uniqueaccessory.txt", "w") as f:
            f.write(" ")
        for i in data_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.currType = "Exalted Orb"
                self.chaosValue = 0
                if "levelRequired" in i:
                    self.lvlreq = i["levelRequired"]
                else:
                    self.lvlreq = 0
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
                self.exaltedValue = 0
                self.currType = "Chaos Orb"
                if "levelRequired" in i:
                    self.lvlreq = i["levelRequired"]
                else:
                    self.lvlreq = 0
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
            with open("uniqueaccessory.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


class UJewelSearch(list):
    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("uniquejewel.txt", "r") as f:
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
                if "levelRequired" in parsed:
                    lvlreq = parsed["levelRequired"]
                else:
                    lvlreq = 0
                print("----------------")
                print("We have found the >", name)
                print("Level Required to Wear >", lvlreq)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            elif searchvar.title() in name_list:
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                if "levelRequired" in parsed:
                    lvlreq = parsed["levelRequired"]
                    curr_type = parsed["currType"]
                else:
                    lvlreq = 0
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Level Required to Wear >", lvlreq)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return exalted_value, chaos_value, curr_type
            else:
                pass


class UJewelValues():
    exportfunction = UJewelSearch()

    def __init__(self, name=" ", lvlreq=0, chaosValue=0, exaltedValue=0, variant = " " ):
        self.name = name
        self.lvlreq = lvlreq
        self.chaosValue = chaosValue
        self.exaltedValue = exaltedValue
        self.variant = variant
    def UniqueJewel(self):
        raw_data = requests.get(
            "https://poe.ninja/api/data/ItemOverview?league=Scourge&type=UniqueJewel&language=en")
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        data = raw_data.text
        data_json = json.loads(data)
        with open("uniquejewel.txt", "w") as f:
            f.write(" ")
        for i in data_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.currType = "Exalted Orb"
                self.chaosValue = 0
                if "levelRequired" in i:
                    self.lvlreq = i["levelRequired"]
                else:
                    self.lvlreq = 0
                if "variant" in i:
                    self.variant = i["variant"]
                else:
                    self.variant = " "
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
                self.exaltedValue = 0
                self.currType = "Chaos Orb"
                if "levelRequired" in i:
                    self.lvlreq = i["levelRequired"]
                else:
                    self.lvlreq = 0
                if "variant" in i:
                    self.variant = i["variant"]
                else:
                    self.variant = " "
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
            with open("uniquejewel.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


class CLJewelSearch(list):
    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("clusters.txt", "r") as f:
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
                variant = parsed["variant"]
                if "levelRequired" in parsed:
                    lvlreq = parsed["levelRequired"]
                else:
                    lvlreq = 0
                print("----------------")
                print("We have found the >", name)
                print("Variant >", variant)
                print("Level Required to Wear >", lvlreq)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return name
            elif searchvar.title() in name_list:
                name = parsed["name"]
                exalted_value = parsed["exaltedValue"]
                chaos_value = parsed["chaosValue"]
                variant = parsed["variant"]
                if "levelRequired" in parsed:
                    lvlreq = parsed["levelRequired"]
                    curr_type = parsed["currType"]
                else:
                    lvlreq = 0
                curr_type = parsed["currType"]
                print("----------------")
                print("We have found the >", name)
                print("Variant >", variant)
                print("Level Required to Wear >", lvlreq)
                print("Exalted Orb Value >", exalted_value)
                print("Chaos Orb Value >", chaos_value)
                print("Currency Type >", curr_type)
                return name
            else:
                pass


class CLJewelValues():
    exportfunction = CLJewelSearch()

    def __init__(self, name=" ", lvlreq=0, chaosValue=0, exaltedValue=0, variant=" "):
        self.name = name
        self.lvlreq = lvlreq
        self.variant = variant
        self.chaosValue = chaosValue
        self.exaltedValue = exaltedValue

    def UniqueJewel(self):
        raw_data = requests.get(
            "https://poe.ninja/api/data/ItemOverview?league=Scourge&type=ClusterJewel&language=en")
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        data = raw_data.text
        data_json = json.loads(data)
        with open("clusters.txt", "w") as f:
            f.write(" ")
        for i in data_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.variant = i["variant"]
                self.currType = "Exalted Orb"
                self.chaosValue = 0
                if "levelRequired" in i:
                    self.lvlreq = i["levelRequired"]
                else:
                    self.lvlreq = 0
                exportlist.append(self)
                self.exportfunction.append(self)
            else:
                self.name = i["name"]
                self.chaosValue = i["chaosValue"]
                self.exaltedValue = 0
                self.currType = "Chaos Orb"
                if "levelRequired" in i:
                    self.lvlreq = i["levelRequired"]
                else:
                    self.lvlreq = 0
                exportlist.append(self)
                self.exportfunction.append(self)
            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            result = json.dumps(exportlist, default=lambda o: o.__dict__)
            with open("clusters.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()

def main():
    print("Are you sure this is gonna be the main function?")
    sys.exit(0)


if __name__ == "__main__":
    main()
