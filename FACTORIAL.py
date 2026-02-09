print("""*******************
Faktoriyel Bulma Programı

Programdan çıkmak için 'q' ya basın.
*******************""")

while True:
    sayi=input("Sayı giriniz: ")
    if(sayi=="q"):
        print("Çıkışınız yapılıyor...")
        break
    sayii=int(sayi)

    fact=1
    for i in range(1,sayii+1):
        fact*=i

    print("Faktoriyel: ", fact)