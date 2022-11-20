from tabulate import tabulate

rak_buku = {'Id': [],
            'Judul Buku': [],
            'Genre': [],
            'Penulis': [],
            'Harga (Rp)': []}


def tambah_buku():
    print("\n"*2)
    print("Silakan masukkan data yang ingin Anda tambahkan.") 
    judul = input("Masukkan judul buku: ")
    genre = input("Masukkan genre buku: ")
    penulis = input("Masukkan nama penulis: ")
    harga = input("Masukkan harga buku: ")
        
    data = [judul, genre, penulis, harga]
        
    # menambahkan index
    if len(rak_buku['Id']) == 0:
        rak_buku['Id'].append(1)
    else:
        rak_buku['Id'].append(rak_buku['Id'][-1] + 1)

    # menambahkan input ke dalam dictionary
    i = 0
    for key, tabel in rak_buku.items():
        if key == 'Id': 
            continue

        tabel.append(data[i])
            
        i += 1

def tampilkan_data():
    print(tabulate(rak_buku, headers='keys', tablefmt='github'))
    print("\n"*2)

def hapus_data():
    print("\n"*2)
    print("Silakan pilih data puku mana yang akan dihapus.")

    # index pada list harus dikurangi 1
    id_hapus = int(input("Masukkan indeks data buku yang ingin dihapus: ")) - 1

    for tabel in rak_buku.values():
        tabel.remove(tabel[id_hapus])
    
    # update index dalam Id
    rak_buku['Id'] = [id-1 for id in rak_buku['Id']]
    
    print("Data buku sudah berhasil dihapus!")




def menu():
    print("*"*70)
    print("Selamat datang di LMS sederhana SMA Maju Mundur Cantik")
    print("*"*70)
    print("Silakan pilih menu berikut.")
    print("1. Tambahkan data buku")
    print("2. Tampilkan semua data buku")
    print("3. Hapus data buku")
    print("0. Akhiri program")
    pilihan = int(input("Pilihan Anda: "))

    fitur = {1: tambah_buku, 2: tampilkan_data, 3: hapus_data}

    # input 0 untuk mengakhiri program
    if pilihan == 0:
        exit()
    
    fitur[pilihan]()
    menu()


menu()
    