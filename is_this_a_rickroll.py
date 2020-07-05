from bs4 import BeautifulSoup as bs
import requests as req
import sys
try:
    if len(sys.argv) < 2:
        print("No argument provided")
    else:
        r = req.get(sys.argv[1])
        soup = bs(r.content,"html.parser")
        yt = soup.title
        print(yt.text)
        title = soup.find("meta",  property = "og:title")
        print("[+] Title:",title["content"])
        desc = soup.find("meta", property = "og:description")
        print("[+] Description:",desc["content"])
        thumbimg = soup.find("meta", property = "og:image")
        print("[+] Thumbnail image link:",thumbimg["content"])
        views = soup.find("meta", itemprop = "interactionCount")
        print("[+] Views:",views["content"])
except Exception as e:
    raise
