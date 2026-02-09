#PROBLEM1
# number=int(input("Sayı giriniz: "))
# total=0
# i=1
# while(i<number):
#     if(number%i==0):
#         total=total+i
#     i=i+1
# if(total==number):
#     print("Mükemmel sayı")
# else:
#     print("Mükemmel sayı değil")



#PROBLEM2
# sayı = input("Sayı: ")
# basamakSayisi = len(sayı)
# toplam = 0
# for i in sayı:
#     i=int(i)
#     toplam=toplam+i**basamakSayisi
#
# if(toplam==int(sayı)):
#     print("Armstrong sayısı")
# else:
#     print("Armstrong sayısı değil")



#PROBLEM3
# for i in range(1, 11):
#     print("*************************************************")
#     for j in range(1, 11):
#         print("{} x {} = {}".format(i, j, i * j))



#PROBLEM4
# toplam = 0
# while True:
#     sayı = input("Sayı:")
#     if (sayı == "q"):
#         break
#     sayı = int(sayı)
#     toplam += sayı
# print("Girdiğiniz Sayıların Toplamı:", toplam)



#PROBLEM5
# for i in range(1, 101):
#     if (i % 3 != 0):
#         continue
#     print(i)



#PROBLEM6
# liste=[]
# for i in range(1,101):
#     if(i%2==0):
#         liste.append(i)
#     else:
#         continue
#
# print(liste)