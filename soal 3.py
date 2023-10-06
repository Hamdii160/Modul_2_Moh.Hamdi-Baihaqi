# Informasi Jaka
nama_jaka = "Jaka"
skor_jaka = 1100
ipk_jaka = 3.5

# Informasi Ida
nama_ida = "Ida"
skor_ida = 1000
ipk_ida = 3.5

# Persyaratan beasiswa
skor_minimal = 1100
ipk_minimal = 3.0

# Mengecek apakah Jaka lulus persyaratan beasiswa
if skor_jaka >= skor_minimal and ipk_jaka >= ipk_minimal:
    status_jaka = "lulus persyaratan beasiswa"
else:
    status_jaka = "tidak lulus persyaratan beasiswa"

# Mengecek apakah Ida lulus persyaratan beasiswa
if skor_ida >= skor_minimal and ipk_ida >= ipk_minimal:
    status_ida = "lulus persyaratan beasiswa"
else:
    status_ida = "tidak lulus persyaratan beasiswa"

# Menampilkan hasil
print(f"{nama_jaka} {status_jaka}")
print(f"{nama_ida} {status_ida}")
