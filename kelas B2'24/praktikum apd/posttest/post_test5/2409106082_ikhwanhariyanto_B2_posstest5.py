characters = []

ADMIN_ROLE = "admin"
REGULAR_ROLE = "regular"

users = {
    "admin": {"username": "admin", "password": "password", "role": ADMIN_ROLE},
    "user1": {"username": "user1", "password": "password1", "role": REGULAR_ROLE}
}

def register_user(username, password, role):
    if username not in users:
        users[username] = {"username": username, "password": password, "role": role}
        print(f"User   {username} registrasi selesai!")
    else:
        print("nama pengguna telah dipakai.silakan  pilih nama pengguna yang lain")


def login_user(username, password):
    if username in users:
        if users[username]["password"] == password:
            return users[username]["role"]
        else:
            print("password salah.")
    else:
        print("Username tidak di temukan.")
    return None

def pembuatan_character(name, element, rarity):
    character = [name, element, rarity]
    characters.append(character)
    print(f"Character '{name}' berhasil di tambahkan!")

def read_characters():
    if len(characters) > 0:
        print("List characters:")
        for character in characters:
            print(f"Name: {character[0]}, Element: {character[1]}, Rarity: {character[2]}")
    else:
        print("no characters available.")

def update_character(name, element, rarity):
    for character in characters:
        if character[0] == name:
            character[1] = element
            character[2] = rarity
            print(f"Character '{name}' update berhasil!")
            return
    print("Character tidak di temukan.")


def delete_character(name):
    for character in characters:
        if character[0] == name:
            characters.remove(character)
            print(f"Character '{name}' berhasil di hapus!")
            return
    print("Character tidak di temukan.")


while True:
    print("Sistem Manajemen Karakter untuk Genshin Impact")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    pilihan = input("pilih dari option: ")
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
                    delete_character(name)
                elif pilihan == "5":
                    break
    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Pilih opsi yang valid.")

characters = {}

def pembuatan_character(name, element, rarity):
    characters[name] = {"element": element, "rarity": rarity}
    print(f"Character '{name}' berhasil di tambahkan!")

def read_characters():
    if len(characters) > 0:
        print("List characters:")
        for name, character in characters.items():
            print(f"Name: {name}, Element: {character['element']}, Rarity: {character['rarity']}")
    else:
        print("no characters available.")

def update_character(name, element, rarity):
    if name in characters:
        characters[name]["element"] = element
        characters[name]["rarity"] = rarity
        print(f"Character '{name}' update berhasil!")
    else:
        print("Character tidak di temukan.")

def delete_character(name):
    if name in characters:
        del characters[name]
        print(f"Character '{name}' berhasil di hapus!")
    else:
        print("Character tidak di temukan.")