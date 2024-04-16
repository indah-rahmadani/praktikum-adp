print("TUGAS MODUL 5 (ARRAY)")
print("INDAH RAHMADANI")
print("---------------------")

nilai_x = list(range(-10, 11))
nilai_f = []

print("| x   | f(x)   |")
print("|-----|--------|")
for x in nilai_x:
    if x > 0:
        fx = x**2 + 2*x
    elif x < 0:
        fx = 1/x
    else:
        fx = 10
    nilai_f.append(fx)
    print(f"| {x} |{fx:.2f}|")