import requests
from bs4 import BeautifulSoup
import sqlite3


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


def write_to_bd(catalog):
    table_name = 'Restored phone'
    with sqlite3.connect("restored_mobile.bd") as con:
        curs = con.cursor()
        curs.execute(f"""DROP TABLE IF EXISTS '{table_name}'""")
        curs.execute(f"""
        CREATE TABLE IF NOT EXISTS '{table_name}'(
            name  TEXT,
            price  TEXT
        )""")
        con.commit()

    for element in catalog:
        curs.execute(f"INSERT INTO '{table_name}' VALUES ('{element['name']}','{element['price']}')")
    con.commit()


def start():
    try:
        catalog = get_restored_phone_catalog()
        write_to_bd(catalog)
    except BaseException:
        print("Something went wrong")


start()
