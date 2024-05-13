"""
梅添良薪水數字大小寫轉換
老闆開發票時，很不擅長數字小寫轉大寫，請幫助他這個金魚腦

// input 輸入
changeCapital(35000)
changeCapital(9876543210)
changeCapital(-33)
changeCapital("安安")
changeCapital("033")
// output 輸出
"參萬伍仟元整"
"玖拾捌億柒仟陸佰伍拾肆萬參仟貳佰壹拾元整"
"格式錯誤"
"格式錯誤"
"參拾參元整"
"""

# Keep trying
unit =  ['零', '壹', '貳', '參', '肆', '伍', '陸', '柒', '捌', '玖', '拾', '念', '佰', '仟', '萬', '億', '兆', '京', '垓', '秭', '穰', '溝', '澗', '正', '載', '極', '恆河沙', '阿僧祇', '那由他', '不可思議', '無量大數']
def changeCapital(input_data):
    ans = []
    if type(input_data) == int:
        if input_data < 0:
            return "格式錯誤"
        data = reversed(str(input_data))
    elif type(input_data) == str:
        try:
            data = int(reversed(input_data))
        except:
            return "格式錯誤"
    for index,value in enumerate(data):
        # if index < 4:
        ans.append(unit[int(value)])
        
    return ''.join(ans)

print(changeCapital(35000))
print(changeCapital(9876543210))
print(changeCapital(-33))
print(changeCapital("安安"))
print(changeCapital("033"))
