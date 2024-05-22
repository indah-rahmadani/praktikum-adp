
film = 'data_film.txt'


def load_data():
    data = {}
    try:
        with open(film, 'r') as file:
            for line in file:
                if line.strip():
                    judul, penulis_skenario, sutradara, tahun_rilis = line.strip().split('|')
                    data[judul] = {
                        'penulis_skenario': penulis_skenario,
                        'sutradara': sutradara,
                        'tahun_rilis': tahun_rilis
                    }
    except FileNotFoundError:
        
        return {}
    return data


def save_data(data):
    with open(film, 'w') as file:
        for judul, info in data.items():
            line = f"{judul}|{info['penulis_skenario']}|{info['sutradara']}|{info['tahun_rilis']}\n"
            file.write(line)

#  menambah data film
def tambah_film(data):
    judul = input("Masukkan judul film: ")
    penulis_skenario = input("Masukkan nama penulis skenario: ")
    sutradara = input("Masukkan nama sutradara: ")
    tahun_rilis = input("Masukkan tahun rilis: ")

    if judul in data:
        print("Film sudah ada dalam database.")
    else:
        data[judul] = {
            'penulis_skenario': penulis_skenario,
            'sutradara': sutradara,
            'tahun_rilis': tahun_rilis
        }
        save_data(data)
        print("Film berhasil ditambahkan.")

#  menghapus data film
def hapus_film(data):
    judul = input("Masukkan judul film yang ingin dihapus: ")
    
    if judul in data:
        del data[judul]
        save_data(data)
        print("Film berhasil dihapus.")
    else:
        print("Film tidak ditemukan dalam database.")

#  mengedit data film
def edit_film(data):
    judul = input("Masukkan judul film yang ingin diedit: ")
    
    if judul in data:
        penulis_skenario = input(f"Masukkan nama penulis skenario baru (sebelumnya: {data[judul]['penulis_skenario']}): ")
        sutradara = input(f"Masukkan nama sutradara baru (sebelumnya: {data[judul]['sutradara']}): ")
        tahun_rilis = input(f"Masukkan tahun rilis baru (sebelumnya: {data[judul]['tahun_rilis']}): ")

        data[judul] = {
            'penulis_skenario': penulis_skenario,
            'sutradara': sutradara,
            'tahun_rilis': tahun_rilis
        }
        save_data(data)
        print("Film berhasil diedit.")
    else:
        print("Film tidak ditemukan dalam database.")

def tampilkan_data(data):
    if data:
        for judul, info in data.items():
            print(f"\nJudul: {judul}")
            print(f"Penulis Skenario: {info['penulis_skenario']}")
            print(f"Sutradara: {info['sutradara']}")
            print(f"Tahun Rilis: {info['tahun_rilis']}")
    else:
        print("Tidak ada data film.")


def main():
    data = load_data()
    while True:
        print("__________Menu:_________")
        print("========================")
        print("|1. Tambah data film   |")
        print("|2. Hapus data film    |")
        print("|3. Edit data film     |")
        print("|4. Tampilkan data film|")
        print("|5. Keluar             |")
        print("========================")

        pilihan = input("Pilih opsi (1/2/3/4/5): ")

        if pilihan == '1':
            tambah_film(data)
        elif pilihan == '2':
            hapus_film(data)
        elif pilihan == '3':
            edit_film(data)
        elif pilihan == '4':
            tampilkan_data(data)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
