"""
停車費 II

描述
承停車費，台大除了社科院停車場之外，還有其他停車場如：水源、校總區等。
為了能夠設計一套停車費計費系統，讓每個停車場都可以使用。
請實作parking_fee函式，計算停車費，該函式具備以下參數：
fee_rate：型態為 int，代表該停車場每半小時的停車費率。以停車費為例，fee_rate 即為 20。
is_vip：型態為 bool，代表該車是否具備台大證件。具備台大證件可享 (1) 停車費半價優惠 (2) 若停車未滿 30 分鐘，則免收停車費。
entry_time：型態為 str，代表該車進入停車場的時間，格式為 hh:mm。ex：18:30 代表晚上 6 點半進入停車場。
exit_time：型態為 str，代表該車離開停車場的時間，格式為 hh:mm。ex：22:30 代表晚上 10 點半離開停車場。
為了方便計算，停車場暫不提供跨夜停車，即每輛車皆會在 23:59（含）前離開。
備註：若停車 0 分鐘，則停車費 0 元。


本題只需實作函式，並將停車費回傳，型態為 int，不需要自己處理輸入和輸出。
你可以直接複製 hint 中提供的程式碼，專心實作parking_fee函式，讓他符合題目的要求。

輸入
輸入有四行，分別為停車費率、是否具備台大證件、進場時間、離場時間。

輸出
輸出有一行，包含一個整數，代表該車的停車費。

輸入範例 1 
parking_fee(30, True, "22:40", "23:40")

輸出範例 1
30

輸入範例 2 
parking_fee(30, True, "07:01", "09:32")

輸出範例 2
90

提示
請直接複製以下內容，並實作函式，並將答案使用return回傳。

def parking_fee(fee_rate, is_vip, entry_time, exit_time):
    # do something to calculate parking fee

    return your_ans


來源
ccClub Judge
"""

def parking_fee(fee_rate, is_vip, entry_time, exit_time):
    # do something to calculate parking fee

    entry_h,entry_m = map(int,entry_time.split(':'))
    exit_h,exit_m = map(int,exit_time.split(':'))
    hour = exit_h - entry_h
    min = exit_m - entry_m

    if min < 0:
      hour -= 1
      min = 60 + min

    if min <= 30 and min > 0:
      min = 30
    elif min > 30:
      min = 60

    all_min = hour*60 + min
    price = 0
    if is_vip:
      if all_min <= 30:
        price = 0
      else:
        price = int(all_min / 30 * fee_rate/2)
    else:
      price = int(all_min / 30 * fee_rate)
    
    return price
