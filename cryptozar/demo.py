# CryptoZar — demo
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.konfigurasi import ALGORITMA  # Mengimpor komponen yang dibutuhkan dari cryptozar.konfigurasi.
from cryptozar.layanan_file import dekripsi_file  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_file.
from cryptozar.layanan_file import enkripsi_file  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_file.
from cryptozar.utilitas import normalisasi  # Mengimpor komponen yang dibutuhkan dari cryptozar.utilitas.


def demo_belajar_kriptografi():  # Mendefinisikan fungsi demo_belajar_kriptografi dengan parameter yang tertulis.
    pesan = "BELAJAR KRIPTOGRAFI"  # Menghitung atau menyiapkan 'BELAJAR KRIPTOGRAFI', lalu menyimpannya pada pesan.
    path = "pesan_demo.txt"  # Menghitung atau menyiapkan 'pesan_demo.txt', lalu menyimpannya pada path.
    with open(path, "w", encoding="utf-8", newline="") as f:  # Mengelola sumber daya atau konteks open(path, "w", encoding="utf-8", newline="") as f.
        f.write(pesan)  # Memanggil f.write untuk menulis data ke file atau aliran.
    print(  # Memanggil print untuk menampilkan informasi.
        f"""\nPlaintext : "{pesan}"  ({len(pesan.encode('utf-8'))} byte, {len(normalisasi(pesan))} huruf A-Z)"""  # Memanggil print untuk menampilkan informasi.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    print(f"File      : {path}")  # Memanggil print untuk menampilkan informasi.
    kunci_demo = {"1": "3", "2": "SANDI", "3": "MONARCHY", "4": "3 3 2 5", "5": None, "6": "77"}  # Menghitung atau menyiapkan {'1': '3', '2': 'SANDI', '3': 'MONARCHY', '4': '3 3 2 5', '5': None, '6': '77'}, lalu menyimpannya pada kunci_demo.
    for kode in ("1", "2", "3", "4", "5", "6"):  # Mengulangi proses untuk kode in ("1", "2", "3", "4", "5", "6").
        try:  # Memulai operasi yang dapat menghasilkan exception.
            e = enkripsi_file(kode, path, kunci_demo[kode])  # Menghitung atau menyiapkan enkripsi_file(kode, path, kunci_demo[kode]), lalu menyimpannya pada e.
            kunci_dek = e["kunci_path"] if kode == "5" else kunci_demo[kode]  # Menghitung atau menyiapkan e['kunci_path'] if kode == '5' else kunci_demo[kode], lalu menyimpannya pada kunci_dek.
            d = dekripsi_file(kode, e["out_path"], kunci_dek)  # Menghitung atau menyiapkan dekripsi_file(kode, e['out_path'], kunci_dek), lalu menyimpannya pada d.
        except (ValueError, OSError) as err:  # Menangani exception (ValueError, OSError) as err.
            print(f"\n[{ALGORITMA[kode][0]}] gagal: {err}")  # Memanggil print untuk menampilkan informasi.
            continue  # Melanjutkan ke iterasi berikutnya.
        print("\n" + "=" * 64)  # Memanggil print untuk menampilkan informasi.
        print(f"{e['algoritma']}")  # Memanggil print untuk menampilkan informasi.
        print("  Kunci       :", e["kunci_tampil"])  # Memanggil print untuk menampilkan informasi.
        if "keystream_tampil" in e:  # Menjalankan blok hanya jika "keystream_tampil" in e.
            print("  Keystream   :", e["keystream_tampil"])  # Memanggil print untuk menampilkan informasi.
        print("  Ciphertext  :", e["cipher_tampil"])  # Memanggil print untuk menampilkan informasi.
        print("  Dekripsi    :", d["plain_tampil"])  # Memanggil print untuk menampilkan informasi.
        print(  # Memanggil print untuk menampilkan informasi.
            f"  Waktu       : enkripsi {e['waktu_ms']:.4f} ms | dekripsi {d['waktu_ms']:.4f} ms"  # Memanggil print untuk menampilkan informasi.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        print("  File        :", e["out_path"])  # Memanggil print untuk menampilkan informasi.
    print("\nSelesai. Semua file hasil ada di folder yang sama dengan program.")  # Memanggil print untuk menampilkan informasi.
