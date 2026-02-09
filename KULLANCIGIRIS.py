print("**********\nKullanıcı Girişi\n**********\n")

sistemKulAdı="Ali"
sistemKulParol="12345"

hakk=3

while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")

    if (kullanıcı_adı != sistemKulAdı and parola == sistemKulParol):
        print("Kullanıcı Adı Hatalı...")
        hakk -= 1
        print("Giriş Hakkı: ", hakk)
    elif (kullanıcı_adı == sistemKulAdı and parola != sistemKulParol):
        print("Parola Hatalı...")
        hakk -= 1

        print("Giriş Hakkı: ", hakk)
    elif (kullanıcı_adı != sistemKulAdı and parola != sistemKulParol):
        print("Kullanıcı Adı ve Parola Hatalı...")
        hakk -= 1
        print("Giriş Hakkı: ", hakk)

    else:
        print("Başarıyla Giriş Yaptınız...")
        break
    if (hakk == 0):
        print("Giriş Hakkınız Bitti...")
        break