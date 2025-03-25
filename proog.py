#print("This is program for modifying")
txt = input("please enter string to translate \n")
for x in txt :
    txt=txt.replace("k" or "K","a")
    txt=txt.replace("j" or "J","i")
    txt=txt.replace("p" or "P","o")
    txt=txt.replace("t" or "T","e")
    txt=txt.replace("f" or "F","u")

print(txt)   