import requests
import json
import os
import sys
from modules import scarabvals, skillgems, general, crafting
from os.path import dirname, basename, isfile, join
## Exit from the program if len(sys.argv) is 1.
if len(sys.argv) == 1:
    sys.exit()
## Get Chaos to Ex ratio first
global chaos_ex_ratio
response_API = requests.get("https://poe.ninja/api/data/currencyoverview?league=Scourge&type=Currency")
data = response_API.text
parse_json = json.loads(data)
for i in parse_json["lines"]:
    if i["currencyTypeName"] == ("Exalted Orb"):
        chaos_ex_ratio = i["receive"]["value"]
        print("Current chaos to ex ratio is:", chaos_ex_ratio)
## Search Item Values
def Navigator(x,name):
   match x:
       case 1:
           Search_Scarab(name)
       case 2:
           Search_Fossil(name)
       case 3:
           Search_Incubator(name)
       case 4:
           Search_Oil(name)
       case 5:
           Search_Resonator(name)
       case 6:
           Search_Essence(name)
       case 8:
           Search_Currency(name)
       case 9:
           Fragment_Search(name)
       case 10:
           Artifact_Search(name)
## Get and Search Beasts
def Beast_Values():
    beast_fetch = crafting.BeastValues()
    beast_fetch.Beast_Values()
def Beast_Search(name):
    beast_search = crafting.SearchBeast()
    beast_search.search(name)


## Get and Search Artifacts
def Artifact_Values():
    artifact_fetch = general.ArtifactValues()
    artifact_fetch.Artifact_Values()
def Artifact_Search(name):
    artifact_search = general.ArtifactSearch()
    artifact_search.search(name)

## Get and Search Divination Cards
def Div_Values():
    div_fetch = general.DivValues()
    div_fetch.Div_Values()
def Div_Search(name):
    div_search = general.DivSearch()
    div_search.search(name)


## Get and Search Currency Ratios
def Currency_Ratios():
   currency_ratios = general.CurrencyRatios()
   currency_ratios.Ratios()
def Search_Currency(name):
   currency_search = general.SearchRatio()
   currency_search.search(name)

## Get and Search Incubator Values
def Incubator_Values():
 incubator_fetch = general.IncuValues()
 incubator_fetch.Incubator_Values()
def Search_Incubator(name):
 incubator_search = general.SearchIncus()
 incubator_search.search(name)

## Get and Search Fragment Values
def Fragment_Values():
  fragment_fetch = general.FragmentValues()
  fragment_fetch.Ratios()
def Fragment_Search(name):
  fragment_search = general.SearchFrags()
  fragment_search.search(name)

## Get and Search Oil Values
def Oil_Values():
 oil_fetch = general.OilValues()
 oil_fetch.Oil_Values()
def Search_Oil(name):
 oil_search = general.SearchOil()
 oil_search.search(name)


## Get  and Search Scarab Values
def Scarab_Values():
 scarab_fetch = scarabvals.ScarabValues()
 scarab_fetch.Scarab_Values()
def Search_Scarab(name):
 scarab_search = scarabvals.SearchScarab()
 scarab_search.search(name)

## Get and Search Fossils Values
def Fossil_Values():
 fossil_fetch = crafting.FossilVals()
 fossil_fetch.Fossil_Values()
def Search_Fossil(name):
 fossil_search = crafting.SearchFossils()
 fossil_search.search(name)


## Get and Search Resonator Values
def Resonator_Values():
 reson_fetch = crafting.ResoValues()
 reson_fetch.Reso_Values()
def Search_Resonator(name):
 reson_search = crafting.SearchResonators()
 reson_search.search(name)


## Get and Search Essence Values
def Essence_Values():
 essence_fetch = crafting.EssenceValues()
 essence_fetch.Essence_Values()
def Search_Essence(name):
 essence_search = crafting.SearchEssences()
 essence_search.search(name)

## Get and Search Skill Gem Values

def SkillGem_Values():
  skillgem_fetch = skillgems.SGValues()
  skillgem_fetch.SG_Values()
def SkillGem_Search(name,gemlvl,gemqual):
  skillgem_search = skillgems.SearchSG()
  skillgem_search.search(name, gemlvl, gemqual)


