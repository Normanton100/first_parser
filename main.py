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

            advantageName_1 = atribut_box.find_all("span", class_="sub-title")[0].text
            advantageValue_1 = atribut_box.find_all("h3", class_="title counter")[0].text
            advantageName_2 = atribut_box.find_all("span", class_="sub-title")[1].text
            advantageValue_2 = atribut_box.find_all("h3", class_="title counter")[1].text
            advantageName_3 = atribut_box.find_all("span", class_="sub-title")[2].text
            advantageValue_3 = atribut_box.find_all("h3", class_="title counter")[2].text
            advantageName_4 = atribut_box.find_all("span", class_="sub-title")[3].text
            advantageValue_4 = atribut_box.find_all("h3", class_="title counter")[3].text
            advantageName_5 = atribut_box.find_all("span", class_="sub-title")[4].text
            advantageValue_5 = atribut_box.find_all("h3", class_="title counter")[4].text
            advantageName_6 = atribut_box.find_all("span", class_="sub-title")[5].text
            advantageValue_6 = atribut_box.find_all("h3", class_="title counter")[5].text
            advantageName_7 = atribut_box.find_all("span", class_="sub-title")[6].text
            advantageValue_7 = atribut_box.find_all("h3", class_="title counter")[6].text
            try:
                advantageName_8 = atribut_box.find_all("span", class_="sub-title")[7].text
            except IndexError:
                advantageName_8 = ""
            try:
                advantageValue_8 = atribut_box.find_all("h3", class_="title counter")[7].text
            except IndexError:
                advantageValue_8 = ""
            try:
                advantageName_9 = atribut_box.find_all("span", class_="sub-title")[8].text
            except IndexError:
                advantageName_9 = ""
            try:
                advantageValue_9 = atribut_box.find_all("h3", class_="title counter")[8].text
            except IndexError:
                advantageValue_9 = ""
            # if atribut_box.find_all("span", class_="sub-title")[7].text == True:
            #     advantageName_8 = atribut_box.find_all("span", class_="sub-title")[7].text
            # else: advantageName_8 = ""
            # if atribut_box.find_all("h3", class_="title counter")[7].text == True:
            #     advantageValue_8 = atribut_box.find_all("h3", class_="title counter")[7].text
            # else: advantageValue_8 = ""
            # advName_9 = atribut_box.find_all("span", class_="sub-title")[8].text
            # if advName_9:
            #     advantageName_9 = advName_9
            # else: advantageName_9 = ""
            # advValue_9 = atribut_box.find_all("h3", class_="title counter")[8].text
            # if advValue_9:
            #     advantageValue_9 = advValue_9
            # else: advantageValue_9 = ""

            list_product.append(Product(title=title,
                                        price=price,
                                        description=description,
                                        tags=tags,
                                        # #gallery=gallery,
                                        advantageName_1=advantageName_1,
                                        advantageValue_1=advantageValue_1,
                                        advantageName_2=advantageName_2,
                                        advantageValue_2=advantageValue_2,
                                        advantageName_3=advantageName_3,
                                        advantageValue_3=advantageValue_3,
                                        advantageName_4=advantageName_4,
                                        advantageValue_4=advantageValue_4,
                                        advantageName_5=advantageName_5,
                                        advantageValue_5=advantageValue_5,
                                        advantageName_6=advantageName_6,
                                        advantageValue_6=advantageValue_6,
                                        advantageName_7=advantageName_7,
                                        advantageValue_7=advantageValue_7,
                                        advantageName_8=advantageName_8,
                                        advantageValue_8=advantageValue_8,
                                        advantageName_9=advantageName_9,
                                        advantageValue_9=advantageValue_9
                                        ))
            print(title)
            print(price)
            print(description)
            print(tags)
            print(advantageName_1)
            print(advantageValue_1)
            print(advantageName_2)
            print(advantageValue_2)
            print(advantageName_3)
            print(advantageValue_3)
            print(advantageName_4)
            print(advantageValue_4)
            print(advantageName_5)
            print(advantageValue_5)
            print(advantageName_6)
            print(advantageValue_6)
            print(advantageName_7)
            print(advantageValue_7)
            print(advantageName_8)
            print(advantageValue_8)
            print(advantageName_9)
            print(advantageValue_9)
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
            "advantageValue_1",
            "advantageName_2",
            "advantageValue_2",
            "advantageName_3",
            "advantageValue_3",
            "advantageName_4",
            "advantageValue_4",
            "advantageName_5",
            "advantageValue_5",
            "advantageName_6",
            "advantageValue_6",
            "advantageName_7",
            "advantageValue_7",
            "advantageName_8",
            "advantageValue_8",
            "advantageName_9",
            "advantageValue_9"
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
                product.advantageValue_1,
                product.advantageName_2,
                product.advantageValue_2,
                product.advantageName_3,
                product.advantageValue_3,
                product.advantageName_4,
                product.advantageValue_4,
                product.advantageName_5,
                product.advantageValue_5,
                product.advantageName_6,
                product.advantageValue_6,
                product.advantageName_7,
                product.advantageValue_7,
                product.advantageName_8,
                product.advantageValue_8,
                product.advantageName_9,
                product.advantageValue_9
            ])

if __name__ == "__main__":
    parser(url="https://luxury-yacht-brokerage.com/yacht-charter.html", max_item=3)

