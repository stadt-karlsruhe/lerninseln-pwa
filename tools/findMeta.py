import os
import sys
import requests
from bs4 import BeautifulSoup
import base64
import json

# we can call this from php like:
# $cmd = "python3 findMeta.py " . $url;
# $data = json_decode(exec($cmd));


def loadUrl(url):
    try:
        page = requests.get(url,timeout=10)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup
    except:
        print ("Url error")
        return None
        
# rule for target
def scan(data,id,labels):
    for i in labels:
        for d in data:
            if d["name"] == i:
                content = d["content"]
                if content > "":
                    return d["content"]

    return None

def findMeta(url):
    parms = {}
    soup = loadUrl(url)
    if soup == None:
        return parms

    # find all link rels
    links = soup.find_all('link')
    linkImgs = []
    icon = ""
    for m in links:
        if m.has_attr("rel"):
            rel = m["rel"][0]
            if rel == "image_src":
                linkImgs.append(m["href"])
            if rel == "icon":
                icon = m["href"]

    # find all meta tags
    results = soup.find_all('meta')

    if len(results) == 0:
        return parms

    # all meta tags
    metas = []
    for m in results:
        if (m.has_attr("name") or m.has_attr("property")) and m.has_attr("content"):
            if m.has_attr("name"):
                name = m["name"]
            else:
                name = m["property"]
                
            metas.append({"name":name,"content":m["content"]})

    # rule definitions: label and identifiers
    search = [("site",["og:site","twitter:site","provider"]),
              ("image",["og:image","twitter:image","image"]),
              ("url",["og:url","twitter:url","default:url"]),
              ("title",["og:title","twitter:title","name"]),
              ("description",["og:description","twitter:description","description"]),
              ("type",["og:type","twitter:card"])
              ]

    # process rules
    for s in search:
        x = scan(metas,s[0],s[1])
        if x != None:
            parms[s[0]] = x

    # potentially add default type and url
    if "type" not in parms.keys():
        parms["type"] = "website"
    if "url" not in parms.keys():
        parms["url"] = url
    # check image and insert from links if possible
    if "image" not in parms.keys():
        if len(linkImgs) > 0:
            if (prnt):
                print("Img: ",linkImgs[0])
            if not linkImgs[0].startswith("data:"):
                if linkImgs[0].startswith("http"):
                    parms["image"] = linkImgs[0] # to be improved
                else:
                    parms["image"] = url + "/" + linkImgs[0] # to be improved
    # insert icon if exists
    if icon > "":
        if not icon.startswith("data:"):
            if icon.startswith("http"):
                parms["icon"] = icon # to be improved
            else:
                parms["icon"] = url + "/" + icon # to be improved
        
    return parms


def main():
    if len(sys.argv) == 2:
        parms = findMeta(sys.argv[1])
        print(json.dumps(parms))
    else:
        print(json.dumps({}))

if __name__ == '__main__':
    main()
    
    
