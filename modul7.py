def input_data(n):
    data = []
    for i in range(n):
        data.append(float(input(f"Masukkan data ke-{i+1}: ")))
    return data

def menghitung_mean(data):
    total = sum(data)
    mean = total / len(data)
    return mean

def menghitung_modus(data):
    count_dict = {}
    for num in data:
        count_dict[num] = count_dict.get(num, 0) + 1
    max_count = max(count_dict.values())
    modus = [num for num, count in count_dict.items() if count == max_count]
    return modus

def menghitung_variance(data):
    mean = menghitung_mean(data)
    kuadrat_data= [(x - mean) ** 2 for x in data]
    variance = sum(kuadrat_data) / len(data)
    return variance

def tampilkan_hasil(data):
    mean = menghitung_mean(data)
    modus = menghitung_modus(data)
    variance = menghitung_variance(data)
    
    print("Hasil Perhitungan:")
    print("|Mean     |{:.2f}|".format(mean))
    print("|Modus    | {}|".format(", ".join(map(str, modus))))
    print("|Variance |{:.2f}|".format(variance))


jumlah_data = int(input("Masukkan jumlah data: "))

data = input_data(jumlah_data)

tampilkan_hasil(data)