a = input("甲方的數字:")
b = input("乙方的數字:")
result = ''
for i in range(len(a)):
    if a[i] == '1' and b[i] == '5':
        result += '贏'
    elif a[i] == '2' and b[i] == '1':
        result += '贏'
    elif a[i] == '3' and b[i] == '2':
        result += '贏'
    elif a[i] == '4' and b[i] == '3':
        result += '贏'
    elif a[i] == '5' and b[i] == '4':
        result += '贏'
    elif a[i] == '1' and b[i] == '2':
        result += '輸'
    elif a[i] == '2' and b[i] == '3':
        result += '輸'
    elif a[i] == '3' and b[i] == '4':
        result += '輸'
    elif a[i] == '4' and b[i] == '5':
        result += '輸'
    elif a[i] == '5' and b[i] == '1':
        result += '輸'
    else:
        result += '和'

print(result)
