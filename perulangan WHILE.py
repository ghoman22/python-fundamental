"""
program perulangan dengan WHILE
"""

jumlah_buku =10
print('Perintah ibu "Baca semua bukumu"')

jumlah_buku_yang_dibaca = 0
print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}")

while jumlah_buku_yang_dibaca < jumlah_buku:
    print(f"Buku ke {jumlah_buku_yang_dibaca + 1} sudah dibaca")
    jumlah_buku_yang_dibaca = jumlah_buku_yang_dibaca + 1

print(f"jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}")

