import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta
import logging
import re 

# лог
logging.basicConfig(filename='prov.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# извлечения новостей
def fetch_news(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # элементы с новостями 
        news_items = soup.find_all('article', class_='article')  # Изменено на 'article'

        for item in news_items:
            try:
                title = item.find('h3', class_='article-preview__title').text.strip() 
                summary = item.find('p', class_='listing-preview__desc').text.strip()
                authors = [author.text.strip() for author in item.find_all('a', class_='article-preview__author')]
            except AttributeError:
                title = ""
                summary = ""
                authors = ""
                logging.warning(f"Не удалось получить данные для статьи на {url}")
                continue

            # Проверка 
            if any(keyword in item.text.lower() for keyword in ['Дрон','Байден','США','Путин','Россия','Крым']):
                logging.info(f'Новая новость: \nЗаголовок: {title}\nАннотация: {summary}\nАвторы: {authors}\n---')
                print(f'Заголовок: {title}')
                print(f'Аннотация: {summary}')
                print(f'Авторы: {authors}')
                print('---')
    except Exception as e:
        logging.error(f'Ошибка при извлечении новостей: {e}')
        print(f'Ошибка при извлечении новостей: {e}')


# запуск скрипта
def run_script():
    while True:
        # скрипт на 4 часа
        end_time = datetime.now() + timedelta(hours=4)
        print(f'на 4 часа. Время окончания: {end_time}')
        logging.info(f'на 4 часа. Время окончания: {end_time}')

        while datetime.now() < end_time:
            # новостной сайт
            url = 'https://www.mk.ru/politics'
            fetch_news(url)

            # Пауза перед следующим запросом (например, 10 минут(2))
            time.sleep(600)  # 600 секунд = 10 минут
            print('Новый запуск поиска')
            logging.info('Новый запуск поиска')

        # После 4 часов ждем 1 час перед следующим запуском
        time.sleep(3600)  # 3600 секунд = 1 час
        print('Скрипт будет запущен снова через 1 час')
        logging.info('Скрипт будет запущен снова через 1 час')



# Запуск скрипта
if __name__ == '__main__':
    run_script()