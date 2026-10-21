# CryptoZar — konfigurasi
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Menghitung atau menyiapkan 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', lalu menyimpannya pada ALFABET.

ALGORITMA = {  # Menghitung atau menyiapkan {'1': ('Caesar', 'caesar'), '2': ('Vigenere', 'vigenere'), '3': ('Playfair', 'playfair'), '4': ('Hill', 'hill', lalu menyimpannya pada ALGORITMA.
    "1": ("Caesar", "caesar"),  # Menghitung atau menyiapkan {'1': ('Caesar', 'caesar'), '2': ('Vigenere', 'vigenere'), '3': ('Playfair', 'playfair'), '4': ('Hill', 'hill', lalu menyimpannya pada ALGORITMA.
    "2": ("Vigenere", "vigenere"),  # Menghitung atau menyiapkan {'1': ('Caesar', 'caesar'), '2': ('Vigenere', 'vigenere'), '3': ('Playfair', 'playfair'), '4': ('Hill', 'hill', lalu menyimpannya pada ALGORITMA.
    "3": ("Playfair", "playfair"),  # Menghitung atau menyiapkan {'1': ('Caesar', 'caesar'), '2': ('Vigenere', 'vigenere'), '3': ('Playfair', 'playfair'), '4': ('Hill', 'hill', lalu menyimpannya pada ALGORITMA.
    "4": ("Hill", "hill"),  # Menghitung atau menyiapkan {'1': ('Caesar', 'caesar'), '2': ('Vigenere', 'vigenere'), '3': ('Playfair', 'playfair'), '4': ('Hill', 'hill', lalu menyimpannya pada ALGORITMA.
    "5": ("One-Time Pad (OTP)", "otp"),  # Menghitung atau menyiapkan {'1': ('Caesar', 'caesar'), '2': ('Vigenere', 'vigenere'), '3': ('Playfair', 'playfair'), '4': ('Hill', 'hill', lalu menyimpannya pada ALGORITMA.
    "6": ("Stream Cipher (LCG)", "stream"),  # Menghitung atau menyiapkan {'1': ('Caesar', 'caesar'), '2': ('Vigenere', 'vigenere'), '3': ('Playfair', 'playfair'), '4': ('Hill', 'hill', lalu menyimpannya pada ALGORITMA.
}  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

PROMPT_KUNCI = {  # Menghitung atau menyiapkan {'1': ('Kunci Caesar (geseran 0-25)', '3'), '2': ('Kunci Vigenere (kata, huruf A-Z)', 'SANDI'), '3': ('Kunci P, lalu menyimpannya pada PROMPT_KUNCI.
    "1": ("Kunci Caesar (geseran 0-25)", "3"),  # Menghitung atau menyiapkan {'1': ('Kunci Caesar (geseran 0-25)', '3'), '2': ('Kunci Vigenere (kata, huruf A-Z)', 'SANDI'), '3': ('Kunci P, lalu menyimpannya pada PROMPT_KUNCI.
    "2": ("Kunci Vigenere (kata, huruf A-Z)", "SANDI"),  # Menghitung atau menyiapkan {'1': ('Kunci Caesar (geseran 0-25)', '3'), '2': ('Kunci Vigenere (kata, huruf A-Z)', 'SANDI'), '3': ('Kunci P, lalu menyimpannya pada PROMPT_KUNCI.
    "3": ("Kunci Playfair (kata, huruf A-Z)", "MONARCHY"),  # Menghitung atau menyiapkan {'1': ('Kunci Caesar (geseran 0-25)', '3'), '2': ('Kunci Vigenere (kata, huruf A-Z)', 'SANDI'), '3': ('Kunci P, lalu menyimpannya pada PROMPT_KUNCI.
    "4": ("Kunci Hill (4 angka untuk 2x2, atau 9 angka untuk 3x3)", "3 3 2 5"),  # Menghitung atau menyiapkan {'1': ('Kunci Caesar (geseran 0-25)', '3'), '2': ('Kunci Vigenere (kata, huruf A-Z)', 'SANDI'), '3': ('Kunci P, lalu menyimpannya pada PROMPT_KUNCI.
    "6": ("Seed Stream Cipher (0-255)", "77"),  # Menghitung atau menyiapkan {'1': ('Kunci Caesar (geseran 0-25)', '3'), '2': ('Kunci Vigenere (kata, huruf A-Z)', 'SANDI'), '3': ('Kunci P, lalu menyimpannya pada PROMPT_KUNCI.
}  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
