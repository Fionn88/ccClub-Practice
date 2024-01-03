"""
秘密紙條

描述
強強是一個高中生，他的學校管理嚴格，進校門的時候就必須要將手機交給學校保管，直到放學才能領回。強強的同學之間很盛行上課傳紙條，上課的時候同學們都會把想要傳的訊息寫在紙上，摺成紙條之後寫上收件人就傳給隔壁同學。強強在班上有一個女朋友，他擔心傳給女朋友的訊息在傳遞的過程中被偷看，而且萬一被老師發現要大聲念出紙條的內容的時候就慘了。所以他跟女朋友約好，要用凱薩密碼來傳訊息：把要傳送的訊息的文字逐一轉換成 Unicode 碼，加上 219 之後再乘以 2。你能協助強強把想要傳的訊息加密嗎?

輸入
輸入為 n+1 行，前 n 行每行為一個句子，最後一行 end 代表終止輸入。

輸出
輸出為 n 行，每行為加密後的數字，數字間以空格分隔。

輸入範例 1 
紅豆生南國
春來發幾枝
願君多採擷
此物最相思
end

輸出範例 1
64448 72258 60404 43108 45004
52736 41154 61102 48818 53488
78438 43500 46058 51448 52132
55422 59016 53174 61350 49648

輸入範例 2 
And the sunlight clasps the earth
And the moonbeams kiss the sea
What are all these kissings worth
If thou kiss not me
end

輸出範例 2
568 658 638 502 670 646 640 502 668 672 658 654 648 644 646 670 502 636 654 632 668 662 668 502 670 646 640 502 640 632 666 670 646
568 658 638 502 670 646 640 502 656 660 660 658 634 640 632 656 668 502 652 648 668 668 502 670 646 640 502 668 640 632
612 646 632 670 502 632 666 640 502 632 654 654 502 670 646 640 668 640 502 652 648 668 668 648 658 644 668 502 676 660 666 670 646
584 642 502 670 646 660 672 502 652 648 668 668 502 658 660 670 502 656 640

提示
使用 ord() 即可轉換成 Unicode
Unicode 的一般介紹可參考這裡
凱薩密碼的介紹可參考這裡
"""

while True:
    s = input()
    if s == "end":
        break
    else:
        nums=[str((ord(i)+219)*2) for i in s]
        print(" ".join(nums))
