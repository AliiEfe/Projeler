def asalMi(number):
    if(number==1):
        return False
    elif(number==2):
        return True
    else:
        for i in range(2,number):
            if(number%i==0):
                return False
        return True
while True:
    number=input("Sayı giriniz: ")
    if(number=="q"):
        break
    else:
        number=int(number)
        if(asalMi(number)):
            print(number, "asal bir sayıdır.")
        else:
            print(number, "asal bir sayı değildir.")

