# Membaca informasi dari pengguna
nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")
nilai_uts = float(input("Masukkan nilai UTS Anda: "))
nilai_uas = float(input("Masukkan nilai UAS Anda: "))

# Menghitung nilai akhir
nilai_akhir = (nilai_uts + nilai_uas) / 2

# Menyelidiki nilai akhir dan menentukan kategori
if nilai_akhir >= 80 and nilai_akhir <= 100:
    kategori = "A"
elif nilai_akhir >= 70 and nilai_akhir < 80:
    kategori = "B"
elif nilai_akhir >= 60 and nilai_akhir < 70:
    kategori = "C"
elif nilai_akhir >= 40 and nilai_akhir < 60:
    kategori = "D"
elif nilai_akhir >= 0 and nilai_akhir < 40:
    kategori = "E"
else:
    kategori = "Nilai tidak valid (harus antara 0 dan 100)"

# Menampilkan informasi lengkap
print("Nama: ", nama)
print("NIM: ", nim)
print("Nilai UTS: ", nilai_uts)
print("Nilai UAS: ", nilai_uas)
print("Nilai Rata Rata nilai anda: ", nilai_akhir)
print("Anda Mendapatkan Nilai : ", kategori)
