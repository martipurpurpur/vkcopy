import re
import urllib.request
from arg_parser import parse_arguments


def main(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    img_urls = re.findall('img .*?src="(.*?)"', str(html))
    index = 0
    for img in img_urls:
        if img.endswith(".jpg") and img.startswith("https"):
            file_path = f"photos/{index}.jpg"
            index += 1
            urllib.request.urlretrieve(img, file_path)
    print(img_urls)


if __name__ == "__main__":
    url = parse_arguments()
    main(vars(url)["url"])
