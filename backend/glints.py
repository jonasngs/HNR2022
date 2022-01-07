import requests
from bs4 import BeautifulSoup as BS
import json

def main():
    url = "https://glints.com/sg/opportunities/jobs/explore?country=SG&locationName=Singapore&jobCategories=1"

    request = requests.get(url)
    page = BS(request.text, "html.parser")
    store = page.findAll("div", {"class": "compact_job_card"})
    results = []
    for posting in store:
        time = posting.findAll("div", {"class": "CompactOpportunityCardsc__OpportunityInfo-sc-1xtox99-13 hiAtMr"})[-1].text.strip().replace("\u2013", "-")
        title = posting.find("h3", {"class": "CompactOpportunityCardsc__JobTitle-sc-1xtox99-7 kJpKeD"}).text.strip()
        company = posting.find("div", {"class": "CompactOpportunityCardsc__Ellipsis-sc-1xtox99-11 hOPlUO"}).text.strip()
        domain = "http://glints.com"
        link = domain + posting.a['href'].strip()
        add = {"company" : company, "title": title, "link": link, "time": time}
        results.append(add)

    return json.dumps(results)

