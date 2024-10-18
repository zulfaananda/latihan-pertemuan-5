#tugas 5.3
# Menginput jumlah mata kuliah
jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))

# Inisialisasi total_sks dan total_nilai
total_sks = 0
total_nilai = 0

# Perulangan untuk input nilai setiap mata kuliah
for i in range(jumlah_mata_kuliah):
    sks = int(input(f"Masukkan SKS untuk mata kuliah ke-{i+1}: "))
    nilai = input(f"Masukkan nilai untuk mata kuliah ke-{i+1} (A/B/C/D): ").upper()

    # Menghitung nilai berdasarkan input
    if nilai == 'A':
        bobot = 4
    elif nilai == 'B':
        bobot = 3
    elif nilai == 'C':
        bobot = 2
    elif nilai == 'D':
        bobot = 1
    else:
        bobot = 0

    # Menghitung total SKS dan total nilai
    total_sks += sks
    total_nilai += bobot * sks

# Menghitung IPS
ips = total_nilai / total_sks
print(f"IPS Anda adalah: {ips:.2f}")





