print("___pembuatan akun baru___")


username = input("masukan username : ")
nim =  input("masukan 3 digit akhir NIM:")
password = nim[-3:].lstrip("0")

percobaan = 0
max_percobaan = 3

print("______menu login______")

while  True:
        masukan_username = input("masukan nama anda: ")
        print("jika nim memiliki angka 0 maka hilangkan angka 0 ")
        masukan_password = input("masukan password anda : ") 
        


        if masukan_username == username and masukan_password == password:
            print("___anda berhasil login____")
            print("//SELAMAT DATANG KEDALAM SISTEM\\")

            break
        else:
            percobaan += 1
            print(f"login gagal , percobaan ke-{percobaan}/{max_percobaan}")
            if  percobaan == max_percobaan:
                print("anda gagal login")
                exit()
                

# sistem posstest sebelumnya

while True:
    def kalkulasi_bmi(berat, tinggi):
        beratkg = berat / 1000000

        tinggim = tinggi * 1000
        
        bmi = beratkg / (tinggim ** 2)
        print ("index bmi:",bmi)

        if bmi < 18.5:
            return "berat badan anda kurang(semangat naikin berat badan)"
        elif bmi < 24.9:
            return "berat badan anda normal(teruskan kawan)"
        elif bmi < 29.9:
            return "berat badan anda berlebihan(hayya kebanyakan ngewibu)"
        else:
            return "obesitas kamu kurang-kuranginlah nonton anime mu mending workout"
        

    berat = float(input("masukan berat badanmu dalam mg: "))
    tinggi = float(input("masukan tinggi badanmu dalam km: "))

    kategoribadan = kalkulasi_bmi(berat, tinggi)
    print("kategori badan anda adalah:", kategoribadan)
    print('selalu menjaga badan mu agar tetap sehat kawan')

    print("ketik 'keluar' untuk meninggalkan sistem" )
    command = input("> ")
    if command.lower() == "keluar":
        print("TERIMA KASIH TELAH MENGGUNAKAN SISTEM KAMI")
        break
    else:
        print("perintah tidak dikenal, silakan mencoba lagi")

