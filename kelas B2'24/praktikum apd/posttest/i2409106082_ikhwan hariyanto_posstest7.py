characters = {}

ADMIN_ROLE = "admin"
REGULAR_ROLE = "regular"

users = {
    "admin": {"username": "admin", "password": "password", "role": ADMIN_ROLE},
    "user1": {"username": "user1", "password": "password1", "role": REGULAR_ROLE}
}

def register_user(username, password, role):
    if username not in users:
        users[username] = {"username": username, "password": password, "role": role}
        print(f"User  {username} registrasi selesai!")
    else:
        print("Nama pengguna telah dipakai. Silakan pilih nama pengguna yang lain.")


def login_user(username, password):
    if username in users:
        if users[username]["password"] == password:
            return users[username]["role"]
        else:
            print("Password salah.")
    else:
        print("Username tidak ditemukan.")
    return None

def pembuatan_character(name, element, rarity):
    characters[name] = {"element": element, "rarity": rarity}
    print(f"Character '{name}' berhasil ditambahkan!")


def read_characters():
    if len(characters) > 0:
        print("List characters:")
        for name, character in characters.items():
            print(f"Name: {name}, Element: {character['element']}, Rarity: {character['rarity']}")
    else:
        print("Tidak ada karakter yang tersedia.")

def update_character(name, element, rarity):
    if name in characters:
        characters[name]["element"] = element
        characters[name]["rarity"] = rarity
        print(f"Character '{name}' update berhasil!")
    else:
        print("Character tidak ditemukan.")


def hapus_character(name):
    if name in characters:
        del characters[name]
        print(f"Character '{name}' berhasil dihapus!")
    else:
        print("Character tidak ditemukan.")

while True:
    print("Sistem Manajemen Karakter untuk Genshin Impact")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    pilihan = input("Pilih dari option: ")
    
    if pilihan == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (admin/regular): ")
        register_user(username, password, role)
    elif pilihan == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = login_user(username, password)
        if role is not None:
            while True:
                print("1. Create character")
                print("2. Read characters")
                print("3. Update character")
                print("4. Delete character")
                print("5. Logout")
                pilihan = input("Choose an option: ")
                if pilihan == "1":
                    name = input("Enter character name: ")
                    element = input("Enter character element: ")
                    rarity = input("Enter character rarity: ")
                    pembuatan_character(name, element, rarity)
                elif pilihan == "2":
                    read_characters()
                elif pilihan == "3":
                    name = input("Enter character name: ")
                    element = input("Enter character element: ")
                    rarity = input("Enter character rarity: ")
                    update_character(name, element, rarity)
                elif pilihan == "4":
                    name = input("Enter character name: ")
                    hapus_character(name)
                elif pilihan == "5":
                    break
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Pilih opsi yang valid.")