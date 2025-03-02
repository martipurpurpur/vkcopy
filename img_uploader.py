import os
import re
import time
import urllib.request

import config
from arg_parser import parse_arguments
from parse_html import get_album_name


def main(html_path, target_base_folder):
    """ Получение фото с html- страницы и сохранение в директорию по названию альбома """
    response = urllib.request.urlopen(f"file:///{html_path}") # для винды
    # Получаем список ссылок на изображения
    html = response.read()
    img_urls = re.findall('img .*?src="(.*?)"', str(html))

    target_folder = get_album_name(html)
    # Создаем директорию по имени альбома, куда будем загружать фото
    os.makedirs(os.path.join(target_base_folder, target_folder), exist_ok=True)
    index = 0
    # Загрузка фото
    for img in img_urls:
        if img.startswith("https"):
            file_path = os.path.join(target_base_folder, target_folder, f"{index}.jpg")
            index += 1
            urllib.request.urlretrieve(img, file_path)
    print(img_urls)


if __name__ == "__main__":
    archive_folder = vars(parse_arguments())["in"]
    target_base_folder = vars(parse_arguments())["out"] or config.BASE_FOLDER
    # Получаем список всех html из архивной папки (каждый html - это альбом с фото)
    files = sorted(f for f in os.listdir(archive_folder) if f.endswith(".html"))
    for file in files:
        html_path = os.path.abspath(os.path.join(archive_folder, file))
        main(html_path, target_base_folder)
        time.sleep(1)
