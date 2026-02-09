def tamBolenleriBulma(sayı):
    tambolen=[]
    for i in range(1,sayı):
        if (sayı%i==0):
            tambolen.append(i)
    return tambolen
while True:
    sayı=input("Sayı: ")
    if(sayı=="q"):
        print("Program sonlandırılıyor...")
        break
    else:
        sayı=int(sayı)
        print("Tam bölenler: ", tamBolenleriBulma(sayı))