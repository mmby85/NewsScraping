import requests
from bs4 import BeautifulSoup as bf


url = "https://www.washingtonpost.com/sports/olympics/2021/07/09/team-usa-coronavirus-tokyo-olympics"

news = requests.get(url)

soup = bf(news.content, "html.parser")

paragraphe = soup.find_all('p')

title =  soup.find_all('h1')


