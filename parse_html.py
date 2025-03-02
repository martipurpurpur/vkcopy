import re
from bs4 import BeautifulSoup


def get_album_name(html):
    """ Парсим название альбома с html-страницы """
    soup = BeautifulSoup(html, "html.parser")
    album_div = soup.find("div", class_="ui_crumb")
    album_name_ = album_div.get_text(strip=True)
    album_name = re.sub(r'[\\/:*?"<>|]', "_", album_name_)
    return album_name
