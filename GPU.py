from bs4 import BeautifulSoup
import requests
import csv
item_prices = {}
names_list = []
prices_list = []
gpu = input("enter the gpu model:   ")
resp = requests.get(f"https://www.newegg.com/p/pl?SrchInDesc={gpu}&N=100007709")
src = resp.content
soup = BeautifulSoup(src,"lxml")
pages = int(str(soup.find(class_="list-tool-pagination").strong).split("/")[1].split(">")[1][:-1])
for page in range(pages):
    resp = requests.get(f"https://www.newegg.com/p/pl?N=100007709&SrchInDesc=3080&page={page+1}").text
    soup = BeautifulSoup(resp,"lxml")
    div = soup.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    names = div.find_all("a",class_="item-title")
    prices = div.find_all("li",class_="price-current")
    for name,price in zip(names,prices):
        try:
            item_prices[name.text] = f"${price.strong.text}"
        except:
            item_prices[name.text] = "$0000"
with open("GPU.csv", "w") as file:
    fieldnames = ["name", "price"]
    csv_file = csv.DictWriter(file, fieldnames=fieldnames)
    csv_file.writeheader()
    for name, price in item_prices.items():
        row = {"name": name, "price": price}
        csv_file.writerow(row)



