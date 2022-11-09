class TransaksiKayu():
    HargaPerKubik = 5000000
    def __init__(self, panjang, lebar, tinggi, diskon):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.diskon = diskon

    def volume(self):
        hasil = self.panjang * self.lebar * self.tinggi
        return hasil

    def HargaKayu(self):
        hasil = self.volume() * TransaksiKayu.HargaPerKubik
        return hasil

    def Transaksi(self):
        hasil = self.HargaKayu() - (self.HargaKayu() * self.diskon)
        return hasil


transaksi1 = TransaksiKayu(2, 1.5, 1.75, 0.0)
transaksi2 = TransaksiKayu(5, 2.5, 1, 0.05)
transaksi3 = TransaksiKayu(3, 2, 1.5, 0.075)
transaksi4 = TransaksiKayu(2, 1.5, 1.75, 0.055)

print("Pembayaran transaksi 1", "(panjang:", transaksi1.panjang, "meter, lebar:", transaksi1.lebar, "meter, tinggi:", transaksi1.tinggi, "meter", ")",)
print("Total = Rp.", "{:,}".format(transaksi1.Transaksi()))
print("Pembayaran transaksi 1", "(panjang:", transaksi2.panjang, "meter, lebar:", transaksi2.lebar, "meter, tinggi:", transaksi2.tinggi, "meter", ")",)
print("Total = Rp.", "{:,}".format(transaksi2.Transaksi()))
print("Pembayaran transaksi 1", "(panjang:", transaksi3.panjang, "meter, lebar:", transaksi3.lebar, "meter, tinggi:", transaksi3.tinggi, "meter", ")",)
print("Total = Rp.", "{:,}".format(transaksi3.Transaksi()))
print("Pembayaran transaksi 1", "(panjang:", transaksi4.panjang, "meter, lebar:", transaksi4.lebar, "meter, tinggi:", transaksi4.tinggi, "meter", ")",)
print("Total = Rp.", "{:,}".format(transaksi4.Transaksi()))