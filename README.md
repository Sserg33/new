Скрипт выполнен на Python, представляет собой сбор новостей с сайта Fox News, который ищет статьи, содержащие слова “democrat” или “republican”.

Устанавливаем библиотеки requests и BeautifulSoup4

Импорт библиотек:

requests: Библиотека для отправки HTTP-запросов к веб-сайтам, для того чтобы получить HTML-код страницы.
BeautifulSoup: Библиотека для парсинга (разбора) HTML-кода, позволяет найти нужные элементы на странице.
time: Библиотека для работы со временем.
datetime: Библиотека для работы с датами и временем.
timedelta: Библиотека для создания интервалов времени.
logging: Библиотека для записи логов.

2. Настройка лог-файла:

logging.basicConfig:  команда настраивает библиотеку logging для записи информации в файл.
filename='1_log.txt': Имя файла, в который будут записываться логи.
level=logging.INFO:  сообщения, которые будут записываться в лог. logging.INFO - это стандартный уровень, он записывает информационные сообщения.
format='%(asctime)s - %(levelname)s - %(message)s': Формат записи сообщений в лог-файл.

3. Функция fetch_news(url):

fetch_news(url):  функция извлекает новости с заданного URL (url).
response = requests.get(url): HTTP-запрос к указанному URL и получает ответ (HTML-код страницы).
soup = BeautifulSoup(response.text, 'html.parser'): Создает объект BeautifulSoup для парсинга HTML-кода.
news_items = soup.find_all('article', class_='article-body'): Находит все элементы на странице, которые имеют тег article и класс article-body.
Цикл for item in news_items:: Проходит по каждому найденному элементу новости.
title = item.find('h2').text.strip(): Находит заголовок (h2) в элементе новости и извлекает его текст. strip() удаляет лишние пробелы.
summary = item.find('p', class_='article-summary').text.strip(): Находит аннотацию (p с классом article-summary) и извлекает ее текст.
authors = [author.text.strip() for author in item.find_all('a', class_='author-link')]: Находит ссылки на авторов (a с классом author-link) и извлекает их текст.
Проверка ключевых слов:
if 'democrat' in item.text.lower() or 'republican' in item.text.lower():: Проверяет, есть ли в тексте статьи слова “democrat” или “republican” (в нижнем регистре).
Если слова найдены, информация о новости записывается в лог и выводится в консоль.
try...except Exception as e: Блок обработки ошибок. 
4. Функция run_script():

run_script():  функция запускает основной цикл работы скрипта.
while True: бесконечный цикл.
end_time = datetime.now() + timedelta(hours=4): Определяет время окончания текущего 4-часового цикла.
while datetime.now() < end_time:: Внутренний цикл, который будет работать до окончания 4-часового интервала.
url = 'https://www.foxnews.com/politics': Задает URL, с которого будут извлекаться новости.
fetch_news(url): Вызывает функцию fetch_news для получения новостей с заданного URL.
time.sleep(600): Ожидает 10 минут перед следующим запросом.
time.sleep(3600): После завершения 4-часового цикла ожидает 1 час перед повторным запуском цикла.


