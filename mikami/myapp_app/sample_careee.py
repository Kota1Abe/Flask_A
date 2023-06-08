import requests
from bs4 import BeautifulSoup

url = 'https://www.wantedly.com/id/sosuke_mikami_samp'

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
elems = soup.select('.headerMainContent h1')


# 経歴
careerSelector = {
    "text": ".fuhLwL span",
    "position": ".eMhnQX h3",
    "img": ".btVpRG img",
    "date_s": "div time:nth-child(1)"
}

caree = []

elems =soup.select(".jxAaMM")
#print(elems)

i = 0
for elem in elems:
    careelist = {}
    for key in careerSelector.keys():
        if key == "img":
            print(key)
            if not bool(elem.select(careerSelector[key])):
                careelist[key] = None
                continue
            print(elem.select(careerSelector[key])[0].attrs["src"])
            careelist[key] = elem.select(careerSelector[key])[0].attrs["src"]
        elif key == "url":
            print(key)
            if not bool(elem.select(careerSelector[key])):
                careelist[key] = None
                continue
            print(elem.select(careerSelector[key])[0].attrs["href"])
            careelist[key] = elem.select(careerSelector[key])[0].attrs["href"]
        else:
            print(key)
            if not bool(elem.select(careerSelector[key])):
                careelist[key] = None
                continue
            print(elem.select(careerSelector[key])[0].string)
            careelist[key] = elem.select(careerSelector[key])[0].string
    caree.append(careelist)
    i += 1


print(caree)