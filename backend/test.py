import requests
from bs4 import BeautifulSoup as BS
import json

url = "https://www.nodeflair.com/jobs?query=&page=1&sort_by=relevant"
request = requests.get(url)
page = BS(request.text, "html.parser")
print(page)