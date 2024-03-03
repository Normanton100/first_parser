import requests
from bs4 import BeautifulSoup
import csv
from model import Product
from fake_useragent import UserAgent
headers = UserAgent()

def parser(url:str, max_item: int):
    create_csv()
    page = 1
    count_items = 0
    while max_item > count_items:
        list_product = []
        res = requests.get(f"{url}?q=yacht-charter.html&page={page}", headers={'user-agent':f'{headers.random}'})
        soup = BeautifulSoup(res.text,"lxml")
        products = soup.find_all("div", class_="info pt-3")

        for product in products:
            if count_items >= max_item:
                break
            count_items += 1
            name = product.find("a").get("href")

            print(name)
            res_page = requests.get(f"https://luxury-yacht-brokerage.com{name}", headers={'user-agent':f'{headers.random}'})
            #print(res_page)
            soup_page = BeautifulSoup(res_page.text, "lxml")
            title = soup_page.find(class_="is-visible").text[3:]
            price = soup_page.find("span", class_="counter").text
            description = soup_page.find("div", class_="contact-info col py-5 mt-lg-0 mt-md-10 flex-column mt-8").find_all(["p", "h4", "ul"])
            tags_1 = soup_page.find("div", class_="row mb-n6 icon-box-shape-animation flex-wrap justify-content-center")
            tags = ""
            for i in tags_1.find_all("img"):
                tags += f"{i.get('title')},"
            tags = tags[:-1]
            # #gallery = soup_page.
            atribut_box = soup_page.find("div", class_="row row-cols-lg-4 row-cols-md-4 row-cols-2 mb-n6 icon-box-shape-animation")
            advantage = 1
            # advantageName_ =
            # advantageValue_
            # for i in atribut_box.find_all("div", class_="content"):
            #     advantageName_ = f'{advantageName_.find("span", class_="sub-title").text}'
            #     advantageValue_ = i.find("h3", class_="title counter").text
            #     advantage += 1
            while advantage >= 9:




            # advantageName_1 = soup_page.
            # advantageValue_1 = soup_page.
            # advantageName_2 = soup_page.
            # advantageValue_2 = soup_page.
            # advantageName_3 = soup_page.
            # advantageValue_3 = soup_page.
            # advantageName_4 = soup_page.
            # advantageValue_4 = soup_page.
            # advantageName_5 = soup_page.
            # advantageValue_5 = soup_page.
            # advantageName_6 = soup_page.
            # advantageValue_6 = soup_page.
            # advantageName_7 = soup_page.
            # advantageValue_7 = soup_page.
            # advantageName_8 = soup_page.
            # advantageValue_8 = soup_page.
            # advantageName_9 = soup_page.
            # advantageValue_9 = soup_page.

            list_product.append(Product(title=title,
                                        price=price,
                                        description=description,
                                        tags=tags,
                                        # #gallery=gallery,
                                        advantageName_1=advantageName_1,
                                        advantageValue_1=advantageValue_1
                                        # advantageName_2=advantageName_2,
                                        # advantageValue_2=advantageValue_2,
                                        # advantageName_3=advantageName_3,
                                        # advantageValue_3=advantageValue_3,
                                        # advantageName_4=advantageName_4,
                                        # advantageValue_4=advantageValue_4,
                                        # advantageName_5=advantageName_5,
                                        # advantageValue_5=advantageValue_5,
                                        # advantageName_6=advantageName_6,
                                        # advantageValue_6=advantageValue_6,
                                        # advantageName_7=advantageName_7,
                                        # advantageValue_7=advantageValue_7,
                                        # advantageName_8=advantageName_8,
                                        # advantageValue_8=advantageValue_8,
                                        # advantageName_9=advantageName_9,
                                        # advantageValue_9=advantageValue_9
                                        ))
            print(title)
            print(price)
            print(description)
            print(tags)
        write_csv(list_product)

        page += 1



def create_csv():
    with open(f"glavsnab.csv", mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow([
            "title",
            "price",
            "description",
            "tags",
            # #"gallery",
            "advantageName_1",
            "advantageValue_1"
            # "advantageName_2",
            # "advantageValue_2",
            # "advantageName_3",
            # "advantageValue_3",
            # "advantageName_4",
            # "advantageValue_4",
            # "advantageName_5",
            # "advantageValue_5",
            # "advantageName_6",
            # "advantageValue_6",
            # "advantageName_7",
            # "advantageValue_7",
            # "advantageName_8",
            # "advantageValue_8",
            # "advantageName_9",
            # "advantageValue_9"
            ])

def write_csv(soup_page: list[Product]):
    with open(f"glavsnab.csv", mode="a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        for product in soup_page:
            writer.writerow([
                product.title,
                product.price,
                product.description,
                product.tags,
                # #product.gallery,
                product.advantageName_1,
                product.advantageValue_1
                # product.advantageName_2,
                # product.advantageValue_2,
                # product.advantageName_3,
                # product.advantageValue_3,
                # product.advantageName_4,
                # product.advantageValue_4,
                # product.advantageName_5,
                # product.advantageValue_5,
                # product.advantageName_6,
                # product.advantageValue_6,
                # product.advantageName_7,
                # product.advantageValue_7,
                # product.advantageName_8,
                # product.advantageValue_8,
                # product.advantageName_9,
                # product.advantageValue_9
            ])

if __name__ == "__main__":
    parser(url="https://luxury-yacht-brokerage.com/yacht-charter.html", max_item=1)

