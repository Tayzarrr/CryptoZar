# CryptoZar — algoritma.caesar
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.utilitas import normalisasi  # Mengimpor komponen yang dibutuhkan dari cryptozar.utilitas.


def caesar_enkripsi(teks, k):  # Mendefinisikan fungsi caesar_enkripsi dengan parameter yang tertulis.
    k %= 26  # Membatasi pergeseran Caesar ke rentang 0–25 dengan modulo 26.
    return "".join((chr((ord(c) - 65 + k) % 26 + 65) for c in normalisasi(teks)))  # Mengembalikan "".join((chr((ord(c) - 65 + k) % 26 + 65) for c in normalisasi(teks))).


def caesar_dekripsi(cipher, k):  # Mendefinisikan fungsi caesar_dekripsi dengan parameter yang tertulis.
    return caesar_enkripsi(cipher, -k)  # Mendekripsi Caesar dengan menggeser huruf berlawanan arah.
