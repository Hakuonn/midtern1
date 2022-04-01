english=input("請輸入一串小寫英文:")
mother=''
for i in english:
    if i == 'a' :
        english=english.replace(i,'.')
    elif i == 'e':
        english=english.replace(i,'.')
    elif i == 'i':
        english=english.replace(i,'.')
    elif i == 'o':
        english=english.replace(i,'.')
    elif i == 'u':
        english=english.replace(i,'.')
print(english)