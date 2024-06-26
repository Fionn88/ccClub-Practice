"""
阿姆斯壯數

描述
在 n 位的整數中，若加總每個數字的 n 次方後等於該整數，該整數稱為阿姆斯壯數（Armstrong number），又稱自戀數（Narcissistic number）。例如 153 可以滿足 1³ + 5³ + 3³ = 153，153 就是個阿姆斯壯數。
*本題不須處理輸入，僅須處理函數(不須上傳註解處程式碼)

輸入
函式有一個參數 num，型態為 int

輸出
函式有一個回傳值 ans，型態為 bool，代表是否為阿姆斯壯數

輸入範例 1
is_armstrong(20)

輸出範例 1
False

輸入範例 2
is_armstrong(115132219018763992565095597973971522401)

輸出範例 2
True
"""

def is_armstrong(num):
    #do something
    num = str(num)
    count = 0
    length = len(num)
    for i in num:
        count = count + int(i) ** length
    return (count == int(num))
