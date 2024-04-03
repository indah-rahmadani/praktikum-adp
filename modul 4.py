print("--------------------------------------")
print("=SELAMAT DATANG DI TOKO INDAH BAHAGIA=")
print("--------------------------------------")
print("toko kami lagi ada promo untuk beberapa barang :")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("< kode A untuk kotak nasi   <")
print("< kode B untuk botol minum  <")
print("< kode C untuk termos       <")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

daftar_barang = {
    "A": {"nama": "kotak nasi", "harga": 35000},
    "B": {"nama": "Botol minum", "harga": 45000},
    "C": {"nama": "termos", "harga": 65000}
}


belanja = []
while True:
    kode_barang = input("Masukkan kode barang (A/B/C) atau ketik 'selesai' untuk mengakhiri: ").upper()
    if kode_barang == "SELESAI":
        break
    elif kode_barang not in daftar_barang:
        print("Kode barang tidak valid.")
        continue
    else:
        jumlah =int(input("Masukkan jumlah barang yang ingin dibeli: "))
        belanja.append({"kode": kode_barang, "jumlah": jumlah})

# Menghitung total belanja sebelum diskon
total_harga = 0
for item in belanja:
    harga_barang = daftar_barang[item["kode"]]["harga"]
    total_harga += harga_barang * item["jumlah"]

# Diskon potongan harga untuk barang tertentu
for item in belanja:
    if item["kode"] == "A" and item["jumlah"] > 5:
        diskon_barang = 0.25 * daftar_barang["A"]["harga"] * item["jumlah"]
        total_harga -= diskon_barang

# Diskon potongan harga untuk total belanja
if total_harga > 400000:
    diskon_total = 0.2 * total_harga
    total_harga -= diskon_total

# Output total belanja setelah diskon
print("Total belanja Anda setelah diskon adalah: Rp", total_harga)
