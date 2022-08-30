from bs4 import BeautifulSoup as bs
import requests
from time import sleep
from string import ascii_lowercase
import re
import os

url = "http://asluniversity.com/asl101/index/"


for c in ascii_lowercase:
    word_base_url = f"http://asluniversity.com/asl101/pages-signs/{c}.htm"
    file_save = open(f"./public/content/dictionary/references/{c}.div", "w")

    file_save.close()

    search_url = url + c + ".htm"

    file = requests.get(search_url)
    if file:
        soup = bs(file.content, 'html.parser')
        links = soup.find_all("a")
        for link in links:
            word = link.text.strip()
            # print(word)
            if not os.path.exists(f"./public/content/dictionary/{word}"):
                os.makedirs(f"./public/content/dictionary/{word}")
            try:
                word_file = requests.get(f"{word_base_url}/{word}.htm")
            except:
                continue
            word_soup = bs(word_file.content, 'html.parser')
            word_contents = word_soup.find("table")
            with open(f"./public/content/dictionary/{word}/{word}.div") as f:
                f.write(str(word_contents))

                # content = str(contents.string)

                # file_save = open(
                #     f"./public/content/dictionary/references/{c}.div", "a")
                # file_save.write(str(contents[1]))
                # file_save.close()

                # extensions = re.findall('"([^"]*)"', str(contents[1]))
                # words = re.findall('>([^"]*)</a>', str(contents[1]))

                #     for index, extension in enumerate(extensions):
                #         extension = extension.replace('..', word_base_url)
                #         try:
                #             word_file = requests.get(extension)
                #         except:
                #             continue

                #         word_soup = bs(word_file.content, 'html.parser')
                #         word_contents = word_soup.find("table")

                #         word = words[index]
                #         word = word.replace(' ', '')
                #         word = word.replace("/", '')
                #         print(word)
                #         try:
                #             word_save = open(
                #                 f"./public/content/dictionary/words/{word}.div", "w")
                #         except:
                #             continue
                #         word_save.write(str(word_contents))
                #         word_save.close()

    else:
        break
