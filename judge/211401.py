"""
信箱地址檢查

描述
小明要開發一款 APP，這個 APP 以客戶的信箱作為帳號，所以 APP 需要在客戶輸入完電子郵件地址之後、送出申請資料之前，初步判斷地址是否符合電子郵件的規則。

電子郵件地址規則如下:
1.完整的電子郵件地址由帳號和域名組成，帳號和域名之間以「@」符號區隔(例如 abcd@gmail.com 這個地址，abcd是帳號，gmail.com是域名)
2.帳號可以使用數字、大小寫的英文字母和「.」、「+」、「_」、「-」符號
3.域名可以使用數字、大小寫的英文字母
4.域名可能有多個層級(例如abcd@gmail.com中，「.com」為頂級域；abcd@yahoo.com.tw中，「.com」為二級域，「.tw」為頂級域)
5.每級域名都由一個「.」符號開頭，且只能有一個「.」
6.帳號可以使用「.」、「+」、「_」、「-」符號，但不能連續使用，也不能放在開頭

請幫助小明檢查字串是否符合電子郵件規則

輸入
輸入為一行，為一個字串，每個待檢查的地址皆以「,」分隔

輸出
輸出為一行，為一個串列，每個元素皆為 True 或 False

輸入範例 1
l.kjd@gmail.com,gy+u86-1m@yahoo.com.tw,lkjd@hotmail.com,l..kjd@gmail.com,lkjd@@gmail.com

輸出範例 1
[True, True, True, False, False]

輸入範例 2
5641@yahoo.com.tw,.l.kjd@gmail.com,lkjdgmail.com,lkjd@gmail..com,lk\jd@gmail.com,lkjd@gmail.com.

輸出範例 2
[True, False, False, False, False, False]

提示
使用正規表達式會比較輕鬆
"""

import re

email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$')
def validate_email(email):
    if email_pattern.match(email):
        return True
    else:
        return False
    
def is_valid_username(username):
    if re.match("^[.+_-]", username):
        return True

    if re.search("[.+_-]{2,}", username):
        return True

    return False

listEmail = input().split(',')
answer = []
for email in listEmail:
    if len(email) == 0:
        answer.append(False)
    elif is_valid_username(email) or email[-1] == ".":
        answer.append(False)
    else:
        answer.append(validate_email(email))

print(answer)
