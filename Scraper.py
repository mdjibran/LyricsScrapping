from urllib.request import urlopen
from bs4 import BeautifulSoup
from _overlapped import NULL


url = "https://www.azlyrics.com/"
def getPage(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    return soup

def getListLink(aClassName, divClassName, url):
    menu = getPage(url).find_all("div", class_=divClassName)
    for a in menu:
        content = ''
        for link in a.find_all("a", class_=aClassName):
            content += str(link) + "," + "http:"+link.get("href") + "\n"        


completed = open("completed.csv", "r+")
existing = completed.readlines()  

url = existing[0].split(',')[1]
artist = getPage(url)
songsList = []
menu = artist.find_all("div", class_='col-sm-6 text-center artist-col')
for a in menu:
    for link in a.find_all("a"):
        songsList.append("http://www.azlyrics.com/"+link.get("href") + "\n")


print(songsList[0])
url = songsList[0]
albumList = getPage(url)
print(albumList.title)
id = 0

menu = albumList.find_all("div", id="listAlbum")
for a in menu:
    for link in a.find_all("a"):
        songUrl = "https://www.azlyrics.com/"+str(link.get("href")).replace("../","")
        if not str(songUrl).endswith("/None"):
            print(songUrl)
            id += 1
            songPage = getPage(songUrl)
            songPageDiv = songPage.find_all("div", class_="col-xs-12 col-lg-8 text-center")
            for b in songPageDiv:
                print(b.findAll("b"))
