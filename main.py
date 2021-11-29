#Sequential
print("Ibu berkata, 'pergi ke toko'")
print("anak menjawab 'Baik apa yang harus saya lakukan di toko'")
print("Ibu menjawab, 'Beli 1 botol susu'")
print("maka budi berangkat ke toko")
print("dan mulai berbelanja")

# percabangan
jumlah_botol_susu =180
jumlah_telur = 1500
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu >0:
    print("Budi mengecek harga, uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 1 botol susu dan 6 butir telur")

else :
    print("Budi tidak membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Budi Memberitahu hasilnya kepada ibu")
