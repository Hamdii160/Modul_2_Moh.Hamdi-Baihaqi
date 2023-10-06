# Membaca umur dari pengguna
umur = int(input("Masukkan umur Anda: "))

# Menyelidiki umur dan menentukan kategori
if umur > 50:
    kategori = "Tua"
elif umur > 25:
    kategori = "Muda"
elif umur > 17:
    kategori = "Dewasa"
elif umur > 7:
    kategori = "Anak-anak"
else:
    kategori = "Balita atau di bawah 7 tahun"

# Menampilkan kategori umur
print("Anda termasuk dalam kategori:", kategori)
