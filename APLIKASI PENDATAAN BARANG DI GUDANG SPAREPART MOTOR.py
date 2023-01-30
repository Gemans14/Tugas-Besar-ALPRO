def LihatBarang ():
    print("=========================================")
    print("|             Daftar Barang             |")
    print("=========================================")
    menu = zip(list_Sparepart, list_harga, list_stok) #zip untuk menggabungkan menjadi 1 list
    print ("|{:<3}| {:<15} | {:<8} | {:<5}|".format("No", "Nama Barang", "Harga", "Stok"))
    print("=========================================")
    for index, y in enumerate (menu): #enumerate untuk mendapatkan index dari list data
        Nama, Harga, Stok = y
        print ("|{:<3}| {:<15} | {:<8} | {:<5}|".format( index+1, Nama, Harga, Stok))

def MasukanBarang (Nama, Harga, Stok):
    list_Sparepart.append(Nama)
    list_harga.append(Harga)
    list_stok.append(Stok)
    stringNama = ",".join(list_Sparepart)
    stringHarga = ",".join(str(x) for x in list_harga) #mengubah harga dari type int menjadi str dan menggabungkan str menggunakan koma
    stringStok= ",".join(str(x) for x in list_stok) #w untuk membuka txt dengan fungsi write pada file
    my_file = open("listsparepart.txt", "w") #\n untuk enter
    my_file.write(stringNama + "\n") #\n untuk enter
    my_file.write(stringHarga + "\n")
    my_file.write(stringStok)
    my_file.close()

def UbahBarang(ubah, Nama, Harga, Stok):
    list_Sparepart[ubah - 1] = Nama  #-1 karena index dimulai dari 0
    list_harga[ubah -1] = Harga
    list_stok[ubah -1] = Stok
    stringNama = ",".join(list_Sparepart)
    stringHarga = ",".join(list_harga)
    stringStok= ",".join(str(x) for x in list_stok) #mengubah harga dari type int menjadi str dan menggabungkan str menggunakan koma
    my_file = open("listsparepart.txt", "w") #w untuk membuka txt dengan fungsi write pada file
    my_file.write(stringNama + "\n")
    my_file.write(stringHarga + "\n")
    my_file.write(stringStok)
    my_file.close()

def HapusBarang (hapus):
    list_Sparepart.pop (hapus-1) 
    list_harga.pop (hapus-1)  #-1 karena index dimulai dari 0
    list_stok.pop (hapus-1)
    stringNama = ",".join(list_Sparepart)
    stringHarga = ",".join(list_harga)
    stringStok= ",".join(str(x) for x in list_stok)  #mengubah harga dari type int menjadi str dan menggabungkan str menggunakan koma
    my_file = open("listsparepart.txt", "w") #w untuk membuka txt dengan fungsi write pada file
    my_file.write(stringNama + "\n")
    my_file.write(stringHarga + "\n")
    my_file.write(stringStok)
    my_file.close()

my_file = open("listsparepart.txt", "r")  #r untuk membaca file txt
count = 0

list_Sparepart = []
list_harga= []
list_stok = []

while True:
    count += 1  
    data = my_file.readline()
    if not data:
        break
    if count == 1 :
        list_Sparepart = data.rstrip().split(",")
    elif count == 2 :
        list_harga = data.rstrip().split(",")
    elif count == 3 :
        list_stok = data.rstrip().split(",")

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
        print("Masukkan Nama Sparepart :")
        Nama = str(input())
        print("Masukkan Harga Sparepart :")
        Harga = int(input())
        print("Masukkan Stok :")
        Stok = int(input())
        MasukanBarang (Nama, Harga, Stok)
        LihatBarang()
    elif menu == 3:
        print("Data yang akan diubah :")
        ubah = int(input())
        if ubah <= len(list_Sparepart) :
            print("Masukkan Nama Sparepart :")
            Nama = str(input())
            print("Masukkan Harga Sparepart :")
            Harga = int(input())
            print("Masukkan Stok :")
            Stok = int(input())
            UbahBarang(ubah, Nama, Harga, Stok)
        else :
            print("Data Tidak Ada")
    elif menu == 4:
        print("Data yang akan dihapus :")
        hapus = int(input())
        if hapus <=len(list_Sparepart) :
            HapusBarang (hapus)
            LihatBarang()
        else :
            print("Data Tidak Ada")
    else:
        break
    print("=========================================")