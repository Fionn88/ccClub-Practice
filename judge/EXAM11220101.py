"""
阿偉傳凱薩密碼

描述
阿偉想要密謀推翻政府，為此，他需要秘密招集夥伴，他上網看到了一種簡易的密碼方式，是將字母向後推移13碼，例如將A替換成N，B替換成O。你能破解阿偉要傳遞的訊息，將阿偉繩之依法嗎？

輸入
輸入為一串英文句子，有大小寫區分以及標點符號。

輸出
輸出仍為一串英文句，標點符號不變，但字母將被替換為解碼後的字母。

輸入範例 1
Uryyb jbeyq.

輸出範例 1
Hello world.

輸入範例 2
Gur dhvpx oebja sbk whzcf bire gur ynml qbt.

輸出範例 2
The quick brown fox jumps over the lazy dog.
"""

s = input()
def decode_sentence(sentence):
    decoded_sentence = ""
    for char in sentence:
        if char.isalpha():
            if char.islower():
                decoded_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            elif char.isupper():
                decoded_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            decoded_char = char
        decoded_sentence += decoded_char
    return decoded_sentence

print(decode_sentence(s))
