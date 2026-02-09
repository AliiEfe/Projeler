print("********************\nATM sistemine hoşgeldiniz\n********************")

print("""
İşlemler:

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme

Programdan 'q' tuşu ile çıkabilirsiniz.

""")

bakiye  = 1000


while True:
    işlem=input("İşlem giriniz: ")

    if(işlem=="q"):
        print("Yine bekleriz...")
        break

    elif(işlem=="1"):
        print("Bakiyeniz {} tl'dir.".format(bakiye))

    elif(işlem=="2"):
        miktar=int(input("Yatırmak istediğiniz tutarı giriniz: "))
        bakiye += miktar

    elif(işlem=="3"):
        miktar2=int(input("Çekmek istediğiniz tutarı giriniz: "))
        if(bakiye<miktar2):
            print("Bu kadar para çekemezsiniz...")
            print("Bakiyeniz {} tl'dir.".format(bakiye))
            continue
        bakiye-=miktar2

    else:
        print("Lütfen geçerli bir işlem giriniz.")