import requests
import urllib.request
import json
import os

global chaos_ex_ratio
import sys

response_API = requests.get("https://poe.ninja/api/data/currencyoverview?league=Standard&type=Currency")
data = response_API.text
parse_json = json.loads(data)
for i in parse_json["lines"]:
    if i["currencyTypeName"] == ("Exalted Orb"):
        chaos_ex_ratio = i["receive"]["value"]
'''
Searches for items in data
'''


class SearchScarab(list):

    def search(self, searchvar):
        ## Change dir to where values lie ##
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        ## Open the related value text file and read it
        with open("scarab.txt", "r") as f:
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


class ScarabValues:
    exportfunction = SearchScarab()
    '''
    Initialize class to store scarab values
    '''

    def __init__(self, name=" ", exval=0, chval=0, curtype=" "):
        self.name = name
        self.exaltedValue = exval
        self.chaosValue = chval
        self.currType = curtype

    def Scarab_Values(self):
        '''
        Yeet the API request.
        '''
        response_API = requests.get("https://poe.ninja/api/data/itemoverview?league=Standard&type=Scarab")
        data = response_API.text
        '''
        Change directory to wherever values lie.
        '''
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        '''
        Parse the json for value extracting
        '''
        parse_json = json.loads(data)
        with open("scarab.txt", "w") as file:
            file.write(" ")
        for i in parse_json["lines"]:
            exportlist = []
            if (i["chaosValue"] > chaos_ex_ratio):
                self.name = i["name"]
                self.exaltedValue = i["exaltedValue"]
                self.currType = "Exalted Orb"
                '''
                exportlist is exporting list to scarab.txt
                exportfunction is exporting list to ScarabValues function.
                '''
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
                '''
                exportlist is exporting list to scarab.txt
                exportfunction is exporting list to ScarabValues function.
                '''
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
            with open("scarab.txt", "a") as file:
                file.write(str(result))
                file.write("\n")
                file.close()
        print("Imported every incubator value on poe.ninja to scarab.txt")
        print("Stored in ScarabValues class.")


def main():
    print("Are you sure this is gonna be the main function?")
    sys.exit(0)


if __name__ == "__main__":
    main()
