"""
Data will be extracted from the mens hair conditioner category.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from lxml import etree as ET

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    "Accept-Encoding": "gzip, deflate, br", "Accept": "*/*", "Connection": "keep-alive"
}

listing_pages = []


def get_listing_pages():

    for i in range(1, 30):
        start_url = "https://www.nykaa.com/mens/hair-care/conditioner/c/1294?page_no=" + str(i) + "&sort=popularity&eq=desktop"
        url = start_url.format(i)

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            dom = ET.HTML(str(soup))
            sub_title_list = dom.xpath('//div[@class="title"]/text()')

            if len(sub_title_list) == 0:
                listing_pages.append(url)
                print(url)
                time.sleep(3)
            else:
                break


get_listing_pages()
print(listing_pages)
