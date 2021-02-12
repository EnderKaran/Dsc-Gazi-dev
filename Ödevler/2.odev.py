
def kontrol(email):
    adet = 0
    for i in email:
        if i == '@':
            adet = adet + 1

    if adet == 1:
        return True
    else:
        return False


email = input('Email Adresi: ')
if (kontrol(email) == True):
    print(email+'\nemail adresiniz doğru')
else:
    print(email+'\nemail adresiniz yanlış')