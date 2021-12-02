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

print("\n list baru")
daftar_buku = ['atomic habits', 'harry potter', 'eating clean','4dx']
daftar_buku2 = daftar_buku [:]
for i in range (0, len(daftar_buku)):
    print(daftar_buku [i])

print("\n list baru2")
del daftar_buku [:]
for i in range (0, len(daftar_buku2)):
    print(daftar_buku2 [i])

