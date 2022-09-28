import requests
from bs4 import BeautifulSoup
import sqlite3


def parse_page_of_phones_to_list(r):
    soup = BeautifulSoup(r.text, "lxml")
    return [{
        "name": getattr(el.find("span", itemprop="name"), "text", None),
        "price": get_price(el),
    } for el in soup.find_all("div", class_="ModelList__ModelBlockRow")]


def get_price(el):
    price = None
    for span in el.find("span", class_="PriceBlock__PriceValue").find_all("span"):
        if span.text.replace(" ", "").replace(",", "").isdigit():
            price = span.text
    return price


def write_to_bd(catalog):
    table_name = 'shop.by apple mobile'
    with sqlite3.connect("apple_mobile.bd") as con:
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


def get_phone_catalog():
    mobile_phone_catalog = []
    page = 1
    url = "https://shop.by/telefony_mobilnye/iphone_13/?page_id="
    while True:
        r = requests.get(url=url + str(page))
        r.encoding = "utf-8"
        page_mobile_phone_catalog = parse_page_of_phones_to_list(r)
        # Exit condition
        if not len(page_mobile_phone_catalog):
            print("No pages more")
            break
        mobile_phone_catalog.extend(page_mobile_phone_catalog)
        print("page: ", page)
        page += 1
    return mobile_phone_catalog


def start():
    try:
        catalog = get_phone_catalog()
        write_to_bd(catalog)
    except BaseException:
        print("Something went wrong")


start()
