import requests
from bs4 import BeautifulSoup
import csv
from model import Product
from fake_useragent import UserAgent
headers = UserAgent()
def parser(url:str, max_item: int):
    #create_csv()
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
            soup_page = BeautifulSoup(res_page.text, "lxml")
            title = soup_page.find(class_="is-visible").text[3:]
            price = soup_page.find("span", class_="counter").text
            description = soup_page.find("div", class_="contact-info col py-5 mt-lg-0 mt-md-10 flex-column mt-8").find_all(["p", "h4", "ul"])
            tags_1 = soup_page.find("div", class_="row mb-n6 icon-box-shape-animation flex-wrap justify-content-center")
            tags = ""
            for i in tags_1.find_all("img"):
                tags += f"{i.get('title')},"
            tags = tags[:-1]


            page_gallery = soup_page.find("div", class_="container-fluid pl-xl-16 pl-lg-3 pl-md-3 pl-sm-3 pl-3 pr-xl-16 pr-lg-3 pr-md-3 pr-sm-3 pr-3").find_all("div", class_="swiper-slide text-center")
            for link in page_gallery:
                url_gallery = link.a.get("href")

                img = requests.get(f"https://luxury-yacht-brokerage.com/{url_gallery}", headers={'user-agent':f'{headers.random}'})


                #img.raise_for_status()
                try:
                    img.raise_for_status()
                    print(url_gallery)
                    name_gallery = url_gallery.split("/")[-1]
                    with open(f'img/{title}/{name_gallery}', 'wb') as file_gallery:
                        file_gallery.write(img.content)
                except requests.exceptions.HTTPError:
                    continue

            #gallery =

            atribut_box = soup_page.find("div", class_="row row-cols-lg-4 row-cols-md-4 row-cols-2 mb-n6 icon-box-shape-animation").find_all("div", class_="icon-box box-border text-center")
            advantageName_1 = atribut_box[0].find("span", class_="sub-title").text
            advantageValue_1 = atribut_box[0].find("h3", class_="title counter").text
            advantageName_2 = atribut_box[1].find("span", class_="sub-title").text
            advantageValue_2 = atribut_box[1].find("h3", class_="title counter").text
            advantageName_3 = atribut_box[2].find("span", class_="sub-title").text
            advantageValue_3 = atribut_box[2].find("h3", class_="title counter").text
            advantageName_4 = atribut_box[3].find("span", class_="sub-title").text
            if atribut_box[3].find("h3", class_="title counter"):
                advantageValue_4 = atribut_box[3].find("h3", class_="title counter").text
            else: advantageValue_4 = atribut_box[3].find("h3", class_="title").text
            advantageName_5 = atribut_box[4].find("span", class_="sub-title").text
            if atribut_box[4].find("h3", class_="title counter"):
                advantageValue_5 = atribut_box[4].find("h3", class_="title counter").text
            else: advantageValue_5 = atribut_box[4].find("h3", class_="title").text
            advantageName_6 = atribut_box[5].find("span", class_="sub-title").text
            if atribut_box[5].find("h3", class_="title counter"):
                advantageValue_6 = atribut_box[5].find("h3", class_="title counter").text
            else: advantageValue_6 = atribut_box[5].find("h3", class_="title").text
            try:
                advantageName_7 = atribut_box[6].find("span", class_="sub-title").text
            except IndexError:
                advantageName_7 = ""
            try:
                advantageValue_7 = atribut_box[6].find("h3", class_="title counter").text
            except IndexError:
                advantageValue_7 = ""
            try:
                advantageName_8 = atribut_box[7].find("span", class_="sub-title").text
            except IndexError:
                advantageName_8 = ""
            try:
                advantageValue_8 = atribut_box[7].find("h3", class_="title counter").text
            except IndexError:
                advantageValue_8 = ""
            try:
                advantageName_9 = atribut_box[8].find("span", class_="sub-title").text
            except IndexError:
                advantageName_9 = ""
            try:
                advantageValue_9 = atribut_box[8].find("h3", class_="title counter").text
            except IndexError:
                advantageValue_9 = ""

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

        #write_csv(list_product)

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
    parser(url="https://luxury-yacht-brokerage.com/yacht-charter.html", max_item=1)

