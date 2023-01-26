list_Sparepart = ["Roller Motor", "Klakson Denso", "Per CVT"]
list_harga = [100000, 150000, 75000]
list_stok = [1, 2, 3,]

def LihatBarang ():
    print("Daftar Barang")
    menu = zip(list_Sparepart, list_harga, list_stok)
    print ("{:<5}| {:<20} | {:<12} | {:<5} |".format("No", "Nama Barang", "Harga", "Stok"))
    for index, y in enumerate (menu):
        Nama, Harga, Stok = y
        print ("{:<5}| {:<20} | {:<12} | {:<5} |".format( index+1, Nama, Harga, Stok))

list_tampilan = ["1. Lihat Barang", "2. Input Barang", "3. Update Barang", "4. Hapus Barang"]

while True :
    print("Pilihan Menu:")
    for x in list_tampilan:
        print(x)
    print("Press any key to continue")
    menu = int(input())
    if menu == 1:
        LihatBarang ()
    elif menu == 2:
        MasukanBarang ()
    elif menu == 3:
        UbahBarang ()
    elif menu == 4:
        HapusBarang ()
    else:
        break