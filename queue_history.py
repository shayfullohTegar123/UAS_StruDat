import csv
import os
from collections import deque

FILE_HISTORY = "history.csv"



def buat_history():
    if not os.path.exists(FILE_HISTORY):
        with open(FILE_HISTORY, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["NIK", "Nama"])



def tambah_history(nik, nama):

    buat_history()

    with open(FILE_HISTORY, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([nik, nama])



def baca_history():

    buat_history()

    queue = deque()

    with open(FILE_HISTORY, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            queue.append(row)

    return queue



def tampil_history():

    queue = baca_history()

    if len(queue) == 0:
        print("\nBelum ada riwayat.")
        return

    print("\n===== RIWAYAT PENAMBAHAN DATA =====")

    nomor = 1

    while len(queue) > 0:

        data = queue.popleft()

        print(f"{nomor}. {data['NIK']} - {data['Nama']}")

        nomor += 1