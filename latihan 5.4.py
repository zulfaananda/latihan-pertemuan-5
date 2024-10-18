# Perkalian dua bilangan tanpa operator *
def perkalian(a, b):
    hasil = 0
    for i in range(abs(b)):
        hasil += a
    if b < 0:
        hasil = -hasil
    return hasil

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
print(f"Hasil perkalian: {perkalian(a, b)}")

# Pemangkatan dua bilangan tanpa operator **
def pemangkatan(x, y):
    hasil = 1
    for i in range(y):
        hasil *= x
    return hasil

x = int(input("Masukkan bilangan dasar: "))
y = int(input("Masukkan pangkat: "))
print(f"Hasil pemangkatan: {pemangkatan(x, y)}")

