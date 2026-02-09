
# list=["Siyah","Beyaz","Sarı","Mavi","Yeşil"]
# print(list[1:4])
#
# küme={"Siyah","Beyaz","Sarı","Mavi","Yeşil","Kırmızı"}
# küme.add("Pembe")
# küme.remove("Siyah")
# print(küme)
#
#
# print("-----------------------------------------------------")
#
# a=6
# b=input("Sayı gir:")
#
# if a==b:
#     print("Aynı sayı")
# else:
#     print("Eşit değiller")
#     liste=[1,2,3,4,5,6]
#     if b in liste:
#         print("Var")
#     else:
#         print("Yok")
#
# print("-----------------------------------------------------")
#
#
# liste2=[1,2,3,4,5,6,7]
# for rakam in liste2:
#     print(rakam)
#
# print("-----------------------------------------------------")
#
# isim="AliEfe"
# for harf in isim:
#     print(harf)
#
# print("-----------------------------------------------------")
#
# x=2
# while x<=10:
#     print(x)
#     x=x+1
#
# import math
#
# def logarithm(a,b):
#     print(math.log(a,b))
#
# logarithm(8,2)
# logarithm(1000000000,5)



#
# def fact(number):
#     total = 1
#     for i in range(1, number + 1):
#         total *= i
#     print(total)
#
# fact(5)



# vize=input("Vize notunu giriniz: ")
# final=input("Final notunu giriniz: ")
#
# ort= int(vize)*0.4 + int(final)*0.6
#
# print("Ortalama: ", ort)




# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)




#Problem1
# number1=int(input("1. sayıyı giriniz:"))
# number2=int(input("2. sayıyı giriniz:"))
# number3=int(input("3. sayıyı giriniz:"))
#
# multip=number3*number2*number1
#
# print("Çarpımları: {}".format(multip))


#Problem2
# boy=int(input("Boyunuzu giriniz: "))
# kilo=int(input("Kilonuzu giriniz: "))
#
# BKI=kilo/(boy**2)
# print(BKI)




#Problem3
# kmyakılan=int(input("Km de ne kadar yakıyor: "))
# kaçkm=int(input("Kaç km yol gidiyor: "))
#
# total=kmyakılan*kaçkm
# print("Ödemeniz gereken tutar: {}".format(total))



#Problem4
# name=input("Adınız: ")
# surname=input("Soyadınız: ")
# number=input("Numaranız: ")
#
# print(name+"\n"+surname+"\n"+number)




#Problem5

# number1=int(input("1. sayıyı giriniz: "))
# number2=int(input("2. sayıyı giriniz: "))
#
# number1,number2=number2,number1
# print("1.sayı: {}, 2.sayı {}".format(number1,number2))




# #Problem6
# a=int(input("1.kenarı giriniz: "))
# b=int(input("2.kenarı giriniz: "))
#
# c=((a**2)+(b**2))**0.5
# print("Hipotenüs uzunluğu: ", c)


class Customer:
    def __init__(self,name):
        self.name=name

class RegularCustomer(Customer):
    def __init__(self,name,tips):
        super().__init__(name)
        self.tips=tips

    def average(self):
        if self.tips==[] :
            print("No Tips")
            return 0

        else:
            ave=sum(self.tips)/ len(self.tips)
            return ave


c1 = RegularCustomer("Ali", [20, 30, 25])
c2 = RegularCustomer("Ayşe", [])
print("Ali average tip:", c1.average())
print("Ayşe average tip:", c2.average())