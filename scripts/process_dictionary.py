import os
import io
import shutil
from bs4 import BeautifulSoup as bs
import unicodedata

root_dir = os.getcwd()
target_dir = f"{root_dir}/src/components/content/dictionary/"

for file in os.scandir(target_dir):
    with open(target_dir + file.name, 'r', encoding="utf-8") as f:
        contents = f.read()
        soup = bs(contents, 'html.parser')
        for script in soup.find_all("script"):
            script.decompose()
        # clean_soup = unicodedata.normalize('NFKD', soup.text)
    with open(target_dir + file.name, 'wb') as f:
        f.write(soup.prettify("ascii"))
