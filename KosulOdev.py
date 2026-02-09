# print("""-------------------------------------------------
# Hesap Makinesi Programına Hoşgeldiniz
# İşlemler;
#
# 1. Toplama İşlemi
#
# 2. Çıkarma İşlemi
#
# 3. Çarpma İşlemi
#
# 4. Bölme İşlemi
# -----------------------------------------------------------
# """)
# number1 = int(input("Birinci Sayı:"))
# number2 = int(input("İkinci Sayı:"))
#
# işlem =  input("İşlem Numarasını Giriniz:")
#
#
# if(işlem=="1"):
#     print("{} ile {} toplamı {} dır.".format(number2,number1,number1+number2))
#
# elif(işlem=="2"):
#     print("{} ile {} 'nin farkı {} dır.".format(number1, number2, number1 - number2))
#
# elif(işlem=="3"):
#     print("{} ile {} 'nin çarpımı {} dır.".format(number2, number1, number1 * number2))
#
# elif(işlem=="4"):
#     print("{}'nın {}'e bölümü {} dır.".format(number1, number2, number1 / number2))
#
# else:
#     print("Lütfen geçerli bir işlem giriniz...")
#
#
# PROBLEM1
# boy = float(input("Boyunuzu Giriniz:"))
# kilo = int(input("Kilonuzu Giriniz:"))
#
# bki =  kilo / (boy ** 2)
#
# if (bki < 18.5):
#     print("Zayıf")
# elif (bki >= 18.5 and bki < 25):
#     print("Normal")
# elif (bki >= 25 and bki < 30):
#     print("Fazla Kilolu")
# else:
#     print("Obez")
#
#
#
# PROBLEM2
# a=int(input("1.sayıyı giriniz: "))
# b=int(input("2.sayıyı giriniz: "))
# c=int(input("3.sayıyı giriniz: "))
#
# if (a >= b and a >= c):
#     print("En büyük sayı:", a)
# elif (b >= a and b >= c):
#     print("En büyük sayı:", b)
# elif (c >= a and c >= b):
#     print("En büyük sayı:", c)
#
#
#
#
# PROBLEM3
# vize1 = int(input("Vize1:"))
# vize2 = int(input("Vize2:"))
# final = int(input("Final:"))
#
# genel_not =  vize1 * 3/10 + vize2 * 3/10 + final * 4/10
#
# if (genel_not >= 90):
#     print("AA")
# elif (genel_not >= 85):
#     print("BA")
# elif (genel_not >= 80):
#     print("BB")
# elif (genel_not >= 75):
#     print("CB")
# elif (genel_not >= 70):
#     print("CC")
# elif (genel_not >= 65):
#     print("DC")
# elif (genel_not >= 60):
#     print("DD")
# elif (genel_not >= 55):
#     print("FD")
# else:
#     print("FF")
#
#
#
#
# PROBLEM4
# şekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz?")
#
# if (şekil == "Dörtgen"):
#     print("Lütfen kenarları sırayla giriniz.")
#     a = int(input("Kenar-1:"))
#     b = int(input("Kenar-2:"))
#     c = int(input("Kenar-3:"))
#     d = int(input("Kenar-4:"))
#
#     if (a == b and a == c and a == d):
#         print("Kare")
#     elif (a == c and b == d):
#         print("Dikdörtgen")
#     else:
#         print("Dörtgen")
#
# elif (şekil == "Üçgen"):
#     a = int(input("Kenar-1:"))
#     b = int(input("Kenar-2:"))
#     c = int(input("Kenar-3:"))
#     if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
#         if (a == b and a == c):
#             print("Eşkenar Üçgen...")
#         elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
#             print("İkizkenar Üçgen....")
#         else:
#             print("Çeşitkenar Üçgen...")
#     else:
#         print("Üçgen belirtmiyor...")
#
# else:
#     print("Geçersiz Şekil...")
#

