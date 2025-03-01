from bs4 import BeautifulSoup


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    album_div = soup.find("div", class_="ui_crumb")
    return album_div.get_text(strip=True)
