import requests
from bs4 import BeautifulSoup

url = 'https://www.wantedly.com/id/sosuke_mikami'
url = 'https://www.wantedly.com/id/lzrjgizhfoai'
#url = "https://www.wantedly.com/id/hiroto_suzuki_aaa"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
elems = soup.select('.headerMainContent h1')

#print(elems[0].contents[0])

userSelector = {
    "user": ".headerMainContent h1",
    "text": "#react-aria-1",
    "url": ".LinkCollection__SocialLinkListUl-sc-140isxv-2 li:nth-child(1) a", #[0]
    "img": ".wui-avatar-layout img",
}

user = {}

for key in userSelector.keys():
    elems = soup.select(userSelector[key])
    if key == "img":
        if not bool(elems):
            user[key] = None
            continue
        user[key] = elems[0].attrs['src']
    elif key == "url":
        if not bool(elems):
            user[key] = None
            continue
        user[key] = elems[0].attrs['href']
    else:
        if not bool(elems):
            user[key] = None
            continue
        user[key] = elems[0].contents[0]

print(user)

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

# 作品
elems =soup.select(".wui-elevation-null>.wui-reaction-by-color")

productSelector = {
    "text": "strong",
    "img": "img",
    "date_s": "time"
}

product = []

i = 0
for elem in elems:
    productList = {}
    for key in productSelector.keys():
        if key == "img":
            print(key)
            if not bool(elem.select(productSelector[key])):
                productList[key] = None
                continue
            print(elem.select(productSelector[key])[0].attrs["src"])
            productList[key] = elem.select(productSelector[key])[0].attrs["src"]
        elif key == "url":
            print(key)
            if not bool(elem.select(productSelector[key])):
                productList[key] = None
                continue
            print(elem.select(productSelector[key])[0].attrs["href"])
            productList[key] = elem.select(productSelector[key])[0].attrs["href"]
        else:
            print(key)
            if not bool(elem.select(productSelector[key])):
                productList[key] = None
                continue
            print(elem.select(productSelector[key])[0].string)
            productList[key] = elem.select(productSelector[key])[0].string
    product.append(productList)
    i += 1

product.pop(-1)
product.pop(-1)
product.pop(-1)
product.pop(-1)
product.pop(-1)

print(product)