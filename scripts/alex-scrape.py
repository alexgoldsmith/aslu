from bs4 import BeautifulSoup as bs
import requests
from time import sleep
from string import ascii_lowercase
import re
import os

root_dir = "/home/alex/aslu"
url = "http://asluniversity.com/asl101/index/"
word_base_url = "http://asluniversity.com/asl101"


for c in ascii_lowercase:
    index_url = url + c + ".htm"
    index_file = requests.get(index_url)
    if index_file:
        soup = bs(index_file.content, 'html.parser')
        links = soup.find_all("a")
        for link in links:
            try:
                word = link.string.strip()
                href = link.get("href")
                href = href.replace('..', word_base_url)
                print(word)
                # print(href)
                if not os.path.exists(f"{root_dir}/extractions/dictionary/{word}"):
                    os.makedirs(f"{root_dir}/extractions/dictionary/{word}")
                word_file = requests.get(href)
                word_soup = bs(word_file.content, 'html.parser')
                block = word_soup.blockquote

                # write blockquotes
                with open(f"{root_dir}/extractions/dictionary/{word}/{word}.div", "w") as f:
                    f.write(block.prettify())

                # write images
                images = block.find_all("img")
                for image in images:
                    img_src = image["src"]
                    img_name_and_ext = img_src.rsplit("/", 1)[-1]
                    img_url = img_src.replace("../..", word_base_url)
                    print(img_url)
                    img_data = requests.get(img_url).content
                    with open(f"{root_dir}/extractions/dictionary/{word}/{img_name_and_ext}", "wb") as f:
                        f.write(img_data)

                # write text only
                with open(f"{root_dir}/extractions/dictionary/{word}/{word}.md", "w") as f:
                    for text in block.stripped_strings:
                        f.write(text)
            except:
                continue
    else:
        continue
