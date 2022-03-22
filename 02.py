ec = int(input("輸入一個度數(正整數)"))
if ec <= 120:
    print("Summer months:%.2f" % (ec*2.10))
    print("Non-Summer months:%.2f" % (ec*2.10))
elif 120<ec<=330:
    print("Summer months:%.2f" % ((ec-120)*3.02+120*2.10))
    print("Summer months:%.2f" % ((ec-120)*2.68+120*2.10))
elif 330<ec<=500:
    print("Summer months:%.2f" %((ec-330)*4.39+(330-120)*3.02+120*2.10))
    print("Summer months:%.2f" %((ec-330)*3.61+(330-120)*2.68+120*2.10))
elif 500<ec<=700:
    print("Summer months%.2f" %((ec-500)*4.97+(500-330)*4.39+(330-120)*3.02+120*2.10))
    print("Summer months%.2f" %((ec-500)*4.01+(500-330)*3.61+(330-120)*2.68+120*2.10))
elif ec>700:
    print("Summer months%.2f" %((ec-700)*5.63+(700-500)*4.97+(500-330)*4.39+(330-120)*3.02+120*2.10))
    print("Summer months%.2f" %((ec-700)*4.50+(700-500)*4.01+(500-330)*3.61+(330-120)*2.68+120*2.10))