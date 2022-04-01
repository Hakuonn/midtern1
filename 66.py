string_a=input("請輸入string_a:")
string_b=input("請輸入string_b:")
same=[]
new_same=[]
for i in string_a:
    for j in string_b:
        if i == j:
            same+=i
same.sort()
for i in same:
    if i not in new_same:
        new_same.append(i)
new_same_str=''.join(new_same)
print(new_same_str)