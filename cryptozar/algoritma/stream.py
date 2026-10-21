# CryptoZar — algoritma.stream
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
def keystream_lcg(seed, n):  # Mendefinisikan fungsi keystream_lcg dengan parameter yang tertulis.
    x = seed % 256  # Membatasi keadaan awal LCG agar muat dalam satu byte.
    hasil = bytearray(n)  # Menghitung atau menyiapkan bytearray(n), lalu menyimpannya pada hasil.
    for i in range(n):  # Mengulangi proses untuk i in range(n).
        x = (5 * x + 1) % 256  # Menghasilkan byte keystream LCG berikutnya dengan pengali 5 dan increment 1.
        hasil[i] = x  # Menyimpan byte LCG yang baru pada posisi ke-i keystream.
    return bytes(hasil)  # Mengembalikan bytes(hasil).
