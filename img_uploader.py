import os
import re
import time
import urllib.request

import config
from arg_parser import parse_arguments
from parse_html import get_album_name


def main(url):
    response = urllib.request.urlopen(f"file:///{url}") # для винды
    html = response.read()
    img_urls = re.findall('img .*?src="(.*?)"', str(html))
    target_folder = get_album_name(html)
    print(target_folder)
    os.makedirs(os.path.join(config.BASE_FOLDER, target_folder), exist_ok=True)
    index = 0
    for img in img_urls:
        if img.startswith("https"):
            file_path = os.path.join(config.BASE_FOLDER, target_folder, f"{index}.jpg")
            index += 1
            urllib.request.urlretrieve(img, file_path)
    print(img_urls)


if __name__ == "__main__":
    folder = vars(parse_arguments())["path"]
    files = sorted(f for f in os.listdir(folder) if f.endswith(".html"))
    for file in files:
        url = os.path.abspath(os.path.join(folder, file))
        main(url)
        time.sleep(1)
