import pyautogui
import os
import cv2
import sys

## Replace spaces with _ to take the file easily
global folder
folder = (r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\icons")


class ReplaceFiles():
    def ReplaceUS(self):
        os.chdir(folder)
        files = os.listdir(os.getcwd())
        [os.replace(file, file.replace(" ", "_")) for file in files]

    def ReplaceSpace(self):
        os.chdir(folder)
        files = os.listdir(os.getcwd())
        [os.replace(file, file.replace("_", " ")) for file in files]


class SearchOnScreen():
    def Search(self, name):
        os.chdir(folder)
        print("----------------")
        y = "essence"
        if y in name or y.title() in name:
            itemlocation = pyautogui.locateOnScreen((name + ".jpg"), confidence=0.75)
            print("Location of the item on your stash >", itemlocation)
        else:
            itemlocation = pyautogui.locateOnScreen((name + ".jpg"), confidence=0.65)
            print("Location of the item on your stash >", itemlocation)
        return itemlocation


class MoveMouse():
    def Move(self, itemlocation,quantity = None):
        print("Yeeting the mouse to the item location...")
        pyautogui.moveTo(itemlocation)
        print("Checking if buyer wants multiple quantities...")
        if quantity == None:
            print("Yeeting item right to your inventory...")
            with pyautogui.hold("ctrl"):
                pyautogui.leftClick(itemlocation)
        if quantity != None:
            with pyautogui.hold("shift"):
                pyautogui.leftClick(itemlocation)

'''
def main():
    print("Are you sure this is gonna be the main function?")
    sys.exit(0)


if __name__ == "__main__":
    main()
'''
