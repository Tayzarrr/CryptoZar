# CryptoZar — utilitas
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
import sys  # Memuat pustaka sys.


def aman(teks):  # Mendefinisikan fungsi aman dengan parameter yang tertulis.
    """Cetak aman pada konsol yang tidak mendukung semua karakter Unicode."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    enc = sys.stdout.encoding or "utf-8"  # Menghitung atau menyiapkan sys.stdout.encoding or 'utf-8', lalu menyimpannya pada enc.
    return str(teks).encode(enc, errors="replace").decode(enc, errors="replace")  # Mengembalikan str(teks).encode(enc, errors="replace").decode(enc, errors="replace").


def ringkas(teks, batas=120):  # Mendefinisikan fungsi ringkas dengan parameter yang tertulis.
    teks = str(teks)  # Menghitung atau menyiapkan str(teks), lalu menyimpannya pada teks.
    return teks if len(teks) <= batas else teks[:batas] + f"... (total {len(teks)} karakter)"  # Mengembalikan teks if len(teks) <= batas else teks[:batas] + f"... (total {len(teks)} karakter)".


def normalisasi(teks):  # Mendefinisikan fungsi normalisasi dengan parameter yang tertulis.
    """Huruf besar saja, hanya A-Z (spasi, angka, tanda baca dibuang)."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    return "".join((c for c in teks.upper() if "A" <= c <= "Z"))  # Mengembalikan "".join((c for c in teks.upper() if "A" <= c <= "Z")).


def huruf_ke_angka(teks):  # Mendefinisikan fungsi huruf_ke_angka dengan parameter yang tertulis.
    return [ord(c) - 65 for c in teks]  # Mengembalikan [ord(c) - 65 for c in teks].


def angka_ke_huruf(angka):  # Mendefinisikan fungsi angka_ke_huruf dengan parameter yang tertulis.
    return "".join((chr(a + 65) for a in angka))  # Mengembalikan "".join((chr(a + 65) for a in angka)).
