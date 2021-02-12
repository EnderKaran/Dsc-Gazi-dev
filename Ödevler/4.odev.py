sayi=[]
tek_sayi=[]
while True:
    say = int(input('Sayı : '))
    sayi.append(say)
    if(int(say)%2!=0):
        tek_sayi.append(say)
    soru=input("Devam etmek istiyorsanız E yaziniz, Çıkmak istiyorsanız H yaziniz. ")
    if soru=="e" or soru=="E":
        continue
    else:
        print("Girdiğiniz değerler= "+str(sayi))
        tek_sayi.sort()
        print("En büyük tek_sylr değer= "+str(tek_sayi[-1]))
        break






