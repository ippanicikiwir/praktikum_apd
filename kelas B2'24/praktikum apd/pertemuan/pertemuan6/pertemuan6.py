# # daftar_buku = {
# #     "Buku1" : "Harry Potter",
# #     "Buku2" : "Percy Jackson",
# #     "Buku3" : "Twillight"
# # }
# # print(daftar_buku["Buku1"])
# # print(daftar_buku["Buku2"])
# # print(daftar_buku["Buku3"])


# # daftar_buku = {}

# # daftar_buku["novel 1"] = "senyuman mu"

# # daftar_buku[1] = "matahari"
# # print(daftar_buku)

# # daftar_buku = dict(buku1 = "harry potter",  buku2 = "percy jackson")
# # print(daftar_buku)

# # print(daftar_buku.get("buku2"))

# # nilai = {
# #     "Matematika" : 80,
# #     "B. Indonesia" : 90,
# #     "B. Inggris" : 81,
# #     "Kimia" : 78,
# #     "Fisika" : 80
# # }

# # for i in nilai:
# #     print(i)

# # for i,j in nilai.items():
# #     print(f"nilai {i} itu veluenya adalah: {j}")

# # nilai["struktur data"]  = 99

# # nilai.update({"struktur data" : 99} )

# # print(nilai)
# # print()
# # trasbin = nilai.pop("matematika")

# # print(trasbin)

# # del{}

# # nilai = {
# #     "Matematika" : 80,
# #     "B. Indonesia" : 90,
# #     "B. Inggris" : 81,
# #     "Kimia" : 78,
# #     "Fisika" : 80
# # }

# # print(f"jumlah element dari variable dick nilai adalah {len(nilai)}")

# # daftar_nilai = nilai.copy()
# # print(daftar_nilai)
# import os
# os.system("cls")
# # key = "naga", "astral_express", "ufo"
# # value = 2
# # daftar_kendaraan = dict.fromkeys(key, value)
# # print(daftar_kendaraan)

# # Musik = {
# #     "The Chainsmoker" : ["All we Know", "TheParis"],
# #     "Alan Walker" : ["Alone", "Lily"],
# #     "Neffex" : ["Best of Me", "Memories"]
# # }
# # for i, j in Musik.items():
# #     print(f"Musik milik {i} adalah : ")
# #     for song in j:
# #         print(song)
# #     print("")

# # mahasiswa = {
# # 101 : {"Nama" : "Aldy", "Umur" : 19},
# # 111 : {"Nama" : "Abdul", "Umur" : 18}
# # }
#     # for key, value in mahasiswa.items():
#     #     print("ID Mahasiswa : ", key)
#     #     for key_a, value_a in value.items():
#     #         print (key_a, " : ", value_a)
#     #         print("")

# # print(mahasiswa[111]["Umur"])


# data_nilai = {
#     "Matematika": 90,
#     "Fisika": 80,
#     "Biologi": 80,
#     "Kimia": 70
# }

# # jumlah_total = sum(data_nilai.values())
# # print("Jumlah total nilai:", jumlah_total)

# # rata_rata = jumlah_total / len(data_nilai)
# # print("Rata-rata nilai:", rata_rata)

# jumlah_total = (data_nilai // 4)