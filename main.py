import json
import os
import vk_api
import requests
import logging




# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Ваш токен и версия API
API_VERSION = '5.131'

def get_wall_posts(group_name):
    url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=40&access_token={token}&v={API_VERSION}"
    req = requests.get(url)
    src = req.json()

    if 'error' in src:
        logging.error(f"Ошибка при получении постов: {src['error']['error_msg']}")
        return

    # Проверяем существует ли директория с именем группы
    directory = f"{group_name}"
    if not os.path.exists(directory):
        os.mkdir(directory)
        logging.info(f"Создана директория: {directory}")

    # Сохраняем данные в json файл
    with open(f"{directory}/{group_name}_wall.json", "w", encoding="utf-8") as file:
        json.dump(src, file, indent=4, ensure_ascii=False)

    posts = src["response"]["items"]
    fresh_posts_ids = {post["id"] for post in posts}

    # Читаем существующие посты
    exist_posts_file = f"{directory}/exist_posts_{group_name}.txt"
    if os.path.exists(exist_posts_file):
        with open(exist_posts_file, 'r') as file:
            existing_ids = {int(line.strip()) for line in file}
    else:
        existing_ids = set()
        logging.info("Файл с ID постов не найден, создаём его.")

    new_posts = fresh_posts_ids - existing_ids
    if new_posts:
        with open(exist_posts_file, 'a') as file:
            for new_post_id in new_posts:
                file.write(f"{new_post_id}n")
                logging.info(f"Добавлен новый пост с ID {new_post_id}")
    else:
        logging.info("Новых постов не найдено.")

    # Извлекаем и обрабатываем данные из постов
    for post in posts:
        # Обработка поста
        print_post_data(post)

def print_post_data(post):
    post_id = post["id"]
    logging.info(f"Обработка поста с ID {post_id}")
    
    # Здесь можно добавить условия для различных типов вложений
    if "attachments" in post:
        for attachment in post["attachments"]:
            if attachment["type"] == "photo":
                extract_photo(attachment["photo"])

def extract_photo(photo):
    photo_quality = ["photo_2560", "photo_1280", "photo_807", "photo_604", "photo_130", "photo_75"]
    for quality in photo_quality:
        if quality in photo:
            logging.info(f"Фото с качеством {quality}: {photo[quality]}")
            break

def main():
    group_name = input("Введите ID группы: ")
    get_wall_posts(group_name)
    # ... Остальные функции вызова

if __name__ == '__main__':
    main()
