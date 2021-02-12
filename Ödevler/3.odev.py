number=[]
sıfırla = []
nc=[ ]
while True:
    say=int(input("Lütfen bir sayı giriniz: "))
    number.append(say)
    for sy in number:
        if sy==0:
            sıfırla.append(sy)
            number.remove(0)
            nc=sıfırla+number
    soru=input("Devam etmek istiyorsanız E yaziniz, Çıkmak istiyorsanız H yaziniz. ")
    if soru=="e" or soru=="E":
        continue
    else:
        print(nc)
        break







