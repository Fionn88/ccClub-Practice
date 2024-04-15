"""
阿偉發行公司債

描述
阿偉開的公司遭遇嚴重的財務困難，因此決定發行公司債進行融資，並以複利計息。已知公司債現值為阿偉現在可拿到的錢，現值由四個因素決定，
分別是債券期限(t)、票面利率(c)、市場利率(i)、面額(F)：
公式如下
其中，每期的 C1, C2, .... Cn 均為定值，為每期收到之利息。計算方式是票面利率*面額 (Cn = C * F)
給定債券融資條件，試四捨五入至整數位計算債券現值，並將答案以整數形式輸出，即int(round(present_value,0))

輸入
給定：
[債券期限(t), 票面利率(c), 市場利率(i), 面額(F)]
其中 t 為整數，票面利率和市場利率為一百分比，面額為一正整數

輸出
回傳債券現值，為一正整數

輸入範例 1 
[5, 4%, 4%, 1000]

輸出範例 1
1000

輸入範例 2
[40, 3%, 4%, 10000]

輸出範例 2
8021

提示
請盡量按照題目公式計算，用等比級數公式可能會有浮點數誤差
"""

inputData = input().replace('[','')
inputData = inputData.replace(']','')
inputData = inputData.split(',')
cleanData = []
for data in inputData:
    data = data.strip()
    if '%' in data:
        data = data.split('%')
        data = float(data[0]) * 0.01
        cleanData.append(data)
    else:
        cleanData.append(float(data))

p = 0
for year in range(1,int(cleanData[0])):
    c = cleanData[1] * cleanData[3]
    p += c / (1 + cleanData[2]) ** year
# last year
p +=  (c + cleanData[3]) / (1 + cleanData[2]) ** cleanData[0] 
print(int(round(p,0)))
