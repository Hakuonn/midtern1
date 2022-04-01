n = int(input("輸入筆數n:"))
translate={}
for i in range(4):
    english,chinese=input().split()
    translate[english]=chinese
word=input("輸入欲查詢的單字")
print(word,'中文意思為',translate[word])