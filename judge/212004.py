num = int(input())
ans = []
prev_row = []
for n in range(num):
    curr_row = [1]  # 每一行的開頭都是1
    if prev_row:  # 如果前一行存在
        for i in range(len(prev_row) - 1):
            curr_row.append(prev_row[i] + prev_row[i + 1])  # 根據前一行生成當前行
        curr_row.append(1)  # 每一行的结尾也是1
    ans.append(curr_row)
    
    prev_row = curr_row  # 更新前一行
print(ans)
