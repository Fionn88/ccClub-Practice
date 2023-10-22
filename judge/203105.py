"""
小明寫論文
描述

小明要出國念 CS 碩士了，不會寫論文可不行，然而，英文不好的他有個困擾，就是不知道寫標題什麼時候該大小寫，以他的個性也懶得記，每次都要上網去查也好麻煩，重要的是，如果標題大小寫沒注意會被那些英文很好的人看一眼就在心底偷偷嘲笑，這是小明一想到就頭皮發麻的事！於是，就像凱文說的，身為一個工程師就該動手解決問題，小明決定寫一個程式來處理這件事，螢幕前的你也一起來試試看吧！規則如下：

書籍、期刊、報紙等作品的標題中每個字皆須首字母大寫，除了 to、冠詞a、an、the、少於五個字母的連接詞 from、for、of、and、in 不須大寫，除非這些字出現於標題句首或句尾。注意，如果名詞或動詞少於五個字母，首字母仍須大寫。

給定一行小寫英文句子輸入，請輸出標題版的句子。例如：

a diamond is forever >>> A Diamond Is Forever
under the dome an affair to remember >>> Under the Dome an Affair to Remember
an end to live for >>> An End to Live For

輸入
輸入為一行，為小寫英文句子。


輸出
輸出為一行，為處理後的標題版句子。


輸入範例 1 
a diamond is forever

輸出範例 1
A Diamond Is Forever

輸入範例 2 
under the dome an affair to remember

輸出範例 2
Under the Dome an Affair to Remember
"""
import string
s = input().split()
for index,value in enumerate(s):
    if index == 0 or index == len(s) - 1:
        print(string.capwords(value),end=' ')
    elif value == 'to' or value == 'a' or value == 'an' or value == 'the' or value == 'from' or value == 'for' or value=='of' or value=='and' or value=='in':
        print(value,end=' ')
    else:
        print(string.capwords(value),end=' ')