## Get Base Type Values, good for pricing scourged influenced items or cluster jewels
def BaseType_Values():
    response_API = requests.get("https://poe.ninja/api/data/itemoverview?league=Scourge&type=BaseType")
    data = response_API.text
    parse_json = json.loads(data)
    os.chdir(r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
    with open("basetypes.txt", "w") as file:
        file.write(" ")
    for i in parse_json["lines"]:
        list = []
        if (i["chaosValue"] > chaos_ex_ratio):
            if "variant" not in i:
             value = (i["baseType"], i["exaltedValue"], "Exalted Orb", i["levelRequired"])
            else:
             value = (i["variant"], i["baseType"], i["exaltedValue"], "Exalted Orb", i["levelRequired"])
        else:
            if "variant" not in i:
                value = (i["baseType"], i["chaosValue"], "Chaos Orb", i["levelRequired"])
            else:
                value = (i["variant"], i["baseType"], i["chaosValue"], "Chaos Orb", i["levelRequired"])
        list.append(value)
        # print(list)
        os.chdir(
            r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
        with open("basetypes.txt", "a") as file:
            file.write(str(list))
            file.write("\n")
            file.close()
def HelmetEnchants():
    response_API = requests.get(r"https://poe.ninja/api/data/itemoverview?league=Scourge&type=HelmetEnchant")
    data = response_API.text
    parse_json = json.loads(data)
    os.chdir(r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
    with open("helmetenchants.txt", "w") as file:
        file.write(" ")
    #TODO Implement this later.


#TODO use other apis
if __name__ == "__main__":
   import argparse
   parser = argparse.ArgumentParser(description="Fetch prices from poe.ninja")
   parser.add_argument("-fa", "--fetchall", action="store_true", help="Fetch everything listed on poe.ninja")
   parser.add_argument("-search","--search", action="store_true", help="Search the item on values folder")
   parser.add_argument("-general","--general",action="store_true", help="Fetch all general values")
   parser.add_argument("-crafting","--crafting",action="store_true", help="Fetch all crafting values")
   parser.add_argument("-scarab", "--scarab", action="store_true", help="Fetch scarab prices")
   parser.add_argument("-base","--bases", action="store_true", help="Fetch base prices")
   parser.add_argument("-sg", "--skillgem", action="store_true", help="Fetch skill gem prices")
   args = parser.parse_args()
   print("Arguments given to system> ",len(sys.argv))
   if len(sys.argv) == 1:
       parser.print_help()
       sys.exit()

general_ = args.general
crafting_ = args.crafting
base_fetch_ = args.bases
skillgem_fetch_ = args.skillgem
scarab_fetch_ = args.scarab
fa_fetch_ = args.fetchall
search_func_ = args.search
if search_func_ == True:
    print("Which type of item you want to search?\n"
          "1 - Scarab\n"
          "2 - Fossil\n"
          "3 - Incubator\n"
          "4 - Oil\n"
          "5 - Resonator\n"
          "6 - Essence\n"
          "7 - Skill Gem\n"
          "8 - Currency\n"
          "9 - Fragment\n")
    var = int(input())
    if (var < 1) or (var > 9):
        print("Please enter numbers in range of 1-9")
        sys.exit()
    print("Enter the type of the item you want to search, the longer it is, output will be better.")
    name = input()
    if var == 7:
        print("Enter the level of gem > ")
        gemlvl = input()
        print("Enter the quality of gem > ")
        gemqual = input()
        SkillGem_Search(name,gemlvl,gemqual)
    Navigator(var,name)
if general_ == True:
    print("Fetching currency values...")
    Currency_Ratios()
    print("Fetching fragment values...")
    Fragment_Values()
    print("Fetching div card values...")
    Div_Values()
    print("Fetching artifact values...")
    Artifact_Values()
    print("Fetching oil values...")
    Oil_Values()
    print("Fetching incubator values...")
    Incubator_Values()
if crafting_ == True:
    print("Fetching fossil values...")
    Fossil_Values()
    print("Done! Please check your values folder.")
    print("Fetching resonator values...")
    Resonator_Values()
    print("Done! Please check your values folder.")
    print("Fetching essence values...")
    Essence_Values()
    print("Done! Please check your values folder.")
    print("Fetching beast values...")
    Beast_Values()
    print("Done! Please check your values folder.")
if base_fetch_ == True:
    print("Fetching base type values...")
    BaseType_Values()
    print("Done! Please check your values folder.")
if skillgem_fetch_ == True:
    print("Fetching skill gem values...")
    SkillGem_Values()
    print("Done! Please check your values folder.")
if scarab_fetch_ == True:
    print("Fetching scarab values...")
    Scarab_Values()
    print("Done! Please check your values folder.")
if fa_fetch_ == True:
    print("Fetching currency values...")
    Currency_Ratios()
    print("Fetching fragment values...")
    Fragment_Values()
    print("Fetching div card values...")
    Div_Values()
    print("Fetching artifact values...")
    Artifact_Values()
    print("Fetching oil values...")
    Oil_Values()
    print("Fetching incubator values...")
    Incubator_Values()
    print("Fetching fossil values...")
    Fossil_Values()
    print("Done! Please check your values folder.")
    print("Fetching resonator values...")
    Resonator_Values()
    print("Done! Please check your values folder.")
    print("Fetching essence values...")
    Essence_Values()
    print("Done! Please check your values folder.")
    print("Fetching fossil values...")
    Fossil_Values()
    print("Done! Please check your values folder.")

# Helmet enchantları PoE serverı nasıl veriyor bilmiyorum. Client ID aldıktan sonra bakıcam.
