from bs4 import BeautifulSoup as bs
import requests
from time import sleep
from string import ascii_lowercase
import re
import os

root_dir = os.getcwd()
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
                word = link.string.strip('"').replace('[','').replace(']','')
                href = link.get("href")
                href = href.replace('..', word_base_url)
                print(word)
                # print(href)
                word_file = requests.get(href)
                word_soup = bs(word_file.content, 'html.parser')

                block = word_soup.blockquote

                # write images
                images = block.find_all("img")
                for image in images:
                    img_src = image["src"]
                    img_name_and_ext = img_src.rsplit("/", 1)[-1]
                    img_url = img_src.replace("../..", word_base_url)
                    img_data = requests.get(img_url).content
                    with open(f"{root_dir}/public/images/{img_name_and_ext}", "wb") as f:
                        f.write(img_data)
                    # replace references
                    image["src"] = f"/images/{img_name_and_ext}"

                # write any linked gifs
                gifs = block.find_all("a", href=lambda href: ".gif" in href)
                for gif in gifs:
                    gif_src = gif["href"]
                    gif_name_and_ext = gif_src.rsplit("/", 1)[-1]
                    print(gif_name_and_ext)
                    gif_url = gif_src.replace("../..", word_base_url)
                    gif_data = requests.get(gif_url).content
                    with open(f"{root_dir}/public/images/{gif_name_and_ext}", "wb") as f:
                        f.write(gif_data)
                    # replace references
                    gif["href"] = f"/images/{gif_name_and_ext}"

                # write blockquotes
                with open(f"{root_dir}/src/pages/dictionary/{word}.astro", "w") as f:
                    f.write(block.prettify())

                # write text only
                # with open(f"{root_dir}/src/pages/pages-text/{c}/{word}/{word}.md", "w") as f:
                #     for text in block.stripped_strings:
                #         f.write(text)
            except:
                continue
    else:
        continue
