import csv
import base64
import config
import re

conf = config.get()
url_map_file = conf['url_map_file']
shortener_domain = conf['shortener_domain']

def add(hash, url):
    with open(url_map_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([hash, url])
    file.close()

def getCount():
    count = 0
    with open(url_map_file, newline="") as file:
        reader = csv.reader(file)
        for _ in reader:
            count+=1
    file.close()
    return count

def find(string):
    r = None
    with open(url_map_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if(string in row):
                r = row
                break
    file.close()
    return r

def mapUrl(url):
    row = find(url)
    if row:
        return "{}/{}".format(shortener_domain, row[0])
    
    id = getCount() + 1
    hash = str(base64.b64encode(bytes(str(id), "utf-8")))
    sanitizedHash = re.sub(r"['b]","",hash)
    add(sanitizedHash,url)
    return "{}/{}".format(shortener_domain,sanitizedHash)

def getUrlByHash(hash):
    url = None
    with open(conf["url_map_file"], "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] == hash):
                url = row[1]
                break
    return url
