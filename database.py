import csv
import os

FILE_NAME = "karyawan.csv"

HEADER = [
    "NIK",
    "Nama",
    "Jabatan",
    "Divisi",
    "Umur",
    "Gaji"
]


def buat_database():
    """
    Membuat file CSV jika belum ada.
    """
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADER)


def baca_data():
    """
    Membaca seluruh data dari CSV.
    Mengembalikan list of dictionary.
    """

    buat_database()

    data = []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data


def simpan_data(data):
    """
    Menyimpan seluruh data ke CSV.
    """

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=HEADER)

        writer.writeheader()

        writer.writerows(data)