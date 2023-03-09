from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest

titles,names,location = [],[],[]

resp = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
src = resp.content
soup = BeautifulSoup(src,"lxml")
job_titles = soup.find_all("h2",{"class":"css-m604qf"})
company_names = soup.find_all("a",{"class":"css-17s97q8"})
company_location = soup.find_all("span",{"class":"css-5wys0k"})

iter = len(job_titles)
for i in range(iter):
    titles.append(job_titles[i].text)
    names.append(company_names[i].text)
    location.append(company_location[i].text)

with open("job_info.csv","w") as info:
    info_writer = csv.writer(info)
    info_writer.writerow(["Job Title","Company Name","Company Location"])
    all = [titles,names,location]
    zipped = (zip_longest(*all))
    info_writer.writerows(zipped)
