# CryptoZar — algoritma.otp
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
import secrets  # Memuat pustaka secrets.


def xor_bytes(a, b):  # Mendefinisikan fungsi xor_bytes dengan parameter yang tertulis.
    if len(a) != len(b):  # Menjalankan blok hanya jika len(a) != len(b).
        raise ValueError(f"Panjang byte harus sama ({len(a)} berbanding {len(b)}).")  # Menghentikan proses dengan exception ValueError(f"Panjang byte harus sama ({len(a)} berbanding {len(b)}).").
    return bytes((x ^ y for x, y in zip(a, b)))  # Mengembalikan bytes((x ^ y for x, y in zip(a, b))).


def otp_buat_kunci(n):  # Mendefinisikan fungsi otp_buat_kunci dengan parameter yang tertulis.
    return secrets.token_bytes(n)  # Membangkitkan n byte acak untuk pad OTP menggunakan sumber acak sistem.
