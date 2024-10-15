# input

namabarang = input("Masukkan nama barang: ")
hargabarang = float(input("Masukkan harga barang: "))
jumlahbarang = int(input("Masukkan jumlah barang: "))
diskon = float(input("Masukkan digit nim akhir : "))

# perhitungan

totalsebelumdiskon = jumlahbarang * hargabarang
totaldiskon = (diskon / 100) * totalsebelumdiskon
totalbayar = totalsebelumdiskon - totaldiskon
sisabaginya = int(diskon) % 3

# output

print(f"Anda membeli {jumlahbarang} {namabarang} dengan harga satuan {hargabarang}, total sebelum diskon adalah {totalsebelumdiskon}, total diskon adalah {totaldiskon}, dan total yang harus dibayar adalah {totalbayar}.")
print(f"{diskon} dibagi dengan 3 sisanya {sisabaginya}")
