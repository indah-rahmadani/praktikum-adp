total_angka = 80
angka_perbaris = 8
counter = 1

for i in range (total_angka // angka_perbaris) :
    for j in range(angka_perbaris):
        print(counter,end=" ")
        if counter % 4 == 0 :
            print("DOR",end=" ")
        counter += 1
    print()
