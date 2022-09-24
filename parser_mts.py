import requests
from bs4 import BeautifulSoup
from db_helper import DBHelper

db_helper = DBHelper("restored_mobile", "Restored phone")


def parse_page_of_phones_to_list(r):
    soup = BeautifulSoup(r.text, "lxml")
    name_class = "linkTovar"
    return [{
        "name": getattr(el.find("a", class_=name_class), "text", None),
        "price": get_price(el)
    } for el in soup.find_all("div", class_="products__unit")]


def get_price(el):
    price_class = "products__unit__price__number products__unit__price__number--full"
    primary_price = getattr(el.find("span", class_=price_class), "text", None)
    price = primary_price.replace(" ", "").replace("\n", "") + " руб"
    return price


def get_restored_phone_catalog():
    restored_phone_catalog = []
    page = 1
    while True:
        url = f"https://shop.mts.by/restored/?page={page}&num=9"
        r = requests.get(url=url)
        r.encoding = "utf-8"
        page_mobile_phone_catalog = parse_page_of_phones_to_list(r)
        # Exit condition
        if page != 1 and restored_phone_catalog[0] == page_mobile_phone_catalog[0]:
            print("No pages more")
            break
        restored_phone_catalog.extend(page_mobile_phone_catalog)
        print("page: ", page)
        page += 1
    return restored_phone_catalog


def get_phones():
    return db_helper.read_data()


def start_parsing():
    try:
        catalog = get_restored_phone_catalog()
        db_helper.write_to_db(catalog)
    except BaseException:
        print("Something went wrong")



