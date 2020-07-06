from bs4 import BeautifulSoup as bs
import requests as req
import sys
import re
def scrapeurl(url):
    try:
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
        print("[-] Error:",e)
try:
    if len(sys.argv) < 2:
        print("[-] No argument provided")
    url = re.search("^https:\/\/www\.youtube\.com\/watch\?v=[a-zA-Z0-9]{11}",sys.argv[1])
    if(url):
        print("[+] Attempting to scrape:",url.string)
        scrapeurl(url)
    else:
        print("[-] Try again with a valid URL")
except Exception as e:
    raise
