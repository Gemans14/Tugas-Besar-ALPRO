list_Sparepart = ["Roller Motor", "Klakson Denso", "Per CVT"]
list_harga = [100000, 150000, 75000]
list_stok = [1, 2, 3,]

def UbahBarang(ubah, Nama, Harga, Stok):
    list_Sparepart[ubah - 1] = Nama
    list_harga[ubah -1] = Harga
    list_stok[ubah -1] = Stok

list_tampilan = ["1. Lihat Barang", "2. Input Barang", "3. Update Barang", "4. Hapus Barang"]

while True :
    print("===================")
    print("|  Pilihan Menu:  |")
    print("===================")
    for x in list_tampilan:
        print(x)
    print("===============================")
    print("| Press any key to continue : |")
    print("===============================")
    menu = int(input())
    if menu == 1:
        LihatBarang ()
    elif menu == 2:
        MasukanBarang ()
    elif menu == 3:
        print("Data yang akan diubah :")
        ubah = int(input())
        print("Masukkan Nama Sparepart :")
        Nama = str(input())
        print("Masukkan Harga Sparepart :")
        Harga = int(input())
        print("Masukkan Stok :")
        Stok = int(input())
        UbahBarang (ubah, Nama, Harga, Stok)
    elif menu == 4:
        HapusBarang ()
    else:
        break
    print("=========================================")