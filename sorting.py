from database import baca_data



def sort_nik():
    data = baca_data()

    n = len(data)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if int(data[j]["NIK"]) > int(data[j + 1]["NIK"]):
                data[j], data[j + 1] = data[j + 1], data[j]

    tampilkan(data)



def sort_nama():
    data = baca_data()

    n = len(data)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if data[j]["Nama"].lower() > data[j + 1]["Nama"].lower():
                data[j], data[j + 1] = data[j + 1], data[j]

    tampilkan(data)



def sort_umur():
    data = baca_data()

    n = len(data)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if int(data[j]["Umur"]) > int(data[j + 1]["Umur"]):
                data[j], data[j + 1] = data[j + 1], data[j]

    tampilkan(data)



def sort_gaji():
    data = baca_data()

    n = len(data)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if int(data[j]["Gaji"]) > int(data[j + 1]["Gaji"]):
                data[j], data[j + 1] = data[j + 1], data[j]

    tampilkan(data)



def tampilkan(data):

    if len(data) == 0:
        print("\nBelum ada data.")
        return

    print("=" * 85)
    print(f"{'NIK':<12}{'Nama':<20}{'Jabatan':<18}{'Divisi':<15}{'Umur':<8}{'Gaji'}")
    print("=" * 85)

    for karyawan in data:

        print(
            f"{karyawan['NIK']:<12}"
            f"{karyawan['Nama']:<20}"
            f"{karyawan['Jabatan']:<18}"
            f"{karyawan['Divisi']:<15}"
            f"{karyawan['Umur']:<8}"
            f"{karyawan['Gaji']}"
        )

    print("=" * 85)



def menu_sorting():

    while True:

        print("\n===== MENU SORTING =====")
        print("1. Urutkan berdasarkan NIK")
        print("2. Urutkan berdasarkan Nama")
        print("3. Urutkan berdasarkan Umur")
        print("4. Urutkan berdasarkan Gaji")
        print("5. Kembali")

        pilih = input("Pilih menu : ")

        if pilih == "1":
            sort_nik()

        elif pilih == "2":
            sort_nama()

        elif pilih == "3":
            sort_umur()

        elif pilih == "4":
            sort_gaji()

        elif pilih == "5":
            break

        else:
            print("Pilihan tidak tersedia.")