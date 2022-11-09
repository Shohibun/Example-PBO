class Lingkaran():
    PHI = 3.14
    def __init__(self, jari_jari):
        self.jari_jari = int(jari_jari)
            
    def KelilingLingkaran(self):
        keliling_lingkaran = 2 * self.PHI * self.jari_jari
        print("Hasil dari keliling lingkaran: ", keliling_lingkaran)

    def LuasLIngkaran(self):
        luas_lingkaran = self.PHI * self.jari_jari**2
        print("Hasil dari luas lingkaran: ", luas_lingkaran)

class Persegi():
    def __init__(self, sisi):
        self.sisi = int(sisi)

    def KelilingPersegi(self):
        keliling_persegi = 4 * self.sisi
        print("Hasil keliling persegi: ", keliling_persegi)

    def LuasPersegi(self): 
        luas_persegi = self.sisi**2
        print("Hasil luas persegi: ", luas_persegi)

class PersegiPanjang():
    def __init__(self, panjang, lebar):
        self.panjang = int(panjang)
        self.lebar = int(lebar)

    def KelilingPersegiPanjang(self):
        keliling_persegi_panjang = 2 * (self.panjang + self.lebar)
        print("Hasil keliling persegi panjang: ", keliling_persegi_panjang)

    def LuasPersegiPanjang(self):
        luas_persegi_panjang = self.panjang * self.lebar
        print("Hasil luas persegi panjang: ", luas_persegi_panjang)

def menu():
    print("Daftar menu program bangun datar")
    print("[1] Lingkaran")
    print("[2] Persegi")
    print("[3] Persegi panjang")
    print("[4} Exit")

    pilihan = input("Pilih program yang ingin anda jalankan: ")
    if pilihan.lower() == "1":
        BangunLingkaran()
    elif pilihan.lower() == "2":
        BangunPersegi()
    elif pilihan.lower() == "3":
        BangunPersegiPanjang()
    elif pilihan.lower() == "4":
        exit()
    else:
        print("Program tidak ada di menu")

def BackToMenu():
    menu()

def BangunLingkaran():
    print("[1] Keliling lingkaran")
    print("[2] Luas lingkaran")
    pilih = input("Pilih program yang ingin anda jalankan: ")

    input_jari_jari = input("Masukan jari-jari lingkaran: ")
    lingkaran = Lingkaran(input_jari_jari)
    
    if pilih.lower() == "1":
        lingkaran.KelilingLingkaran()

    elif pilih.lower() == "2":
        lingkaran.LuasLIngkaran()
    BackToMenu()

def BangunPersegi():
    print("[1] Keliling persegi")
    print("[2] Luas persegi")
    pilih = input("Pilih program yang ingin anda jalankan: ")

    input_sisi = input("Masukan sisi persegi: ")
    persegi = Persegi(input_sisi)

    if pilih.lower() == "1":
        persegi.KelilingPersegi()

    elif pilih.lower() == "2":
        persegi.LuasPersegi()
    BackToMenu()

def BangunPersegiPanjang():
    print("[1] Keliling persegi panjang")
    print("[2] Luas persegi panjang")
    pilih = input("Pilih program yang ingin anda jalankan: ")

    input_panjang = input("Masukan panjang persegi panjang: ")
    input_lebar = input("Masukan lebar persegi panjang: ")
    persegi_panjang = PersegiPanjang(input_panjang, input_lebar)

    if pilih.lower() == "1":
        persegi_panjang.KelilingPersegiPanjang()

    elif pilih.lower() == "2":
        persegi_panjang.LuasPersegiPanjang()
    BackToMenu()

def exit():
    exit

if __name__ == "__main__":
    menu()