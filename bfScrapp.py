import requests
from bs4 import BeautifulSoup as bf


url = input('please enter url :')

news = requests.get(url)

soup = bf(news.content, "html.parser")

paragraphe = soup.find_all('p')

title =  soup.find_all('h1')


