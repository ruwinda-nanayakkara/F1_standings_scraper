from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.formula1.com/en/results.html/2022/drivers.html").text
print(source)

