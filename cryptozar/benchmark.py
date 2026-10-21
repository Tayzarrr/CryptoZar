# CryptoZar — benchmark
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.konfigurasi import ALFABET  # Mengimpor komponen yang dibutuhkan dari cryptozar.konfigurasi.
from cryptozar.algoritma.caesar import caesar_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.caesar.
from cryptozar.algoritma.caesar import caesar_enkripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.caesar.
import csv  # Memuat pustaka csv.
from cryptozar.algoritma.hill import hill_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.hill.
from cryptozar.algoritma.hill import hill_enkripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.hill.
from cryptozar.algoritma.hill import hill_parse_kunci  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.hill.
from cryptozar.algoritma.stream import keystream_lcg  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.stream.
from cryptozar.algoritma.otp import otp_buat_kunci  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.otp.
from cryptozar.algoritma.playfair import playfair_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.playfair.
from cryptozar.algoritma.playfair import playfair_enkripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.playfair.
import random  # Memuat pustaka random.
import statistics  # Memuat pustaka statistics.
import time  # Memuat pustaka time.
import tracemalloc  # Memuat pustaka tracemalloc.
from cryptozar.algoritma.vigenere import vigenere_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.vigenere.
from cryptozar.algoritma.vigenere import vigenere_enkripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.vigenere.
from cryptozar.algoritma.otp import xor_bytes  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.otp.


