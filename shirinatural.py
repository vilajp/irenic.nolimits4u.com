import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS ProductosShiri
    (id INTEGER PRIMARY KEY, nombre TEXT UNIQUE, precio INTEGER)''')

url = "https://www.shirinatural.com.ar/productos/?mpage=3"

try:
    document = urlopen(url, context=ctx)

    html = document.read()

    if document.getcode() != 200 :
        print("Error on page: ",document.getcode())

    if 'text/html' != document.info().get_content_type() :
        print("Ignore non text/html page")

    print('('+str(len(html))+')', end=' ')

    soup = BeautifulSoup(html, "html.parser")
except KeyboardInterrupt:
    print('')
    print('Program interrupted by user...')

except:
    print("Unable to retrieve or parse page")

# Retrieve all of the script tags
tags = soup('script')
count = 0
productos = "[\n"
for tag in tags:
    tipo = tag.get("type", None)

    if tipo == "application/ld+json":
        if '"@type": "Product",' in str(tag):
            productos += str(tag)[len('<script type="application/ld+json">'):-len('</script>')].strip() + ","

            continue

productos = productos[:-1] + "\n]"

print(productos)

todos = json.loads(productos)

for item in todos:
    print(item["name"])


    # cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( href, ) )
    # count = count + 1
    # conn.commit()
    #
    # cur.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', ( href, ))
    # try:
    #     row = cur.fetchone()
    #     toid = row[0]
    # except:
    #     print('Could not retrieve id')
    #     continue
    # # print fromid, toid
    # cur.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES ( ?, ? )', ( fromid, toid ) )
    #

cur.close()


