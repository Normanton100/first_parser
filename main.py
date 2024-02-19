import requests
from bs4 import BeautifulSoup
import csv
from model import Product
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

def parser(url:str):
    create_csv()
    list_product = []
    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    products = soup.find_all("div", class_="info pt-3")
    for product in products:
        name = product.find("a").text
        print(name)
        list_product.append(Product(name=name))
    write_csv(list_product)


def create_csv():
    with open(f"glavsnab.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "name",
        ])

def write_csv(products: list[Product]):
    with open(f"glavsnab.csv", mode="a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([
                product.name
            ])

if __name__ == "__main__":
    parser(url="https://luxury-yacht-brokerage.com/yacht/yacht-charter.html?q=yacht%2Fyacht-charter.html&page=1")

