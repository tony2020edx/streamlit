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

pdp_urls = []

url = "https://www.nykaa.com/mens/hair-care/conditioner/c/1294?page_no=15&sort=popularity&eq=desktop%22"

def get_pdp_urls():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        dom = ET.HTML(str(soup))
        pdp_url_list = dom.xpath('//a[@class="css-qlopj4"]/@href')
        print(pdp_url_list)





for j in pdp_urls:
    print(j)
    print("\n")






