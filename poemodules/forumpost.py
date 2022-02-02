import json
import os

idfolder = r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\poemodules"
stashvaluefolder = r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\stashvalues"
forumpostoutputfolder = r"C:\Users\emosc\PycharmProjects\GithubPushs\psychescape_price_fetcher\psychescape_price_fetcher\forumoutput"


class ForumPostGenerator:
    def Post(self):
        j = 1
        os.chdir(forumpostoutputfolder)
        with open("forumpost.txt", "w") as file:
            file.write(" ")
            file.close()
        os.chdir(idfolder)
        with open("stashid.txt", "r") as stashid:
            stashids = stashid.readlines()
        for lines in stashids:
            item = lines.strip()
            parsed = json.loads(item)[0]
            os.chdir(stashvaluefolder)
            txtfile = (parsed["name"] + ".txt").replace("~b/o", "buyout")
            stashindex = j
            if os.path.getsize(txtfile) > 1:
                os.chdir(forumpostoutputfolder)
                with open("forumpost.txt", "a") as datafile:
                    datafile.write("\n")
                    datafile.write('[spoiler="Stash ' + parsed["name"] + ' by Psychescape Pricer"]')
                os.chdir(stashvaluefolder)
                with open(txtfile, "r") as stashfiles:
                    files = stashfiles.readlines()
                for datalines in files:
                    itemdata = datalines.strip()
                    itemparsed = json.loads(itemdata)[0]
                    os.chdir(forumpostoutputfolder)
                    with open("forumpost.txt", "a") as datafile:
                        if itemparsed["note"] != "Unknown":
                            datafile.write("\n")
                            datafile.write('[linkItem location="{}"'.format(
                                "Stash" + str(stashindex)) + ' league="Standard"' + str(
                                ' x="{}"'.format(itemparsed["x"])) + str(' y="{}"]'.format(itemparsed["y"])))
                            datafile.write("\n")
                            datafile.write(("{}".format(itemparsed["note"])).replace("~price", "~b/o"))
                        else:
                            pass
                with open("forumpost.txt", "a") as datafile:
                    datafile.write("\n")
                    datafile.write('[/spoiler]')
                j = j + 1
            else:
                j = j + 1
