#PROBLEM1
# def mukemmel(sayı):
#     toplam = 0
#     for i in range(1, sayı):
#         if (sayı % i == 0):
#             toplam += i
#     return toplam == sayı

# for i in range(1, 1001):
#     if (mukemmel(i)):
#         print("Mükemmel Sayı:", i)



#PROBLEM2
# def ebobBul(number1,number2):
#     i=2
#     total=1
#     if (number1<number2):
#         kucukSayı=number1
#     else:
#         kucukSayı=number2
#
#     while(i<=kucukSayı):
#         if((number1%i==0) and (number2%i==0)):
#             total=i
#         i+=1
#     print("{} ve {} sayılarının ebobu: {}".format(number1,number2,total))
# ebobBul(6,12)



#PROBLEM3
# birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
# onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
#
# def okunus(sayı):
#     birinci = sayı % 10
#     ikinci = sayı // 10
#
#     return onlar[ikinci] + " " + birler[birinci]
#
# sayı = int(input("Sayı:"))
#
# print(okunus(sayı))




#PROBLEM4
# def ekokBulma(sayı1, sayı2):
#     i = 2
#     ekok = 1
#     while True:
#         if (sayı1 % i == 0 and sayı2 % i == 0):
#             ekok *= i
#             sayı1 //= i
#             sayı2 //= i
#
#         elif (sayı1 % i == 0 and sayı2 % i != 0):
#             ekok *= i
#
#             sayı1 //= i
#
#         elif (sayı1 % i != 0 and sayı2 % i == 0):
#             ekok *= i
#             sayı2 //= i
#
#         else:
#             i += 1
#         if (sayı1 == 1 and sayı2 == 1):
#             break
#     return ekok
#
# sayı1 = int(input("Sayı 1:"))
# sayı2 = int(input("Sayı 2:"))
#
# print("Ekok:", ekokBulma(sayı1, sayı2))



#PROBLEM5
# def pisagor_bulma():
#     pisagor_listesi = list()
#     for i in range(1, 101):
#         for j in range(1, 101):
#
#             c = (i ** 2 + j ** 2) ** 0.5
#
#             if (c == int(c)):
#                 pisagor_listesi.append((i, j, int(c)))
#
#     return pisagor_listesi
# for i in pisagor_bulma():
#     print(i)