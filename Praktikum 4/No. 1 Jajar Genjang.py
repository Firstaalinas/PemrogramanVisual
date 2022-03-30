# Nama  : Firsta Alina S
# NIM   : 20051397085
# D4 Manajemen Informatika 2020 A

class hasil:
    def hitung(angka):
        print(' ')
        print('-----HASIL-----')
        print('panjang sisi a mendatar : ', angka.bil1)
        print('panjang sisi b mendatar : ', angka.bil2)
        print('Tinggi : ', angka.bil3)
        print('Luas Bangun Jajargenjang Adalah :', angka.bil1*angka.bil3)
        print('Keliling Bangun Jajargenjang Adalah :',
              2 * (angka.bil1+angka.bil2))


class nilai(hasil):
    def __init__(self):
        self.bil1 = int(input('Masukan Panjang sisi a mendatar : '))
        self.bil2 = int(input('Masukan Panjang sisi b mendatar : '))
        self.bil3 = int(input('Masukan tinggi : '))


coba = ('y')
while coba == ('y') or coba == ('Y'):
    print('Mencari Luas Dan Keliling Jajargenjang')

    objek = nilai()
    objek.hitung()
    print(' ')
    break
