"""
使用 BeautifulSoup 去取得功課有公告的日期
"""
import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20211010120951/https://www.ccclub.io/course/2019Spring'
re = requests.get(url)
trs = soup.find_all("tr")
ccClub = []
for tr in trs:
  tds = tr.find_all("td")
  week = tds[0].text
  date = tds[1].text
  content = tds[2].text
  if 'announce' in content:
    ccClub.append(date)
print(ccClub)