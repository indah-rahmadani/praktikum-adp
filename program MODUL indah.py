print("daftar paket yang tersedia:")
print("___________________________")

harga_paket = 0
paket_A = 25000
paket_B = 30000
paket_C = 45000

print("paket A: " + str(paket_A))
print("paket B: " + str(paket_B))
print("paket C: " + str(paket_C))
mau_belanja  = input("apakah anda ingin belanja? (y/n): ")

while mau_belanja == "y" :	  
	paket = input("paket yang ingin anda beli : ")
	if (paket == "A") :
		harga_makanan = 25000
	elif(paket == "B") :
		harga_makanan= 30000
	else :
		harga_makanan = 45000
	harga_paket = harga_paket + harga_makanan
	mau_belanja  = input("apakah anda ingin belanja? (y/n): ")
		
if mau_belanja == "n" :
	print("total pesanan anda saat ini : " + str(harga_paket))	
	
jarak = float(input("jarak rumah anda(dalam km) : "))
if jarak < 0.5 :
	  ongkir = 0
elif 0.5 < jarak < 1.5 :
	  ongkir = 10000
else :
	  ongkir = 20000
	  
biaya_total = harga_paket + ongkir
print("biaya total yang harus dibayar: Rp" + str(biaya_total))