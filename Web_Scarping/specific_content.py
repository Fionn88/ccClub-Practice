"""
使用 BeautifulSoup 去取得功課有公告的日期
"""
import requests
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20211010120951/https://www.ccclub.io/course/2019Spring'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
re = requests.get(url, headers=header)
soup = BeautifulSoup(re.text,"html.parser")
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