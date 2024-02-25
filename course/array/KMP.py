
# O(m+n)
def kmp_search(string, patt):
    next = build_next(patt)

    i,j = 0,0 # 主串指針, 子串指針
    while i < len(string): 
        if string[i] == patt[j]: # 字符匹配，指針後移
            i += 1
            j += 1
        elif j > 0: # 字符不匹配，根據 next 跳過字串前的一些字符
            j = next[j - 1]
        else: # 字串第一個就不匹配
            i += 1

        if j == len(patt): # 匹配成功
            return i - j

def build_next(patt):
    next = [0] # 初始為 0
    prefix_len = 0 # 當前共同前後綴長度
    i = 1
    while i < len(patt):
        if patt[prefix_len] == patt[i]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:
            prefix_len = next[prefix_len - 1]
            if prefix_len == 0:
                next.append(0)
                i += 1
    return next

print(build_next("ABACABAB")) # [0, 0, 1, 0, 1, 2, 3, 2]
print(build_next("ABABC")) # [0, 0, 1, 2, 0]

# 這裡回傳匹配相符開頭的 index
print(kmp_search("ABABABCAA","ABABC")) # 2