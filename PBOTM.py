class MobilSedan():
    def __init__(self, nama_pemilik, mobil, merk):
        self.nama_pemilik = nama_pemilik
        self.mobil = mobil
        self.merk = merk

    def set_name(self, nama_pemilik_baru):
        self.nama_pemilik = nama_pemilik_baru

    def set_mobil(self, merk_baru):
        self.mo = mobil_baru

    def get_name(self):
        return self.nama_pemilik

    def get_mobil(self):
        return self.mobil

corola = MobilSedan("Afin", "Corola", "Toyota")
civic = MobilSedan("Shohibun", "Civic", "Honda")
city = MobilSedan("Rino", "City", "Honda")
mercedez = MobilSedan("Celvin", "Mercedez", "MercedezBenz")

print(civic.get_name())
civic.set_name("Lugas")
print(civic.get_name())
print(civic.get_mobil())
civic.set_mobil("Vios")
print(civic.get_mobil())
print("\n")


class Ikan():
    def __init__(self, nama, jenis, warna, harga):
        self.nama = nama
        self.jenis = jenis
        self.warna = warna
        self.harga = harga

    def get_nama(self):
        return self.nama

    def get_harga(self):
        return self.harga

    def set_nama(self, nama_baru):
        self.nama = nama_baru
    
    def set_harga(self, harga_terbaru):
        self.harga = harga_terbaru

koki = Ikan("Koki", "ikan mas", "orange", 20000)
arwana = Ikan("Arwanan", "ikan hias", "merah", 2000000)

print(koki.get_nama())
koki.set_nama("Jojo")
print(koki.get_nama())
print(arwana.get_harga())
arwana.set_harga(2500000)
print(arwana.get_harga())
print("\n")


class Burung():
    def __init__(self, nama_burung, jenis_burung, Ukuran_burung):
        self.nama_burung = nama_burung
        self.jenis_burung = jenis_burung
        self.Ukuran_burung = Ukuran_burung

    def get_nama_burung(self):
        return self.nama_burung

    def get_jenis_burung(self):
        return self.jenis_burung

    def set_nama_burung(self, nama_baru_burung):
        self.nama_burung = nama_baru_burung

    def set_jenis_burung(self, jenis_baru_burung):
        self.jenis_burung = jenis_baru_burung

elang = Burung("Elang", "Karnivora", "Gede")
pipit = Burung("Pipit", "Omnivora", "Kecil")

print("Nama burung ini adalah " + elang.get_nama_burung())
elang.set_nama_burung("Rajawali")
print("Dan sekarang nama burung ini menjadi " + elang.get_nama_burung())
print("Jenis burung ini adalah " + pipit.get_jenis_burung())
pipit.set_jenis_burung("Karnivora")
print("Tetapi burung ini juga bisa menjadi " + pipit.get_jenis_burung())
print("\n")


class Komputer():
    def __init__(self, merk_komputer, jenis_komputer, harga_komputer):
        self.merk_komputer = merk_komputer
        self.jenis_komputer = jenis_komputer
        self.harga_komputer = harga_komputer

    def get_merk_komputer(self):
        return self.merk_komputer

    def get_jenis_komputer(self):
        return self.jenis_komputer

    def set_jenis_komputer(self, jenis_baru_komputer):
        self.jenis_komputer = jenis_baru_komputer

ROG = Komputer("ROG", "Laptop", 25000000)
MSI = Komputer("MSI", "Laptop", 21000000)

print(ROG.get_merk_komputer() + " adalah sebuah merk laptop yang ternama")
ROG.set_jenis_komputer("PC atau Personal Computer")
print(ROG.get_merk_komputer() + " Juga memiliki jenis " + ROG.get_jenis_komputer())


class PionCatur():
    def __init__(self, pion, warna_papan, pemain):
        self.pion = pion
        self.warna_papan = warna_papan
        self.pemain = pemain

    def get_pion(self):
        return self.pion

    def get_pemain(self):
        return self.pemain

    def set_pion(self, pion_baru):
        self.pion = pion_baru

    def set_pemain(self, rival):
        self.pemain = rival

afin = PionCatur("Ratu", "Hitam", "Afin")
aqrom = PionCatur("Kuda", "coklat", "Aqrom")

print(afin.get_pion())
afin.set_pion("Kuda")
print(afin.get_pion())
print(afin.get_pemain())
afin.set_pemain("Ucup")
print(afin.get_pemain())
print("\n")

class RekeningBank():
    def __init__(self, pemilik_rekening, pin, nama_bank):
        self.pemilik_rekening = pemilik_rekening
        self.pin = pin
        self.nama_bank = nama_bank

    def get_pin(self):
        return self.pin

    def get_pemilik_rekening(self):
        return self.pemilik_rekening

    def set_pin(self, pin_baru):
        self.pin = pin_baru

    def set_pemilik_rekening(self, pemilik_baru):
        self.pemilik_rekening = pemilik_baru

zainiya = RekeningBank("Zainiya", "676869", "BRI")
eva = RekeningBank("Eva", "343536", "BNI")

print("Pin eva sekarang adalah " + eva.get_pin())
eva.set_pin("121314")
print("Tapi sekarang menjadi " + eva.get_pin())
print("Pin Zainiya sekarang adalah " + zainiya.get_pin())
zainiya.set_pin("409080")
print("Tapi sekarang menjadi " + zainiya.get_pin())
