import os
file,x=input("Dosya Adı: "),input("İstenen Uzantı: ").replace(".","")
os.rename(file,".".join(file.split(".")[:-1]) + u"\u202E"+ x[::-1] +"."+file.split(".")[-1:][0])
