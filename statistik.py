from database import baca_data


def tampil_statistik():

    data = baca_data()

    if len(data) == 0:
        print("\nBelum ada data karyawan.")
        return

    jumlah_karyawan = len(data)
    total_gaji = 0
    total_umur = 0

    divisi = {}

    for karyawan in data:

        total_gaji += int(karyawan["Gaji"])
        total_umur += int(karyawan["Umur"])

        nama_divisi = karyawan["Divisi"]

        if nama_divisi in divisi:
            divisi[nama_divisi] += 1
        else:
            divisi[nama_divisi] = 1

    rata_gaji = total_gaji / jumlah_karyawan
    rata_umur = total_umur / jumlah_karyawan

    print("\n" + "=" * 40)
    print("      STATISTIK KARYAWAN")
    print("=" * 40)

    print(f"Jumlah Karyawan   : {jumlah_karyawan}")
    print(f"Total Gaji        : Rp {total_gaji:,}")
    print(f"Rata-rata Gaji    : Rp {rata_gaji:,.0f}")
    print(f"Rata-rata Umur    : {rata_umur:.1f} Tahun")

    print("\nJumlah Karyawan per Divisi")

    for nama_divisi, jumlah in divisi.items():
        print(f"- {nama_divisi:<15}: {jumlah}")

    print("=" * 40)