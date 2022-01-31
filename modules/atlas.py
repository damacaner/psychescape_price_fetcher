import json
import requests
import os
global chaos_ex_ratio
import urllib.request
response_API = requests.get("https://poe.ninja/api/data/currencyoverview?league=Scourge&type=Currency")
data = response_API.text
parse_json = json.loads(data)
for i in parse_json["lines"]:
    if i["currencyTypeName"] == ("Exalted Orb"):
        chaos_ex_ratio = i["receive"]["value"]
class SearchMap(list):
    def search(self, searchvar, tier):
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        with open("maps.txt", "r") as f:
            lines = f.readlines()
        i = 0
        for line in lines:
            i += 1
            item = line.strip()
            parsed = json.loads(item)[0]
            name_list = parsed["name"]
            tier_list = parsed["mapTier"]
            if (searchvar == name_list) and (tier == name_list):
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
class MapValues:
    exportfunction = SearchMap()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" ", mapTier = 0):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype
        self.mapTier = mapTier
    def Map_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/ItemOverview?league=Scourge&type=Map&language=en")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("maps.txt", "w") as file:
            file.write(" ")
        j = 0
        for i in parse_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.mapTier = i["mapTier"]
                self.currType = "Exalted Orb"
                exportlist.append(self)
                self.chaosValue = 0
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
                self.mapTier = i["mapTier"]
                self.currType = "Chaos Orb"
                self.exaltedValue = 0
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
            with open("maps.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()

class BlightedMapSearch(list):
    def search(self, searchvar, tier):
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        with open("blightedmaps.txt", "r") as f:
            lines = f.readlines()
        i = 0
        for line in lines:
            i += 1
            item = line.strip()
            parsed = json.loads(item)[0]
            name_list = parsed["name"]
            tier_list = parsed["mapTier"]
            if (searchvar == name_list) and (tier == name_list):
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
class BlightedMapValues:
    exportfunction = BlightedMapSearch()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" ", mapTier = 0):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype
        self.mapTier = mapTier
    def BlightedMap_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/ItemOverview?league=Scourge&type=BlightedMap&language=en")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("blightedmaps.txt", "w") as file:
            file.write(" ")
        j = 0
        for i in parse_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.mapTier = i["mapTier"]
                self.currType = "Exalted Orb"
                exportlist.append(self)
                self.chaosValue = 0
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
                self.mapTier = i["mapTier"]
                self.currType = "Chaos Orb"
                self.exaltedValue = 0
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
            with open("blightedmaps.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()
class UniqueMapSearch(list):
    def search(self, searchvar, tier):
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        with open("uniquemaps.txt", "r") as f:
            lines = f.readlines()
        i = 0
        for line in lines:
            i += 1
            item = line.strip()
            parsed = json.loads(item)[0]
            name_list = parsed["name"]
            tier_list = parsed["mapTier"]
            if (searchvar == name_list) and (tier == name_list):
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
class UniqueMapValues:
    exportfunction = UniqueMapSearch()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" ", mapTier = 0):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype
        self.mapTier = mapTier
    def UniqueMap_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/ItemOverview?league=Scourge&type=UniqueMap&language=en")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("uniquemaps.txt", "w") as file:
            file.write(" ")
        j = 0
        for i in parse_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = str(i["name"]).replace(r"\u00f6m", "ö")
                self.exaltedValue = i["exaltedValue"]
                self.mapTier = i["mapTier"]
                self.currType = "Exalted Orb"
                exportlist.append(self)
                self.chaosValue = 0
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
                self.mapTier = i["mapTier"]
                self.currType = "Chaos Orb"
                self.exaltedValue = 0
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
            with open("uniquemaps.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()