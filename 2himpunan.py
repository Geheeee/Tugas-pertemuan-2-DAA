# Fungsi untuk menjumlahkan semua angka dalam sebuah daftar
def getSum(angka):
    return sum(angka)

# Fungsi untuk membagi jumlah dari dua daftar angka
def bagiJumlah(daftar1, daftar2):
    jumlah1 = getSum(daftar1)
    jumlah2 = getSum(daftar2)
    if jumlah2 == 0:  # Menghindari pembagian dengan nol
        return None  # Kembalikan None jika penyebut adalah nol
    return jumlah1 / jumlah2

# Contoh daftar angka
daftar1 = [10, 20, 30]
daftar2 = [2, 3, 5]

# Memanggil fungsi bagiJumlah dan menyimpan hasilnya
hasil = bagiJumlah(daftar1, daftar2)

# Mencetak hasilnya
print("Hasil dari pembagian jumlah dua daftar adalah:", hasil)
