"""
program perulangan dengan WHILE sampai paham
"""

book_count =10
read_count =0
print('Perintah ibu "Baca semua bukumu sampai paham"')

understood_count = 0
print(f"jumlah buku yang sudah dibaca dan dipahami {understood_count}")

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Buku ke {understood_count + 1} belum paham")

    else:
        understood_count= understood_count + 1
        print(f"Buku ke {understood_count } sudah dibaca dan dipahami")

print(f'jumlah buku yang sudah dibaca {understood_count}')
if understood_count == book_count:
    print(f" semua buku bisa dipahami {understood_count}")
else:
        print(f"tidak semua buku bisa dipahami, hanya {understood_count} yang bisa dipahami")




