from bs4 import BeautifulSoup as bs
import requests
from time import sleep

url = "https://www.lifeprint.com/asl101/lessons/"

count = 1
while True:
    file_save = open(f"/workspace/aslu/src/pages/lessons/content/lesson{count}.div", "w")
    file_save.close()

    if count<10:
        search_url = url + "lesson0" + str(count) + ".htm"
    else:
        search_url = url + "lesson" + str(count) + ".htm"
    file = requests.get(search_url)
    if file:
        soup = bs(file.content, 'html.parser')
        contents = soup.body.div.blockquote
        content = str(contents.string)
        for content in contents:
            if content and content != 'None':
                content = str(contents.string)
                if content and content != 'None':
                    file_save = open(f"/workspace/aslu/src/content/lessons/lesson{count}.div", "a")
                    file_save.write(content)
                    file_save.close()
    else:
        break
    count += 1