"""
列印出PTT熱門列表，爬取在線人數1000人以上的看板，列出看板名稱和人數
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/hotboards.html'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
re = requests.get(url, headers=header)
soup = BeautifulSoup(re.text,"html.parser")
boards = soup.find_all("div", {"class":{"b-ent"}})
for board in boards:
  name = board.find("div", {"class":{"board-name"}}).text
  nuser = board.find("div", {"class":{"board-nuser"}}).text
  if int(nuser) >= 1000:
    print(name,nuser)