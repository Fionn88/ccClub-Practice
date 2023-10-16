"""
小胖想演講
描述

小胖從小就很容易緊張，因此上台演講的時候講話總是斷斷續續的

這天他想把自己演講的內容上字幕，發現字幕也是斷斷續續的，請問你能幫他把完整的一句話給串起來嗎？


輸入
輸入有若干行


輸出
輸出有一行，為一完整的字串


輸入範例 1 
你
好
嗎

輸出範例 1
你好嗎

輸入範例 2 
怎麼了
你累了
說好的
幸福呢

輸出範例 2
怎麼了你累了說好的幸福呢
"""
full_sentence = ""

while True:
    try:
        line = input()
        full_sentence += line
    except EOFError:
        break

print(full_sentence)
