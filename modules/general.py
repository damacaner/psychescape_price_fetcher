import json
import os
import requests
import sys

global chaos_ex_ratio
import urllib.request

'''
GENERAL ECONOMY
Currency
Fragments
Divination Cards
Artifacts
Prophecies
Oils
'''

response_API = requests.get("https://poe.ninja/api/data/currencyoverview?league=Scourge&type=Currency")
data = response_API.text
parse_json = json.loads(data)
for i in parse_json["lines"]:
    if i["currencyTypeName"] == ("Exalted Orb"):
        chaos_ex_ratio = i["receive"]["value"]


class SearchRatio(list):
    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("currency.txt", "r") as f:
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


class CurrencyRatios:
    exportfunction = SearchRatio()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Ratios(self):
        response_API = requests.get("https://poe.ninja/api/data/currencyoverview?league=Scourge&type=Currency")
        data = response_API.text
        parsed_data = json.loads(data)
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        with open("currency.txt", "w") as f:
            f.write(" ")
        for i in parsed_data["lines"]:
            exportlist = []
            if i["chaosEquivalent"] > chaos_ex_ratio:
                self.name = i["currencyTypeName"]
                self.exaltedValue = round((int(i["chaosEquivalent"]) / chaos_ex_ratio), 1)
                self.currType = "Exalted Orb"
                exportlist.append(self)
                self.exportfunction.append(self)
            else:
                self.name = i["currencyTypeName"]
                self.chaosValue = i["chaosEquivalent"]
                self.currType = "Chaos Orb"
                self.exaltedValue = 0
                exportlist.append(self)
                self.exportfunction.append(self)

            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            result = json.dumps(exportlist, default=lambda o: o.__dict__)
            with open("currency.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()
        print("Done!")


class SearchFrags(list):
    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("fragment.txt", "r") as f:
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


class FragmentValues:
    exportfunction = SearchFrags()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Ratios(self):
        response_API = requests.get("https://poe.ninja/api/data/currencyoverview?league=Scourge&type=Fragment")
        data = response_API.text
        parsed_data = json.loads(data)
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        with open("fragment.txt", "w") as f:
            f.write(" ")
        for i in parsed_data["lines"]:
            exportlist = []
            if i["chaosEquivalent"] > chaos_ex_ratio:
                self.name = i["currencyTypeName"]
                self.exaltedValue = round((int(i["chaosEquivalent"]) / chaos_ex_ratio), 1)
                self.currType = "Exalted Orb"
                exportlist.append(self)
                self.exportfunction.append(self)
            else:
                self.name = i["currencyTypeName"]
                self.chaosValue = i["chaosEquivalent"]
                self.currType = "Chaos Orb"
                self.exaltedValue = 0
                exportlist.append(self)
                self.exportfunction.append(self)
            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            result = json.dumps(exportlist, default=lambda o: o.__dict__)
            with open("fragment.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()
        print("Done!")


class SearchOil(list):

    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("oil.txt", "r") as f:
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


class OilValues:
    exportfunction = SearchOil()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Oil_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/itemoverview?league=Scourge&type=Oil")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("oil.txt", "w") as file:
            file.write(" ")
        j = 0
        for i in parse_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
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
            with open("oil.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()

    def Check_Oils(self):
        pass
        # TODO Get every oil on character's stash. PoE still didnt give me an authorization key.


class SearchIncus(list):

    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("incubators.txt", "r") as f:
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


class IncuValues:
    exportfunction = SearchIncus()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Incubator_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/itemoverview?league=Scourge&type=Incubator")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("incubators.txt", "w") as file:
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
            with open("incubators.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


class ArtifactSearch(list):

    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("artifacts.txt", "r") as f:
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


class ArtifactValues:
    exportfunction = ArtifactSearch()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Artifact_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/ItemOverview?league=Scourge&type=Artifact&language=en")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("artifacts.txt", "w") as file:
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
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            result = json.dumps(exportlist, default=lambda o: o.__dict__)
            with open("artifacts.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


class DivSearch(list):

    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("divination.txt", "r") as f:
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


class DivValues:
    exportfunction = DivSearch()

    def __init__(self, name=" ", exval=0, chval=0, curtype=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Div_Values(self):
        response_API = requests.get(
            "https://poe.ninja/api/data/ItemOverview?league=Scourge&type=DivinationCard&language=en")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("divination.txt", "w") as file:
            file.write(" ")
        j = 0
        for i in parse_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.currType = "Exalted Orb"
                self.chaosValue = 0
                exportlist.append(self)
                self.exportfunction.append(self)
            else:
                self.name = i["name"]
                self.chaosValue = i["chaosValue"]
                self.currType = "Chaos Orb"
                self.exaltedValue = 0
                exportlist.append(self)
                self.exportfunction.append(self)
            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            result = json.dumps(exportlist, default=lambda o: o.__dict__)
            with open("divination.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()


def main():
    print("Are you sure this is gonna be the main function?")
    sys.exit(0)


if __name__ == "__main__":
    main()
