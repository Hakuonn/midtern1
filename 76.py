while True:
    code_str=input("請輸入傳送密碼:")
    if len(code_str)<6:
        print("請重新輸入")
    else:
        code_list=[]
        code_new_list=[]
        for i in code_str:
            code_list.append(i)
        code_list=list(map(int,code_str))
        for i in range(len(code_list)):
            code_new_list.append(code_list[i]*4%7)
        code_new_list=list(map(str,code_new_list))
        code_new_str=''.join(code_new_list)
        print("解密後的密碼:%s" %(code_new_str))
        break