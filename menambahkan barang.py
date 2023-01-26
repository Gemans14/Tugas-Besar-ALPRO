list_Sparepart = ["Roller Motor", "Klakson Denso", "Per CVT"]
list_harga = [100000, 150000, 75000]
list_stok = [1, 2, 3,]

def MasukanBarang (Nama, Harga, Stok):
    list_Sparepart.append(Nama)
    list_harga.append(Harga)
    list_stok.append(Stok)

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
        print("Masukkan Nama Sparepart")
        Nama = str(input())
        print("Masukkan Harga Sparepart")
        Harga = int(input())
        print("Masukkan Stok")
        Stok = int(input())
        MasukanBarang (Nama, Harga, Stok)
    elif menu == 3:
        UbahBarang ()
    elif menu == 4:
        HapusBarang ()
    else:
        break