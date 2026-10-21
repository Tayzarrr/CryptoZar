# CryptoZar — algoritma.hill
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.utilitas import angka_ke_huruf  # Mengimpor komponen yang dibutuhkan dari cryptozar.utilitas.
from cryptozar.utilitas import huruf_ke_angka  # Mengimpor komponen yang dibutuhkan dari cryptozar.utilitas.
import math  # Memuat pustaka math.
from cryptozar.utilitas import normalisasi  # Mengimpor komponen yang dibutuhkan dari cryptozar.utilitas.


def determinan(M):  # Mendefinisikan fungsi determinan dengan parameter yang tertulis.
    n = len(M)  # Menghitung atau menyiapkan len(M), lalu menyimpannya pada n.
    if n == 1:  # Menjalankan blok hanya jika n == 1.
        return M[0][0]  # Mengembalikan M[0][0].
    if n == 2:  # Menjalankan blok hanya jika n == 2.
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]  # Menghitung determinan matriks 2 × 2 menggunakan rumus ad − bc.
    total = 0  # Menghitung atau menyiapkan 0, lalu menyimpannya pada total.
    for j in range(n):  # Mengulangi proses untuk j in range(n).
        minor = [baris[:j] + baris[j + 1 :] for baris in M[1:]]  # Menghitung atau menyiapkan [baris[:j] + baris[j + 1:] for baris in M[1:]], lalu menyimpannya pada minor.
        total += (-1) ** j * M[0][j] * determinan(minor)  # Menghitung atau menyiapkan (-1) ** j * M[0][j] * determinan(minor), lalu menyimpannya pada total.
    return total  # Mengembalikan total.


def invers_matriks_mod26(M):  # Mendefinisikan fungsi invers_matriks_mod26 dengan parameter yang tertulis.
    n = len(M)  # Menghitung atau menyiapkan len(M), lalu menyimpannya pada n.
    det = determinan(M) % 26  # Menghitung determinan matriks kunci dalam aritmetika modulo 26.
    det_inv = pow(det, -1, 26)  # Mencari invers perkalian determinan modulo 26.
    adj = [[0] * n for _ in range(n)]  # Menghitung atau menyiapkan [[0] * n for _ in range(n)], lalu menyimpannya pada adj.
    for i in range(n):  # Mengulangi proses untuk i in range(n).
        for j in range(n):  # Mengulangi proses untuk j in range(n).
            minor = [baris[:j] + baris[j + 1 :] for k, baris in enumerate(M) if k != i]  # Menghitung atau menyiapkan [baris[:j] + baris[j + 1:] for k, baris in enumerate(M) if k != i], lalu menyimpannya pada minor.
            kofaktor = (-1) ** (i + j) * determinan(minor)  # Menghitung atau menyiapkan (-1) ** (i + j) * determinan(minor), lalu menyimpannya pada kofaktor.
            adj[j][i] = kofaktor  # Mentransposisikan kofaktor untuk membentuk matriks adjoin.
    return [[det_inv * adj[i][j] % 26 for j in range(n)] for i in range(n)]  # Mengembalikan [[det_inv * adj[i][j] % 26 for j in range(n)] for i in range(n)].


def hill_parse_kunci(teks):  # Mendefinisikan fungsi hill_parse_kunci dengan parameter yang tertulis.
    try:  # Memulai operasi yang dapat menghasilkan exception.
        angka = [int(x) for x in teks.replace(",", " ").split()]  # Menghitung atau menyiapkan [int(x) for x in teks.replace(',', ' ').split()], lalu menyimpannya pada angka.
    except ValueError:  # Menangani exception ValueError.
        raise ValueError("Kunci Hill harus berupa angka yang dipisah spasi, contoh: 3 3 2 5")  # Menghentikan proses dengan exception ValueError("Kunci Hill harus berupa angka yang dipisah spasi, contoh: 3 3 2 5").
    n = math.isqrt(len(angka))  # Menentukan kandidat ukuran sisi matriks dari jumlah bilangan kunci.
    if n * n != len(angka) or n not in (2, 3):  # Menjalankan blok hanya jika n * n != len(angka) or n not in (2, 3).
        raise ValueError("Kunci Hill harus 4 angka (matriks 2x2) atau 9 angka (matriks 3x3).")  # Menghentikan proses dengan exception ValueError("Kunci Hill harus 4 angka (matriks 2x2) atau 9 angka (matriks 3x3).").
    M = [[a % 26 for a in angka[i * n : (i + 1) * n]] for i in range(n)]  # Menghitung atau menyiapkan [[a % 26 for a in angka[i * n:(i + 1) * n]] for i in range(n)], lalu menyimpannya pada M.
    det = determinan(M) % 26  # Menghitung determinan matriks kunci dalam aritmetika modulo 26.
    if math.gcd(det, 26) != 1:  # Menolak matriks kunci jika determinan tidak relatif prima terhadap 26.
        raise ValueError(  # Menghentikan proses dengan exception ValueError(.
            f"Matriks tidak memiliki invers mod 26 (determinan = {det}; harus koprima dengan 26)."  # Menyusun bagian ekspresi f"Matriks tidak memiliki invers mod 26 (determinan = {det}; harus koprima dengan 26).".
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    return M  # Mengembalikan M.


def _hill_proses(angka, M):  # Mendefinisikan fungsi _hill_proses dengan parameter yang tertulis.
    n = len(M)  # Menghitung atau menyiapkan len(M), lalu menyimpannya pada n.
    hasil = []  # Menghitung atau menyiapkan [], lalu menyimpannya pada hasil.
    for i in range(0, len(angka), n):  # Mengulangi proses untuk i in range(0, len(angka), n).
        blok = angka[i : i + n]  # Menghitung atau menyiapkan angka[i:i + n], lalu menyimpannya pada blok.
        for r in range(n):  # Mengulangi proses untuk r in range(n).
            hasil.append(sum((M[r][c] * blok[c] for c in range(n))) % 26)  # Memanggil hasil.append untuk menambahkan elemen ke daftar.
    return hasil  # Mengembalikan hasil.


def hill_enkripsi(teks, M):  # Mendefinisikan fungsi hill_enkripsi dengan parameter yang tertulis.
    n = len(M)  # Menghitung atau menyiapkan len(M), lalu menyimpannya pada n.
    t = normalisasi(teks)  # Menghitung atau menyiapkan normalisasi(teks), lalu menyimpannya pada t.
    if len(t) % n:  # Menjalankan blok hanya jika len(t) % n.
        t += "X" * (n - len(t) % n)  # Menambahkan padding X supaya panjang pesan menjadi kelipatan ukuran blok Hill.
    return angka_ke_huruf(_hill_proses(huruf_ke_angka(t), M))  # Mengembalikan angka_ke_huruf(_hill_proses(huruf_ke_angka(t), M)).


def hill_dekripsi(cipher, M):  # Mendefinisikan fungsi hill_dekripsi dengan parameter yang tertulis.
    c = normalisasi(cipher)  # Menghitung atau menyiapkan normalisasi(cipher), lalu menyimpannya pada c.
    if len(c) % len(M):  # Menjalankan blok hanya jika len(c) % len(M).
        raise ValueError(f"Jumlah huruf ciphertext harus kelipatan {len(M)}.")  # Menghentikan proses dengan exception ValueError(f"Jumlah huruf ciphertext harus kelipatan {len(M)}.").
    return angka_ke_huruf(_hill_proses(huruf_ke_angka(c), invers_matriks_mod26(M)))  # Mengembalikan angka_ke_huruf(_hill_proses(huruf_ke_angka(c), invers_matriks_mod26(M))).
