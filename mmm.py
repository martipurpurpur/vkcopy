import re
import time
import urllib.request
import config


def main():
    response = urllib.request.urlopen(config.URL)
    html = response.read()
    img_urls = re.findall('img .*?src="(.*?)"', str(html))
    index = 0
    for img in img_urls:
        if img.endswith(".jpg") and img.startswith("https"):
            file_path = f"photos/{index}.jpg"
            index +=1
            urllib.request.urlretrieve(img, file_path)
    print(img_urls)


if __name__ == "__main__":
    main()
