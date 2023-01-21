for item in list_barang:
                    str_item = "| {:5} | {:20} | {:>12} | {:>5} |"\
                                    .format(["Kode"], ["Nama"], ["Harga"], ["Stok"])
                    print(str_item)
print("-"*55)

elif menu == "2":
    kode = input("Kode:")
    pos_kode = cari_kode(list_barang, kode)
    if pos_kode > -1:
    stok = int(input("Stok: "))
    list_barang[pos_kode] ['stok'] += stok
else:
nama = input("Nama: ")
harga = input("Harga: ")
stok = input("Stok")
list_barang.append({'kode':kode, 'nama':nama, 'harga':harga, 'stok':stok})
            
else:
    print("Hanya boleh memilih menu 0, 1, atau 2")