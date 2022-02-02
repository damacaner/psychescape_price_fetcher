import requests
import json
import os
import sys
from modules import scarabvals, skillgems, general, crafting, uniques
from ocrmodules import icontest
from os.path import dirname, basename, isfile, join
import stashcontents
from poemodules import stashid
## Exit from the program if len(sys.argv) is 1.
if len(sys.argv) == 1:
    sys.exit()
## Get Chaos to Ex ratio first
global chaos_ex_ratio
response_API = requests.get("https://poe.ninja/api/data/currencyoverview?league=Standard&type=Currency")
data = response_API.text
parse_json = json.loads(data)
for i in parse_json["lines"]:
    if i["currencyTypeName"] == ("Exalted Orb"):
        chaos_ex_ratio = i["receive"]["value"]
        print("Current chaos to ex ratio is:", chaos_ex_ratio)


## Search Item Values
def Navigator(x, name):
    match x:
        case 1:
            output = Search_Scarab(name)
            return output
        case 2:
            output = Search_Fossil(name)
            return output
        case 3:
            output = Search_Incubator(name)
            return output
        case 4:
            output = Search_Oil(name)
        case 5:
            output = Search_Resonator(name)
            return output
        case 6:
            output = Search_Essence(name)
            return output
        case 8:
            output = Search_Currency(name)
            return output
        case 9:
            output = Fragment_Search(name)
            return output
        case 10:
            output = Artifact_Search(name)
            return output


## Get and Search Beasts

def Beast_Values():
    beast_fetch = crafting.BeastValues()
    beast_fetch.Beast_Values()


def Beast_Search(name):
    beast_search = crafting.SearchBeast()
    y = beast_search.search(name)
    return y


## Get and Search Artifacts
def Artifact_Values():
    artifact_fetch = general.ArtifactValues()
    artifact_fetch.Artifact_Values()


def Artifact_Search(name):
    artifact_search = general.ArtifactSearch()
    y = artifact_search.search(name)
    return y


## Get and Search Divination Cards
def Div_Values():
    div_fetch = general.DivValues()
    div_fetch.Div_Values()


def Div_Search(name):
    div_search = general.DivSearch()
    y = div_search.search(name)
    return y


## Get and Search Currency Ratios
def Currency_Ratios():
    currency_ratios = general.CurrencyRatios()
    currency_ratios.Ratios()


def Search_Currency(name):
    currency_search = general.SearchRatio()
    y = currency_search.search(name)
    return y


## Get and Search Incubator Values
def Incubator_Values():
    incubator_fetch = general.IncuValues()
    incubator_fetch.Incubator_Values()


def Search_Incubator(name):
    incubator_search = general.SearchIncus()
    output = incubator_search.search(name)
    return output


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
    y = oil_search.search(name)
    return y


## Get  and Search Scarab Values
def Scarab_Values():
    scarab_fetch = scarabvals.ScarabValues()
    scarab_fetch.Scarab_Values()


def Search_Scarab(name):
    scarab_search = scarabvals.SearchScarab()
    y = scarab_search.search(name)
    return y


## Get and Search Fossils Values
def Fossil_Values():
    fossil_fetch = crafting.FossilVals()
    fossil_fetch.Fossil_Values()


def Search_Fossil(name):
    fossil_search = crafting.SearchFossils()
    y = fossil_search.search(name)
    return y


## Get and Search Resonator Values
def Resonator_Values():
    reson_fetch = crafting.ResoValues()
    reson_fetch.Reso_Values()


def Search_Resonator(name):
    reson_search = crafting.SearchResonators()
    y = reson_search.search(name)
    return y


## Get and Search Essence Values
def Essence_Values():
    essence_fetch = crafting.EssenceValues()
    essence_fetch.Essence_Values()


def Search_Essence(name):
    essence_search = crafting.SearchEssences()
    output = essence_search.search(name)
    return output


## Get and Search Skill Gem Values

def SkillGem_Values():
    skillgem_fetch = skillgems.SGValues()
    skillgem_fetch.SG_Values()


def SkillGem_Search(name, gemlvl, gemqual):
    skillgem_search = skillgems.SearchSG()
    skillgem_search.search(name, gemlvl, gemqual)


## Get and Search Unique Values

def Unique_Search(name):
    os.chdir(r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\values")
    with open("uniqueweapons.txt", "w") as file:
        if name in file:
            unique = uniques.UWeaponSearch()
            unique.search(name)
        else:
            pass
    with open("uniquearmour.txt", "w") as file:
        if name in file:
            unique = uniques.UArmourSearch()
            unique.search(name)
        else:
            pass
    with open("uniqueaccessory.txt", "w") as file:
        if name in file:
            unique = uniques.UAccessorySearch()
            unique.search(name)
        else:
            pass


def Unique_Fetch():
    f1 = uniques.UArmourValues()
    f1.UniqueArmours()
    f2 = uniques.UWeaponValues()
    f2.UniqueWeapons()
    f3 = uniques.UAccessoryValues()
    f3.UniqueAccessory()
    f4 = uniques.UJewelValues()
    f4.UniqueJewel()
    f5 = uniques.CLJewelValues()
    f5.UniqueJewel()


def LocateOnScreen(name):
    replace = icontest.ReplaceFiles()
    replace.ReplaceUS()
    locate = icontest.SearchOnScreen()
    locate.Search(name)
    replace.ReplaceSpace()


# TODO use other apis
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch prices from poe.ninja")
    parser.add_argument("-fa", "--fetchall", action="store_true", help="Fetch everything listed on poe.ninja")
    parser.add_argument("-search", "--search", action="store_true", help="Search the item on values folder")
    parser.add_argument("-sids", "--sids", action="store_true", help="Fetch stash IDs on temporary league")
    parser.add_argument("-sincludes", "--sincludes", action="store_true", help="Fetch stash items with stash IDs on temporary league")
    parser.add_argument("-general", "--general", action="store_true", help="Fetch all general values")
    parser.add_argument("-crafting", "--crafting", action="store_true", help="Fetch all crafting values")
    parser.add_argument("-unique", "--unique", action="store_true", help="Fetch all unique item values")
    parser.add_argument("-scarab", "--scarab", action="store_true", help="Fetch scarab prices")
    parser.add_argument("-sg", "--skillgem", action="store_true", help="Fetch skill gem prices")
    args = parser.parse_args()
    print("Arguments given to system> ", len(sys.argv))
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

general_ = args.general
sids_ = args.sids
sincludes_ = args.sincludes
crafting_ = args.crafting
skillgem_fetch_ = args.skillgem
scarab_fetch_ = args.scarab
fa_fetch_ = args.fetchall
unq_fetch_ = args.unique
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
        SkillGem_Search(name, gemlvl, gemqual)
    x = Navigator(var, name)

if sincludes_ == True:
    yarram = stashcontents.GetStash()
    yarram.StashNotes()
if sids_ == True:
    yarram = stashid.StashIDFetch()
    yarram.StashID()
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
if unq_fetch_ == True:
    print("Fetching unique item values...")
    Unique_Fetch()
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
    print("Fetching unique item values...")
    Unique_Fetch()

# Helmet enchantları PoE serverı nasıl veriyor bilmiyorum. Client ID aldıktan sonra bakıcam.
