# Fungsi untuk menjumlahkan semua angka dalam sebuah daftar
def getSum(angka):
    return sum(angka)

# Fungsi untuk mengurangi jumlah dari dua daftar angka
def kurangiJumlah(daftar1, daftar2):
    jumlah1 = getSum(daftar1)
    jumlah2 = getSum(daftar2)
    return jumlah1 - jumlah2

# Contoh daftar angka
daftar1 = [50, 30, 20]
daftar2 = [10, 5, 5]

# Memanggil fungsi kurangiJumlah dan menyimpan hasilnya
hasil = kurangiJumlah(daftar1, daftar2)

# Mencetak hasilnya
print("Hasil dari pengurangan jumlah dua daftar adalah:", hasil)
