import requests
from bs4 import BeautifulSoup
import csv
from model import Product
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

def parser(url:str, max_item: int):
    create_csv()
    page = 1
    count_items = 0
    while max_item > count_items:
        list_product = []
        res = requests.get(f"{url}?q=yacht-charter.html&page={page}", headers=headers)
        soup = BeautifulSoup(res.text,"lxml")
        products = soup.find_all("div", class_="info pt-3")

        for product in products:
            if count_items >= max_item:
                break
            count_items += 1
            name = product.find("a").text
            print(name)
            list_product.append(Product(name=name))
        write_csv(list_product)
        page += 1


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
    parser(url="https://luxury-yacht-brokerage.com/yacht-charter.html", max_item=40)

