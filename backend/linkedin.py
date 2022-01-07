import urllib

from bs4 import BeautifulSoup
import requests
import csv
from flask import json


def search(keyword):
    result = []
    for i in range(0, 5):
        kw = urllib.parse.quote_plus(keyword)
        page = '&location=Singapore&start=' + str(i * 25)

        # for sg only
        # source = requests.get('https://www.linkedin.com/jobs/search/?geoId=102454443&keywords=' + kw + page).text
        source = requests.get('https://www.linkedin.com/jobs/search/?keywords=' + kw + '&location=Singapore' + page).text
        # print('https://www.linkedin.com/jobs/search/?geoId=102454443&keywords=' + kw + page)
        soup = BeautifulSoup(source, 'lxml')
        jobs = soup.findAll('div', class_='base-card base-card--link base-search-card base-search-card--link job-search-card')

        for job in jobs:
            try:
                date = job.time['datetime']
                # print(date)
                time = job.time.text.strip()
                # print(time)
                title = job.a.text.strip()
                # print(title)
                company = job.find('a', class_='hidden-nested-link').text.strip()
                link = job.a['href'].strip()
                add = {"company" : company, "title" : title, "link" : link, "time" : date}
                result.append(add)
            except Exception as e:
                print('Error')

    # for key, value in result.items():
    #     print(key, ' : ', value)
    # print(result)
    return json.dumps(result)

search('software engineer intern')

