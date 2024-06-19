import os
import time
from termcolor import colored, cprint

os.system('cls')

cprint("                  PROGRAM KONSULTASI KESEHATAN DASAR MAHASISWA FMIPA UNAND                 ", "black","on_yellow")
print("===========================================================================================")
print(colored("Selamat Datang di Konsultasi Kesehatan Dasar Mahasiswa Universitas Andalas!!!", "green"))
print(colored("Jawab beberapa pertanyaan berikut dengan jujur untuk mendapatkan saran kesehatan dasar!11", "cyan"))

def waktu(proses):
    print(f"{proses}", end="")
    for i in range(5):
        print(colored(".", "blue"), end=" ", flush=True)
        time.sleep(0.5)
    print()

#menambah data konsultasi
def konsultasi(nama, nim, jurusan, usia, bb, tb, gigi, makan, tidur, olahraga, riwayat, merokok):
    with open("database_konsul.txt", "a") as file:
        file.write(f"{nama}, {nim}, {jurusan}, {usia}, {bb}, {tb}, {gigi}, {makan}, {tidur}, {olahraga}, {riwayat}, {merokok}\n")
    print("[Data konsultasi berhasil ditambahkan]")

#menghapus data konsultasi
def hapus_data(nim):
    with open("database_konsul.txt", "r") as file:
        lines = file.readlines()
    with open("database_konsul.txt", "w") as file:
        for line in lines:
            if line.split(",")[1].strip() != nim:
                file.write(line)
    print("[Data konsultasi berhasil dihapus]")

#menampilkan seluruh data konsultasi
def tampilkan_data():
    with open("database_konsul.txt", "r") as file:
        data_konsul = file.readlines()
    if data_konsul:
        print(colored("\n                         Data Konsultasi:                         ", "yellow"))
        for data in data_konsul:
            data = data.strip().split(", ")
            print(f"Nama                      : {data[0]}")
            print(f"NIM                       : {data[1]}")
            print(f"Jurusan                   : {data[2]}")
            print(f"Usia                      : {data[3]}")
            print(f"BB                        : {data[4]} kg")
            print(f"TB                        : {data[5]} cm")
            print(f"Menyikat Gigi 2-3x Sehari : {data[6]}")
            print(f"Makan 3x Sehari           : {data[7]}")
            print(f"Tidur ≥ 7 Jam             : {data[8]}")
            print(f"Olahraga Teratur          : {data[9]}")
            print(f"Riwayat Penyakit Kronis   : {data[10]}")
            print(f"Merokok                   : {data[11]}")
            print(colored("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", "yellow"))
    else:
        print("[Database konsultasi kosong]")

