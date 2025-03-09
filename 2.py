import json
import requests
from datetime import datetime


key = "c793debe7a584e1f83d75028bedbd10d"
topic = input("Введите тему новости: ")
language = "ru"
page_size = 3
url = (f"https://newsapi.org/v2/everything?q={topic}&language={language}&pageSize={page_size}&apiKey={key}")
response = requests.get(url)
result = json.loads(response.text)
print(f"Всего найдено новостей: {result['totalResults']}\n")


if result["totalResults"] > 0:
    print(f"Последние новости по теме '{topic}':\n")
    for index, article in enumerate(result["articles"], start=1):
        print(f"Новость #{index}:")
        print(f"Источник: {article['source']['name']}")
        print(f"Автор: {article['author'] or 'Не указан'}")
        print(f"Заголовок: {article['title']}")
        print(f"Описание: {article['description']}")
        print(f"Ссылка на статью: {article['url']}")
        published_at = datetime.fromisoformat(article['publishedAt'].replace("Z", ""))
        print(f"Дата публикации: {published_at.strftime('%Y-%m-%d %H:%M:%S')}\n")
else:
    print(f"По вашему запросу '{topic}' новостей нет :(( ")

