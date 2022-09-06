import os
import re
from bs4 import BeautifulSoup as bs
import unicodedata

root_dir = os.getcwd()
target_dir = f"{root_dir}/src/components/content/dictionary/"

for file in os.scandir(target_dir):
    with open(target_dir + file.name, 'r', encoding="utf-8") as f:
        contents = f.read().replace('&lt;', '').replace('&gt;', '')
        soup = bs(contents, 'lxml')

        for script in soup.find_all("script"):  # remove script tags
            script.decompose()

        for obj in soup.find_all("object"):  # remove defunct flash objects
            obj.decompose()

        def findFoot(string):  # find defunct footer ptags
            return re.compile("Want to help").search(string) or re.compile("Want even").search(string) or re.compile("Bandwidth").search(string) or re.compile("Dr. Bill's new").search(string) or re.compile("You can learn").search(string)

        ptags = soup.find_all("p")
        for ptag in ptags:
            for font_tag in ptag.find_all(string=findFoot):
                ptag.decompose()

        for form in soup.find_all("form"):
            form.decompose()  # remove old footer search bar

        # TODO: could be more specific in the search criteria
        def linkFilter(href):  # find links to .htm files
            return href and re.compile(".htm").search(href)

        for link in soup.find_all(href=linkFilter):  # replace references
            newref = link["href"].rsplit("/", 1)[-1].replace(".htm", "")
            link["href"] = "/dictionary/" + newref

    with open(target_dir + file.name, 'w', encoding="utf-8") as f:
        f.write(soup.prettify(formatter=lambda s: unicodedata.normalize("NFKD", s)))
