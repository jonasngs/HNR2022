import requests
from bs4 import BeautifulSoup as BS
import json

def main(keyword):
    url = f"https://www.internsg.com/jobs/1/?f_p&f_i&filter_s{keyword}#isg-top"

    request = requests.get(url)
    page = BS(request.text, "html.parser")
    store1 = page.findAll("div", {"class":"ast-row list-even"})
    result = []
    for i in store1:
        t1 = i.findAll("div", {"class":"ast-col-lg-3"})
        t2 = i.findAll("div", {"class":"ast-col-lg-2"})
        t3 = i.findAll("div", {"class":"ast-col-lg-1"})
        name = t1[0].text
        domain = t1[0].span.text
        title = t1[1].text
        index = name.find(domain)
        name = name[:index]
        date = t3[0].text
        temp = {}
        temp[name] = {}
        temp[name]["title"] = title.strip()
        temp[name]["date"] = date.strip()
        result.append(temp)
    store2 = page.findAll("div", {"class":"ast-row list-odd"})
    for i in store2:
        t1 = i.findAll("div", {"class":"ast-col-lg-3"})
        t2 = i.findAll("div", {"class":"ast-col-lg-2"})
        t3 = i.findAll("div", {"class":"ast-col-lg-1"})
        name = t1[0].text
        domain = t1[0].span.text
        title = t1[1].text
        index = name.find(domain)
        name = name[:index]
        date = t3[0].text
        temp = {}
        temp[name] = {}
        temp[name]["title"] = title.strip()
        temp[name]["date"] = date.strip()
        result.append(temp)
    return json.dumps(result)
print(main(""))