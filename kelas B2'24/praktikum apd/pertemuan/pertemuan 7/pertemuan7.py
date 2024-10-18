# def tambah():
#     print("hello world")

# tambah()

# def tambah(a,b):
#     hasil = a+b
#     print(hasil)

import os
os.system("cls")

# def tambah(a,b):
#     hasil = a
#     return 2

# tambahan = tambah(2,4) + tambah(4,6)

# print(tambahan)  

def pilihan(opsi):
    match opsi:
        case 1:
            print(1)
            return
        case 2:
            print(2)
            return
    
    print(3)

# pilihan(2)

def cetak(nama,nim,*matkul):
    print(nama,nim,matkul)

cetak("fathir",41,"kalkulus","fisdas")


Nama = "Informatika"
Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
kelas = "IT MENGASYIKANNN"

def info():
    Nama = "Teknik Elektro"
    Mata_Kuliah = "Pengantar Teknik ELektro"
    print("Prodi:", Nama)
    print("Mata Kuliah:", Mata_Kuliah, kelas)


print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)

