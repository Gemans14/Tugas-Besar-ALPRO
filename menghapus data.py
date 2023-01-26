list_Sparepart = ["Roller Motor", "Klakson Denso", "Per CVT"]
list_harga = [100000, 150000, 75000]
list_stok = [1, 2, 3,]

def HapusBarang (hapus):
    list_Sparepart.pop (hapus-1)
    list_harga.pop (hapus-1)
    list_stok.pop (hapus-1)

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
        UbahBarang ()
    elif menu == 4:
        print("Data yang akan dihapus :")
        hapus = int(input())
        HapusBarang (hapus)
    else:
        break
    print("=========================================")