mod, time = input("輸入月租費形式與通話時間:").split(',')
mod, time = int(mod), int(time)
if mod == 186:
    if time*0.09 <= 186:
        print("通話費為:", mod)
    elif 186 < time*0.09 <= 186*2:
        print("通話費為:", mod*0.9)
    elif 186*2 < time*0.09:
        print("通話費為:", mod*0.8)
if mod == 386:
    if time*0.08 <= 386:
        print("通話費為:%.0f" % (time*0.08))
    elif 386 < time*0.08 <= 386*2:
        print("通話費為:%.0f" % (time*0.08*0.8))
    elif 386*2 < time*0.08:
        print("通話費為:%.0f" % (time*0.08*0.7))
if mod == 586:
    if time*0.07 <= 186:
        print("通話費為:" % (time*0.07))
    elif 586 < time*0.07 <= 186*2:
        print("通話費為:%.0f" % (time*0.07*0.7))
    elif 586*2 < time*0.07:
        print("通話費為:%.0f" % (time*0.07*0.6))
if mod == 986:
    if time*0.06 <= 186:
        print("通話費為:%.0f" % (time*0.06))
    elif 986 < time*0.06 <= 986*2:
        print("通話費為:%.0f" % (time*0.06*0.6))
    elif 986*2 < time*0.06:
        print("通話費為:%.0f" % (time*0.06*0.5))