def median_waktu_ms(fn, ulang):  # Mendefinisikan fungsi median_waktu_ms dengan parameter yang tertulis.
    """Jalankan fn sebanyak 'ulang' kali; kembalikan (median ms, hasil terakhir)."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    waktu = []  # Menghitung atau menyiapkan [], lalu menyimpannya pada waktu.
    hasil = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada hasil.
    for _ in range(ulang):  # Mengulangi proses untuk _ in range(ulang).
        t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
        hasil = fn()  # Menghitung atau menyiapkan fn(), lalu menyimpannya pada hasil.
        waktu.append((time.perf_counter() - t0) * 1000)  # Memanggil waktu.append untuk menambahkan elemen ke daftar.
    return (statistics.median(waktu), hasil)  # Mengembalikan (statistics.median(waktu), hasil).


def puncak_memori_kib(fn):  # Mendefinisikan fungsi puncak_memori_kib dengan parameter yang tertulis.
    tracemalloc.start()  # Memulai pencatatan alokasi memori Python untuk pengukuran terpisah.
    try:  # Memulai operasi yang dapat menghasilkan exception.
        fn()  # Memanggil fn untuk menjalankan operasi dengan argumen yang diberikan.
        _, puncak = tracemalloc.get_traced_memory()  # Menghitung atau menyiapkan tracemalloc.get_traced_memory(), lalu menyimpannya pada (_, puncak).
    finally:  # Menjalankan pembersihan meskipun terjadi exception.
        tracemalloc.stop()  # Menghentikan pencatatan memori setelah pengukuran selesai.
    return puncak / 1024  # Mengembalikan puncak / 1024.


def ukur_satu_ukuran(n, ulang):  # Mendefinisikan fungsi ukur_satu_ukuran dengan parameter yang tertulis.
    """Ukur 7 konfigurasi algoritma untuk data berukuran n karakter/byte."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    rng = random.Random(2026)  # Menghitung atau menyiapkan random.Random(2026), lalu menyimpannya pada rng.
    teks = "".join(rng.choices(ALFABET, k=n))  # Menghitung atau menyiapkan ''.join(rng.choices(ALFABET, k=n)), lalu menyimpannya pada teks.
    data = teks.encode("ascii")  # Menghitung atau menyiapkan teks.encode('ascii'), lalu menyimpannya pada data.
    hasil = []  # Menghitung atau menyiapkan [], lalu menyimpannya pada hasil.

    def baris(nama, gen_ms, proses_ms, enk_ms, dek_ms, memori, kunci_byte, ct_byte):  # Mendefinisikan fungsi baris dengan parameter yang tertulis.
        hasil.append(  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
            {  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
                "algoritma": nama,  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
                "ukuran_data_byte": n,  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
                "gen_kunci_ms": round(gen_ms, 4),  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
                "proses_ms": round(proses_ms, 4),  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
                "enkripsi_total_ms": round(enk_ms, 4),  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
                "dekripsi_total_ms": round(dek_ms, 4),  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
                "memori_puncak_kib": round(memori, 2),  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
                "ukuran_kunci_byte": kunci_byte,  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
                "ukuran_ciphertext_byte": ct_byte,  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
            }  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

    klasik = [  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
        ("Caesar", lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1),  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
        (  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
            "Vigenere",  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
            lambda: vigenere_enkripsi(teks, "SANDI"),  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
            lambda c: vigenere_dekripsi(c, "SANDI"),  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
            5,  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
        ),  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        (  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
            "Playfair",  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
            lambda: playfair_enkripsi(teks, "MONARCHY"),  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
            lambda c: playfair_dekripsi(c, "MONARCHY"),  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
            8,  # Menghitung atau menyiapkan [('Caesar', lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1), ('Vigenere', lambda: vigene, lalu menyimpannya pada klasik.
        ),  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    ]  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    M2 = hill_parse_kunci("3 3 2 5")  # Menghitung atau menyiapkan hill_parse_kunci('3 3 2 5'), lalu menyimpannya pada M2.
    M3 = hill_parse_kunci("6 24 1 13 16 10 20 17 15")  # Menghitung atau menyiapkan hill_parse_kunci('6 24 1 13 16 10 20 17 15'), lalu menyimpannya pada M3.
    klasik.append(  # Memanggil klasik.append untuk menambahkan elemen ke daftar.
        ("Hill 2x2", lambda: hill_enkripsi(teks, M2), lambda c: hill_dekripsi(c, M2), 4)  # Memanggil klasik.append untuk menambahkan elemen ke daftar.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    klasik.append(  # Memanggil klasik.append untuk menambahkan elemen ke daftar.
        ("Hill 3x3", lambda: hill_enkripsi(teks, M3), lambda c: hill_dekripsi(c, M3), 9)  # Memanggil klasik.append untuk menambahkan elemen ke daftar.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    for nama, enk, dek, kb in klasik:  # Mengulangi proses untuk nama, enk, dek, kb in klasik.
        t_enk, c = median_waktu_ms(enk, ulang)  # Menghitung atau menyiapkan median_waktu_ms(enk, ulang), lalu menyimpannya pada (t_enk, c).
        t_dek, _ = median_waktu_ms(lambda: dek(c), ulang)  # Menghitung atau menyiapkan median_waktu_ms(lambda: dek(c), ulang), lalu menyimpannya pada (t_dek, _).
        mem = puncak_memori_kib(enk)  # Menghitung atau menyiapkan puncak_memori_kib(enk), lalu menyimpannya pada mem.
        baris(nama, 0.0, t_enk, t_enk, t_dek, mem, kb, len(c))  # Memanggil baris untuk menjalankan operasi dengan argumen yang diberikan.
    t_gen, pad = median_waktu_ms(lambda: otp_buat_kunci(n), ulang)  # Menghitung atau menyiapkan median_waktu_ms(lambda: otp_buat_kunci(n), ulang), lalu menyimpannya pada (t_gen, pad).
    t_xor, c = median_waktu_ms(lambda: xor_bytes(data, pad), ulang)  # Menghitung atau menyiapkan median_waktu_ms(lambda: xor_bytes(data, pad), ulang), lalu menyimpannya pada (t_xor, c).
    t_dek, _ = median_waktu_ms(lambda: xor_bytes(c, pad), ulang)  # Menghitung atau menyiapkan median_waktu_ms(lambda: xor_bytes(c, pad), ulang), lalu menyimpannya pada (t_dek, _).
    mem = puncak_memori_kib(lambda: xor_bytes(data, otp_buat_kunci(n)))  # Menghitung atau menyiapkan puncak_memori_kib(lambda: xor_bytes(data, otp_buat_kunci(n))), lalu menyimpannya pada mem.
    baris("OTP", t_gen, t_xor, t_gen + t_xor, t_dek, mem, n, 2 * n)  # Memanggil baris untuk menjalankan operasi dengan argumen yang diberikan.
    t_gen, s = median_waktu_ms(lambda: keystream_lcg(77, n), ulang)  # Menghitung atau menyiapkan median_waktu_ms(lambda: keystream_lcg(77, n), ulang), lalu menyimpannya pada (t_gen, s).
    t_xor, c = median_waktu_ms(lambda: xor_bytes(data, s), ulang)  # Menghitung atau menyiapkan median_waktu_ms(lambda: xor_bytes(data, s), ulang), lalu menyimpannya pada (t_xor, c).
    mem = puncak_memori_kib(lambda: xor_bytes(data, keystream_lcg(77, n)))  # Menghitung atau menyiapkan puncak_memori_kib(lambda: xor_bytes(data, keystream_lcg(77, n))), lalu menyimpannya pada mem.
    baris("Stream (LCG)", t_gen, t_xor, t_gen + t_xor, t_gen + t_xor, mem, 1, 2 * n)  # Memanggil baris untuk menjalankan operasi dengan argumen yang diberikan.
    return hasil  # Mengembalikan hasil.


def tampilkan_tabel_bench(baris_hasil):  # Mendefinisikan fungsi tampilkan_tabel_bench dengan parameter yang tertulis.
    kepala = [  # Menghitung atau menyiapkan ['Algoritma', 'Ukuran(B)', 'Gen(ms)', 'Proses(ms)', 'Enk(ms)', 'Dek(ms)', 'Mem(KiB)', 'Kunci(B)', 'Cipher(B)'], lalu menyimpannya pada kepala.
        "Algoritma",  # Menghitung atau menyiapkan ['Algoritma', 'Ukuran(B)', 'Gen(ms)', 'Proses(ms)', 'Enk(ms)', 'Dek(ms)', 'Mem(KiB)', 'Kunci(B)', 'Cipher(B)'], lalu menyimpannya pada kepala.
        "Ukuran(B)",  # Menghitung atau menyiapkan ['Algoritma', 'Ukuran(B)', 'Gen(ms)', 'Proses(ms)', 'Enk(ms)', 'Dek(ms)', 'Mem(KiB)', 'Kunci(B)', 'Cipher(B)'], lalu menyimpannya pada kepala.
        "Gen(ms)",  # Menghitung atau menyiapkan ['Algoritma', 'Ukuran(B)', 'Gen(ms)', 'Proses(ms)', 'Enk(ms)', 'Dek(ms)', 'Mem(KiB)', 'Kunci(B)', 'Cipher(B)'], lalu menyimpannya pada kepala.
        "Proses(ms)",  # Menghitung atau menyiapkan ['Algoritma', 'Ukuran(B)', 'Gen(ms)', 'Proses(ms)', 'Enk(ms)', 'Dek(ms)', 'Mem(KiB)', 'Kunci(B)', 'Cipher(B)'], lalu menyimpannya pada kepala.
        "Enk(ms)",  # Menghitung atau menyiapkan ['Algoritma', 'Ukuran(B)', 'Gen(ms)', 'Proses(ms)', 'Enk(ms)', 'Dek(ms)', 'Mem(KiB)', 'Kunci(B)', 'Cipher(B)'], lalu menyimpannya pada kepala.
        "Dek(ms)",  # Menghitung atau menyiapkan ['Algoritma', 'Ukuran(B)', 'Gen(ms)', 'Proses(ms)', 'Enk(ms)', 'Dek(ms)', 'Mem(KiB)', 'Kunci(B)', 'Cipher(B)'], lalu menyimpannya pada kepala.
        "Mem(KiB)",  # Menghitung atau menyiapkan ['Algoritma', 'Ukuran(B)', 'Gen(ms)', 'Proses(ms)', 'Enk(ms)', 'Dek(ms)', 'Mem(KiB)', 'Kunci(B)', 'Cipher(B)'], lalu menyimpannya pada kepala.
        "Kunci(B)",  # Menghitung atau menyiapkan ['Algoritma', 'Ukuran(B)', 'Gen(ms)', 'Proses(ms)', 'Enk(ms)', 'Dek(ms)', 'Mem(KiB)', 'Kunci(B)', 'Cipher(B)'], lalu menyimpannya pada kepala.
        "Cipher(B)",  # Menghitung atau menyiapkan ['Algoritma', 'Ukuran(B)', 'Gen(ms)', 'Proses(ms)', 'Enk(ms)', 'Dek(ms)', 'Mem(KiB)', 'Kunci(B)', 'Cipher(B)'], lalu menyimpannya pada kepala.
    ]  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    kunci = [  # Menghitung atau menyiapkan ['algoritma', 'ukuran_data_byte', 'gen_kunci_ms', 'proses_ms', 'enkripsi_total_ms', 'dekripsi_total_ms', 'memo, lalu menyimpannya pada kunci.
        "algoritma",  # Menghitung atau menyiapkan ['algoritma', 'ukuran_data_byte', 'gen_kunci_ms', 'proses_ms', 'enkripsi_total_ms', 'dekripsi_total_ms', 'memo, lalu menyimpannya pada kunci.
        "ukuran_data_byte",  # Menghitung atau menyiapkan ['algoritma', 'ukuran_data_byte', 'gen_kunci_ms', 'proses_ms', 'enkripsi_total_ms', 'dekripsi_total_ms', 'memo, lalu menyimpannya pada kunci.
        "gen_kunci_ms",  # Menghitung atau menyiapkan ['algoritma', 'ukuran_data_byte', 'gen_kunci_ms', 'proses_ms', 'enkripsi_total_ms', 'dekripsi_total_ms', 'memo, lalu menyimpannya pada kunci.
        "proses_ms",  # Menghitung atau menyiapkan ['algoritma', 'ukuran_data_byte', 'gen_kunci_ms', 'proses_ms', 'enkripsi_total_ms', 'dekripsi_total_ms', 'memo, lalu menyimpannya pada kunci.
        "enkripsi_total_ms",  # Menghitung atau menyiapkan ['algoritma', 'ukuran_data_byte', 'gen_kunci_ms', 'proses_ms', 'enkripsi_total_ms', 'dekripsi_total_ms', 'memo, lalu menyimpannya pada kunci.
        "dekripsi_total_ms",  # Menghitung atau menyiapkan ['algoritma', 'ukuran_data_byte', 'gen_kunci_ms', 'proses_ms', 'enkripsi_total_ms', 'dekripsi_total_ms', 'memo, lalu menyimpannya pada kunci.
        "memori_puncak_kib",  # Menghitung atau menyiapkan ['algoritma', 'ukuran_data_byte', 'gen_kunci_ms', 'proses_ms', 'enkripsi_total_ms', 'dekripsi_total_ms', 'memo, lalu menyimpannya pada kunci.
        "ukuran_kunci_byte",  # Menghitung atau menyiapkan ['algoritma', 'ukuran_data_byte', 'gen_kunci_ms', 'proses_ms', 'enkripsi_total_ms', 'dekripsi_total_ms', 'memo, lalu menyimpannya pada kunci.
        "ukuran_ciphertext_byte",  # Menghitung atau menyiapkan ['algoritma', 'ukuran_data_byte', 'gen_kunci_ms', 'proses_ms', 'enkripsi_total_ms', 'dekripsi_total_ms', 'memo, lalu menyimpannya pada kunci.
    ]  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    lebar = [14, 10, 10, 11, 10, 10, 10, 9, 10]  # Menghitung atau menyiapkan [14, 10, 10, 11, 10, 10, 10, 9, 10], lalu menyimpannya pada lebar.
    print("".join((h.ljust(w) for h, w in zip(kepala, lebar))))  # Memanggil print untuk menampilkan informasi.
    print("-" * sum(lebar))  # Memanggil print untuk menampilkan informasi.
    for b in baris_hasil:  # Mengulangi proses untuk b in baris_hasil.
        print("".join((str(b[k]).ljust(w) for k, w in zip(kunci, lebar))))  # Memanggil print untuk menampilkan informasi.


def ukur_beban_komputasi(ukuran=None, ulang=5, csv_path="hasil_beban_komputasi.csv"):  # Mendefinisikan fungsi ukur_beban_komputasi dengan parameter yang tertulis.
    ukuran = ukuran or [1024, 10 * 1024, 100 * 1024]  # Menghitung atau menyiapkan ukuran or [1024, 10 * 1024, 100 * 1024], lalu menyimpannya pada ukuran.
    semua = []  # Menghitung atau menyiapkan [], lalu menyimpannya pada semua.
    print(f"\nPengukuran beban komputasi (median dari {ulang} kali ulang, time.perf_counter)")  # Memanggil print untuk menampilkan informasi.
    print("Memori diukur terpisah memakai tracemalloc agar tidak memengaruhi waktu.")  # Memanggil print untuk menampilkan informasi.
    for n in ukuran:  # Mengulangi proses untuk n in ukuran.
        print(f"\n>>> Ukuran data: {n} byte ({n / 1024:g} KiB)")  # Memanggil print untuk menampilkan informasi.
        b = ukur_satu_ukuran(n, ulang)  # Menghitung atau menyiapkan ukur_satu_ukuran(n, ulang), lalu menyimpannya pada b.
        tampilkan_tabel_bench(b)  # Memanggil tampilkan_tabel_bench untuk menjalankan operasi dengan argumen yang diberikan.
        semua.extend(b)  # Memanggil semua.extend untuk menjalankan operasi dengan argumen yang diberikan.
    with open(csv_path, "w", encoding="utf-8", newline="") as f:  # Mengelola sumber daya atau konteks open(csv_path, "w", encoding="utf-8", newline="") as f.
        w = csv.DictWriter(f, fieldnames=list(semua[0].keys()))  # Menghitung atau menyiapkan csv.DictWriter(f, fieldnames=list(semua[0].keys())), lalu menyimpannya pada w.
        w.writeheader()  # Memanggil w.writeheader untuk menjalankan operasi dengan argumen yang diberikan.
        w.writerows(semua)  # Memanggil w.writerows untuk menjalankan operasi dengan argumen yang diberikan.
    print("\nKeterangan kolom:")  # Memanggil print untuk menampilkan informasi.
    print(  # Memanggil print untuk menampilkan informasi.
        "  Gen     : waktu membangkitkan pad (OTP) atau keystream (Stream); 0 untuk cipher klasik"  # Memanggil print untuk menampilkan informasi.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    print("  Proses  : waktu inti enkripsi (XOR atau substitusi/transposisi) tanpa Gen")  # Memanggil print untuk menampilkan informasi.
    print("  Enk     : total enkripsi = Gen + Proses")  # Memanggil print untuk menampilkan informasi.
    print("  Dek     : total dekripsi (OTP: hanya XOR karena pad sudah dimiliki penerima;")  # Memanggil print untuk menampilkan informasi.
    print("            Stream: penerima membangkitkan keystream lagi lalu XOR)")  # Memanggil print untuk menampilkan informasi.
    print("  Mem     : puncak memori Python saat enkripsi")  # Memanggil print untuk menampilkan informasi.
    print("  Kunci   : ukuran kunci (OTP = sepanjang pesan; Stream = 1 byte seed)")  # Memanggil print untuk menampilkan informasi.
    print(  # Memanggil print untuk menampilkan informasi.
        "  Cipher  : ukuran ciphertext yang disimpan (OTP/Stream disimpan hex = 2x ukuran data)"  # Memanggil print untuk menampilkan informasi.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    print("\nKompleksitas teoretis (n = jumlah karakter/byte, k = ukuran matriks Hill):")  # Memanggil print untuk menampilkan informasi.
    print("  Caesar    O(n)       Vigenere  O(n)       Playfair  O(n)")  # Memanggil print untuk menampilkan informasi.
    print("  Hill      O(n.k^2)   OTP       O(n)       Stream    O(n)")  # Memanggil print untuk menampilkan informasi.
    print(f"\nTabel disimpan ke: {csv_path}")  # Memanggil print untuk menampilkan informasi.


def menu_benchmark():  # Mendefinisikan fungsi menu_benchmark dengan parameter yang tertulis.
    tambah = input("Tambahkan ukuran 1 MiB? (lebih lama) [y/N]: ").strip().lower() == "y"  # Menghitung atau menyiapkan input('Tambahkan ukuran 1 MiB? (lebih lama) [y/N]: ').strip().lower() == 'y', lalu menyimpannya pada tambah.
    ukuran = [1024, 10 * 1024, 100 * 1024] + ([1024 * 1024] if tambah else [])  # Menghitung atau menyiapkan [1024, 10 * 1024, 100 * 1024] + ([1024 * 1024] if tambah else []), lalu menyimpannya pada ukuran.
    ukur_beban_komputasi(ukuran)  # Memanggil ukur_beban_komputasi untuk menjalankan operasi dengan argumen yang diberikan.
