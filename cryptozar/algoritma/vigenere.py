# CryptoZar — algoritma.vigenere
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.utilitas import normalisasi  # Mengimpor komponen yang dibutuhkan dari cryptozar.utilitas.


def _geseran_vigenere(kunci):  # Mendefinisikan fungsi _geseran_vigenere dengan parameter yang tertulis.
    kunci = normalisasi(kunci)  # Membersihkan kunci menjadi huruf kapital A–Z saja.
    if not kunci:  # Menjalankan blok hanya jika not kunci.
        raise ValueError("Kunci Vigenere harus berisi minimal satu huruf A-Z.")  # Menghentikan proses dengan exception ValueError("Kunci Vigenere harus berisi minimal satu huruf A-Z.").
    return [ord(c) - 65 for c in kunci]  # Mengembalikan [ord(c) - 65 for c in kunci].


def vigenere_enkripsi(teks, kunci, arah=1):  # Mendefinisikan fungsi vigenere_enkripsi dengan parameter yang tertulis.
    g = _geseran_vigenere(kunci)  # Menghitung atau menyiapkan _geseran_vigenere(kunci), lalu menyimpannya pada g.
    m = len(g)  # Menyimpan panjang kunci Vigenere untuk pengulangan indeks kunci.
    return "".join(  # Mengembalikan "".join(.
        (  # Menyusun bagian ekspresi (.
            chr((ord(c) - 65 + arah * g[i % m]) % 26 + 65)  # Menyusun bagian ekspresi chr((ord(c) - 65 + arah * g[i % m]) % 26 + 65).
            for i, c in enumerate(normalisasi(teks))  # Mengulangi proses untuk i, c in enumerate(normalisasi(teks).
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.


def vigenere_dekripsi(cipher, kunci):  # Mendefinisikan fungsi vigenere_dekripsi dengan parameter yang tertulis.
    return vigenere_enkripsi(cipher, kunci, arah=-1)  # Mengurangi pergeseran kunci Vigenere untuk memulihkan plaintext.
