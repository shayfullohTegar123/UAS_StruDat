from queue_history import tambah_history
from database import baca_data, simpan_data



def tambah_data():
    data = baca_data()

    nik = input("Masukkan NIK      : ")

    for karyawan in data:
        if karyawan["NIK"] == nik:
            print("\nNIK sudah terdaftar!")
            return

    nama = input("Masukkan Nama     : ")
    jabatan = input("Masukkan Jabatan  : ")
    divisi = input("Masukkan Divisi   : ")
    umur = input("Masukkan Umur     : ")
    gaji = input("Masukkan Gaji     : ")

    data.append({
        "NIK": nik,
        "Nama": nama,
        "Jabatan": jabatan,
        "Divisi": divisi,
        "Umur": umur,
        "Gaji": gaji
    })

    simpan_data(data)
    tambah_history(nik, nama)

    print("\nData berhasil ditambahkan!")



def lihat_data():
    data = baca_data()

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



def update_data():
    data = baca_data()

    nik = input("Masukkan NIK yang akan diupdate : ")

    for karyawan in data:

        if karyawan["NIK"] == nik:

            print("\nData ditemukan!")

            print("Tekan ENTER jika tidak ingin mengubah data.\n")

            nama = input(f"Nama ({karyawan['Nama']}) : ")
            jabatan = input(f"Jabatan ({karyawan['Jabatan']}) : ")
            divisi = input(f"Divisi ({karyawan['Divisi']}) : ")
            umur = input(f"Umur ({karyawan['Umur']}) : ")
            gaji = input(f"Gaji ({karyawan['Gaji']}) : ")

            if nama != "":
                karyawan["Nama"] = nama

            if jabatan != "":
                karyawan["Jabatan"] = jabatan

            if divisi != "":
                karyawan["Divisi"] = divisi

            if umur != "":
                karyawan["Umur"] = umur

            if gaji != "":
                karyawan["Gaji"] = gaji

            simpan_data(data)

            print("\nData berhasil diupdate!")

            return

    print("\nNIK tidak ditemukan.")



def hapus_data():
    data = baca_data()

    nik = input("Masukkan NIK yang akan dihapus : ")

    for karyawan in data:

        if karyawan["NIK"] == nik:

            konfirmasi = input(
                f"Yakin ingin menghapus data {karyawan['Nama']}? (Y/T): "
            )

            if konfirmasi.upper() == "Y":

                data.remove(karyawan)

                simpan_data(data)

                print("\nData berhasil dihapus!")

            else:
                print("\nPenghapusan dibatalkan.")

            return

    print("\nNIK tidak ditemukan.")