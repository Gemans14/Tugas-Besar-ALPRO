from os import system
     
if __name__ == "__main__":
    list_barang = []

    while True:
        system('cls') 
        
        print("="*40)
        print("Aplikasi Pendataan Gudang Sparepart Motor : JAYA MOTOR")
        print("="*40)

        print("-"*20)
        print("Pilihan Menu:")
        print("1. Lihat Barang")
        print("2. Input Barang")
        print("0. Keluar")
        print("-"*20)
        menu = ("menu: ")

        if menu == "0":
            break
        elif menu == "1":           
                print("Lihat Barang")

        elif menu == "2":
            print("Input Barang")       
        else:
            print("Hanya boleh memilih menu 0, 1, atau 2")

        input("-- press any key to continue --")
