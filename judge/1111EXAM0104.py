"""
小仔打羽球

描述
小仔最近在練習打羽球雙打，但他實在搞不懂站位和發球，所以寫個程式幫他判斷接下來該由誰發球吧～

如下圖示，有四位玩家 a, b, c, d，a, b 為一組 ，c, d 為一組，比分從 0:0 開始，
羽球雙打的發球規則為，
1. 若發球那方的分數為偶數，則由面對網的右邊玩家發球，
反之，比分為奇數，則由面對網的左邊玩家發球。

2. 若某位玩家發球得分，則下一球也會由同一位發球，但因為分數奇偶數變化
所以那隊的站位會交換。舉例來說，站位如下圖，現在 ab 隊是 2 分，由站右邊的 a 發球後得分，
下一球也由 a 發球，但 ab 隊是 3 分，應該由左方發球，所以 a b 的站位會交換。

3.若某位玩家發球由對方得分，則下一球由另一隊依照分數奇偶對應站位的玩家發球

=====
圖片至 judge 查看
=====

題目的基礎站位固定如圖示，比分皆由 0:0 開始。
題目輸入會有兩行，
第一行會提供是由哪隊先發球，字串 ab 或字串 cd，
第二行會提供一段以 0 1 組成的字串，代表比賽每一球的得分情況，
0 表示由 ab 隊得分，1 表示由 cd 隊得分
請輸出由那一串得分情況後，下一球應該由哪位玩家發球

輸入
共兩行，
第一行會提供是由哪隊先發球，字串 ab 或字串 cd，
第二行會提供一段以 0 1 組成的字串，代表比賽每一球的得分情況，
0 表示由 ab 隊得分，1 表示由 cd 隊得分

輸出
共一行，
包含一字串，為下一球應該由哪位玩家發球

輸入範例 1 
ab
100

輸出範例 1
b

輸入範例 2 
cd
1000010101

輸出範例 2
c
"""

team = input()
score = input()
abTeamScore,cdTeamScore = 0,0
abPosition,cdPosition = 0,0 # 0ab 1ba 0cd 1dc
start = 0 # 0ab 1dc
ans = ''
if team == 'ab':
  start = 0
else:
  start = 1

for s in score:
  # ab 得分
  if s == '0':
    # 連續得分交換位置
    if start == 0:
      abPosition ^= 1  
    # 非連續得分
    else:
      start ^= 1
    abTeamScore += 1
  # cd 得分
  else:
    # 連續得分交換位置
    if start == 1:
      cdPosition ^= 1  
    # 非連續得分
    else:
      start ^= 1
    cdTeamScore += 1

# ab 方發球
if start == 0:
  # 位置
  if abPosition == 0:
    ans = 'ab'
  else:
    ans = 'ba'
  # 偶為面對往右方
  if abTeamScore % 2 == 0:
    print(ans[0])
  else:
    print(ans[1])
# cd 方發球
else:
  if cdPosition == 0:
    ans = 'cd'
  else:
    ans = 'dc'
  if cdTeamScore % 2 == 0 :
    print(ans[1])
  else:
    print(ans[0])
    