from database import baca_data



def buat_hashmap():
    data = baca_data()

    hashmap = {}

    for karyawan in data:
        hashmap[karyawan["NIK"]] = karyawan

    return hashmap



def cari_nik():

    hashmap = buat_hashmap()

    nik = input("Masukkan NIK : ")

    if nik in hashmap:

        karyawan = hashmap[nik]

        print("\n===== DATA KARYAWAN =====")
        print(f"NIK      : {karyawan['NIK']}")
        print(f"Nama     : {karyawan['Nama']}")
        print(f"Jabatan  : {karyawan['Jabatan']}")
        print(f"Divisi   : {karyawan['Divisi']}")
        print(f"Umur     : {karyawan['Umur']}")
        print(f"Gaji     : {karyawan['Gaji']}")

    else:
        print("\nNIK tidak ditemukan.")


def cari_nama():

    data = baca_data()

    nama = input("Masukkan Nama : ").lower()

    ditemukan = False

    print("\n===== HASIL PENCARIAN =====")

    for karyawan in data:

        if nama in karyawan["Nama"].lower():

            ditemukan = True

            print("-----------------------------")
            print(f"NIK      : {karyawan['NIK']}")
            print(f"Nama     : {karyawan['Nama']}")
            print(f"Jabatan  : {karyawan['Jabatan']}")
            print(f"Divisi   : {karyawan['Divisi']}")
            print(f"Umur     : {karyawan['Umur']}")
            print(f"Gaji     : {karyawan['Gaji']}")

    if not ditemukan:
        print("Data tidak ditemukan.")