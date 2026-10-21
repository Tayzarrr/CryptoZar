# CryptoZar — algoritma.playfair
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.konfigurasi import ALFABET  # Mengimpor komponen yang dibutuhkan dari cryptozar.konfigurasi.
from cryptozar.utilitas import normalisasi  # Mengimpor komponen yang dibutuhkan dari cryptozar.utilitas.


def playfair_tabel(kunci):  # Mendefinisikan fungsi playfair_tabel dengan parameter yang tertulis.
    kunci = normalisasi(kunci).replace("J", "I")  # Menghitung atau menyiapkan normalisasi(kunci).replace('J', 'I'), lalu menyimpannya pada kunci.
    urut = []  # Menghitung atau menyiapkan [], lalu menyimpannya pada urut.
    for c in kunci + ALFABET:  # Mengulangi proses untuk c in kunci + ALFABET.
        if c != "J" and c not in urut:  # Menjalankan blok hanya jika c != "J" and c not in urut.
            urut.append(c)  # Memanggil urut.append untuk menambahkan elemen ke daftar.
    return urut  # Mengembalikan urut.


def playfair_digraf(teks):  # Mendefinisikan fungsi playfair_digraf dengan parameter yang tertulis.
    teks = normalisasi(teks).replace("J", "I")  # Menghitung atau menyiapkan normalisasi(teks).replace('J', 'I'), lalu menyimpannya pada teks.
    pasangan = []  # Menghitung atau menyiapkan [], lalu menyimpannya pada pasangan.
    i = 0  # Menghitung atau menyiapkan 0, lalu menyimpannya pada i.
    while i < len(teks):  # Mengulangi blok selama i < len(teks).
        a = teks[i]  # Menghitung atau menyiapkan teks[i], lalu menyimpannya pada a.
        pengisi = "X" if a != "X" else "Q"  # Memilih pengisi Q untuk huruf X, atau X untuk huruf lainnya agar pasangan berbeda.
        if i + 1 < len(teks):  # Menjalankan blok hanya jika i + 1 < len(teks).
            b = teks[i + 1]  # Menghitung atau menyiapkan teks[i + 1], lalu menyimpannya pada b.
            if a == b:  # Menjalankan blok hanya jika a == b.
                pasangan.append((a, pengisi))  # Memanggil pasangan.append untuk menambahkan elemen ke daftar.
                i += 1  # Menghitung atau menyiapkan 1, lalu menyimpannya pada i.
            else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
                pasangan.append((a, b))  # Memanggil pasangan.append untuk menambahkan elemen ke daftar.
                i += 2  # Menghitung atau menyiapkan 2, lalu menyimpannya pada i.
        else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
            pasangan.append((a, pengisi))  # Memanggil pasangan.append untuk menambahkan elemen ke daftar.
            i += 1  # Menghitung atau menyiapkan 1, lalu menyimpannya pada i.
    return pasangan  # Mengembalikan pasangan.


def _playfair_geser(pasangan, tabel, arah):  # Mendefinisikan fungsi _playfair_geser dengan parameter yang tertulis.
    pos = {c: divmod(i, 5) for i, c in enumerate(tabel)}  # Memetakan setiap huruf Playfair ke koordinat baris dan kolom dalam tabel 5 × 5.
    hasil = []  # Menghitung atau menyiapkan [], lalu menyimpannya pada hasil.
    for a, b in pasangan:  # Mengulangi proses untuk a, b in pasangan.
        (r1, c1), (r2, c2) = (pos[a], pos[b])  # Menghitung atau menyiapkan (pos[a], pos[b]), lalu menyimpannya pada ((r1, c1), (r2, c2)).
        if r1 == r2:  # Menjalankan blok hanya jika r1 == r2.
            hasil.append(tabel[r1 * 5 + (c1 + arah) % 5])  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
            hasil.append(tabel[r2 * 5 + (c2 + arah) % 5])  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
        elif c1 == c2:  # Memeriksa kondisi alternatif c1 == c2.
            hasil.append(tabel[(r1 + arah) % 5 * 5 + c1])  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
            hasil.append(tabel[(r2 + arah) % 5 * 5 + c2])  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
        else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
            hasil.append(tabel[r1 * 5 + c2])  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
            hasil.append(tabel[r2 * 5 + c1])  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
    return "".join(hasil)  # Mengembalikan "".join(hasil).


def playfair_enkripsi(teks, kunci):  # Mendefinisikan fungsi playfair_enkripsi dengan parameter yang tertulis.
    return _playfair_geser(playfair_digraf(teks), playfair_tabel(kunci), +1)  # Mengembalikan _playfair_geser(playfair_digraf(teks), playfair_tabel(kunci), +1).


def playfair_dekripsi(cipher, kunci):  # Mendefinisikan fungsi playfair_dekripsi dengan parameter yang tertulis.
    c = normalisasi(cipher).replace("J", "I")  # Menghitung atau menyiapkan normalisasi(cipher).replace('J', 'I'), lalu menyimpannya pada c.
    if len(c) % 2:  # Menjalankan blok hanya jika len(c) % 2.
        raise ValueError("Ciphertext Playfair harus berjumlah huruf genap.")  # Menghentikan proses dengan exception ValueError("Ciphertext Playfair harus berjumlah huruf genap.").
    pasangan = [(c[i], c[i + 1]) for i in range(0, len(c), 2)]  # Menghitung atau menyiapkan [(c[i], c[i + 1]) for i in range(0, len(c), 2)], lalu menyimpannya pada pasangan.
    return _playfair_geser(pasangan, playfair_tabel(kunci), -1)  # Mengembalikan _playfair_geser(pasangan, playfair_tabel(kunci), -1).
