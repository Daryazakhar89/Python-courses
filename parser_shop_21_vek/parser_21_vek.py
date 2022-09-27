import requests
from bs4 import BeautifulSoup
import re
import json
import csv
import asyncio


def parse_page_of_tv_to_list(request):
    status_class = "g-catalog-status"
    price_class = "g-item-data"
    name_class = "result__name"
    soup = BeautifulSoup(request.text, "lxml")
    return [{
        "availability": getattr(el.find("span", class_=status_class), "text", None),
        "name": getattr(el.find("span", class_=name_class), "text", None),
        "price": getattr(el.find("span", class_=price_class), "text", None),
    } for el in soup.find_all("dl") if el.find("div", class_="catalog-result__item_data")]


def write_to_json(catalog):
    result_json = []
    for position, element in enumerate(catalog):
        result_json.append({
            "id": position,
            "name": element["name"],
            "price": element["price"],
            "availability": element["availability"]
        })

    with open("res.json", "w", encoding="utf-8") as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)


def write_to_csv(catalog):
    with open('res.csv', 'w', encoding='UTF8', newline="") as f:
        writer = csv.writer(f, delimiter=',')
        data = [[position, element["name"], element["price"], element["availability"]]
                for position, element in enumerate(catalog)]
        writer.writerow(["id", "name", "price", "availability"])
        writer.writerows(data)


async def get_tv_catalog():
    tv_catalog = []
    page_number = 1
    url = "https://www.21vek.by/tv/page:"
    while True:
        await asyncio.sleep(0.5)
        r = requests.get(url=url + str(page_number))
        r.encoding = "utf-8"
        if re.search("/page:\d+/", r.request.url):
            tv_catalog.extend(parse_page_of_tv_to_list(r))
            print("page: ", page_number)
            page_number += 1
        else:
            print("No pages more")
            break
    return tv_catalog


async def start():
    try:
        catalog = await get_tv_catalog()
        write_to_json(catalog)
        write_to_csv(catalog)
    except BaseException:
        print("Something went wrong")

asyncio.run(start())
