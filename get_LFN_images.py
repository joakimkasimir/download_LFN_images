#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import shutil
import os
import argparse

parser = argparse.ArgumentParser(description='Load images from Local Food Node to directory outputdir')
parser.add_argument('foodnodeUrl', action='store', help='URL like https://localfoodnodes.org/node/kavlinge-matnod?date=2018-10-24')
arg_parameters = parser.parse_args()

#arg_parameters.foodnodeUrl = 'https://localfoodnodes.org/node/kavlinge-matnod?date=2018-10-24'

def loadHtml(url=arg_parameters.foodnodeUrl):
    content = requests.get(url)
    if content.status_code == 200:
        return content.text
    else:
        print "No data from "+matnodsUrl+": Return Code "+content.status_code
        exit(1)

def loadFile(filename='landskrona-matnod.html'):
    with open(filename) as fh:
        content = fh.read()
    return content

#content = loadFile()
content = loadHtml()
soup = BeautifulSoup(content, 'html.parser')


images_files = [x['src'] for x in soup.findAll('img', {'class': 'card-image-top'})]
#print images_files
filenumber = 1
directory = 'outputdir'
if not os.path.exists(directory):
    os.makedirs(directory)
for image in images_files:
    if image != '/images/product-image-placeholder.jpg':
        r = requests.get(image, stream=True)
        if r.status_code == 200:
            with open(directory+"/"+str(filenumber)+".jpg", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
                filenumber = filenumber + 1

