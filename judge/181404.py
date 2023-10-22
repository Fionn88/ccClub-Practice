"""
簡易終端機
描述

在 Linux 系統中，我們常使用一些指令來做事情，試著寫一個程式來模擬這件事。

我們的程式需要包含以下指令：

ls
列出當下位置中所有的資料夾
cd <資料夾名稱>
移動工作目錄
若資料夾存在，則將當下位置移至該資料夾下，若資料夾不存在，則不移動當下位置，並輸出對應的 error指令。
若 cd ..，則將當下位置往上移一層。若原本的位置為 「home/ccClub/kevin，執行完「cd ..」之後，當下位置會變成 「home/ccClub」。
pwd
印出當下位置
mkdir <資料夾名稱>
在當下位置中創立一個資料夾
rmdir <資料夾名稱>
將當下位置中的資料夾移除


輸入
輸入有數行。

第一行為一個 json 格式的字串，代表著電腦中的資料夾結構。

接下來數行每行都是一個 linux指令。


輸出
輸出有數行。

當遇到指令 ls 時，需要輸出當下位置中所有的資料夾/檔案名稱

當遇到指令 pwd 時，需要輸出當下位置。

當遇到指令 cd，且資料夾不存在時，需輸出錯誤訊息（請參考sample input 1）。

當遇到指令 rmdir，且資料夾不存在時，需輸出錯誤訊息（請參考sample input 3）。


輸入範例 1 
{"home": ["a"], "a": ["b", "c"], "b": [], "c": []}
ls
cd a
ls
cd b
ls
pwd
cd ..
mkdir d
rmdir b
ls
cd f
exit

輸出範例 1
a
b,c

home/a/b
c,d
cd f error

輸入範例 2 
{"home": ["a", "b", "c", "d", "e"], "a": [], "b": [], "c": [], "d": [], "e": []}
ls
cd ..
ls
exit

輸出範例 2
a,b,c,d,e
a,b,c,d,e

輸入範例 3 
{"home": ["a"], "a": []}
cd a
mkdir x
mkdir y
cd y
cd x
pwd
rmdir c
exit

輸出範例 3
cd x error
home/a/y
rmdir c error

來源
ccClub Judge
"""

s = eval(input())
locate = 'home'
path = 'home'
while True:
  user_input = input()
  if user_input == 'exit':
    break
  else:
    user_input = user_input.split()
    if user_input[0] == 'ls':
       print(','.join(s.get(locate,'')))
    elif user_input[0] == 'cd' and user_input[1] == '..':
      path = path.rsplit('/', 1)[0]
      locate = path.rsplit('/', 1)[-1]
    elif user_input[0] == 'cd' and user_input[1] not in s.get(locate,''):
      print(user_input[0],user_input[1],'error')
    elif user_input[0] == 'cd' and user_input[1] in s.get(locate,''):
      locate = user_input[1]
      path = path +'/'+user_input[1]
    elif user_input[0] == 'pwd':
      print(path)
    elif user_input[0] == 'mkdir':
      s[locate].append(user_input[1])
      s[user_input[1]] = []
    elif user_input[0] == 'rmdir' and user_input[1] in s.get(locate,''):
      s[locate].remove(user_input[1])
      del s[user_input[1]]
    elif user_input[0] == 'rmdir' and user_input[1] not in s.get(locate,''):
      print(user_input[0],user_input[1],'error')
