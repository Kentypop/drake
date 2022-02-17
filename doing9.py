import requests

import bs4

result= requests.get("https://example.com/")

print(dir(result))

print(result.text)

soup= bs4.BeautifulSoup(result.text, "lxml")

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print(soup.select("p")[0].getText())