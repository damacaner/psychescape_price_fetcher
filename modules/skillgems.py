import requests
import json
import os
import re

global chaos_ex_ratio
import sys

response_API = requests.get("https://poe.ninja/api/data/currencyoverview?league=Standard&type=Currency")
data = response_API.text
parse_json = json.loads(data)
for i in parse_json["lines"]:
    if i["currencyTypeName"] == ("Exalted Orb"):
        chaos_ex_ratio = i["receive"]["value"]

folder = r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values"


class RegexSearch():
    def __init__(self, name=" ", exval=0, chval=0, curtype=" ", gemlvl=0, gemqual=0, corrupted=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype
        self.gemlvl = gemlvl
        self.gemqual = gemqual
        self.corrupted = corrupted

    def useRegex(self, input):
        os.chdir(folder)
        with open("corruptgem.txt", "w") as file:
            file.write(" ")
        pattern = re.compile(r"^[a-zA-Z]+$")
        textfile = open("skillgem.txt", "r")
        edited = textfile.readlines()
        pattern = re.compile(r"[a-zA-Z]+")
        y = pattern.match(input, re.IGNORECASE)
        awakened = (y is not None)
        print(awakened)
        for line in edited:
            list = []
            item = line.strip()
            parsed = json.loads(item)[0]
            if (input == parsed["name"]) and (parsed["gemlvl"] >= 1) and (
                    parsed["corrupted"] == "True") and (awakened == False):
                self.name = input
                self.exaltedValue = parsed["exaltedValue"]
                self.chaosValue = parsed["chaosValue"]
                self.gemlvl = parsed["gemlvl"]
                self.gemqual = ("+" + parsed["gemqual"] + "%")
                self.corrupted = parsed["corrupted"]
                list.append(self)
                result = json.dumps(list, default=lambda o: o.__dict__)
                with open("corruptgem.txt", "a") as file:
                    file.write(str(result))
                    file.write("\n")
                    file.close()
            elif (input == parsed["name"]) and (parsed["gemlvl"] >= 1) and (
                    parsed["corrupted"] == "False") and (awakened == False):
                self.name = input
                self.exaltedValue = parsed["exaltedValue"]
                self.chaosValue = parsed["chaosValue"]
                self.gemlvl = parsed["gemlvl"]
                self.gemqual = ("+" + parsed["gemqual"] + "%")
                self.corrupted = parsed["corrupted"]
                list.append(self)
                result = json.dumps(list, default=lambda o: o.__dict__)
                with open("corruptgem.txt", "a") as file:
                    file.write(str(result))
                    file.write("\n")
                    file.close()
            elif (input == parsed["name"]) and (parsed["corrupted"] == True) and (awakened == True):
                print(awakened)
                self.name = input
                self.exaltedValue = parsed["exaltedValue"]
                self.chaosValue = parsed["chaosValue"]
                self.gemlvl = parsed["gemlvl"]
                self.gemqual = ("+" + parsed["gemqual"] + "%")
                self.corrupted = parsed["corrupted"]
                list.append(self)
                i = i + 1
                result = json.dumps(list, default=lambda o: o.__dict__)
                with open("corruptgem.txt", "a") as file:
                    file.write(str(result))
                    file.write("\n")
                    file.close()


class SearchSG(list):

    def search(self, searchvar, gemlevel, gemquality):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("skillgem.txt", "r") as f:
            lines = f.readlines()  ## Read all the lines
        i = 0
        for line in lines:
            i += 1
            item = line.strip()  ## Strip \n from the lines
            parsed = json.loads(item)[0]  ## Load the i'th line with json
            name_list = parsed["name"]  ## Extract the name_list
            lvl_list = parsed["gemlvl"]
            qual_list = parsed["gemqual"]
            if gemquality != None:
                if (gemlevel == lvl_list) and (gemlevel == qual_list) and (
                        searchvar == name_list):  ## If searched term is in searchvar go through
                    name = parsed["name"]
                    exalted_value = parsed["exaltedValue"]
                    chaos_value = parsed["chaosValue"]
                    curr_type = parsed["currType"]
                    corrupted = parsed["corrupted"]
                    gemlvl = parsed["gemlvl"]
                    gemqual = parsed["gemqual"]
                    print("----------------")
                    print("We have found the >", name)
                    print("Exalted Orb Value >", exalted_value)
                    print("Chaos Orb Value >", chaos_value)
                    print("Currency Type >", curr_type)
                    print("Corrupted >", corrupted)
                    print("Gem LvL >", gemlvl)
                    print("Gem Quality >", gemqual)
                    return exalted_value, chaos_value, curr_type
                elif (gemlevel == lvl_list) and (gemquality == qual_list) and (searchvar.title() == name_list):
                    name = parsed["name"]
                    exalted_value = parsed["exaltedValue"]
                    chaos_value = parsed["chaosValue"]
                    curr_type = parsed["currType"]
                    print("----------------")
                    print("We have found the >", name)
                    print("Exalted Orb Value >", exalted_value)
                    print("Chaos Orb Value >", chaos_value)
                    print("Currency Type >", curr_type)
                    print("Gem Level >", gemlevel)
                    print("Gem Quality >", gemquality)
                    return exalted_value, chaos_value, curr_type


class SGValues:
    def __init__(self, name=" ", exval=0, chval=0, curtype=" ", gemlvl=0, gemqual=0, corrupted=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype
        self.gemlvl = gemlvl
        self.gemqual = gemqual
        self.corrupted = corrupted

    def SG_Values(self):
        response_API = requests.get("https://poe.ninja/api/data/itemoverview?league=Standard&type=SkillGem")
        data = response_API.text
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        parse_json = json.loads(data)
        with open("skillgem.txt", "w") as file:
            file.write(" ")
        for i in parse_json["lines"]:
            list = []
            if (i["chaosValue"] > chaos_ex_ratio):
                if ("corrupted" not in i) and ("gemQuality" not in i):
                    ''' Gem has no quality and not corrupted. '''
                    self.name = i["name"]
                    self.exaltedValue = i["exaltedValue"]
                    self.currType = "Exalted Orb"
                    self.gemlvl = i["gemLevel"]
                    self.corrupted = "False"
                    list.append(self)
                elif ("gemQuality" not in i):
                    self.name = i["name"]
                    self.exaltedValue = i["exaltedValue"]
                    self.currType = "Exalted Orb"
                    self.gemlvl = i["gemLevel"]
                    self.corrupted = i["corrupted"]
                    list.append(self)
                elif ("corrupted" not in i):
                    self.name = i["name"]
                    self.exaltedValue = i["exaltedValue"]
                    self.currType = "Exalted Orb"
                    self.gemlvl = i["gemLevel"]
                    self.corrupted = "False"
                    self.gemqual = ("+" + str(i["gemQuality"]) + "%")
                    list.append(self)
                else:
                    self.name = i["name"]
                    self.exaltedValue = i["exaltedValue"]
                    self.currType = "Exalted Orb"
                    self.gemlvl = i["gemLevel"]
                    self.gemqual = ("+" + str(i["gemQuality"]) + "%")
                    self.corrupted = i["corrupted"]
                    list.append(self)
            else:
                self.exaltedValue = 0
                if ("corrupted" not in i) and ("gemQuality" not in i):
                    ''' Gem has no quality and not corrupted. '''
                    self.name = i["name"]
                    self.chaosValue = i["chaosValue"]
                    self.currType = "Chaos Orb"
                    self.gemlvl = i["gemLevel"]
                    self.corrupted = "False"
                    list.append(self)
                elif ("gemQuality" not in i):
                    self.name = i["name"]
                    self.chaosValue = i["chaosValue"]
                    self.currType = "Chaos Orb"
                    self.gemlvl = i["gemLevel"]
                    self.corrupted = i["corrupted"]
                    list.append(self)
                elif ("corrupted" not in i):
                    self.name = i["name"]
                    self.chaosValue = i["chaosValue"]
                    self.currType = "Chaos Orb"
                    self.gemlvl = i["gemLevel"]
                    self.corrupted = "False"
                    self.gemqual = ("+" + str(i["gemQuality"]) + "%")
                    list.append(self)
                else:
                    self.name = i["name"]
                    self.chaosValue = i["chaosValue"]
                    self.currType = "Chaos Orb"
                    self.gemlvl = i["gemLevel"]
                    self.gemqual = ("+" + str(i["gemQuality"]) + "%")
                    self.corrupted = i["corrupted"]
                    list.append(self)
            os.chdir(
                r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
            result = json.dumps(list, default=lambda o: o.__dict__)
            with open("skillgem.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()
        print("Imported every incubator value on poe.ninja to skillgem.txt")
        print("Stored in SGValues class.")

    def Check_Incus(self):
        pass
        # TODO Get every incubators on character's stash. PoE still didnt give me an authorization key.


'''
def main():
    print("Are you sure this is gonna be the main function?")
    sys.exit(0)


if __name__ == "__main__":
    main()
'''
