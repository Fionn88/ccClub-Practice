"""
博客來抓取頁數
"""

import requests
from bs4 import BeautifulSoup
# 連續送請求的情況
# 請求之間要停一下，停頓時間有隨機性比較不容易被抓到
from time import sleep
from random import random

urls = [
    'https://www.books.com.tw/products/0010923803?sloc=main',
    'https://www.books.com.tw/products/0010916863?sloc=main'
]

for url in urls:
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    for i in soup.find_all('div', {'class':'mod_b type02_m058 clearfix'})[0].find('ul').find_all('li'):
        if '頁' in i.text:
            pages = i.text.split('/')[1].strip().replace('頁', '')
            print(pages)
    #break # 停在第一筆測資
    sleep(1+random())