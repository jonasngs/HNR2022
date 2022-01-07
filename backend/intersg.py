import requests
from bs4 import BeautifulSoup as BS
import json

def main(keyword):
    url = f"https://www.internsg.com/jobs/1/?f_p&f_i&filter_s{keyword}#isg-top"

    request = requests.get(url)
    page = BS(request.text, "html.parser")
    store = page.findAll("div",{"class":"ast-row latestJobItem"})
    results = {}
    for posting in store:
        temp = posting.find("div",{"class":"ast-col-sm-10"})
        job_name = temp.text
        url = temp.a["href"]
        results[job_name] = url
    
    return results