n = int(input("Masukkan ukuran matriks (n): "))

matriks_a = []
matriks_b = []

# Input matriks A
print("Masukkan nilai MATRIKS A:")
for i in range(n):
    baris_a = []
    for j in range(n):
        entri = int(input(f"Masukkan elemen A[{i + 1}][{j + 1}]: "))
        baris_a.append(entri)
    matriks_a.append(baris_a)

# Input matriks B
print("Masukkan nilai MATRIKS B:")
for i in range(n):
    baris_b = []
    for j in range(n):
        entri = int(input(f"Masukkan elemen B[{i + 1}][{j + 1}]: "))
        baris_b.append(entri)
    matriks_b.append(baris_b)

# Perkalian matriks A dan B
hasil_perkalian = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            hasil_perkalian[i][j] += matriks_a[i][k] * matriks_b[k][j]

print("MATRIKS C:")
for i in range(n):
    for j in range(n):
        print(hasil_perkalian[i][j], end=" ")
    print()


# Transposisi matriks A dan B
transposisi_a = [[matriks_a[j][i] for j in range(n)] for i in range(n)]
transposisi_b = [[matriks_b[j][i] for j in range(n)] for i in range(n)]

# Penjumlahan transposisi matriks A dan B
hasil_transpose = [[transposisi_a[i][j] + transposisi_b[i][j] for j in range(n)] for i in range(n)]

print("MATRIKS D:")
for i in range(n):
    for j in range(n):
        print(hasil_transpose[i][j], end=" ")
    print()       