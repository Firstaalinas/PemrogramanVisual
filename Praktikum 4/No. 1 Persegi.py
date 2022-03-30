# Nama  : Firsta Alina S
# NIM   : 20051397085
# D4 Manajemen Informatika 2020 A


class hasil:
    def hitung(angka):
        print(' ')
        print('-----HASIL-----')
        print('Panjang sisi : ', angka.bil)
        print('Luas Bangun Persegi Adalah :', angka.bil**2)
        print('Keliling Bangun Persegi Adalah :', 4*angka.bil)


class nilai(hasil):
    def __init__(self):
        self.bil = int(input('Masukan Panjang sisi : '))


coba = ('y')
while coba == ('y') or coba == ('Y'):
    print('Mencari Luas Dan Keliling Persegi')

    objek = nilai()
    objek.hitung()
    print(' ')
    break
