from bs4 import BeautifulSoup
import requests
import csv

product = input("enter the product name:   ").split(" ") #product name
product = "+".join(product) #product+name  supported by URLs

Product_name = []
Product_price = []
Product_image_URL = []
Product_rating = []

URL = f"https://www.jumia.dz/catalog/?q={product}"

try:
    resp = requests.get(URL)
except:
    raise ValueError(f"Unable to access URL {requests.exceptions.RequestException}")
src = resp.content  # getting url content
soup = BeautifulSoup(src,"lxml")  # parsing the url content with the lxml parser

name = soup("h3")
price = soup("div",class_="prc")
image_URL = soup("img",class_="img")
rating = soup("div",class_="stars _s")

iter = len(name) # how many iteration to be done

for i in range(iter):
    Product_name.append(name[i].text)
    Product_price.append(price[i].text)
    Product_image_URL.append(image_URL[i]["data-src"])
    try:  # because the rating is not always available
        Product_rating.append(rating[i].text)
    except:
        Product_rating.append("Undefined")

with open("jumia.csv", "w", encoding='utf-8') as file:
    fieldnames = ['product_name', 'product_price', 'product_image', 'product_rating']
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    for name, price, img, rating in zip(Product_name, Product_price, Product_image_URL, Product_rating):
        writer.writerow([name, price, img, rating])
