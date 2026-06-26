from database import buat_database

from crud import (
    tambah_data,
    lihat_data,
    update_data,
    hapus_data
)

from search import (
    cari_nik,
    cari_nama
)

from sorting import menu_sorting

from queue_history import tampil_history

from statistik import tampil_statistik


def tampil_menu():

    print("\n")
    print("=" * 55)
    print("      SISTEM MANAJEMEN NIK KARYAWAN")
    print("=" * 55)
    print("1. Tambah Data Karyawan")
    print("2. Lihat Semua Data")
    print("3. Cari Berdasarkan NIK")
    print("4. Cari Berdasarkan Nama")
    print("5. Update Data")
    print("6. Hapus Data")
    print("7. Sorting Data")
    print("8. Riwayat Penambahan")
    print("9. Statistik")
    print("10. Keluar")
    print("=" * 55)


def main():

    buat_database()

    while True:

        tampil_menu()

        pilihan = input("Pilih Menu : ")

        if pilihan == "1":
            tambah_data()

        elif pilihan == "2":
            lihat_data()

        elif pilihan == "3":
            cari_nik()

        elif pilihan == "4":
            cari_nama()

        elif pilihan == "5":
            update_data()

        elif pilihan == "6":
            hapus_data()

        elif pilihan == "7":
            menu_sorting()

        elif pilihan == "8":
            tampil_history()

        elif pilihan == "9":
            tampil_statistik()

        elif pilihan == "10":
            print("\nTerima kasih telah menggunakan aplikasi.")
            break

        else:
            print("\nPilihan tidak tersedia!")


if __name__ == "__main__":
    main()