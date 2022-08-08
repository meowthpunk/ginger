import requests
from bs4 import BeautifulSoup as BS

r = requests.get(
    "https://psycatgames.com/ru/magazine/party-games/trivia-questions/#random-trivia-questions")

html = BS(r.content, "html.parser")
# print(html)

for el in html.select("h3 + ul"):
    # title = html.select("h3 + ul")
    print(el.select("li"))


#
