# CryptoZar — file_io
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
import os  # Memuat pustaka os.


def baca_teks(path):  # Mendefinisikan fungsi baca_teks dengan parameter yang tertulis.
    with open(path, "r", encoding="utf-8-sig") as f:  # Mengelola sumber daya atau konteks open(path, "r", encoding="utf-8-sig") as f.
        return f.read()  # Mengembalikan f.read().


def baca_bytes(path):  # Mendefinisikan fungsi baca_bytes dengan parameter yang tertulis.
    with open(path, "rb") as f:  # Mengelola sumber daya atau konteks open(path, "rb") as f.
        return f.read()  # Mengembalikan f.read().


def tulis_teks(path, teks):  # Mendefinisikan fungsi tulis_teks dengan parameter yang tertulis.
    with open(path, "w", encoding="utf-8", newline="") as f:  # Mengelola sumber daya atau konteks open(path, "w", encoding="utf-8", newline="") as f.
        f.write(teks)  # Memanggil f.write untuk menulis data ke file atau aliran.


def tulis_bytes(path, data):  # Mendefinisikan fungsi tulis_bytes dengan parameter yang tertulis.
    with open(path, "wb") as f:  # Mengelola sumber daya atau konteks open(path, "wb") as f.
        f.write(data)  # Memanggil f.write untuk menulis data ke file atau aliran.


def tulis_hex(path, data):  # Mendefinisikan fungsi tulis_hex dengan parameter yang tertulis.
    tulis_teks(path, data.hex() + "\n")  # Memanggil tulis_teks untuk menjalankan operasi dengan argumen yang diberikan.


def baca_hex(path):  # Mendefinisikan fungsi baca_hex dengan parameter yang tertulis.
    isi = "".join(baca_teks(path).split())  # Menghitung atau menyiapkan ''.join(baca_teks(path).split()), lalu menyimpannya pada isi.
    try:  # Memulai operasi yang dapat menghasilkan exception.
        return bytes.fromhex(isi)  # Mengembalikan bytes.fromhex(isi).
    except ValueError:  # Menangani exception ValueError.
        raise ValueError(f"Isi file '{path}' bukan heksadesimal yang valid.")  # Menghentikan proses dengan exception ValueError(f"Isi file '{path}' bukan heksadesimal yang valid.").


def path_hasil_dekripsi(path):  # Mendefinisikan fungsi path_hasil_dekripsi dengan parameter yang tertulis.
    akhiran = ".enc.txt"  # Menghitung atau menyiapkan '.enc.txt', lalu menyimpannya pada akhiran.
    if path.endswith(akhiran):  # Menjalankan blok hanya jika path.endswith(akhiran).
        return path[: -len(akhiran)] + ".dec.txt"  # Mengembalikan path[: -len(akhiran)] + ".dec.txt".
    return os.path.splitext(path)[0] + ".dec.txt"  # Mengembalikan os.path.splitext(path)[0] + ".dec.txt".
