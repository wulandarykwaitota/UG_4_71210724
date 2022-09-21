import json

with open("karyawan.json","r") as datafile:
    data =json.load(datafile)

    temp = dict()
    jumlah = int(input("Masukkan jumlah karyawan baru : "))

    for i in range(jumlah):
        nama = input("Masukkan nama : ")
        alamat = input("Masukkan alamat : ")
        kolega = []

        x_kolega = int(input("Masukkan jumlah kolega : "))
        for j in range (x_kolega):
            kolega_i = input("Masukkan kolega ke-{} : " .format(j+1))
            kolega.append(kolega_i)

        print("=== Data berhasil ditambahkan ===")
        print()

        temp[nama] = [{"alamat" : alamat, "kolega" : kolega}]

    data.update(temp)

with open("karyawan.json", "w") as datafile:
    json.dump(data, datafile)