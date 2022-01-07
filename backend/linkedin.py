import urllib

from bs4 import BeautifulSoup
import requests
import csv


# number of jobs
# match = soup.title.text
# pretty = soup.prettify()
# print(soup.prettify())
#joblist
# jobs = soup.find('div', class_='jobs-search-results display-flex flex-column')
# jobs = soup.findAll('div', class_='base-search-card__info')
# for job in jobs:
#     # card = job
#     # title = job.find('a', class_='hidden-nested-link')
#     try:
#         company = job.a.text
#         link = job.a['href']
#     except Exception as e:
#         company = 'None'
#         link = 'None'
#
#     print(company)
#     print(link)
from flask import json


def search(keyword):
    kw = urllib.parse.quote_plus(keyword)
    # for sg only
    source = requests.get('https://www.linkedin.com/jobs/search/?geoId=102454443&keywords=' + kw).text
    soup = BeautifulSoup(source, 'lxml')
    jobs = soup.findAll('div', class_='base-card base-card--link base-search-card base-search-card--link job-search-card')
    result = {}
    for job in jobs:
        # card = job
        # title = job.find('a', class_='hidden-nested-link')
        try:
            title = job.a.text.strip()
            company = job.find('a', class_='hidden-nested-link').text.strip()
            link = job.a['href'].strip()
        except Exception as e:
            title = 'None'
            company = 'None'
            link = 'None'
        add = {"title" : title, "link" : link}
        result[company] = add
    for key, value in result.items():
        print(key, ' : ', value)
    return json.dumps(result)

# search('software engineer intern')

