class bilangan_pecahan():
    def __init__(self, pembilang, penyebut):
        self.pembilang = pembilang
        self.penyebut = penyebut

    def perkalian(self, rival):
        hasil_pembilang = self.pembilang * rival.pembilang
        hasil_penyebut = self.penyebut * rival.penyebut
        hasil = bilangan_pecahan(hasil_pembilang, hasil_penyebut)
        return hasil

    def pembagian(self, rival):
        hasil_pembilang = self.pembilang * rival.penyebut
        hasil_penyebut = self.penyebut * rival.pembilang
        hasil_jadi = bilangan_pecahan(hasil_pembilang, hasil_penyebut)
        return hasil_jadi

    def penambahan(self, rival):
        hasil_pembilang = self.pembilang + rival.pembilang
        hasil_penyebut = self.penyebut + rival.penyebut
        hasilnya = bilangan_pecahan(hasil_pembilang, hasil_penyebut)
        return hasilnya

    def pengurangan(self, rival):
        hasil_pembilang = self.pembilang - rival.pembilang
        hasil_penyebut = self.penyebut - rival.penyebut
        jadi_hasilnya = bilangan_pecahan(hasil_pembilang, hasil_penyebut)
        return jadi_hasilnya

pecahan_a = bilangan_pecahan(10,5)
pecahan_b = bilangan_pecahan(8, 4)

pecahan_c = pecahan_a.perkalian(pecahan_b)
pecahan_d = pecahan_a.pembagian(pecahan_b)
pecahan_e = pecahan_a.penambahan(pecahan_b)
pecahan_f = pecahan_a.pengurangan(pecahan_b)

print("Hasil perkalian pecahan_c: "+ str(pecahan_c.pembilang) + "/" + str(pecahan_c.penyebut))
print("\n")
print("Hasil pembagian pecahan_d: " + str(pecahan_d.pembilang) + "/" + str(pecahan_d.penyebut))
print("\n")
print("Hasil penambahan pecahan_e: " + str(pecahan_e.pembilang) + "/" + str(pecahan_e.penyebut))
print("\n")
print("Hasil pengurangan pecahan_f: " + str(pecahan_f.pembilang) + "/" + str(pecahan_f.penyebut))
