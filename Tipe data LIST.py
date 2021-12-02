daftar_buku = ['atomic habits', 'harry potter', 'eating clean']
print("Tampilkan variabel daftar buku")
print(daftar_buku)

print("\nproses semua dengan for in")
for buku in daftar_buku:
    print(buku)

print("\ntampilkan isi daftar buku pada indeks tertentu")
print(daftar_buku[0])
print(daftar_buku[2])

print("\nTampilkan dengan for in range")
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

daftar_buku = ['3.14', 'kenji', '-98']
print("\nTampilkan dengan for in range dimana tipe data tiap elemen berbeda2")
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\nkembalikan nilai awal buku")
daftar_buku = ['atomic habits', 'harry potter', 'eating clean']
print(("\nTambahkan 1 buku baru"))
daftar_buku.append("miracle morning")
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\n clear list")
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\n mengganti elemen 0")
daftar_buku = ['atomic habits', 'harry potter', 'eating clean']
daftar_buku[0] = 'seven habits'
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\n buku ke 2 menghilang")
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\n mengambil buku ke2 ")
print(buku)

print("\n pop")
daftar_buku.pop()
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\n pop -1")
daftar_buku = ['atomic habits', 'harry potter', 'eating clean']
daftar_buku.pop(-1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\n perintah del")
daftar_buku = ['atomic habits', 'harry potter', 'eating clean']
del daftar_buku[0]
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\n perintah del dengan list comprehension")
daftar_buku = ['atomic habits', 'harry potter', 'eating clean']
del daftar_buku[:]
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\n perintah del dengan list comprehension start")
daftar_buku = ['atomic habits', 'harry potter', 'eating clean','4dx']
del daftar_buku[0:2] #start:end
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\n perintah del dengan list comprehension step")
daftar_buku = ['atomic habits', 'harry potter', 'eating clean','4dx']
del daftar_buku[0::2] #start:end:step
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])


