import os
import shutil

root_dir = os.getcwd()
src = f"{root_dir}/extractions/dictionary"
dest = f"{root_dir}/src/pages/dictionary"

before = """---
import { SITE } from "~/config.mjs";
import PageLayout from "~/layouts/PageLayout.astro";

const title = `${SITE.org} | Dictionary`;
const description = `Dictionary page`;
const canonical = new URL("", Astro.site);
---
<PageLayout meta={{ title, description, canonical }}>
    <main>"""

after = """    </main>
</PageLayout>"""

for filename in os.scandir(src):
    with open(src + filename, 'w'):

        # shutil.copy(src, dest)