def konsultasi_kesehatan():
    data_konsul = [
        "Masukkan Nama Anda            : ",
        "Masukkan NIM  Anda            : ",
        "Masukkan Jurusan              : ",
        "Berapa Usia Anda              : ",
        "Berapa berat badan Anda (kg)  : ",
        "Berapa tinggi badan Anda (cm) : ",
        "Apakah Anda menyikat gigi 2x-3x dalam sehari (y/n)                                                     : ",
        "Apakah Anda makan 3x dalam sehari (y/n)                                                                : ",
        "Apakah Anda tidur ≥ 7 jam setiap malam (y/n)                                                           : ",
        "Apakah Anda berolahraga secara teratur (y/n)                                                           : ",
        "Apakah Anda memiliki riwayat penyakit kronis seperti diabetes, hipertensi, atau penyakit jantung (y/n) : ",
        "Apakah Anda merokok? (y/n)                                                                             : "
    ]

    data = []
    for p in data_konsul[0:6]:
        data.append(input(p))
    
    nama = str(data[0])
    nim = str(data[1]) 
    jurusan = str(data[2])
    usia = int(data[3])
    bb = float(data[4])
    tb = float(data[5])
    
    print("\nMenghitung BMI Anda")
    tb_bmi = tb/100
    bmi = bb/(tb_bmi**2)
        
    waktu("loading")
    print(f"BMI Anda adalah: {bmi:.2f}")
    
    if bmi < 18.5:
        saran_bmi = "Anda kekurangan berat badan. Konsultasikan dengan ahli gizi untuk rencana peningkatan berat badan."
    elif 18.5 <= bmi < 24.9:
        saran_bmi = "Berat badan Anda normal. Pertahankan gaya hidup sehat!"
    elif 24.9 <= bmi < 29.9:
        saran_bmi = "Anda kelebihan berat badan. Konsultasikan dengan ahli gizi untuk memulai program penurunan berat badan."
    else:
        saran_bmi = "Anda mengalami obesitas. Sangat disarankan untuk berkonsultasi dengan dokter untuk rencana penurunan berat badan."
      
    print(colored(f"Saran berdasarkan hasil BMI: {saran_bmi}\n", "cyan"))

    print(colored("next.....", "red"))
    time.sleep(3)
    print(colored("wait...", "yellow"))
    time.sleep(1)
    os.system('cls')
    print("loading...")
    time.sleep(2)
    print("menyiapkan pertanyaan...")
    time.sleep(1)
    os.system('cls')
    print("30%")
    time.sleep(1)
    os.system('cls')
    print("43%")
    time.sleep(1)
    os.system('cls')
    print("62%")
    time.sleep(1)
    os.system('cls')
    print("79%")
    time.sleep(2)
    os.system('cls')
    print("90%")
    time.sleep(1)
    os.system('cls')
    print("95%")
    time.sleep(1)
    os.system('cls')
    print("99%")
    time.sleep(2)
    os.system('cls')
    print("100%")
    time.sleep(1)
    os.system('cls')
    print(colored("succesfull!!!", "yellow"))
    time.sleep(2)
    os.system('cls')

    hasil_konsul = []
    for q in data_konsul[6:]:
        hasil_konsul.append(input(q).strip().lower())
        
    gigi = hasil_konsul[0]
    makan = hasil_konsul[1]
    tidur = hasil_konsul[2]
    olahraga = hasil_konsul[3]
    riwayat = hasil_konsul[4]
    merokok = hasil_konsul[5]

    print()
    cprint("HASIL KONSULTASI : ","black", "on_yellow")
    
    # gigi
    if gigi == 'y':
        saran_gigi = "[gigi] Nice! Lanjutkan kebiasaan baik Anda, karena menyikat gigi bisa mencegah penumpukan bakteri di mulut"
        saran_gigii = " "
    else:
        saran_gigi = "[gigi] Saran: Biasakan untuk menyikat gigi minimal 2x sehari, karena malas menyikat gigi tidak hanya menimbulkan rasa sakit,"
        saran_gigii = "tetapi juga menghabiskan banyak uang untuk mengatasi permasalahan tersebut."
    print(colored(saran_gigi,"cyan"), end=" ")
    print(colored(saran_gigii, "cyan"))

    # makan
    if makan == 'y':
        saran_makan = "[makan] Nice! Lanjutkan kebiasaan baik Anda, karena dengan menjaga pola makan dapat membantu memberikan dukungan terbaik"
        saran_makann = "bagi kesehatan tubuh, terutama bagi kita sebagai mahasiswa."
    else:
        saran_makan = "[makan] Saran: Biasakan makan 3x dalam sehari agar kebutuhan nutrisi yang diperlukan oleh tubuh dapat terpenuhi, "
        saran_makann = "karena tidak menjaga pola makan akan meningkatkan resiko terkena berbagai penyakit."
    print(colored(saran_makan, "cyan"), end=" ")
    print(colored(saran_makann, "cyan"))

    # tidur
    if tidur == 'y':
        saran_tidur = "[tidur] Nice! Lanjutkan kebiasaan baik Anda. Dengan tidur yang cukup dapat meningkatkan konsentrasi dan produktivitas."
    else:
        saran_tidur = "[tidur] Saran: Biasakan untuk tidur ≥ 7 jam dan konsultasikan kepada dokter jika Anda mengalami insomnia."
    print(colored(saran_tidur, "cyan"))

    # olahraga
    if olahraga == 'y':
        saran_olahraga = "[olahraga] Nice! Lanjutkan kebiasaan baik Anda. Dengan olahraga yang teratur dapat meningkatkan daya tahan tubuh,"
        saran_olahragaa = "sehingga tubuh tidak mudah terserang penyakit"
    else:
        saran_olahraga = "[olahraga] Saran: Cobalah untuk memulai rutinitas olahraga ringan seperti berjalan kaki, bersepeda, atau senam."
        saran_olahragaa = " "
    print(colored(saran_olahraga, "cyan"), end=" ")
    print(colored(saran_olahragaa, "cyan"))

    # riwayat
    if riwayat == 'y':
        saran_riwayat = "[riwayat] Saran: Sangat penting untuk melakukan pemeriksaan rutin dan mengikuti saran serta pengobatan dari dokter."
    else:
        saran_riwayat = "[riwayat] Saran: Lanjutkan gaya hidup sehat dan lakukan pemeriksaan kesehatan secara berkala untuk pencegahan."
    print(colored(saran_riwayat, "cyan"))

    # merokok
    if merokok == 'y':
        saran_merokok = "[merokok] Saran: Pertimbangkan untuk berhenti merokok. Merokok dapat meningkatkan risiko berbagai penyakit serius."
    else:
        saran_merokok = "[merokok] Nice! Hindari merokok untuk menjaga kesehatan jangka panjang."
    print(colored(saran_merokok, "cyan"))

    konsultasi(nama, nim, jurusan, usia, bb, tb, gigi, makan, tidur, olahraga, riwayat, merokok)
    
    print(colored("\nTerima kasih telah menggunakan layanan konsultasi kesehatan sederhana ini!", "green"), end=" ")
    print(colored("Ingat!! selalu konsultasikan masalah kesehatan Anda dengan profesional medis.", "green"))

# Main program
while True:
    cprint("\nMenu:", "black", "on_yellow")
    print("1. Konsultasi Kesehatan")
    print("2. Hapus Data Konsultasi")
    print("3. Tampilkan Data Konsultasi")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1/2/3/4) : ")
    
    if pilihan == "1":
        konsultasi_kesehatan()
    elif pilihan == "2":
        nim = input("Masukkan NIM konsultasi yang akan dihapus: ")
        hapus_data(nim)
    elif pilihan == "3":
        tampilkan_data()
    elif pilihan == "4":
        print(colored("\nTerima kasih telah menggunakan layanan konsultasi kesehatan.", "green"))
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

print("===========================================================================================")
print(colored("\n                              - BIODATA KELOMPOK -                              ", "yellow"))
Biodata = [["Kelompok", "Anggota Kelompok ", "Jurusan", "Mata ujian"],
           [29, "Angelina Zaskya Hulda (2310432041)", "Indah Rahmadani (2310431019)", "Matematika dan Sains Data", "UAP ADP"] ]
print(Biodata[0][0], "         :", Biodata[1][0])
print(Biodata[0][1], ":", Biodata[1][1])
print(Biodata[0][1], ":", Biodata[1][2])
print(Biodata[0][2], "          :", Biodata[1][3])
print(Biodata[0][3], "       :", Biodata[1][4])
print("\n===========================================================================================")