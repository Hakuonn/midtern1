n=int(input("輸入n值:"))
name=[]
email=[]
for i in range(n):
    name.append(input("請輸入姓名"))
    email.append(input("請輸入電子郵件"))

email_dict={}

for i in range(n):
    email_dict[name[i]]=email[i]

check=input("請輸入要查詢電子郵件的姓名:")

print(check,'的電子郵件帳號為',email_dict[check])