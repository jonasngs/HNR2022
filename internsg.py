import requests
from bs4 import BeautifulSoup as BS
import json

def sortList(store):
    result = sorted(store, key = lambda i: i['company']['name'])
    return result

def main(keyword):
    keyword = "software"
    count = 0
    result = []
    for page in range(1, 121):
        toBreak = False
        count += 1
        current = []
        url = f"https://www.internsg.com/jobs/{page}/?f_p&f_i&filter_s={keyword}#isg-top"

        request = requests.get(url)
        page = BS(request.text, "html.parser")
        store1 = page.findAll("div", {"class":"ast-row list-even"})
        for i in store1:
            t1 = i.findAll("div", {"class":"ast-col-lg-3"})
            t2 = i.findAll("div", {"class":"ast-col-lg-2"})
            t3 = i.findAll("div", {"class":"ast-col-lg-1"})
            name = t1[0].text
            domain = t1[0].span.text
            title = t1[1].text
            link = t1[1].a['href']
            isPage = link.find("f_pg=")
            if isPage == -1:
                pageNum = 1
            else:
                pageNum = int(link[link.find("f_pg=")+len("f_pg="):])
            # print(pageNum, count, pageNum == count)
            if pageNum != count:
                toBreak = True
                break
            index = name.find(domain)
            name = name[:index]
            date = t3[0].text
            temp = {}
            temp["company"] = {}
            temp["company"]["name"] = name.strip()
            temp["company"]["title"] = title.strip()
            temp["company"]["time"] = date.strip()
            temp["company"]["link"] = link.strip()
            current.append(temp)
        if not toBreak:
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
                link = t1[1].a['href']
                temp = {}
                temp["company"] = {}
                temp["company"]['name'] = name.strip()
                temp["company"]["title"] = title.strip()
                temp["company"]["time"] = date.strip()
                temp["company"]["link"] = link.strip()
                current.append(temp)
            result += current
        else:
            break
    return json.dumps(result)
