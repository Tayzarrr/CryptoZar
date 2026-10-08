#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CryptoZar - Aplikasi Enkripsi

"""

# ######################################################################
#                              BACKEND 
# ######################################################################
import csv
import math
import os
import random
import secrets
import statistics
import sys
import time
import tracemalloc

ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# kode menu -> (nama tampilan, nama untuk file)
ALGORITMA = {
    "1": ("Caesar", "caesar"),
    "2": ("Vigenere", "vigenere"),
    "3": ("Playfair", "playfair"),
    "4": ("Hill", "hill"),
    "5": ("One-Time Pad (OTP)", "otp"),
    "6": ("Stream Cipher (LCG)", "stream"),
}

# kode menu -> (label kunci, nilai default)
PROMPT_KUNCI = {
    "1": ("Kunci Caesar (geseran 0-25)", "3"),
    "2": ("Kunci Vigenere (kata, huruf A-Z)", "SANDI"),
    "3": ("Kunci Playfair (kata, huruf A-Z)", "MONARCHY"),
    "4": ("Kunci Hill (4 angka untuk 2x2, atau 9 angka untuk 3x3)", "3 3 2 5"),
    "6": ("Seed Stream Cipher (0-255)", "77"),
}


# ======================================================================
# FUNGSI BANTU UMUM
# ======================================================================
def aman(teks):
    """Cetak aman pada konsol yang tidak mendukung semua karakter Unicode."""
    enc = sys.stdout.encoding or "utf-8"
    return str(teks).encode(enc, errors="replace").decode(enc, errors="replace")


def ringkas(teks, batas=120):
    teks = str(teks)
    return teks if len(teks) <= batas else teks[:batas] + f"... (total {len(teks)} karakter)"


def normalisasi(teks):
    """Huruf besar saja, hanya A-Z (spasi, angka, tanda baca dibuang)."""
    return "".join(c for c in teks.upper() if "A" <= c <= "Z")


def huruf_ke_angka(teks):
    return [ord(c) - 65 for c in teks]


def angka_ke_huruf(angka):
    return "".join(chr(a + 65) for a in angka)

# ======================================================================
# CAESAR CIPHER
# ======================================================================
def caesar_enkripsi(teks, k):
    k %= 26
    return "".join(chr((ord(c) - 65 + k) % 26 + 65) for c in normalisasi(teks))


def caesar_dekripsi(cipher, k):
    return caesar_enkripsi(cipher, -k)

# ======================================================================
# VIGENERE CIPHER
# ======================================================================
def _geseran_vigenere(kunci):
    kunci = normalisasi(kunci)
    if not kunci:
        raise ValueError("Kunci Vigenere harus berisi minimal satu huruf A-Z.")
    return [ord(c) - 65 for c in kunci]


def vigenere_enkripsi(teks, kunci, arah=1):
    g = _geseran_vigenere(kunci)
    m = len(g)
    return "".join(
        chr((ord(c) - 65 + arah * g[i % m]) % 26 + 65)
        for i, c in enumerate(normalisasi(teks))
    )


def vigenere_dekripsi(cipher, kunci):
    return vigenere_enkripsi(cipher, kunci, arah=-1)

# ======================================================================
# PLAYFAIR CIPHER
# ======================================================================
def playfair_tabel(kunci):
    kunci = normalisasi(kunci).replace("J", "I")
    urut = []
    for c in kunci + ALFABET:
        if c != "J" and c not in urut:
            urut.append(c)
    return urut  # 25 huruf, dibaca per baris


def playfair_digraf(teks):
    teks = normalisasi(teks).replace("J", "I")
    pasangan = []
    i = 0
    while i < len(teks):
        a = teks[i]
        pengisi = "X" if a != "X" else "Q"
        if i + 1 < len(teks):
            b = teks[i + 1]
            if a == b:
                pasangan.append((a, pengisi))
                i += 1
            else:
                pasangan.append((a, b))
                i += 2
        else:
            pasangan.append((a, pengisi))
            i += 1
    return pasangan


def _playfair_geser(pasangan, tabel, arah):
    pos = {c: divmod(i, 5) for i, c in enumerate(tabel)}
    hasil = []
    for a, b in pasangan:
        (r1, c1), (r2, c2) = pos[a], pos[b]
        if r1 == r2:                       # satu baris: geser kolom
            hasil.append(tabel[r1 * 5 + (c1 + arah) % 5])
            hasil.append(tabel[r2 * 5 + (c2 + arah) % 5])
        elif c1 == c2:                     # satu kolom: geser baris
            hasil.append(tabel[((r1 + arah) % 5) * 5 + c1])
            hasil.append(tabel[((r2 + arah) % 5) * 5 + c2])
        else:                              # persegi panjang: tukar kolom
            hasil.append(tabel[r1 * 5 + c2])
            hasil.append(tabel[r2 * 5 + c1])
    return "".join(hasil)


def playfair_enkripsi(teks, kunci):
    return _playfair_geser(playfair_digraf(teks), playfair_tabel(kunci), +1)


def playfair_dekripsi(cipher, kunci):
    c = normalisasi(cipher).replace("J", "I")
    if len(c) % 2:
        raise ValueError("Ciphertext Playfair harus berjumlah huruf genap.")
    pasangan = [(c[i], c[i + 1]) for i in range(0, len(c), 2)]
    return _playfair_geser(pasangan, playfair_tabel(kunci), -1)

# ======================================================================
# HILL CIPHER
# ======================================================================
def determinan(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    total = 0
    for j in range(n):
        minor = [baris[:j] + baris[j + 1:] for baris in M[1:]]
        total += ((-1) ** j) * M[0][j] * determinan(minor)
    return total


def invers_matriks_mod26(M):
    n = len(M)
    det = determinan(M) % 26
    det_inv = pow(det, -1, 26)
    adj = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [baris[:j] + baris[j + 1:] for k, baris in enumerate(M) if k != i]
            kofaktor = ((-1) ** (i + j)) * determinan(minor)
            adj[j][i] = kofaktor
    return [[(det_inv * adj[i][j]) % 26 for j in range(n)] for i in range(n)]


def hill_parse_kunci(teks):
    try:
        angka = [int(x) for x in teks.replace(",", " ").split()]
    except ValueError:
        raise ValueError("Kunci Hill harus berupa angka yang dipisah spasi, contoh: 3 3 2 5")
    n = math.isqrt(len(angka))
    if n * n != len(angka) or n not in (2, 3):
        raise ValueError("Kunci Hill harus 4 angka (matriks 2x2) atau 9 angka (matriks 3x3).")
    M = [[a % 26 for a in angka[i * n:(i + 1) * n]] for i in range(n)]
    det = determinan(M) % 26
    if math.gcd(det, 26) != 1:
        raise ValueError(
            f"Matriks tidak memiliki invers mod 26 (determinan = {det}; harus koprima dengan 26)."
        )
    return M


def _hill_proses(angka, M):
    n = len(M)
    hasil = []
    for i in range(0, len(angka), n):
        blok = angka[i:i + n]
        for r in range(n):
            hasil.append(sum(M[r][c] * blok[c] for c in range(n)) % 26)
    return hasil


def hill_enkripsi(teks, M):
    n = len(M)
    t = normalisasi(teks)
    if len(t) % n:
        t += "X" * (n - len(t) % n)        # padding X sampai kelipatan n
    return angka_ke_huruf(_hill_proses(huruf_ke_angka(t), M))


def hill_dekripsi(cipher, M):
    c = normalisasi(cipher)
    if len(c) % len(M):
        raise ValueError(f"Jumlah huruf ciphertext harus kelipatan {len(M)}.")
    return angka_ke_huruf(_hill_proses(huruf_ke_angka(c), invers_matriks_mod26(M)))

# ======================================================================
# ONE-TIME PAD
# ======================================================================
def xor_bytes(a, b):
    if len(a) != len(b):
        raise ValueError(f"Panjang byte harus sama ({len(a)} berbanding {len(b)}).")
    return bytes(x ^ y for x, y in zip(a, b))


def otp_buat_kunci(n):
    return secrets.token_bytes(n)

# ======================================================================
# STREAM CIPHER
# ======================================================================
def keystream_lcg(seed, n):
    x = seed % 256
    hasil = bytearray(n)
    for i in range(n):
        x = (5 * x + 1) % 256
        hasil[i] = x
    return bytes(hasil)

# ======================================================================
# FILE INPUT dan OUTPUT
# ======================================================================
def baca_teks(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        return f.read()


def baca_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def tulis_teks(path, teks):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(teks)


def tulis_bytes(path, data):
    with open(path, "wb") as f:
        f.write(data)


def tulis_hex(path, data):
    tulis_teks(path, data.hex() + "\n")


def baca_hex(path):
    isi = "".join(baca_teks(path).split())
    try:
        return bytes.fromhex(isi)
    except ValueError:
        raise ValueError(f"Isi file '{path}' bukan heksadesimal yang valid.")


def path_hasil_dekripsi(path):
    akhiran = ".enc.txt"
    if path.endswith(akhiran):
        return path[:-len(akhiran)] + ".dec.txt"
    return os.path.splitext(path)[0] + ".dec.txt"

# ======================================================================
# ENKRIPSI DAN DEKRIPSI FILE
# ======================================================================
def enkripsi_file(kode, path_in, kunci_str=None):
    """Enkripsi file .txt. Mengembalikan dict berisi ringkasan hasil."""
    nama_tampil, nama_file = ALGORITMA[kode]
    base = os.path.splitext(path_in)[0]
    out_path = f"{base}_{nama_file}.enc.txt"
    info = {
        "algoritma": nama_tampil,
        "path_in": path_in,
        "out_path": out_path,
        "kunci_path": None,
    }

    if kode in ("1", "2", "3", "4"):
        teks = baca_teks(path_in)
        info["ukuran_in"] = len(teks.encode("utf-8"))
        if kode == "1":
            try:
                k = int(kunci_str)
            except (TypeError, ValueError):
                raise ValueError("Kunci Caesar harus berupa bilangan bulat.")
            t0 = time.perf_counter()
            cipher = caesar_enkripsi(teks, k)
            info["kunci_tampil"] = str(k % 26)
        elif kode == "2":
            t0 = time.perf_counter()
            cipher = vigenere_enkripsi(teks, kunci_str)
            info["kunci_tampil"] = normalisasi(kunci_str)
        elif kode == "3":
            t0 = time.perf_counter()
            cipher = playfair_enkripsi(teks, kunci_str)
            info["kunci_tampil"] = normalisasi(kunci_str).replace("J", "I")
        else:
            M = hill_parse_kunci(kunci_str)
            t0 = time.perf_counter()
            cipher = hill_enkripsi(teks, M)
            info["kunci_tampil"] = str(M)
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000
        tulis_teks(out_path, cipher)
        info["cipher_tampil"] = cipher
        info["ukuran_cipher"] = len(cipher)
        if not cipher:
            raise ValueError("File tidak berisi huruf A-Z sehingga tidak ada yang dienkripsi.")

    elif kode == "5":
        data = baca_bytes(path_in)
        info["ukuran_in"] = len(data)
        t0 = time.perf_counter()
        kunci = otp_buat_kunci(len(data))
        c = xor_bytes(data, kunci)
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000
        kunci_path = f"{base}_otp.key.txt"
        tulis_hex(kunci_path, kunci)
        tulis_hex(out_path, c)
        info["kunci_path"] = kunci_path
        info["kunci_tampil"] = kunci.hex()
        info["cipher_tampil"] = c.hex()
        info["ukuran_cipher"] = len(c)

    else:  # kode == "6"
        try:
            seed = int(kunci_str) % 256
        except (TypeError, ValueError):
            raise ValueError("Seed harus berupa bilangan bulat 0-255.")
        data = baca_bytes(path_in)
        info["ukuran_in"] = len(data)
        t0 = time.perf_counter()
        s = keystream_lcg(seed, len(data))
        c = xor_bytes(data, s)
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000
        tulis_hex(out_path, c)
        info["kunci_tampil"] = f"seed = {seed}"
        info["keystream_tampil"] = s.hex()
        info["cipher_tampil"] = c.hex()
        info["ukuran_cipher"] = len(c)

    return info


def dekripsi_file(kode, path_cipher, kunci_str=None):
    """Dekripsi file hasil enkripsi. Untuk OTP, kunci_str = path file kunci."""
    nama_tampil, _ = ALGORITMA[kode]
    out_path = path_hasil_dekripsi(path_cipher)
    info = {"algoritma": nama_tampil, "path_in": path_cipher, "out_path": out_path}

    if kode in ("1", "2", "3", "4"):
        cipher = baca_teks(path_cipher)
        if kode == "1":
            try:
                k = int(kunci_str)
            except (TypeError, ValueError):
                raise ValueError("Kunci Caesar harus berupa bilangan bulat.")
            t0 = time.perf_counter()
            plain = caesar_dekripsi(cipher, k)
        elif kode == "2":
            t0 = time.perf_counter()
            plain = vigenere_dekripsi(cipher, kunci_str)
        elif kode == "3":
            t0 = time.perf_counter()
            plain = playfair_dekripsi(cipher, kunci_str)
        else:
            M = hill_parse_kunci(kunci_str)
            t0 = time.perf_counter()
            plain = hill_dekripsi(cipher, M)
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000
        tulis_teks(out_path, plain)
        info["plain_tampil"] = plain

    elif kode == "5":
        c = baca_hex(path_cipher)
        kunci = baca_hex(kunci_str)
        if len(kunci) != len(c):
            raise ValueError(
                f"Panjang kunci ({len(kunci)} byte) tidak sama dengan ciphertext ({len(c)} byte)."
            )
        t0 = time.perf_counter()
        data = xor_bytes(c, kunci)
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000
        tulis_bytes(out_path, data)
        info["plain_tampil"] = data.decode("utf-8", errors="replace")

    else:  # kode == "6"
        try:
            seed = int(kunci_str) % 256
        except (TypeError, ValueError):
            raise ValueError("Seed harus berupa bilangan bulat 0-255.")
        c = baca_hex(path_cipher)
        t0 = time.perf_counter()
        s = keystream_lcg(seed, len(c))
        data = xor_bytes(c, s)
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000
        tulis_bytes(out_path, data)
        info["plain_tampil"] = data.decode("utf-8", errors="replace")

    return info

# ======================================================================
# DEMO: BELAJAR KRIPTOGRAFI
# ======================================================================
def demo_belajar_kriptografi():
    pesan = "BELAJAR KRIPTOGRAFI"
    path = "pesan_demo.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(pesan)
    print(f'\nPlaintext : "{pesan}"  ({len(pesan.encode("utf-8"))} byte, '
          f"{len(normalisasi(pesan))} huruf A-Z)")
    print(f"File      : {path}")
    kunci_demo = {"1": "3", "2": "SANDI", "3": "MONARCHY", "4": "3 3 2 5", "5": None, "6": "77"}
    for kode in ("1", "2", "3", "4", "5", "6"):
        try:
            e = enkripsi_file(kode, path, kunci_demo[kode])
            kunci_dek = e["kunci_path"] if kode == "5" else kunci_demo[kode]
            d = dekripsi_file(kode, e["out_path"], kunci_dek)
        except (ValueError, OSError) as err:
            print(f"\n[{ALGORITMA[kode][0]}] gagal: {err}")
            continue
        print("\n" + "=" * 64)
        print(f"{e['algoritma']}")
        print("  Kunci       :", e["kunci_tampil"])
        if "keystream_tampil" in e:
            print("  Keystream   :", e["keystream_tampil"])
        print("  Ciphertext  :", e["cipher_tampil"])
        print("  Dekripsi    :", d["plain_tampil"])
        print(f"  Waktu       : enkripsi {e['waktu_ms']:.4f} ms | dekripsi {d['waktu_ms']:.4f} ms")
        print("  File        :", e["out_path"])
    print("\nSelesai. Semua file hasil ada di folder yang sama dengan program.")

# ======================================================================
# PENGUKURAN BEBAN KOMPUTASI
# ======================================================================
def median_waktu_ms(fn, ulang):
    """Jalankan fn sebanyak 'ulang' kali; kembalikan (median ms, hasil terakhir)."""
    waktu = []
    hasil = None
    for _ in range(ulang):
        t0 = time.perf_counter()
        hasil = fn()
        waktu.append((time.perf_counter() - t0) * 1000)
    return statistics.median(waktu), hasil


def puncak_memori_kib(fn):
    tracemalloc.start()
    try:
        fn()
        _, puncak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return puncak / 1024


def ukur_satu_ukuran(n, ulang):
    """Ukur 7 konfigurasi algoritma untuk data berukuran n karakter/byte."""
    rng = random.Random(2026)                       # data uji tetap agar dapat diulang
    teks = "".join(rng.choices(ALFABET, k=n))        # A-Z acak (adil untuk semua algoritma)
    data = teks.encode("ascii")
    hasil = []

    def baris(nama, gen_ms, proses_ms, enk_ms, dek_ms, memori, kunci_byte, ct_byte):
        hasil.append({
            "algoritma": nama,
            "ukuran_data_byte": n,
            "gen_kunci_ms": round(gen_ms, 4),
            "proses_ms": round(proses_ms, 4),
            "enkripsi_total_ms": round(enk_ms, 4),
            "dekripsi_total_ms": round(dek_ms, 4),
            "memori_puncak_kib": round(memori, 2),
            "ukuran_kunci_byte": kunci_byte,
            "ukuran_ciphertext_byte": ct_byte,
        })

    # --- Cipher klasik: tidak ada pembangkitan kunci terpisah ---
    klasik = [
        ("Caesar", lambda: caesar_enkripsi(teks, 3), lambda c: caesar_dekripsi(c, 3), 1),
        ("Vigenere", lambda: vigenere_enkripsi(teks, "SANDI"),
         lambda c: vigenere_dekripsi(c, "SANDI"), 5),
        ("Playfair", lambda: playfair_enkripsi(teks, "MONARCHY"),
         lambda c: playfair_dekripsi(c, "MONARCHY"), 8),
    ]
    M2 = hill_parse_kunci("3 3 2 5")
    M3 = hill_parse_kunci("6 24 1 13 16 10 20 17 15")
    klasik.append(("Hill 2x2", lambda: hill_enkripsi(teks, M2), lambda c: hill_dekripsi(c, M2), 4))
    klasik.append(("Hill 3x3", lambda: hill_enkripsi(teks, M3), lambda c: hill_dekripsi(c, M3), 9))

    for nama, enk, dek, kb in klasik:
        t_enk, c = median_waktu_ms(enk, ulang)
        t_dek, _ = median_waktu_ms(lambda: dek(c), ulang)
        mem = puncak_memori_kib(enk)
        baris(nama, 0.0, t_enk, t_enk, t_dek, mem, kb, len(c))

    # --- OTP: pembangkitan pad dipisah dari XOR ---
    t_gen, pad = median_waktu_ms(lambda: otp_buat_kunci(n), ulang)
    t_xor, c = median_waktu_ms(lambda: xor_bytes(data, pad), ulang)
    t_dek, _ = median_waktu_ms(lambda: xor_bytes(c, pad), ulang)   # penerima sudah punya pad
    mem = puncak_memori_kib(lambda: xor_bytes(data, otp_buat_kunci(n)))
    baris("OTP", t_gen, t_xor, t_gen + t_xor, t_dek, mem, n, 2 * n)

    # --- Stream cipher: pembangkitan keystream dipisah dari XOR ---
    t_gen, s = median_waktu_ms(lambda: keystream_lcg(77, n), ulang)
    t_xor, c = median_waktu_ms(lambda: xor_bytes(data, s), ulang)
    mem = puncak_memori_kib(lambda: xor_bytes(data, keystream_lcg(77, n)))
    # penerima harus membangkitkan keystream lagi, lalu XOR
    baris("Stream (LCG)", t_gen, t_xor, t_gen + t_xor, t_gen + t_xor, mem, 1, 2 * n)
    return hasil


def tampilkan_tabel_bench(baris_hasil):
    kepala = ["Algoritma", "Ukuran(B)", "Gen(ms)", "Proses(ms)", "Enk(ms)", "Dek(ms)",
              "Mem(KiB)", "Kunci(B)", "Cipher(B)"]
    kunci = ["algoritma", "ukuran_data_byte", "gen_kunci_ms", "proses_ms",
             "enkripsi_total_ms", "dekripsi_total_ms", "memori_puncak_kib",
             "ukuran_kunci_byte", "ukuran_ciphertext_byte"]
    lebar = [14, 10, 10, 11, 10, 10, 10, 9, 10]
    print("".join(h.ljust(w) for h, w in zip(kepala, lebar)))
    print("-" * sum(lebar))
    for b in baris_hasil:
        print("".join(str(b[k]).ljust(w) for k, w in zip(kunci, lebar)))


def ukur_beban_komputasi(ukuran=None, ulang=5, csv_path="hasil_beban_komputasi.csv"):
    ukuran = ukuran or [1024, 10 * 1024, 100 * 1024]
    semua = []
    print(f"\nPengukuran beban komputasi (median dari {ulang} kali ulang, time.perf_counter)")
    print("Memori diukur terpisah memakai tracemalloc agar tidak memengaruhi waktu.")
    for n in ukuran:
        print(f"\n>>> Ukuran data: {n} byte ({n / 1024:g} KiB)")
        b = ukur_satu_ukuran(n, ulang)
        tampilkan_tabel_bench(b)
        semua.extend(b)

    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(semua[0].keys()))
        w.writeheader()
        w.writerows(semua)

    print("\nKeterangan kolom:")
    print("  Gen     : waktu membangkitkan pad (OTP) atau keystream (Stream); 0 untuk cipher klasik")
    print("  Proses  : waktu inti enkripsi (XOR atau substitusi/transposisi) tanpa Gen")
    print("  Enk     : total enkripsi = Gen + Proses")
    print("  Dek     : total dekripsi (OTP: hanya XOR karena pad sudah dimiliki penerima;")
    print("            Stream: penerima membangkitkan keystream lagi lalu XOR)")
    print("  Mem     : puncak memori Python saat enkripsi")
    print("  Kunci   : ukuran kunci (OTP = sepanjang pesan; Stream = 1 byte seed)")
    print("  Cipher  : ukuran ciphertext yang disimpan (OTP/Stream disimpan hex = 2x ukuran data)")
    print("\nKompleksitas teoretis (n = jumlah karakter/byte, k = ukuran matriks Hill):")
    print("  Caesar    O(n)       Vigenere  O(n)       Playfair  O(n)")
    print("  Hill      O(n.k^2)   OTP       O(n)       Stream    O(n)")
    print(f"\nTabel disimpan ke: {csv_path}")


def menu_benchmark():
    tambah = input("Tambahkan ukuran 1 MiB? (lebih lama) [y/N]: ").strip().lower() == "y"
    ukuran = [1024, 10 * 1024, 100 * 1024] + ([1024 * 1024] if tambah else [])
    ukur_beban_komputasi(ukuran)


# ######################################################################
# ######################################################################
#                      BAGIAN GUI  -  CRYPTOZAR
# ######################################################################
# ######################################################################
import base64
import contextlib
import io
import queue
import shutil
import tempfile
import threading
from tkinter import filedialog
from tkinter import font as tkfont

try:
    import customtkinter as ctk
except ImportError:                                  
    sys.exit("customtkinter belum terpasang.\nJalankan:  pip install customtkinter")


# ======================================================================
# TEMA
# ======================================================================
BG = "#EDE6D6"            # latar utama 
SIDEBAR = "#E0D7C2"       # sidebar
NAV_H = "#D3C9B2"         # hover menu sidebar
METRIK_BG = "#F8F4EA"     # panel metrik
CARD = "#FFFFFF"
BORDER = "#D9CFB8"
FIELD = "#FBF9F3"         # latar textbox / entry
INK = "#2D2A26"
MUTED = "#7A7366"

BLUE = "#D9E0F7"          # pastel biru
BLUE_H = "#C6D0F1"
BLUE_INK = "#2B3A67"
MINT = "#CDEBDA"          # pastel mint
MINT_H = "#B9E0CB"
MINT_INK = "#1F5A3A"
PRIMARY = "#6B84DE"       # aksen tegas untuk tombol aksi utama
PRIMARY_H = "#566FCB"
NEUTRAL = "#F1EDE0"
NEUTRAL_H = "#E7E1D0"

TOAST = {                 # jenis -> (latar, garis, teks)
    "success": ("#DDF3E6", "#B5DEC6", "#1F5A3A"),
    "error": ("#FBE3E1", "#EFB9B4", "#8A2B25"),
    "info": ("#E3E9FA", "#BFCBF0", "#2B3A67"),
}

NAMA_ALGO = {             # teks dropdown -> kode menu backend
    "Caesar Cipher": "1",
    "Vigenere Cipher": "2",
    "Playfair Cipher": "3",
    "Hill Cipher": "4",
    "One-Time Pad": "5",
    "Stream Cipher (LCG)": "6",
}

BATAS_TAMPIL = 100_000    # karakter maksimum yang ditampilkan di textbox hasil
BATAS_PRATINJAU = 20_000  # karakter maksimum pratinjau file input
BATAS_KUNCI = 3_000       # kunci lebih panjang disimpan di memori, bukan di textbox

_cache_font = {}


def _pilih_font(kandidat, cadangan):
    ada = set(tkfont.families())
    for k in kandidat:
        if k in ada:
            return k
    return cadangan


def fnt(ukuran=13, bobot="normal", mono=False):
    """Buat CTkFont; keluarga font dipilih sekali setelah jendela utama ada."""
    if "sans" not in _cache_font:
        _cache_font["sans"] = _pilih_font(
            ("Inter", "Segoe UI", "SF Pro Text", "Helvetica Neue", "Roboto", "Noto Sans",
             "DejaVu Sans"), "Helvetica")
        _cache_font["mono"] = _pilih_font(
            ("Cascadia Mono", "Consolas", "Menlo", "SF Mono", "DejaVu Sans Mono",
             "Liberation Mono"), "Courier")
    return ctk.CTkFont(family=_cache_font["mono" if mono else "sans"], size=ukuran, weight=bobot)


# ======================================================================
# FORMAT dan PESAN
# ======================================================================
def fmt_ukuran(b):
    if b < 1024:
        return f"{b} B"
    if b < 1024 * 1024:
        return f"{b / 1024:.2f} KB"
    return f"{b / (1024 * 1024):.2f} MB"


def fmt_durasi(detik):
    if detik < 1:
        return f"{detik * 1000:.1f} ms"
    if detik < 60:
        return f"{detik:.2f} s"
    m, s = divmod(int(round(detik)), 60)
    return f"{m} m {s:02d} s"


def frak_log(nilai, lo, hi):
    """Posisi 0..1 pada skala logaritmik untuk panjang bilah metrik."""
    if nilai is None or nilai <= 0:
        return 0.0
    return max(0.03, min(1.0, math.log10(nilai / lo) / math.log10(hi / lo)))


def pesan_error(e):
    """Ubah exception menjadi pesan yang ramah untuk pengguna."""
    if isinstance(e, UnicodeDecodeError):
        return "File bukan teks UTF-8 yang valid. Pilih file .txt berformat teks."
    if isinstance(e, FileNotFoundError):
        return "File tidak ditemukan. Pastikan file masih ada di lokasinya."
    if isinstance(e, PermissionError):
        return "Akses ke file ditolak oleh sistem."
    if isinstance(e, MemoryError):
        return "Memori tidak cukup untuk memproses data sebesar ini."
    if isinstance(e, (ValueError, OSError)):
        return str(e)
    return f"Terjadi kesalahan tak terduga ({type(e).__name__}): {e}"



def _hex_ke_bytes(teks, nama):
    bersih = "".join(str(teks).split())
    try:
        return bytes.fromhex(bersih)
    except ValueError:
        raise ValueError(
            f"{nama} harus berupa heksadesimal yang valid (karakter 0-9 dan A-F, jumlah genap)."
        )


def _siapkan_input(folder, teks, path_file, nama_default):
    """Salin file upload (atau tulis teks ketikan) ke folder sementara."""
    if path_file:
        tujuan = os.path.join(folder, os.path.basename(path_file))
        shutil.copyfile(path_file, tujuan)
    else:
        tujuan = os.path.join(folder, nama_default)
        tulis_teks(tujuan, teks)
    return tujuan


def _enkripsi_otp_kunci_manual(path_in, kunci_hex):
    """OTP dengan kunci yang disediakan pengguna (backend hanya membangkitkan kunci acak)."""
    kunci = _hex_ke_bytes(kunci_hex, "Kunci OTP")
    data = baca_bytes(path_in)
    if len(kunci) != len(data):
        raise ValueError(
            f"Panjang kunci OTP ({len(kunci)} byte) harus sama dengan panjang pesan "
            f"({len(data)} byte). Klik 'Generate Random Key' lagi, atau kosongkan kunci "
            f"agar dibangkitkan otomatis."
        )
    out_path = f"{os.path.splitext(path_in)[0]}_otp.enc.txt"
    t0 = time.perf_counter()
    c = xor_bytes(data, kunci)
    waktu_ms = (time.perf_counter() - t0) * 1000
    tulis_hex(out_path, c)
    return {
        "algoritma": ALGORITMA["5"][0], "path_in": path_in, "out_path": out_path,
        "kunci_path": None, "ukuran_in": len(data), "waktu_ms": waktu_ms,
        "kunci_tampil": kunci.hex(), "cipher_tampil": c.hex(), "ukuran_cipher": len(c),
    }


def jalankan_enkripsi(kode, teks, path_file, kunci):
    """Enkripsi teks ketikan (teks) atau file (path_file). Mengembalikan dict hasil untuk GUI."""
    t_awal = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="cryptozar_") as tmp:
        path_in = _siapkan_input(tmp, teks, path_file, "pesan.txt")
        if kode == "5" and kunci:
            info = _enkripsi_otp_kunci_manual(path_in, kunci)
        else:
            info = enkripsi_file(kode, path_in, kunci or None)
        data_out = baca_bytes(info["out_path"])
        nama_hasil = os.path.basename(info["out_path"])
        if kode == "5":
            kunci_simpan = info["kunci_tampil"]               
        else:
            kunci_simpan = " ".join(str(kunci).split())
        ukuran_in = info["ukuran_in"]
    nama_kunci = nama_hasil[:-len(".enc.txt")] + ".key.txt"
    return {
        "mode": "encrypt", "algoritma": info["algoritma"],
        "teks_hasil": info["cipher_tampil"], "bytes_hasil": data_out,
        "nama_hasil": nama_hasil, "kunci_simpan": kunci_simpan, "nama_kunci": nama_kunci,
        "ukuran_in": ukuran_in, "ukuran_out": len(data_out),
        "waktu_ms": info["waktu_ms"], "waktu_total_s": time.perf_counter() - t_awal,
    }


def jalankan_dekripsi(kode, teks, path_file, kunci):
    """Dekripsi teks ketikan atau file. Untuk OTP, kunci = string hex."""
    t_awal = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="cryptozar_") as tmp:
        path_in = _siapkan_input(tmp, teks, path_file, "pesan.enc.txt")
        ukuran_in = os.path.getsize(path_in)
        if kode in ("5", "6"):
            try:
                bytes.fromhex("".join(baca_teks(path_in).split()))
            except ValueError:
                raise ValueError(
                    "Ciphertext harus berupa heksadesimal yang valid "
                    "(karakter 0-9 dan A-F, jumlah genap)."
                )
        if kode == "5":
            kunci_bytes = _hex_ke_bytes(kunci, "Kunci OTP")
            path_kunci = os.path.join(tmp, "kunci.key.txt")
            tulis_hex(path_kunci, kunci_bytes)
            info = dekripsi_file(kode, path_in, path_kunci)    
        else:
            info = dekripsi_file(kode, path_in, kunci)
        data_out = baca_bytes(info["out_path"])
        nama_hasil = os.path.basename(info["out_path"])
    return {
        "mode": "decrypt", "algoritma": info["algoritma"],
        "teks_hasil": info["plain_tampil"], "bytes_hasil": data_out,
        "nama_hasil": nama_hasil, "kunci_simpan": None, "nama_kunci": None,
        "ukuran_in": ukuran_in, "ukuran_out": len(data_out),
        "waktu_ms": info["waktu_ms"], "waktu_total_s": time.perf_counter() - t_awal,
    }


def kunci_acak(kode, panjang_otp=0):
    """Kunci acak yang valid untuk algoritma terpilih."""
    if kode == "1":
        return str(secrets.randbelow(25) + 1)
    if kode in ("2", "3"):
        return "".join(secrets.choice(ALFABET) for _ in range(8))
    if kode == "4":
        while True:
            angka = " ".join(str(secrets.randbelow(26)) for _ in range(4))
            try:
                hill_parse_kunci(angka)           
                return angka
            except ValueError:
                continue
    if kode == "5":
        return otp_buat_kunci(panjang_otp).hex()
    return str(secrets.randbelow(256))


@contextlib.contextmanager
def _folder_sementara():
    """Pindah ke folder sementara agar file demo/benchmark tidak mengotori folder program."""
    awal = os.getcwd()
    with tempfile.TemporaryDirectory(prefix="cryptozar_") as tmp:
        os.chdir(tmp)
        try:
            yield tmp
        finally:
            os.chdir(awal)


def jalankan_demo():
    with _folder_sementara():
        demo_belajar_kriptografi()
    print("\n[GUI] File hasil demo bersifat sementara dan dihapus otomatis setelah demo selesai.")


def jalankan_benchmark(sertakan_1mib, ulang):
    ukuran = [1024, 10 * 1024, 100 * 1024] + ([1024 * 1024] if sertakan_1mib else [])
    nama_csv = "hasil_beban_komputasi.csv"
    with _folder_sementara():
        ukur_beban_komputasi(ukuran, ulang, nama_csv)
        return baca_teks(nama_csv)


class _PenulisAntrean:
    """Pengganti sys.stdout: mengalirkan print() backend ke antrean untuk ditampilkan di GUI."""
    encoding = "utf-8"

    def __init__(self, q):
        self.q = q

    def write(self, s):
        if s:
            self.q.put(("log", s))
        return len(s)

    def flush(self):
        pass

    def isatty(self):
        return False


# ======================================================================
# KOMPONEN UI
# ======================================================================
# ======================================================================
# ANALISIS TANPA KUNCI (KRIPTANALISIS)
# Dipakai tab "Analyze": menebak kunci dan plaintext hanya dari ciphertext.
# Semua langkah ditulis ke laporan agar proses pencarian kunci terlihat.
# ======================================================================
import heapq
import itertools

SAMPEL = 4000          # maksimum huruf yang dipakai untuk menilai kandidat (agar cepat)
SAMPEL_KAMUS = 400     # huruf yang dipakai pada serangan kamus
MAKS_KAMUS = 50_000    # maksimum kata dari wordlist unggahan

# Frekuensi huruf (persen). Indonesia = perkiraan dari teks umum berbahasa Indonesia.
FREK_BAHASA = {
    "Indonesia": dict(A=19.2, N=10.0, I=8.6, E=7.9, K=6.0, T=5.6, R=5.4, U=5.3, D=4.4, M=4.1,
                      S=4.2, L=3.3, G=3.4, B=3.1, H=2.5, P=2.6, O=2.4, Y=1.6, C=1.3, J=1.0,
                      W=0.9, F=0.2, Z=0.1, V=0.1, X=0.03, Q=0.03),
    "English": dict(E=12.70, T=9.06, A=8.17, O=7.51, I=6.97, N=6.75, S=6.33, H=6.09, R=5.99,
                    D=4.25, L=4.03, C=2.78, U=2.76, M=2.41, W=2.36, F=2.23, G=2.02, Y=1.97,
                    P=1.93, B=1.49, V=0.98, K=0.77, J=0.15, X=0.15, Q=0.10, Z=0.07),
}


def _prob(d):
    total = sum(d.values())
    return [max(d.get(ch, 0.0) / total, 0.0005) for ch in ALFABET]


PROB = {b: _prob(d) for b, d in FREK_BAHASA.items()}
LOGP = {b: [math.log(p) for p in v] for b, v in PROB.items()}
IC_BAHASA = {b: sum(p * p for p in v) for b, v in PROB.items()}

_KATA_TEKS = """
yang dan dengan untuk dari pada adalah ini itu akan atau dalam tidak juga saya kami kita mereka
anda ada bisa sudah belum karena sebagai oleh telah para harus lebih saat sangat antara setelah
tersebut dapat lagi hanya semua setiap banyak belajar kriptografi enkripsi dekripsi kunci pesan
rahasia sandi data informasi komputer keamanan teks file algoritma program aplikasi selamat pagi
siang malam terima kasih hari besok kemarin tugas kuliah kelas dosen mahasiswa universitas serang
laporan kerja sama bersama tentang bahwa jika maka namun tetapi sehingga ketika sebuah suatu orang
dunia negara masalah sistem proses hasil waktu tahun bulan minggu teman rumah sekolah buku baca
tulis lihat dengar makan minum tidur bertemu kembali jangan sampai segera cepat hati pergi datang
the and that have for not with you this but his from they say her she will one all would there
their what out about who get which when make can like time just him know take people into year
your good some could them see other than then now look only come its over think also back after
use two how our work first well way even new want because any these give day most are was were
secret message attack dawn hello world crypto key cipher plain text encrypt decrypt security
information computer meet tomorrow night morning please thank
"""
KATA_UMUM = sorted({w.upper() for w in _KATA_TEKS.split() if len(w) >= 3},
                   key=lambda w: (-len(w), w))
_KATA_AWAL = {}
for _w in KATA_UMUM:
    _KATA_AWAL.setdefault(_w[0], []).append(_w)

KATA_KUNCI_BAWAAN = """
SANDI MONARCHY KEYWORD SECRET PLAYFAIR CRYPTO CRYPTOZAR CRYPTOGRAPHY KRIPTOGRAFI KRIPTO RAHASIA
KUNCI PASSWORD PASSWD ADMIN LOGIN INFORMATIKA KOMPUTER UNIVERSITAS KAMPUS INDONESIA JAKARTA
YOGYAKARTA MERDEKA GARUDA PANCASILA NUSANTARA CIPHER VIGENERE CAESAR HILL SECURITY SECURE LEMON
ORANGE APPLE BANANA TIGER DRAGON NAGA MATAHARI BULAN BINTANG LANGIT BUMI GUNUNG LAUT SAMUDRA
HARIMAU KUCING ANJING BURUNG PELANGI ENIGMA ALPHA BETA GAMMA DELTA OMEGA SIGMA MATRIX SYSTEM
NETWORK INTERNET SERVER CLIENT DATABASE SOFTWARE HARDWARE PROGRAM PYTHON JAVA LINUX WINDOWS
ANDROID GOOGLE FACEBOOK TWITTER MERAH BIRU HIJAU KUNING HITAM PUTIH COKLAT ORANYE UNGU RAJA RATU
KERAJAAN PERANG DAMAI CINTA SAYANG KASIH SEMANGAT BELAJAR KULIAH TUGAS UJIAN NILAI DOSEN KELAS
MAHASISWA SEKOLAH SECRETKEY MASTER HELLO WORLD TEST TESTING ABC ABCD QWERTY ZEBRA STONE FOREST
OCEAN RIVER MOUNTAIN SUNSHINE MOONLIGHT STARLIGHT FREEDOM LIBERTY JUSTICE TRUTH POWER ENERGY
""".split()


# ----------------------------------------------------------------------
# Alat ukur bahasa
# ----------------------------------------------------------------------
def _hitung(s):
    c = [0] * 26
    for ch in s:
        c[ord(ch) - 65] += 1
    return c


def indeks_koinsidensi(s):
    n = len(s)
    if n < 2:
        return 0.0
    return sum(f * (f - 1) for f in _hitung(s)) / (n * (n - 1))


def cakupan_kata(teks):
    """Proporsi huruf yang tertutup kata umum (pencocokan terpanjang, tanpa tumpang tindih)."""
    n = len(teks)
    if n == 0:
        return 0.0
    i = tertutup = 0
    while i < n:
        for w in _KATA_AWAL.get(teks[i], ()):
            if teks.startswith(w, i):
                tertutup += len(w)
                i += len(w)
                break
        else:
            i += 1
    return tertutup / n


def skor_teks(teks, bahasa="Auto"):
    """Nilai kemiripan sebuah teks dengan bahasa alami. skor lebih besar = lebih mirip."""
    t = teks[:SAMPEL]
    n = len(t)
    if n == 0:
        return {"skor": -9.0, "chi2": 9.0, "kata": 0.0, "bahasa": "-"}
    cnt = _hitung(t)
    terbaik = None
    for b in ([bahasa] if bahasa in PROB else list(PROB)):
        chi = sum((cnt[i] - n * PROB[b][i]) ** 2 / (n * PROB[b][i]) for i in range(26)) / n
        if terbaik is None or chi < terbaik[0]:
            terbaik = (chi, b)
    kata = cakupan_kata(t)
    return {"skor": kata - 0.15 * terbaik[0], "chi2": terbaik[0], "kata": kata,
            "bahasa": terbaik[1]}


def keyakinan(s, n):
    if n < 12:
        return "Rendah (ciphertext terlalu pendek)"
    if s["kata"] >= 0.35 and s["chi2"] <= 0.9:
        return "Tinggi"
    if s["kata"] >= 0.18 or s["chi2"] <= 0.4:
        return "Sedang"
    return "Rendah (hasil belum tentu terbaca)"


def keyakinan_kata(s, n):
    """Untuk hasil yang sudah dioptimalkan terhadap frekuensi huruf (chi2 pasti kecil): hanya kata yang dipercaya."""
    if n < 12:
        return "Rendah (ciphertext terlalu pendek)"
    if s["kata"] >= 0.35:
        return "Tinggi"
    if s["kata"] >= 0.18:
        return "Sedang"
    return "Rendah (hasil belum tentu terbaca)"


def _logp_teks(t, daftar_bahasa):
    return max(sum(LOGP[b][ord(c) - 65] for c in t) for b in daftar_bahasa)


def _daftar_bahasa(bahasa):
    return [bahasa] if bahasa in PROB else list(PROB)


def _pot(teks, n=44):
    return teks if len(teks) <= n else teks[:n] + "..."


def _bar(nilai, skala, lebar=24):
    return "#" * max(0, min(lebar, round(nilai / skala * lebar)))


def _ciri_ciphertext(teks):
    """Sidik jari ciphertext huruf: panjang, IC, pola digraf."""
    n = len(teks)
    ic = indeks_koinsidensi(teks)
    baris = [f"Panjang ciphertext      : {n} huruf (A-Z)",
             f"Huruf berbeda           : {len(set(teks))} dari 26",
             f"Index of Coincidence    : {ic:.4f}   (bahasa alami ~{IC_BAHASA['English']:.3f}-"
             f"{IC_BAHASA['Indonesia']:.3f}; acak ~0.0385)"]
    if ic >= 0.060:
        baris.append("  -> IC mirip bahasa alami: kemungkinan substitusi satu alfabet (mis. Caesar).")
    elif ic >= 0.045:
        baris.append("  -> IC di antara bahasa alami dan acak: kemungkinan polialfabetik / digraf.")
    else:
        baris.append("  -> IC mendekati acak: polialfabetik (kunci panjang), Hill, atau teks terlalu pendek.")
    if n % 2 == 0:
        ganda = sum(1 for i in range(0, n - 1, 2) if teks[i] == teks[i + 1])
        baris.append(f"Genap / pasangan kembar : panjang genap; pasangan huruf kembar (AA, BB, ...) = {ganda}"
                     + ("  <- ciri khas Playfair (tidak pernah ada)" if ganda == 0 and n >= 20 else ""))
    else:
        baris.append("Panjang ganjil          : bukan Playfair (digraf harus genap)")
    if "J" in teks:
        baris.append("Huruf J ada             : bukan Playfair (tabel 5x5 menggabungkan I/J)")
    baris.append(f"Habis dibagi 2 / 3      : {'ya' if n % 2 == 0 else 'tidak'} / "
                 f"{'ya' if n % 3 == 0 else 'tidak'}  (syarat Hill 2x2 / 3x3)")
    return baris


def _hasil(kode, kunci, laporan, skor, dicoba, ringkas, n_huruf=0, yakin=None):
    return {"kode": kode, "kunci": kunci, "laporan": laporan, "skor": skor, "dicoba": dicoba,
            "ringkas": ringkas, "n": n_huruf, "yakin": yakin}


def _judul(L, teks):
    L.append("")
    L.append("=" * 72)
    L.append(teks)
    L.append("=" * 72)


# ----------------------------------------------------------------------
# CAESAR: brute force 26 kunci
# ----------------------------------------------------------------------
def analisis_caesar(teks, bahasa, crib, offset, daftar):
    c = normalisasi(teks)
    if len(c) < 2:
        raise ValueError("Ciphertext Caesar harus berisi huruf A-Z.")
    L = []
    _judul(L, "ANALISIS CAESAR (tanpa kunci)")
    L.append("Rumus enkripsi : C = (P + k) mod 26      Rumus dekripsi : P = (C - k) mod 26")
    L.append("Ruang kunci    : hanya 26 kemungkinan (k = 0..25) -> cukup brute force.")
    L.append("")
    L.append("LANGKAH 1 - Coba semua 26 geseran, nilai kemiripan tiap hasil dengan bahasa alami")
    L.append("  chi2 = selisih frekuensi huruf dengan frekuensi bahasa (kecil = mirip)")
    L.append("  kata = proporsi huruf yang membentuk kata umum (besar = mirip)")
    L.append("")
    L.append(f"  {'k':>2} {'huruf kunci':<11} {'chi2':>7} {'kata':>6}  hasil dekripsi")
    kand = []
    for k in range(26):
        p = caesar_dekripsi(c[:SAMPEL], k)
        kand.append((k, p, skor_teks(p, bahasa)))
    terbaik = max(kand, key=lambda x: x[2]["skor"])
    for k, p, s in kand:
        tanda = "  <== TERBAIK" if k == terbaik[0] else ""
        L.append(f"  {k:>2} {ALFABET[k]:<11} {s['chi2']:>7.2f} {s['kata']:>6.2f}  {_pot(p)}{tanda}")
    k, p, s = terbaik
    L.append("")
    L.append("LANGKAH 2 - Pilih kandidat terbaik")
    urut = sorted(kand, key=lambda x: -x[2]["skor"])
    L.append(f"  Peringkat 1: k = {urut[0][0]} (skor {urut[0][2]['skor']:.3f}); "
             f"peringkat 2: k = {urut[1][0]} (skor {urut[1][2]['skor']:.3f})")
    L.append(f"  Bahasa yang paling cocok: {s['bahasa']}")
    L.append("")
    L.append(f"KESIMPULAN: kunci Caesar k = {k} (huruf '{ALFABET[k]}' = geser {k} posisi)")
    y = keyakinan(s, len(c))
    L.append(f"Keyakinan  : {y}")
    return _hasil("1", str(k), L, s, 26, f"Caesar, brute force 26 kunci", len(c), y)


# ----------------------------------------------------------------------
# VIGENERE: Kasiski + Index of Coincidence + frekuensi per kolom + kamus
# ----------------------------------------------------------------------
def _periode_minimal(k):
    for p in range(1, len(k) + 1):
        if len(k) % p == 0 and k[:p] * (len(k) // p) == k:
            return k[:p]
    return k


def _chi_geser(kol, bahasa):
    cnt = _hitung(kol)
    m = len(kol)
    hasil = []
    for s in range(26):
        chi = 0.0
        for i in range(26):
            e = m * PROB[bahasa][i]
            chi += (cnt[(i + s) % 26] - e) ** 2 / e
        hasil.append((chi / m, s))
    hasil.sort()
    return hasil


def _kunci_dari_panjang(teks, panjang, bahasa):
    terbaik = None
    for b in _daftar_bahasa(bahasa):
        kolom = [teks[i::panjang] for i in range(panjang)]
        rinci = [_chi_geser(k, b) for k in kolom]
        total = sum(r[0][0] for r in rinci) / panjang
        if terbaik is None or total < terbaik["chi"]:
            terbaik = {"kunci": "".join(ALFABET[r[0][1]] for r in rinci), "chi": total,
                       "bahasa": b, "rinci": rinci}
    return terbaik


def _kasiski(teks):
    t = teks[:SAMPEL]
    jarak = []
    for pj in (4, 3):
        posisi = {}
        for i in range(len(t) - pj + 1):
            posisi.setdefault(t[i:i + pj], []).append(i)
        for g, ps in posisi.items():
            if len(ps) > 1:
                for a, b in zip(ps, ps[1:]):
                    jarak.append((g, b - a))
        if jarak:
            break
    tally = {f: sum(1 for _, d in jarak if d % f == 0) for f in range(2, 21)}
    return jarak, tally


def _sempurnakan_vigenere(c, kunci, bahasa):
    """Coordinate ascent: ubah satu huruf kunci sekali waktu bila membuat teks lebih mirip bahasa."""
    sampel = c[:1200]
    kunci = list(kunci)
    terbaik = skor_teks(vigenere_dekripsi(sampel, "".join(kunci)), bahasa)["skor"]
    berubah = []
    for _ in range(2):
        ada = False
        for j in range(len(kunci)):
            asli = kunci[j]
            for h in ALFABET:
                if h == asli:
                    continue
                kunci[j] = h
                sk = skor_teks(vigenere_dekripsi(sampel, "".join(kunci)), bahasa)["skor"]
                if sk > terbaik + 1e-9:
                    terbaik, asli, ada = sk, h, True
                    berubah.append((j + 1, h))
            kunci[j] = asli
        if not ada:
            break
    return "".join(kunci), berubah


def serangan_kamus(kode, teks, bahasa, daftar):
    """Coba tiap kata sebagai kunci (Vigenere/Playfair). Mengembalikan daftar (skor, kata)."""
    dekripsi = vigenere_dekripsi if kode == "2" else playfair_dekripsi
    s = teks[:SAMPEL_KAMUS]
    if kode == "3":
        s = s.replace("J", "I")
        if len(s) % 2:
            s = s[:-1]
    kata_uniq = []
    lihat = set()
    for w in daftar:
        w = normalisasi(w)
        if kode == "3":
            w = w.replace("J", "I")
        if len(w) >= 2 and w not in lihat:
            lihat.add(w)
            kata_uniq.append(w)
    langs = _daftar_bahasa(bahasa)
    if len(kata_uniq) > 400:                         # saring cepat dengan frekuensi huruf tunggal
        pra = []
        for w in kata_uniq:
            pra.append((_logp_teks(dekripsi(s[:80 - (80 % 2)], w), langs), w))
        kata_uniq = [w for _, w in heapq.nlargest(80, pra)]
    hasil = []
    for w in kata_uniq:
        p = dekripsi(s, w)
        hasil.append((skor_teks(p, bahasa), w, p))
    hasil.sort(key=lambda x: -x[0]["skor"])
    return hasil, len(lihat)


def analisis_vigenere(teks, bahasa, crib, offset, daftar):
    c = normalisasi(teks)
    n = len(c)
    if n < 4:
        raise ValueError("Ciphertext Vigenere terlalu pendek untuk dianalisis.")
    L = []
    _judul(L, "ANALISIS VIGENERE (tanpa kunci)")
    L.append("Rumus enkripsi : C[i] = (P[i] + K[i mod m]) mod 26   (m = panjang kunci)")
    L.append("Ide serangan   : jika panjang kunci m diketahui, tiap kolom ke-j (huruf ke j, j+m, j+2m, ...)")
    L.append("                 hanyalah sandi Caesar -> dipecahkan dengan analisis frekuensi.")
    L.append("")
    L.append("LANGKAH 0 - Ciri ciphertext")
    L += ["  " + x for x in _ciri_ciphertext(c)]
    if n < 100:
        L.append(f"  PERHATIAN: hanya {n} huruf. Analisis statistik Vigenere butuh sekitar 100+ huruf; "
                 f"hasil mungkin meleset.")

    # --- Kasiski
    L.append("")
    L.append("LANGKAH 1 - Uji Kasiski: jarak antar urutan huruf berulang")
    jarak, tally = _kasiski(c)
    if jarak:
        L.append("  Urutan berulang (maks 8 ditampilkan):  urutan -> jarak")
        for g, d in jarak[:8]:
            L.append(f"    {g:<5} -> {d}")
        top = sorted(tally.items(), key=lambda x: (-x[1], x[0]))[:5]
        L.append("  Faktor persekutuan jarak (panjang kunci biasanya faktor dari jarak-jarak ini):")
        L.append("    " + ", ".join(f"{f} ({v}x)" for f, v in top if v))
    else:
        L.append("  Tidak ada urutan 3-4 huruf yang berulang (ciphertext pendek / kunci panjang).")

    # --- IC per panjang kunci
    L.append("")
    L.append("LANGKAH 2 - Index of Coincidence (IC) rata-rata kolom untuk tiap panjang kunci m")
    L.append("  IC bahasa alami ~0.065-0.075; IC acak ~0.0385. Panjang kunci benar -> IC tinggi.")
    maks = min(20, max(1, n // 4))
    ic_rata = {}
    for m in range(1, maks + 1):
        kolom = [c[i::m] for i in range(m)]
        nilai = [indeks_koinsidensi(k) for k in kolom if len(k) >= 2]
        ic_rata[m] = sum(nilai) / len(nilai) if nilai else 0.0
    ic_max = max(ic_rata.values())
    L.append(f"  {'m':>3} {'IC rata-rata':>13}")
    for m, v in ic_rata.items():
        L.append(f"  {m:>3} {v:>13.4f}  {_bar(v, 0.08)}")
    lmin = next((m for m, v in ic_rata.items() if v >= 0.9 * ic_max), 1)
    top_ic = [m for m, _ in sorted(ic_rata.items(), key=lambda x: -x[1])[:3]]
    kandidat_m = sorted({lmin, *top_ic})
    L.append(f"  Kandidat panjang kunci: {kandidat_m} (terkecil yang IC-nya mendekati maksimum: {lmin})")

    # --- Frekuensi per kolom
    L.append("")
    L.append("LANGKAH 3 - Analisis frekuensi per kolom untuk tiap kandidat panjang kunci")
    L.append("  Tiap kolom dicoba 26 geseran; geseran dengan chi2 terkecil dipilih sebagai huruf kunci.")
    ev = []
    for m in kandidat_m:
        hasil = _kunci_dari_panjang(c, m, bahasa)
        kunci = _periode_minimal(hasil["kunci"])
        p = vigenere_dekripsi(c[:SAMPEL], kunci)
        s = skor_teks(p, bahasa)
        ev.append((s["skor"] - 0.004 * len(kunci), m, kunci, p, s, hasil))
        L.append(f"  m = {m}: huruf kunci per kolom = {hasil['kunci']}"
                 + (f"  (periode minimal: {kunci})" if kunci != hasil["kunci"] else ""))
        for j, r in enumerate(hasil["rinci"][:6]):
            alt = ", ".join(f"{ALFABET[s_]} ({chi:.2f})" for chi, s_ in r[:3])
            L.append(f"      kolom {j + 1}: terbaik {alt}")
        if len(hasil["rinci"]) > 6:
            L.append(f"      ... ({len(hasil['rinci']) - 6} kolom lain)")
        L.append(f"      -> kunci '{kunci}', skor kemiripan {s['skor']:.3f} (chi2 {s['chi2']:.2f}, kata {s['kata']:.2f})")
    ev.sort(key=lambda x: -x[0])
    _, m_best, k_stat, p_stat, s_stat, _h = ev[0]
    if len(k_stat) <= 24:
        L.append("")
        L.append("LANGKAH 3b - Penyempurnaan: tiap huruf kunci diuji ulang dengan kecocokan kata")
        L.append("  (menolong bila satu kolom terlalu pendek untuk analisis frekuensi yang pasti)")
        k_baru, ubah = _sempurnakan_vigenere(c, k_stat, bahasa)
        if ubah:
            L.append("  Perubahan huruf kunci: " + ", ".join(f"kolom {j} -> {h}" for j, h in ubah))
            k_stat = k_baru
            p_stat = vigenere_dekripsi(c[:SAMPEL], k_stat)
            s_stat = skor_teks(p_stat, bahasa)
        else:
            L.append("  Tidak ada perubahan; huruf kunci sudah optimal.")
        L.append(f"  Kunci kandidat statistik: '{k_stat}' (skor {s_stat['skor']:.3f})")

    # --- kamus
    L.append("")
    L.append("LANGKAH 4 - Serangan kamus (coba daftar kata sebagai kunci)")
    sumber = list(KATA_KUNCI_BAWAAN) + list(daftar or [])
    kam, jumlah = serangan_kamus("2", c, bahasa, sumber)
    L.append(f"  {jumlah} kata kunci dicoba (bawaan{' + wordlist unggahan' if daftar else ''}). 5 terbaik:")
    for s, w, p in kam[:5]:
        L.append(f"    {w:<14} skor {s['skor']:>7.3f}  kata {s['kata']:.2f}  {_pot(p, 34)}")

    dicoba = 26 * sum(kandidat_m) + jumlah
    # --- pilih
    L.append("")
    s_k, w_k, _p = kam[0] if kam else ({"skor": -9, "kata": 0, "chi2": 9, "bahasa": "-"}, "", "")
    pakai_kamus = bool(kam) and (s_k["kata"] >= 0.35 and s_k["skor"] > s_stat["skor"] - 0.05
                                 or s_k["skor"] > s_stat["skor"] + 0.02)
    if pakai_kamus and w_k == k_stat:
        kunci, s = w_k, s_k
        L.append(f"KESIMPULAN: kunci Vigenere = '{kunci}' (ditemukan analisis statistik dan dikonfirmasi "
                 f"serangan kamus)")
    elif pakai_kamus:
        kunci, s = w_k, s_k
        L.append(f"KESIMPULAN: kunci Vigenere = '{kunci}' (ditemukan lewat serangan kamus)")
    else:
        kunci, s = k_stat, s_stat
        L.append(f"KESIMPULAN: kunci Vigenere = '{kunci}' (panjang {len(kunci)}, ditemukan lewat "
                 f"Kasiski/IC + frekuensi kolom)")
    y = keyakinan(s, n)
    L.append(f"Keyakinan  : {y}")
    return _hasil("2", kunci, L, s, dicoba, "Vigenere, Kasiski/IC + frekuensi kolom + kamus", n, y)


# ----------------------------------------------------------------------
# PLAYFAIR: tidak ada serangan frekuensi huruf tunggal -> serangan kamus
# ----------------------------------------------------------------------
def analisis_playfair(teks, bahasa, crib, offset, daftar):
    c = normalisasi(teks)
    n = len(c)
    if n < 4:
        raise ValueError("Ciphertext Playfair terlalu pendek untuk dianalisis.")
    L = []
    _judul(L, "ANALISIS PLAYFAIR (tanpa kunci)")
    L.append("Playfair mengenkripsi pasangan huruf memakai tabel 5x5 dari kata kunci.")
    L.append("Ruang kunci = 25! ~ 1,55 x 10^25 susunan tabel -> TIDAK bisa di-brute-force,")
    L.append("dan frekuensi huruf tunggal tidak berguna (satu huruf bisa jadi banyak huruf berbeda).")
    L.append("")
    L.append("LANGKAH 0 - Ciri ciphertext")
    L += ["  " + x for x in _ciri_ciphertext(c)]
    if n % 2:
        raise ValueError("Ciphertext Playfair harus berjumlah huruf genap (ciphertext ini ganjil).")
    pasang = {}
    for i in range(0, n, 2):
        pasang[c[i:i + 2]] = pasang.get(c[i:i + 2], 0) + 1
    top = sorted(pasang.items(), key=lambda x: -x[1])[:6]
    L.append("  Digraf paling sering: " + ", ".join(f"{d} ({v}x)" for d, v in top))
    L.append("  (Digraf yang sama selalu berasal dari digraf plaintext yang sama; contoh dalam bahasa Inggris: TH, HE;"
             " Indonesia: AN, NG, KA.)")
    L.append("")
    L.append("LANGKAH 1 - Serangan kamus: tiap kata dijadikan kunci, ciphertext didekripsi, lalu dinilai")
    sumber = list(KATA_KUNCI_BAWAAN) + list(daftar or [])
    kam, jumlah = serangan_kamus("3", c, bahasa, sumber)
    L.append(f"  {jumlah} kata kunci dicoba (bawaan{' + wordlist unggahan' if daftar else ''}). 8 terbaik:")
    L.append(f"  {'kunci':<14} {'skor':>7} {'kata':>6} {'chi2':>6}  hasil dekripsi")
    for s, w, p in kam[:8]:
        L.append(f"  {w:<14} {s['skor']:>7.3f} {s['kata']:>6.2f} {s['chi2']:>6.2f}  {_pot(p, 34)}")
    s, kunci, p = kam[0]
    L.append("")
    L.append("LANGKAH 2 - Tabel 5x5 dari kunci terbaik")
    tabel = playfair_tabel(kunci)
    for r in range(5):
        L.append("    " + " ".join(tabel[r * 5:(r + 1) * 5]))
    L.append("")
    y = keyakinan(s, n)
    if s["kata"] < 0.18 and s["chi2"] > 0.4:
        L.append("KESIMPULAN: tidak ada kata kunci dalam daftar yang menghasilkan teks terbaca.")
        L.append("  Kunci kemungkinan berada di luar daftar. Unggah wordlist yang lebih besar, atau")
        L.append(f"  gunakan kunci terbaik di bawah hanya sebagai tebakan lemah: '{kunci}'.")
    else:
        L.append(f"KESIMPULAN: kunci Playfair = '{kunci}' (ditemukan lewat serangan kamus)")
    L.append(f"Keyakinan  : {y}")
    return _hasil("3", kunci, L, s, jumlah, "Playfair, serangan kamus", n, y)


# ----------------------------------------------------------------------
# HILL: known-plaintext (eksak) atau serangan statistik per baris
# ----------------------------------------------------------------------
def _mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % 26 for j in range(len(B[0]))]
            for i in range(len(A))]


def _fmt_mat(M):
    return " ".join(str(x) for baris in M for x in baris)


def _hill_known_plaintext(c, n, crib, offset, L):
    """Hitung K = C * P^-1 (mod 26) dari pasangan blok plaintext-ciphertext yang diketahui."""
    mulai = -(-offset // n) * n                       # naikkan ke batas blok
    sub = crib[mulai - offset:]
    banyak = len(sub) // n
    L.append(f"  crib '{crib}' pada posisi {offset}; blok berukuran {n} mulai dari posisi {mulai} "
             f"-> {banyak} blok tersedia (butuh minimal {n}).")
    if banyak < n:
        L.append(f"  Crib terlalu pendek: butuh minimal {n * n} huruf (= {n} blok).")
        return None
    P_blok = [huruf_ke_angka(sub[i * n:(i + 1) * n]) for i in range(banyak)]
    c_awal = mulai
    C_blok = [huruf_ke_angka(c[c_awal + i * n:c_awal + (i + 1) * n]) for i in range(banyak)]
    if len(C_blok[-1]) < n:
        P_blok, C_blok = P_blok[:-1], C_blok[:-1]
    if len(C_blok) < n:
        return None
    kombinasi = itertools.islice(itertools.combinations(range(len(C_blok)), n), 60)
    for idx in kombinasi:
        nama_blok = ",".join(str(i + 1) for i in idx)
        P = [[P_blok[j][i] for j in idx] for i in range(n)]               # kolom = blok plaintext
        C = [[C_blok[j][i] for j in idx] for i in range(n)]
        try:
            Pinv = invers_matriks_mod26(P)
        except ValueError:
            L.append(f"  Blok {nama_blok}: matriks P tidak punya invers mod 26 (det = "
                     f"{determinan(P) % 26}), coba kombinasi blok lain.")
            continue
        K = _mm(C, Pinv)
        try:
            hill_parse_kunci(_fmt_mat(K))
        except ValueError as e:
            L.append(f"  Blok {nama_blok}: K hasil tidak valid ({e}).")
            continue
        ok = all(_mm(K, [[x] for x in pb]) == [[x] for x in cb] for pb, cb in zip(P_blok, C_blok))
        L.append(f"  Blok {nama_blok}:")
        L.append(f"    P (kolom = blok plaintext) = {P}")
        L.append(f"    C (kolom = blok ciphertext) = {C}")
        L.append(f"    P^-1 mod 26 = {Pinv}")
        L.append(f"    K = C x P^-1 mod 26 = {K}")
        L.append(f"    Uji K pada seluruh {len(C_blok)} blok crib: {'COCOK' if ok else 'TIDAK COCOK'}")
        if ok:
            return K
    L.append("  Tidak ada kombinasi blok yang matriks P-nya punya invers mod 26. Perpanjang crib"
             " (6-12 huruf biasanya cukup) atau geser posisinya.")
    return None


def _hill_statistik(c, n, bahasa, L):
    """Serangan ciphertext-only: tiap baris matriks dekripsi dinilai terpisah (unigram)."""
    langs = _daftar_bahasa(bahasa)
    angka = huruf_ke_angka(c[:min(len(c) - len(c) % n, 240 - 240 % n)])
    blok = [angka[i:i + n] for i in range(0, len(angka), n)]
    L.append(f"  Pakai {len(blok)} blok pertama ({len(angka)} huruf) untuk menilai kandidat baris.")
    baris_skor = {b: {} for b in langs}
    for baris in itertools.product(range(26), repeat=n):
        if all(x % 2 == 0 for x in baris) or all(x % 13 == 0 for x in baris):
            continue                                   # baris ini membuat matriks tak berinvers
        huruf = [sum(baris[j] * blk[j] for j in range(n)) % 26 for blk in blok]
        for b in langs:
            lp = LOGP[b]
            baris_skor[b][baris] = sum(lp[h] for h in huruf)
    L.append(f"  {len(next(iter(baris_skor.values())))} kemungkinan baris diberi nilai; "
             f"baris bernilai tinggi digabung menjadi matriks (urutan baris ikut diuji), lalu"
             f" 400 matriks terbaik dinilai ulang dengan kecocokan kata.")
    kandidat = {}
    for b in langs:
        pilih = heapq.nlargest(26 * 26 if n == 2 else 60, baris_skor[b].items(), key=lambda x: x[1])
        for kombinasi in itertools.product(pilih, repeat=n):
            D = [list(k[0]) for k in kombinasi]
            if math.gcd(determinan(D) % 26, 26) != 1:
                continue
            kunci_d = tuple(x for r in D for x in r)
            kandidat[kunci_d] = sum(k[1] for k in kombinasi)
    top = heapq.nlargest(400, kandidat.items(), key=lambda x: x[1])
    hasil = []
    for kd, _sk in top:
        D = [list(kd[i * n:(i + 1) * n]) for i in range(n)]
        K = invers_matriks_mod26(D)
        p = hill_dekripsi(c[:600 - 600 % n], K)
        hasil.append((skor_teks(p, bahasa), K, p))
    hasil.sort(key=lambda x: -x[0]["skor"])
    return hasil, len(kandidat)


def analisis_hill(teks, bahasa, crib, offset, daftar):
    c = normalisasi(teks)
    n_huruf = len(c)
    if n_huruf < 4:
        raise ValueError("Ciphertext Hill terlalu pendek untuk dianalisis.")
    ukuran = [n for n in (2, 3) if n_huruf % n == 0]
    if not ukuran:
        raise ValueError("Jumlah huruf ciphertext Hill harus kelipatan 2 atau 3.")
    L = []
    _judul(L, "ANALISIS HILL (tanpa kunci)")
    L.append("Rumus enkripsi : C = K x P (mod 26)   (P, C = vektor kolom blok huruf; K = matriks kunci n x n)")
    L.append("Hill 2x2 punya 157.248 kunci valid; 3x3 punya miliaran -> pendekatan cerdas diperlukan:")
    L.append("  * dengan known plaintext (crib): K = C x P^-1 mod 26 dihitung langsung (aljabar linear)")
    L.append("  * tanpa crib: tiap baris matriks dinilai terpisah dengan frekuensi huruf (butuh teks cukup panjang)")
    L.append("")
    L.append("LANGKAH 0 - Ciri ciphertext")
    L += ["  " + x for x in _ciri_ciphertext(c)]
    L.append(f"  Ukuran matriks yang mungkin: {', '.join(f'{n}x{n}' for n in ukuran)}")
    crib_n = normalisasi(crib or "")
    dicoba = 0
    kandidat = []
    for n in ukuran:
        L.append("")
        L.append(f"LANGKAH 1 ({n}x{n}) - " + ("Known-plaintext attack" if crib_n else
                                              "Serangan statistik per baris"))
        if crib_n:
            K = _hill_known_plaintext(c, n, crib_n, offset, L)
            dicoba += 1
            if K is not None:
                p = hill_dekripsi(c[:SAMPEL - SAMPEL % n], K)
                kandidat.append((skor_teks(p, bahasa), K, p, n, True))
                L.append(f"  -> K = {K}; dekripsi: {_pot(p)}")
            else:
                L.append(f"  -> gagal untuk {n}x{n}.")
        else:
            if n_huruf < 8 * n:
                L.append(f"  Ciphertext {n_huruf} huruf terlalu pendek untuk serangan statistik {n}x{n}; "
                         f"berikan crib (known plaintext).")
                continue
            hasil, jml = _hill_statistik(c, n, bahasa, L)
            dicoba += jml
            L.append(f"  {jml} matriks dekripsi valid dievaluasi. 5 terbaik:")
            L.append(f"  {'kunci K (baris demi baris)':<28} {'skor':>7} {'kata':>6}  hasil dekripsi")
            for s, K, p in hasil[:5]:
                L.append(f"  {_fmt_mat(K):<28} {s['skor']:>7.3f} {s['kata']:>6.2f}  {_pot(p, 34)}")
            if hasil:
                s, K, p = hasil[0]
                kandidat.append((s, K, p, n, False))
    L.append("")
    if not kandidat:
        L.append("KESIMPULAN: kunci Hill tidak dapat ditentukan. Tambahkan crib (potongan plaintext yang")
        L.append("  diketahui, mis. salam pembuka) atau gunakan ciphertext yang lebih panjang.")
        return _hasil("4", None, L, None, dicoba, "Hill, gagal", n_huruf, None)
    kandidat.sort(key=lambda x: -x[0]["skor"] - (0.3 if x[4] else 0))
    s, K, p, n, eksak = kandidat[0]
    kunci = _fmt_mat(K)
    L.append(f"KESIMPULAN: kunci Hill {n}x{n} = [{kunci}]"
             + ("  (dihitung eksak dari known plaintext)" if eksak else "  (hasil serangan statistik)"))
    y = keyakinan_kata(s, n_huruf)
    if eksak:
        y = "Tinggi (K cocok dengan seluruh crib)"
    L.append(f"Keyakinan  : {y}")
    return _hasil("4", kunci, L, s, dicoba, f"Hill {n}x{n}, {'known-plaintext' if eksak else 'statistik'}",
                  n_huruf, y)


# ----------------------------------------------------------------------
# STREAM CIPHER (LCG) & OTP: ciphertext heksadesimal
# ----------------------------------------------------------------------
def _parse_hex(teks):
    bersih = "".join(teks.split())
    try:
        return bytes.fromhex(bersih)
    except ValueError:
        raise ValueError("Ciphertext OTP / Stream harus heksadesimal yang valid "
                         "(karakter 0-9 dan A-F, jumlah genap).")


def _skor_byte(p):
    if not p:
        return (0.0, -9.0)
    baca = sum(1 for b in p if 32 <= b < 127 or b in (9, 10, 13)) / len(p)
    huruf = "".join(chr(b).upper() for b in p if 65 <= b <= 90 or 97 <= b <= 122)
    sk = skor_teks(huruf)["skor"] if len(huruf) >= 5 else -1.0
    return (baca, sk)


def _teks_cetak(p, n=40):
    s = "".join(chr(b) if 32 <= b < 127 else "." for b in p[:n])
    return s + ("..." if len(p) > n else "")


def analisis_stream(teks, bahasa, crib, offset, daftar):
    data = _parse_hex(teks)
    if not data:
        raise ValueError("Ciphertext kosong.")
    L = []
    _judul(L, "ANALISIS STREAM CIPHER LCG (tanpa kunci)")
    L.append("Keystream : x[i+1] = (5 * x[i] + 1) mod 256, x[0] = seed; plaintext = ciphertext XOR keystream.")
    L.append("Kunci     : seed 0..255 saja -> hanya 256 kemungkinan, sangat lemah (bahkan 1 byte plaintext")
    L.append("            yang diketahui sudah cukup untuk menghitung seed).")
    L.append("")
    L.append(f"Ciphertext: {len(data)} byte")
    L.append("")
    L.append("LANGKAH 1 - Brute force 256 seed, nilai keterbacaan tiap hasil (ASCII tercetak + kemiripan bahasa)")
    sampel = data[:2000]
    kand = []
    for seed in range(256):
        p = xor_bytes(sampel, keystream_lcg(seed, len(sampel)))
        baca, sk = _skor_byte(p)
        kand.append((baca, sk, seed, p))
    kand.sort(key=lambda x: (-x[0], -x[1]))
    L.append(f"  {'seed':>4} {'terbaca':>8} {'skor':>7}  hasil dekripsi (40 byte pertama)")
    for baca, sk, seed, p in kand[:8]:
        tanda = "  <== TERBAIK" if seed == kand[0][2] else ""
        L.append(f"  {seed:>4} {baca * 100:>7.1f}% {sk:>7.2f}  {_teks_cetak(p)}{tanda}")
    L.append(f"  ... ({len(kand) - 8} seed lain dengan keterbacaan lebih rendah)")
    baca, sk, seed, p = kand[0]
    kedua = kand[1][0]
    crib_b = (crib or "").encode("utf-8")
    seed_crib = None
    if crib_b:
        L.append("")
        L.append("LANGKAH 2 - Known plaintext: hitung seed secara aljabar")
        i = offset
        if i + len(crib_b) > len(data):
            L.append("  Crib melewati panjang ciphertext; dilewati.")
        else:
            x = data[i] ^ crib_b[0]
            L.append(f"  keystream[{i}] = ciphertext[{i}] XOR crib[0] = 0x{data[i]:02x} XOR 0x{crib_b[0]:02x} = {x}")
            L.append(f"  keystream[{i}] = x[{i + 1}], mundurkan LCG {i + 1} langkah dengan x[j-1] = (x[j] - 1) * 205 mod 256")
            L.append("  (205 adalah invers dari 5 mod 256, karena 5 x 205 = 1025 = 1 mod 256)")
            for _ in range(i + 1):
                x = ((x - 1) * 205) % 256
            seed_crib = x
            cocok = xor_bytes(data[i:i + len(crib_b)], keystream_lcg(seed_crib, i + len(crib_b))[i:]) == crib_b
            L.append(f"  seed = {seed_crib}; uji pada seluruh crib: {'COCOK' if cocok else 'TIDAK COCOK'}")
            if cocok:
                seed = seed_crib
                p = xor_bytes(sampel, keystream_lcg(seed, len(sampel)))
                baca, sk = _skor_byte(p)
            else:
                seed_crib = None
    L.append("")
    if baca >= 0.95 and (kedua < 0.9 or seed_crib is not None):
        y = "Tinggi"
    elif baca >= 0.9:
        y = "Sedang"
    else:
        y = "Rendah (tidak ada seed yang menghasilkan teks terbaca)"
    if baca >= 0.9:
        L.append(f"KESIMPULAN: seed = {seed} (keterbacaan {baca * 100:.1f}%)")
        L.append(f"Keyakinan  : {y}")
        return _hasil("6", str(seed), L, {"skor": sk, "kata": 0, "chi2": 0, "bahasa": "-"}, 256,
                      "Stream LCG, brute force 256 seed", len(data), y)
    L.append("KESIMPULAN: tidak ada seed LCG (0-255) yang menghasilkan teks terbaca.")
    L.append("  Ciphertext ini kemungkinan bukan Stream Cipher LCG (mis. One-Time Pad), atau plaintext-nya biner.")
    return _hasil("6", None, L, None, 256, "Stream LCG, gagal", len(data), None)


def analisis_otp(teks, bahasa, crib, offset, daftar):
    data = _parse_hex(teks)
    if not data:
        raise ValueError("Ciphertext kosong.")
    n = len(data)
    L = []
    _judul(L, "ANALISIS ONE-TIME PAD (tanpa kunci)")
    L.append("Enkripsi OTP : C = P XOR K, K acak sepanjang pesan dan dipakai sekali saja.")
    L.append(f"Ciphertext   : {n} byte  ->  ada 2^{8 * n} kemungkinan kunci, dan SETIAP plaintext {n} byte")
    L.append("               punya tepat satu kunci yang cocok.")
    L.append("")
    L.append("KESIMPULAN: OTP tidak dapat dipecahkan tanpa kunci (perfect secrecy, Shannon 1949).")
    L.append("  Aplikasi tidak bisa mengetahui kunci maupun plaintext; ciphertext tidak memuat informasi")
    L.append("  tentang isi pesan selain panjangnya.")
    L.append("")
    L.append("LANGKAH 1 - Demonstrasi: dua 'plaintext' berbeda sama-sama masuk akal")
    L.append("  Untuk dugaan plaintext P apa pun, kunci yang bersesuaian adalah K = C XOR P:")
    for kalimat in ("SERANGAN FAJAR DIMULAI PUKUL ENAM", "RAPAT DITUNDA SAMPAI HARI JUMAT DEPAN"):
        cand = (kalimat * (n // len(kalimat) + 1)).encode()[:n]
        kunci = xor_bytes(data, cand)
        L.append(f"    dugaan P = {_teks_cetak(cand, 36)}")
        L.append(f"             K = {kunci[:18].hex()}{'...' if n > 18 else ''}")
    L.append("  Keduanya konsisten dengan ciphertext yang sama -> tidak ada cara memilih yang benar.")
    crib_b = (crib or "").encode("utf-8")
    if crib_b:
        L.append("")
        L.append("LANGKAH 2 - Known plaintext: sebagian kunci terbuka")
        i = offset
        if i + len(crib_b) > n:
            L.append("  Crib melewati panjang ciphertext; dilewati.")
        else:
            bagian = xor_bytes(data[i:i + len(crib_b)], crib_b)
            L.append(f"  K[{i}..{i + len(crib_b) - 1}] = C XOR crib = {bagian.hex()}")
            L.append(f"  Hanya {len(crib_b)} dari {n} byte kunci yang terbuka; sisanya tetap tidak diketahui.")
    L.append("")
    L.append("CATATAN: OTP menjadi lemah hanya jika kunci dipakai ulang (two-time pad): C1 XOR C2 = P1 XOR P2.")
    return _hasil("5", None, L, None, 0, "OTP: tidak dapat dipecahkan", n, None)


# ----------------------------------------------------------------------
# PENGENDALI: pilih analisis & mode otomatis
# ----------------------------------------------------------------------
_ANALIS = {"1": analisis_caesar, "2": analisis_vigenere, "3": analisis_playfair,
           "4": analisis_hill, "5": analisis_otp, "6": analisis_stream}


def _mirip_hex(teks):
    bersih = "".join(teks.split())
    return (len(bersih) >= 2 and len(bersih) % 2 == 0
            and all(ch in "0123456789abcdefABCDEF" for ch in bersih)
            and any(ch.isdigit() for ch in bersih))


def _analisis_auto(teks, bahasa, crib, offset, daftar):
    L = []
    _judul(L, "ANALISIS OTOMATIS (tanpa kunci)")
    if _mirip_hex(teks):
        L.append("Jenis ciphertext: heksadesimal (ada angka 0-9) -> keluaran One-Time Pad atau Stream Cipher.")
        L.append("Algoritma klasik (Caesar/Vigenere/Playfair/Hill) selalu menghasilkan huruf A-Z saja.")
        st = analisis_stream(teks, bahasa, crib, offset, daftar)
        if st["kunci"] is not None:
            L.append("Seed LCG ditemukan, jadi ini Stream Cipher.")
            st["laporan"] = L + st["laporan"]
            return st
        ot = analisis_otp(teks, bahasa, crib, offset, daftar)
        L.append("Tidak ada seed LCG yang cocok -> kemungkinan One-Time Pad.")
        ot["laporan"] = L + st["laporan"] + ot["laporan"]
        ot["dicoba"] = st["dicoba"]
        return ot
    c = normalisasi(teks)
    L.append("Jenis ciphertext: huruf A-Z -> kandidat Caesar, Vigenere, Playfair, Hill.")
    L += ["  " + x for x in _ciri_ciphertext(c)]
    percobaan = []
    for kode in ("1", "2", "3", "4"):
        if kode == "3" and (len(c) % 2 or "J" in c):
            continue
        if kode == "4" and not (len(c) % 2 == 0 or len(c) % 3 == 0):
            continue
        if kode == "4" and len(c) < 24 and not normalisasi(crib or ""):
            continue
        try:
            percobaan.append(_ANALIS[kode](teks, bahasa, crib, offset, daftar))
        except ValueError:
            continue
    percobaan = [r for r in percobaan if r["kunci"] is not None and r["skor"]]
    if not percobaan:
        raise ValueError("Tidak ada algoritma yang berhasil dianalisis. Coba pilih algoritma secara manual.")
    terbaik = None
    for r in percobaan:
        if terbaik is None or r["skor"]["skor"] > terbaik["skor"]["skor"] + 0.05:
            terbaik = r
    L.append("")
    L.append("PERBANDINGAN HASIL TIAP ALGORITMA (skor kemiripan dengan bahasa alami; makin besar makin baik)")
    L.append(f"  {'algoritma':<10} {'kunci':<18} {'skor':>7} {'kata':>6} {'chi2':>6}  dekripsi")
    for r in percobaan:
        s = r["skor"]
        nama = ALGORITMA[r["kode"]][0]
        mark = "  <== DIPILIH" if r is terbaik else ""
        kunci = r["kunci"] if len(r["kunci"]) <= 18 else r["kunci"][:15] + "..."
        L.append(f"  {nama:<10} {kunci:<18} {s['skor']:>7.3f} {s['kata']:>6.2f} {s['chi2']:>6.2f}{mark}")
    L.append("  Aturan: algoritma yang lebih sederhana dipilih kecuali yang lain jelas lebih baik.")
    terbaik = dict(terbaik)
    terbaik["laporan"] = L + terbaik["laporan"]
    terbaik["dicoba"] = sum(r["dicoba"] for r in percobaan)
    return terbaik


def analisis_ciphertext(pilihan, teks, bahasa="Auto", crib="", offset=0, daftar=None):
    """pilihan: 'auto' atau kode algoritma '1'..'6'. Mengembalikan dict hasil analisis."""
    t0 = time.perf_counter()
    if not teks or not teks.strip():
        raise ValueError("Ciphertext kosong.")
    if pilihan == "auto":
        hasil = _analisis_auto(teks, bahasa, crib, offset, daftar)
    else:
        if pilihan in ("1", "2", "3", "4") and _mirip_hex(teks):
            raise ValueError("Ciphertext berupa heksadesimal (ada angka). Pilih One-Time Pad atau "
                             "Stream Cipher, atau gunakan Auto-detect.")
        hasil = _ANALIS[pilihan](teks, bahasa, crib, offset, daftar)
    hasil["waktu_ms"] = (time.perf_counter() - t0) * 1000
    return hasil



# ----------------------------------------------------------------------
# ADAPTER ANALISIS: jalankan analisis, lalu verifikasi dengan dekripsi backend
# ----------------------------------------------------------------------
def jalankan_analisis(pilihan, teks, path_file, bahasa, crib, offset, path_wordlist):
    """Analisis ciphertext tanpa kunci. Jika kunci ditemukan, plaintext dihitung ulang memakai
    jalankan_dekripsi (backend asli) sehingga hasil dan nama file konsisten dengan tab Decrypt."""
    t_awal = time.perf_counter()
    cipher = baca_teks(path_file) if path_file else teks
    daftar = baca_teks(path_wordlist).split()[:MAKS_KAMUS] if path_wordlist else None
    h = analisis_ciphertext(pilihan, cipher, bahasa, crib, offset, daftar)
    laporan = list(h["laporan"])
    out = {"kode": h["kode"], "algoritma": ALGORITMA[h["kode"]][0], "kunci": h["kunci"],
           "yakin": h["yakin"], "dicoba": h["dicoba"], "waktu_ms": h["waktu_ms"],
           "metode": h["ringkas"], "teks_hasil": "", "bytes_hasil": None,
           "nama_hasil": None, "nama_kunci": None}
    _judul(laporan, "HASIL AKHIR")
    if h["kunci"] is None:
        laporan.append("Kunci   : tidak dapat ditentukan")
        laporan.append("Plaintext: tidak dapat dipulihkan")
    else:
        laporan.append(f"Algoritma: {out['algoritma']}")
        laporan.append(f"Kunci    : {h['kunci']}")
        try:
            d = jalankan_dekripsi(h["kode"], None if path_file else cipher, path_file, h["kunci"])
            out["teks_hasil"], out["bytes_hasil"] = d["teks_hasil"], d["bytes_hasil"]
            out["nama_hasil"] = d["nama_hasil"]
            out["nama_kunci"] = d["nama_hasil"][:-len(".dec.txt")] + ".key.txt"
            tampil = out["teks_hasil"]
            laporan.append("Verifikasi: kunci dipakai pada fungsi dekripsi backend -> berhasil.")
            laporan.append(f"Plaintext: {tampil[:600]}" + ("..." if len(tampil) > 600 else ""))
        except Exception as e:                              # noqa: BLE001
            laporan.append(f"Verifikasi gagal: {pesan_error(e)}")
    out["laporan"] = "\n".join(laporan).lstrip("\n")
    out["waktu_total_s"] = time.perf_counter() - t_awal
    return out


# ----------------------------------------------------------------------
# ASET GAMBAR 
# LOGO_PNG: logo sidebar, EMBLEM_PNG: emblem samar sidebar, IKON_PNG: ikon jendela/taskbar
# ----------------------------------------------------------------------
LOGO_PNG = (
    "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"
)
EMBLEM_PNG = (
    "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"
)
IKON_PNG = (
    "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"
)


def muat_b64(data):
    from PIL import Image
    return Image.open(io.BytesIO(base64.b64decode(data))).convert("RGBA")


def pil_ke_ctk(img, lebar):
    tinggi = round(img.height * lebar / img.width)
    return ctk.CTkImage(light_image=img, dark_image=img, size=(lebar, tinggi))


def kartu(master, **kw):
    return ctk.CTkFrame(master, fg_color=CARD, corner_radius=16, border_width=1,
                        border_color=BORDER, **kw)


def tombol(master, teks, perintah, gaya="neutral", **kw):
    warna = {
        "neutral": (NEUTRAL, NEUTRAL_H, INK),
        "blue": (BLUE, BLUE_H, BLUE_INK),
        "mint": (MINT, MINT_H, MINT_INK),
        "primary": (PRIMARY, PRIMARY_H, "#FFFFFF"),
        "ghost": ("transparent", NEUTRAL, MUTED),
    }[gaya]
    kw.setdefault("height", 38)
    kw.setdefault("corner_radius", 10)
    kw.setdefault("font", fnt(13, "bold" if gaya == "primary" else "normal"))
    return ctk.CTkButton(master, text=teks, command=perintah, fg_color=warna[0],
                         hover_color=warna[1], text_color=warna[2],
                         text_color_disabled="#B9B3A5", **kw)


def kotak_teks(master, mono=False, wrap="word", **kw):
    return ctk.CTkTextbox(master, fg_color=FIELD, border_width=1, border_color=BORDER,
                          text_color=INK, corner_radius=12, wrap=wrap,
                          font=fnt(12 if mono else 13, mono=mono), **kw)


def isi_readonly(tb, teks):
    tb.configure(state="normal")
    tb.delete("1.0", "end")
    tb.insert("1.0", teks)
    tb.configure(state="disabled")


class Toast:
    """Notifikasi singkat di kanan-bawah jendela (klik untuk menutup)."""

    def __init__(self, root):
        self.root = root
        self.frame = None
        self._job = None

    def tutup(self):
        if self._job:
            try:
                self.root.after_cancel(self._job)
            except Exception:
                pass
            self._job = None
        if self.frame is not None:
            self.frame.destroy()
            self.frame = None

    def tampil(self, pesan, jenis="info", ms=None):
        self.tutup()
        bg, garis, teks = TOAST[jenis]
        judul = {"success": "Berhasil", "error": "Gagal", "info": "Info"}[jenis]
        f = ctk.CTkFrame(self.root, fg_color=bg, corner_radius=14, border_width=1,
                         border_color=garis)
        ctk.CTkLabel(f, text=judul, font=fnt(13, "bold"), text_color=teks,
                     anchor="w").pack(fill="x", padx=18, pady=(12, 0))
        ctk.CTkLabel(f, text=pesan, font=fnt(12), text_color=teks, anchor="w",
                     justify="left", wraplength=360).pack(fill="x", padx=18, pady=(2, 12))
        f.place(relx=1.0, rely=1.0, anchor="se", x=-24, y=-24)
        f.lift()
        for w in (f, *f.winfo_children()):
            w.bind("<Button-1>", lambda _e: self.tutup())
        self.frame = f
        self._job = self.root.after(ms or (7000 if jenis == "error" else 3500), self.tutup)


class BarisMetrik(ctk.CTkFrame):
    def __init__(self, master, judul, warna):
        super().__init__(master, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self, text=judul, font=fnt(13), text_color=INK,
                     anchor="w").grid(row=0, column=0, sticky="w")
        self.nilai = ctk.CTkLabel(self, text="-", font=fnt(13, "bold"), text_color=INK,
                                  anchor="e")
        self.nilai.grid(row=0, column=1, sticky="e")
        self.bar = ctk.CTkProgressBar(self, height=6, corner_radius=3, fg_color="#E4DDCB",
                                      progress_color=warna)
        self.bar.set(0)
        self.bar.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(4, 0))

    def set(self, teks, frak):
        self.nilai.configure(text=teks)
        self.bar.set(frak)


# ======================================================================
# HALAMAN ENCRYPT / DECRYPT
# ======================================================================
class HalamanKripto(ctk.CTkFrame):
    def __init__(self, master, app, mode):
        super().__init__(master, fg_color=BG, corner_radius=0)
        self.app = app
        self.mode = mode                      # "encrypt" | "decrypt"
        self.file_path = None
        self.key_full = None                  # kunci panjang yang disimpan di memori
        self.hasil = None
        self.running = False
        enc = mode == "encrypt"
        self.teks_run = "Run Encryption" if enc else "Run Decryption"

        self.grid_columnconfigure(0, weight=3, uniform="kol")
        self.grid_columnconfigure(1, weight=2, uniform="kol")
        self.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(self, text="Encrypt" if enc else "Decrypt", font=fnt(28, "bold"),
                     text_color=INK, anchor="w").grid(row=0, column=0, columnspan=2,
                                                      sticky="w", padx=28, pady=(24, 10))

        kiri = ctk.CTkFrame(self, fg_color="transparent")
        kiri.grid(row=1, column=0, sticky="nsew", padx=(28, 10), pady=(0, 22))
        kiri.grid_columnconfigure(0, weight=1)
        kiri.grid_rowconfigure(0, weight=1)
        kanan = ctk.CTkFrame(self, fg_color="transparent")
        kanan.grid(row=1, column=1, sticky="nsew", padx=(10, 28), pady=(0, 22))
        kanan.grid_columnconfigure(0, weight=1)
        kanan.grid_rowconfigure(1, weight=1)

        self._bangun_input(kiri)
        self._bangun_kunci(kiri)
        self._bangun_metrik(kanan)
        self._bangun_hasil(kanan)
        self._bangun_aksi(kanan)
        self._ganti_algoritma()

    # ------------------------------------------------------------ kartu input
    def _bangun_input(self, induk):
        k = kartu(induk)
        k.grid(row=0, column=0, sticky="nsew", pady=(0, 14))
        k.grid_columnconfigure(0, weight=1)
        k.grid_rowconfigure(3, weight=1)
        pad = {"padx": 20}

        ctk.CTkLabel(k, text="Cryptography Algorithm", font=fnt(14, "bold"), text_color=INK,
                     anchor="w").grid(row=0, column=0, sticky="w", pady=(16, 6), **pad)
        self.algo_var = ctk.StringVar(value="Caesar Cipher")
        ctk.CTkOptionMenu(
            k, values=list(NAMA_ALGO), variable=self.algo_var,
            command=lambda _v: self._ganti_algoritma(), height=38, corner_radius=10,
            fg_color=NEUTRAL, button_color=NEUTRAL_H, button_hover_color="#DAD3BE",
            text_color=INK, dropdown_fg_color=CARD, dropdown_hover_color=BLUE,
            dropdown_text_color=INK, font=fnt(13), dropdown_font=fnt(13), anchor="w",
        ).grid(row=1, column=0, sticky="ew", **pad)

        judul = "Enter Plaintext" if self.mode == "encrypt" else \
            "Enter Ciphertext (hex untuk OTP / Stream)"
        ctk.CTkLabel(k, text=judul, font=fnt(14, "bold"), text_color=INK,
                     anchor="w").grid(row=2, column=0, sticky="w", pady=(14, 6), **pad)
        self.input = kotak_teks(k, height=120)
        self.input.grid(row=3, column=0, sticky="nsew", **pad)

        baris = ctk.CTkFrame(k, fg_color="transparent")
        baris.grid(row=4, column=0, sticky="ew", pady=(10, 16), **pad)
        baris.grid_columnconfigure(1, weight=1)
        tombol(baris, "Upload .txt File", self._upload_input, "blue",
               width=150).grid(row=0, column=0)
        self.lbl_file = ctk.CTkLabel(baris, text="Belum ada file - ketik teks di atas atau unggah file",
                                     font=fnt(12), text_color=MUTED, anchor="w")
        self.lbl_file.grid(row=0, column=1, sticky="w", padx=12)
        self.btn_hapus_file = tombol(baris, "Remove", self._hapus_file, "ghost", width=70,
                                     height=30)
        self.btn_hapus_file.grid(row=0, column=2)
        self.btn_hapus_file.grid_remove()

    # ------------------------------------------------------------ kartu kunci
    def _bangun_kunci(self, induk):
        k = kartu(induk)
        k.grid(row=1, column=0, sticky="ew")
        k.grid_columnconfigure(0, weight=1)
        pad = {"padx": 20}

        ctk.CTkLabel(k, text="Key Configuration", font=fnt(16, "bold"), text_color=INK,
                     anchor="w").grid(row=0, column=0, columnspan=2, sticky="w",
                                      pady=(16, 0), **pad)
        ctk.CTkLabel(k, text="Cryptographic Key (Manual Input)", font=fnt(13),
                     text_color=INK, anchor="w").grid(row=1, column=0, columnspan=2,
                                                      sticky="w", pady=(2, 6), **pad)
        self.keybox = kotak_teks(k, mono=True, height=84, wrap="char")
        self.keybox.grid(row=2, column=0, sticky="nsew", padx=(20, 10))

        sisi = ctk.CTkFrame(k, fg_color="transparent")
        sisi.grid(row=2, column=1, sticky="n", padx=(0, 20))
        self.btn_gen = tombol(sisi, "Generate Random Key", self._generate_kunci, "mint",
                              width=190)
        self.btn_gen.grid(row=0, column=0, pady=(0, 6))
        tombol(sisi, "Upload Key File", self._upload_kunci, "neutral",
               width=190).grid(row=1, column=0, pady=(0, 6))
        tombol(sisi, "Clear Key", self._hapus_kunci, "ghost", width=190,
               height=28).grid(row=2, column=0)

        self.lbl_hint = ctk.CTkLabel(k, text="", font=fnt(12), text_color=MUTED, anchor="w",
                                     justify="left", wraplength=470)
        self.lbl_hint.grid(row=3, column=0, columnspan=2, sticky="w", pady=(8, 16), **pad)

    # ------------------------------------------------------------ metrik
    def _bangun_metrik(self, induk):
        k = ctk.CTkFrame(induk, fg_color=METRIK_BG, corner_radius=16, border_width=1,
                         border_color=BORDER)
        k.grid(row=0, column=0, sticky="ew", pady=(0, 14))
        k.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(k, text="Performance Metrics", font=fnt(18, "bold"), text_color=INK,
                     anchor="w").grid(row=0, column=0, sticky="w", padx=20, pady=(16, 8))
        self.m_proses = BarisMetrik(k, "Processing Time (ms)", "#8FA2E6")
        self.m_thr = BarisMetrik(k, "Throughput (KB/s)", "#8FA2E6")
        self.m_ukuran = BarisMetrik(k, "File Size", "#7CCBA0")
        self.m_total = BarisMetrik(k, "Time Taken", "#7CCBA0")
        for i, m in enumerate((self.m_proses, self.m_thr, self.m_ukuran, self.m_total), 1):
            m.grid(row=i, column=0, sticky="ew", padx=20, pady=(0, 9 if i < 4 else 18))

    # ------------------------------------------------------------ hasil
    def _bangun_hasil(self, induk):
        k = kartu(induk)
        k.grid(row=1, column=0, sticky="nsew", pady=(0, 14))
        k.grid_columnconfigure(0, weight=1)
        k.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(k, text="Results Area", font=fnt(18, "bold"), text_color=INK,
                     anchor="w").grid(row=0, column=0, columnspan=2, sticky="w", padx=20,
                                      pady=(16, 0))
        ctk.CTkLabel(k, text="Output Results", font=fnt(13), text_color=MUTED,
                     anchor="w").grid(row=1, column=0, sticky="w", padx=20, pady=(0, 6))
        self.btn_copy = tombol(k, "Copy to Clipboard", self._salin, "neutral", width=140,
                               height=30, state="disabled")
        self.btn_copy.grid(row=1, column=1, sticky="e", padx=(0, 20), pady=(0, 6))

        self.output = kotak_teks(k, mono=True, wrap="char", height=90, state="disabled")
        self.output.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20)

        self.lbl_judul_hasil = ctk.CTkLabel(
            k, text="Encryption Result" if self.mode == "encrypt" else "Decryption Result",
            font=fnt(13, "bold"), text_color=INK, anchor="w")
        self.lbl_judul_hasil.grid(row=3, column=0, columnspan=2, sticky="w", padx=20,
                                  pady=(10, 0))
        self.lbl_ringkas = ctk.CTkLabel(
            k, text="File size: -\nTime taken: -\nStatus: menunggu proses", font=fnt(12),
            text_color=INK, anchor="w", justify="left", wraplength=360)
        self.lbl_ringkas.grid(row=4, column=0, columnspan=2, sticky="w", padx=20, pady=(2, 8))

        baris = ctk.CTkFrame(k, fg_color="transparent")
        baris.grid(row=5, column=0, columnspan=2, sticky="ew", padx=20, pady=(0, 16))
        self.btn_dl = tombol(baris, "Download Result", self._unduh_hasil, "blue", width=150,
                             state="disabled")
        self.btn_dl.grid(row=0, column=0, padx=(0, 8))
        self.btn_dlkey = tombol(baris, "Download Key", self._unduh_kunci, "neutral", width=130,
                                state="disabled")
        if self.mode == "encrypt":
            self.btn_dlkey.grid(row=0, column=1)

    # ------------------------------------------------------------ aksi
    def _bangun_aksi(self, induk):
        baris = ctk.CTkFrame(induk, fg_color="transparent")
        baris.grid(row=2, column=0, sticky="ew")
        baris.grid_columnconfigure(0, weight=1)
        self.btn_run = tombol(baris, self.teks_run, self._run, "primary", height=44)
        self.btn_run.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        tombol(baris, "Reset Input", self._reset, "neutral", height=44, width=120,
               border_width=1, border_color=BORDER).grid(row=0, column=1)

    # ================================================================ logika
    def kode(self):
        return NAMA_ALGO[self.algo_var.get()]

    def _ganti_algoritma(self):
        kode = self.kode()
        enc = self.mode == "encrypt"
        if kode == "5":
            hint = ("Kunci dibangkitkan otomatis sepanjang pesan jika dikosongkan. "
                    "Atau klik Generate / unggah kunci hex sendiri."
                    if enc else
                    "Tempel kunci OTP (hex) atau unggah file .key.txt. "
                    "Panjangnya harus sama dengan ciphertext.")
        else:
            label, contoh = PROMPT_KUNCI[kode]
            hint = f"{label}. Contoh: {contoh}"
        self.lbl_hint.configure(text=hint)
        self.btn_gen.configure(state="normal" if enc else "disabled")

    # ---- input
    def _teks_input(self):
        return self.input.get("1.0", "end-1c")

    def _upload_input(self):
        p = filedialog.askopenfilename(
            parent=self.app, title="Pilih file .txt",
            filetypes=[("Text file", "*.txt"), ("Semua file", "*.*")])
        if not p:
            return
        try:
            ukuran = os.path.getsize(p)
            with open(p, "rb") as f:
                mentah = f.read(BATAS_PRATINJAU * 4)
        except OSError as e:
            self.app.toast.tampil(pesan_error(e), "error")
            return
        pratinjau = mentah.decode("utf-8-sig", errors="replace")[:BATAS_PRATINJAU]
        if ukuran > len(mentah) or len(pratinjau) >= BATAS_PRATINJAU:
            pratinjau += "\n\n... (pratinjau dipotong; seluruh isi file tetap diproses)"
        self.file_path = p
        isi_readonly(self.input, pratinjau)
        self.lbl_file.configure(
            text=f"{os.path.basename(p)}  ({fmt_ukuran(ukuran)}) - pratinjau, tidak bisa diedit",
            text_color=BLUE_INK)
        self.btn_hapus_file.grid()
        self.app.toast.tampil(f"File dimuat: {os.path.basename(p)}", "info")

    def _hapus_file(self):
        self.file_path = None
        self.input.configure(state="normal")
        self.input.delete("1.0", "end")
        self.lbl_file.configure(text="Belum ada file - ketik teks di atas atau unggah file",
                                text_color=MUTED)
        self.btn_hapus_file.grid_remove()

    # ---- kunci
    def set_kunci(self, teks):
        self.keybox.configure(state="normal")
        self.keybox.delete("1.0", "end")
        if len(teks) > BATAS_KUNCI:
            self.key_full = teks
            self.keybox.insert(
                "1.0", teks[:200] + f"...\n[Kunci panjang: {len(teks):,} karakter - "
                                    f"tersimpan penuh di memori]")
            self.keybox.configure(state="disabled")
        else:
            self.key_full = None
            self.keybox.insert("1.0", teks)

    def get_kunci(self):
        if self.key_full is not None:
            return self.key_full
        return self.keybox.get("1.0", "end-1c").strip()

    def _hapus_kunci(self):
        self.set_kunci("")

    def _generate_kunci(self):
        kode = self.kode()
        n = 0
        if kode == "5":
            if self.file_path:
                try:
                    n = os.path.getsize(self.file_path)
                except OSError as e:
                    self.app.toast.tampil(pesan_error(e), "error")
                    return
            else:
                n = len(self._teks_input().encode("utf-8"))
            if n == 0:
                self.app.toast.tampil(
                    "Isi teks atau unggah file dulu - panjang kunci OTP harus sama "
                    "dengan panjang pesan.", "info")
                return
        self.set_kunci(kunci_acak(kode, n))
        self.app.toast.tampil("Kunci acak dibuat.", "success")

    def _upload_kunci(self):
        p = filedialog.askopenfilename(
            parent=self.app, title="Pilih file kunci",
            filetypes=[("Text file", "*.txt"), ("Semua file", "*.*")])
        if not p:
            return
        try:
            if self.kode() == "5":
                teks = baca_hex(p).hex()            
            else:
                teks = " ".join(baca_teks(p).split())
        except Exception as e:                        
            self.app.toast.tampil(pesan_error(e), "error")
            return
        if not teks:
            self.app.toast.tampil("File kunci kosong.", "error")
            return
        self.set_kunci(teks)
        self.app.toast.tampil(f"Kunci dimuat dari {os.path.basename(p)}", "info")

    # ---- proses
    def _run(self):
        if self.running:
            return
        kode = self.kode()
        teks = None if self.file_path else self._teks_input()
        if not self.file_path and not teks:
            self.app.toast.tampil("Masukkan teks atau unggah file .txt terlebih dahulu.", "error")
            return
        kunci = self.get_kunci()
        enc = self.mode == "encrypt"
        if not kunci and not (enc and kode == "5"):
            self.app.toast.tampil(
                "Kunci masih kosong. Isi kunci, unggah file kunci, atau klik Generate "
                "Random Key.", "error")
            return

        self._bersihkan_hasil()
        self.running = True
        self.btn_run.configure(state="disabled", text="Processing...")
        self.lbl_ringkas.configure(text="File size: -\nTime taken: -\nStatus: memproses...")
        fn = jalankan_enkripsi if enc else jalankan_dekripsi
        self.app.jalankan_tugas(lambda: fn(kode, teks, self.file_path, kunci),
                                self._selesai, self._gagal)

    def _selesai(self, h):
        self.running = False
        self.btn_run.configure(state="normal", text=self.teks_run)
        self.hasil = h
        teks = h["teks_hasil"]
        if len(teks) > BATAS_TAMPIL:
            teks = (teks[:BATAS_TAMPIL] + f"\n\n... (ditampilkan {BATAS_TAMPIL:,} dari "
                                          f"{len(h['teks_hasil']):,} karakter; gunakan Download "
                                          f"Result untuk hasil lengkap)")
        isi_readonly(self.output, teks)

        ms = h["waktu_ms"]
        thr = (h["ukuran_in"] / 1024) / (ms / 1000) if ms > 0 else None
        self.m_proses.set(f"{ms:,.4f}", frak_log(ms, 0.01, 5000))
        self.m_thr.set(f"{thr:,.1f}" if thr else "-", frak_log(thr, 10, 1e6))
        self.m_ukuran.set(fmt_ukuran(h["ukuran_in"]), frak_log(h["ukuran_in"], 10, 1e8))
        self.m_total.set(fmt_durasi(h["waktu_total_s"]), frak_log(h["waktu_total_s"], 1e-3, 30))

        self.lbl_ringkas.configure(
            text=(f"Algorithm: {h['algoritma']}\n"
                  f"File size: {fmt_ukuran(h['ukuran_in'])} (input) -> "
                  f"{fmt_ukuran(h['ukuran_out'])} (output)\n"
                  f"Time taken: {fmt_durasi(h['waktu_total_s'])}\n"
                  f"Status: Success"))
        self.btn_copy.configure(state="normal")
        self.btn_dl.configure(state="normal")
        if h["kunci_simpan"]:
            self.btn_dlkey.configure(state="normal")
        aksi = "Enkripsi" if self.mode == "encrypt" else "Dekripsi"
        pesan = f"{aksi} selesai dalam {ms:.3f} ms."
        if self.mode == "encrypt" and h["algoritma"].startswith("One-Time") \
                and not self.get_kunci():
            pesan += " Kunci OTP dibangkitkan otomatis - simpan lewat Download Key!"
        self.app.toast.tampil(pesan, "success")

    def _gagal(self, e):
        self.running = False
        self.btn_run.configure(state="normal", text=self.teks_run)
        msg = pesan_error(e)
        self.lbl_ringkas.configure(text=f"File size: -\nTime taken: -\nStatus: Failed")
        self.app.toast.tampil(msg, "error")

    def _bersihkan_hasil(self):
        self.hasil = None
        isi_readonly(self.output, "")
        for m in (self.m_proses, self.m_thr, self.m_ukuran, self.m_total):
            m.set("-", 0)
        for b in (self.btn_copy, self.btn_dl, self.btn_dlkey):
            b.configure(state="disabled")
        self.lbl_ringkas.configure(text="File size: -\nTime taken: -\nStatus: menunggu proses")

    def _reset(self):
        if self.running:
            return
        self._hapus_file()
        self.set_kunci("")
        self._bersihkan_hasil()

    # ---- keluaran
    def _salin(self):
        if not self.hasil:
            return
        self.app.clipboard_clear()
        self.app.clipboard_append(self.hasil["teks_hasil"])
        self.app.toast.tampil("Hasil disalin ke clipboard.", "success", 2000)

    def _simpan(self, judul, nama_awal, tulis):
        path = filedialog.asksaveasfilename(
            parent=self.app, title=judul, initialfile=nama_awal, defaultextension=".txt",
            filetypes=[("Text file", "*.txt"), ("Semua file", "*.*")])
        if not path:
            return
        try:
            tulis(path)
        except OSError as e:
            self.app.toast.tampil(f"Gagal menyimpan: {pesan_error(e)}", "error")
            return
        self.app.toast.tampil(f"Tersimpan: {path}", "success")

    def _unduh_hasil(self):
        if self.hasil:
            h = self.hasil
            self._simpan("Simpan hasil", h["nama_hasil"],
                         lambda p: tulis_bytes(p, h["bytes_hasil"]))

    def _unduh_kunci(self):
        if self.hasil and self.hasil["kunci_simpan"]:
            h = self.hasil
            self._simpan("Simpan kunci", h["nama_kunci"],
                         lambda p: tulis_teks(p, h["kunci_simpan"] + "\n"))


# ======================================================================
# HALAMAN DEMO dan BENCHMARK 
# ======================================================================
class HalamanLog(ctk.CTkFrame):
    def __init__(self, master, app, judul, deskripsi, wrap):
        super().__init__(master, fg_color=BG, corner_radius=0)
        self.app = app
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        ctk.CTkLabel(self, text=judul, font=fnt(28, "bold"), text_color=INK,
                     anchor="w").grid(row=0, column=0, sticky="w", padx=28, pady=(24, 10))

        panel = kartu(self)
        panel.grid(row=1, column=0, sticky="ew", padx=28, pady=(0, 14))
        panel.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(panel, text=deskripsi, font=fnt(13), text_color=MUTED, anchor="w",
                     justify="left", wraplength=820).grid(row=0, column=0, sticky="w",
                                                          padx=20, pady=(16, 10))
        self.kontrol = ctk.CTkFrame(panel, fg_color="transparent")
        self.kontrol.grid(row=1, column=0, sticky="w", padx=20, pady=(0, 10))
        self.progress = ctk.CTkProgressBar(panel, height=6, corner_radius=3, fg_color="#E4DDCB",
                                           progress_color="#8FA2E6", mode="indeterminate")
        self.progress.set(0)
        self.progress.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 16))

        hasil = kartu(self)
        hasil.grid(row=2, column=0, sticky="nsew", padx=28, pady=(0, 22))
        hasil.grid_columnconfigure(0, weight=1)
        hasil.grid_rowconfigure(0, weight=1)
        self.output = kotak_teks(hasil, mono=True, wrap=wrap, state="disabled")
        self.output.grid(row=0, column=0, sticky="nsew", padx=14, pady=14)

    def tombol_run(self, teks, perintah):
        self.btn_run = tombol(self.kontrol, teks, perintah, "primary", width=170)
        self.btn_run.grid(row=0, column=0, padx=(0, 8))
        self._teks_run = teks

    def tambah(self, teks):
        self.output.configure(state="normal")
        self.output.insert("end", teks)
        self.output.see("end")
        self.output.configure(state="disabled")

    def mulai(self, fn, on_selesai):
        if self.app.busy:
            self.app.toast.tampil("Masih ada proses Demo/Benchmark yang berjalan.", "info")
            return
        self.app.busy = True
        isi_readonly(self.output, "")
        self.btn_run.configure(state="disabled", text="Running...")
        self.progress.start()

        def selesai(hasil):
            self._akhir()
            on_selesai(hasil)

        def gagal(e):
            self._akhir()
            self.tambah(f"\n[ERROR] {pesan_error(e)}\n")
            self.app.toast.tampil(pesan_error(e), "error")

        self.app.jalankan_tugas(fn, selesai, gagal, on_log=self.tambah)

    def _akhir(self):
        self.app.busy = False
        self.progress.stop()
        self.progress.set(0)
        self.btn_run.configure(state="normal", text=self._teks_run)

    def salin(self):
        self.app.clipboard_clear()
        self.app.clipboard_append(self.output.get("1.0", "end-1c"))
        self.app.toast.tampil("Output disalin ke clipboard.", "success", 2000)

    def simpan(self, judul, nama, ekstensi, isi):
        if not isi:
            self.app.toast.tampil("Belum ada data untuk disimpan. Jalankan dulu.", "info")
            return
        path = filedialog.asksaveasfilename(
            parent=self.app, title=judul, initialfile=nama, defaultextension=ekstensi,
            filetypes=[(f"File {ekstensi}", f"*{ekstensi}"), ("Semua file", "*.*")])
        if not path:
            return
        try:
            tulis_teks(path, isi)
        except OSError as e:
            self.app.toast.tampil(f"Gagal menyimpan: {pesan_error(e)}", "error")
            return
        self.app.toast.tampil(f"Tersimpan: {path}", "success")


class HalamanDemo(HalamanLog):
    def __init__(self, master, app):
        super().__init__(
            master, app, "Demo",
            "Menjalankan demo_belajar_kriptografi(): pesan \"BELAJAR KRIPTOGRAFI\" dienkripsi "
            "lalu didekripsi dengan keenam algoritma, lengkap dengan kunci, ciphertext, dan waktu.",
            wrap="word")
        self.tombol_run("Run Demo", self._run)
        tombol(self.kontrol, "Copy Output", self.salin, "neutral",
               width=120).grid(row=0, column=1, padx=(0, 8))
        tombol(self.kontrol, "Save Log", self._simpan_log, "blue",
               width=110).grid(row=0, column=2)

    def _run(self):
        self.mulai(jalankan_demo, lambda _h: self.app.toast.tampil("Demo selesai.", "success"))

    def _simpan_log(self):
        self.simpan("Simpan log demo", "demo_cryptozar.txt", ".txt",
                    self.output.get("1.0", "end-1c"))


class HalamanBenchmark(HalamanLog):
    def __init__(self, master, app):
        super().__init__(
            master, app, "Benchmark",
            "Menjalankan ukur_beban_komputasi(): waktu, memori puncak, dan ukuran kunci/ciphertext "
            "semua algoritma pada beberapa ukuran data (median dari beberapa kali ulang). "
            "Ukuran 1 MiB bisa memakan waktu cukup lama pada cipher klasik.",
            wrap="none")
        self.csv_text = ""
        self.tombol_run("Run Benchmark", self._run)
        self.sw = ctk.CTkSwitch(self.kontrol, text="Sertakan 1 MiB", font=fnt(13),
                                text_color=INK, progress_color="#8FA2E6")
        self.sw.grid(row=0, column=1, padx=(14, 14))
        ctk.CTkLabel(self.kontrol, text="Ulang:", font=fnt(13), text_color=INK).grid(
            row=0, column=2, padx=(0, 6))
        self.seg = ctk.CTkSegmentedButton(
            self.kontrol, values=["3", "5", "10"], font=fnt(13), fg_color=NEUTRAL,
            selected_color=BLUE, selected_hover_color=BLUE_H, unselected_color=NEUTRAL,
            unselected_hover_color=NEUTRAL_H, text_color=INK)
        self.seg.set("5")
        self.seg.grid(row=0, column=3, padx=(0, 14))
        tombol(self.kontrol, "Copy Output", self.salin, "neutral",
               width=110).grid(row=0, column=4, padx=(0, 8))
        tombol(self.kontrol, "Save CSV", self._simpan_csv, "blue",
               width=100).grid(row=0, column=5)

    def _run(self):
        besar = bool(self.sw.get())
        ulang = int(self.seg.get())
        self.csv_text = ""

        def selesai(csv_text):
            self.csv_text = csv_text
            self.app.toast.tampil("Benchmark selesai. Klik Save CSV untuk menyimpan tabel.",
                                  "success")

        self.mulai(lambda: jalankan_benchmark(besar, ulang), selesai)

    def _simpan_csv(self):
        self.simpan("Simpan tabel benchmark", "hasil_beban_komputasi.csv", ".csv", self.csv_text)


# ======================================================================
# HALAMAN ANALYZE (kriptanalisis tanpa kunci)
# ======================================================================
NAMA_ANALISIS = {"Auto-detect": "auto", **NAMA_ALGO}
PILIHAN_BAHASA = {"Auto (Indonesia / English)": "Auto", "Indonesia": "Indonesia",
                  "English": "English"}
HINT_ANALISIS = {
    "auto": "Otomatis: mengenali jenis ciphertext (huruf atau heksadesimal), mencoba algoritma yang "
            "mungkin, lalu memilih hasil yang paling terbaca.",
    "1": "Brute force 26 geseran; tabel semua kandidat ditampilkan. Beberapa kata sudah cukup.",
    "2": "Kasiski + Index of Coincidence + frekuensi per kolom + serangan kamus. Idealnya 100+ huruf.",
    "3": "Playfair tidak bisa diserang dengan frekuensi huruf. Serangan kamus: kata kunci yang tidak "
         "ada di daftar tidak bisa ditemukan (unggah wordlist untuk memperluas).",
    "4": "Dengan crib (potongan plaintext yang diketahui, 6-12 huruf) kunci dihitung eksak. Tanpa crib: "
         "serangan statistik, butuh teks panjang.",
    "5": "OTP tidak dapat dipecahkan. Aplikasi menjelaskan alasannya; crib hanya membuka sebagian kunci.",
    "6": "Ciphertext heksadesimal. Brute force 256 seed; crib mempercepat dan memastikan seed.",
}


class HalamanAnalisis(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color=BG, corner_radius=0)
        self.app = app
        self.file_path = None
        self.wordlist_path = None
        self.hasil = None
        self.running = False
        self.laporan = ""
        self.plain_tampil = ""

        self.grid_columnconfigure(0, weight=3, uniform="kol")
        self.grid_columnconfigure(1, weight=2, uniform="kol")
        self.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(self, text="Analyze", font=fnt(28, "bold"), text_color=INK,
                     anchor="w").grid(row=0, column=0, columnspan=2, sticky="w", padx=28,
                                      pady=(24, 10))
        self._bangun_input()
        kanan = ctk.CTkFrame(self, fg_color="transparent")
        kanan.grid(row=1, column=1, sticky="nsew", padx=(10, 28), pady=(0, 14))
        kanan.grid_columnconfigure(0, weight=1)
        kanan.grid_rowconfigure(0, weight=1)
        self._bangun_ringkasan(kanan)
        self._bangun_aksi(kanan)
        self._bangun_laporan()
        self._ganti_algoritma()
        self._tampil_awal()

    # ------------------------------------------------------------ input
    def _bangun_input(self):
        k = kartu(self)
        k.grid(row=1, column=0, sticky="nsew", padx=(28, 10), pady=(0, 14))
        k.grid_columnconfigure(0, weight=1)
        k.grid_rowconfigure(3, weight=1)
        pad = {"padx": 20}

        baris = ctk.CTkFrame(k, fg_color="transparent")
        baris.grid(row=0, column=0, sticky="ew", pady=(16, 0), **pad)
        baris.grid_columnconfigure(0, weight=3)
        baris.grid_columnconfigure(1, weight=2)
        ctk.CTkLabel(baris, text="Cryptography Algorithm", font=fnt(14, "bold"), text_color=INK,
                     anchor="w").grid(row=0, column=0, sticky="w", pady=(0, 6))
        ctk.CTkLabel(baris, text="Bahasa Plaintext", font=fnt(14, "bold"), text_color=INK,
                     anchor="w").grid(row=0, column=1, sticky="w", padx=(10, 0), pady=(0, 6))
        gaya = dict(height=38, corner_radius=10, fg_color=NEUTRAL, button_color=NEUTRAL_H,
                    button_hover_color="#DAD3BE", text_color=INK, dropdown_fg_color=CARD,
                    dropdown_hover_color=BLUE, dropdown_text_color=INK, font=fnt(13),
                    dropdown_font=fnt(13), anchor="w")
        self.algo_var = ctk.StringVar(value="Auto-detect")
        ctk.CTkOptionMenu(baris, values=list(NAMA_ANALISIS), variable=self.algo_var,
                          command=lambda _v: self._ganti_algoritma(), **gaya
                          ).grid(row=1, column=0, sticky="ew")
        self.bahasa_var = ctk.StringVar(value="Auto (Indonesia / English)")
        ctk.CTkOptionMenu(baris, values=list(PILIHAN_BAHASA), variable=self.bahasa_var, **gaya
                          ).grid(row=1, column=1, sticky="ew", padx=(10, 0))

        ctk.CTkLabel(k, text="Ciphertext (tanpa kunci)", font=fnt(14, "bold"), text_color=INK,
                     anchor="w").grid(row=2, column=0, sticky="w", pady=(12, 6), **pad)
        self.input = kotak_teks(k, mono=True, wrap="char", height=90)
        self.input.grid(row=3, column=0, sticky="nsew", **pad)

        up = ctk.CTkFrame(k, fg_color="transparent")
        up.grid(row=4, column=0, sticky="ew", pady=(10, 4), **pad)
        up.grid_columnconfigure(1, weight=1)
        tombol(up, "Upload .txt File", self._upload_input, "blue", width=150).grid(row=0, column=0)
        self.lbl_file = ctk.CTkLabel(up, text="Belum ada file - tempel ciphertext di atas",
                                     font=fnt(12), text_color=MUTED, anchor="w")
        self.lbl_file.grid(row=0, column=1, sticky="w", padx=12)
        self.btn_hapus_file = tombol(up, "Remove", self._hapus_file, "ghost", width=70, height=30)
        self.btn_hapus_file.grid(row=0, column=2)
        self.btn_hapus_file.grid_remove()

        ctk.CTkLabel(k, text="Informasi Tambahan (opsional)", font=fnt(14, "bold"),
                     text_color=INK, anchor="w").grid(row=5, column=0, sticky="w",
                                                      pady=(10, 6), **pad)
        crib = ctk.CTkFrame(k, fg_color="transparent")
        crib.grid(row=6, column=0, sticky="ew", **pad)
        crib.grid_columnconfigure(0, weight=1)
        ent = dict(height=36, corner_radius=10, fg_color=FIELD, border_color=BORDER,
                   border_width=1, text_color=INK, placeholder_text_color=MUTED, font=fnt(13))
        self.ent_crib = ctk.CTkEntry(crib, placeholder_text="Known plaintext / crib (mis. BELAJAR)",
                                     **ent)
        self.ent_crib.grid(row=0, column=0, sticky="ew")
        self.ent_offset = ctk.CTkEntry(crib, placeholder_text="Posisi (0)", width=100, **ent)
        self.ent_offset.grid(row=0, column=1, padx=(10, 0))

        wl = ctk.CTkFrame(k, fg_color="transparent")
        wl.grid(row=7, column=0, sticky="ew", pady=(8, 0), **pad)
        wl.grid_columnconfigure(1, weight=1)
        self.btn_wordlist = tombol(wl, "Upload Wordlist .txt", self._upload_wordlist, "neutral",
                                   width=170)
        self.btn_wordlist.grid(row=0, column=0)
        self.lbl_wordlist = ctk.CTkLabel(wl, text="Opsional: daftar kata kunci untuk serangan kamus",
                                         font=fnt(12), text_color=MUTED, anchor="w")
        self.lbl_wordlist.grid(row=0, column=1, sticky="w", padx=12)
        self.btn_hapus_wl = tombol(wl, "Remove", self._hapus_wordlist, "ghost", width=70, height=30)
        self.btn_hapus_wl.grid(row=0, column=2)
        self.btn_hapus_wl.grid_remove()

        self.lbl_hint = ctk.CTkLabel(k, text="", font=fnt(12), text_color=MUTED, anchor="w",
                                     justify="left", wraplength=560)
        self.lbl_hint.grid(row=8, column=0, sticky="w", pady=(8, 14), **pad)

    # ------------------------------------------------------------ ringkasan
    def _bangun_ringkasan(self, induk):
        k = ctk.CTkFrame(induk, fg_color=METRIK_BG, corner_radius=16, border_width=1,
                         border_color=BORDER)
        k.grid(row=0, column=0, sticky="nsew", pady=(0, 14))
        k.grid_columnconfigure(1, weight=1)
        ctk.CTkLabel(k, text="Hasil Analisis", font=fnt(18, "bold"), text_color=INK,
                     anchor="w").grid(row=0, column=0, columnspan=2, sticky="w", padx=20,
                                      pady=(16, 8))
        self.nilai = {}
        for i, (kunci, judul) in enumerate((("algo", "Algoritma"), ("metode", "Metode"),
                                            ("kunci", "Kunci ditemukan"), ("yakin", "Keyakinan"),
                                            ("dicoba", "Kandidat dicoba"),
                                            ("waktu", "Waktu proses")), 1):
            ctk.CTkLabel(k, text=judul, font=fnt(12), text_color=MUTED, anchor="w").grid(
                row=i, column=0, sticky="nw", padx=(20, 10), pady=2)
            besar = kunci == "kunci"
            lbl = ctk.CTkLabel(k, text="-", font=fnt(15 if besar else 13, "bold", mono=besar),
                               text_color=INK, anchor="w", justify="left", wraplength=250)
            lbl.grid(row=i, column=1, sticky="w", padx=(0, 20), pady=2)
            self.nilai[kunci] = lbl
        tb = ctk.CTkFrame(k, fg_color="transparent")
        tb.grid(row=7, column=0, columnspan=2, sticky="ew", padx=20, pady=(10, 16))
        tb.grid_columnconfigure((0, 1), weight=1)
        self.btn_copy_key = tombol(tb, "Copy Key", self._salin_kunci, "neutral", height=34,
                                   state="disabled")
        self.btn_copy_key.grid(row=0, column=0, sticky="ew", padx=(0, 4))
        self.btn_dl_key = tombol(tb, "Download Key", self._unduh_kunci, "blue", height=34,
                                 state="disabled")
        self.btn_dl_key.grid(row=0, column=1, sticky="ew", padx=(4, 0))
        self.btn_dl_plain = tombol(tb, "Download Plaintext", self._unduh_plain, "blue", height=34,
                                   state="disabled")
        self.btn_dl_plain.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(8, 0))

    def _bangun_aksi(self, induk):
        k = kartu(induk)
        k.grid(row=1, column=0, sticky="ew")
        k.grid_columnconfigure(0, weight=1)
        self.btn_run = tombol(k, "Run Analysis", self._run, "primary", height=44)
        self.btn_run.grid(row=0, column=0, sticky="ew", padx=(16, 8), pady=14)
        tombol(k, "Reset Input", self._reset, "neutral", height=44, width=120, border_width=1,
               border_color=BORDER).grid(row=0, column=1, padx=(0, 16), pady=14)

    # ------------------------------------------------------------ detail
    def _bangun_laporan(self):
        k = kartu(self)
        k.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=28, pady=(0, 22))
        k.grid_columnconfigure(0, weight=1)
        k.grid_rowconfigure(1, weight=1)
        kepala = ctk.CTkFrame(k, fg_color="transparent")
        kepala.grid(row=0, column=0, sticky="ew", padx=20, pady=(14, 8))
        kepala.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(kepala, text="Detail Langkah Analisis", font=fnt(16, "bold"),
                     text_color=INK, anchor="w").grid(row=0, column=0, sticky="w")
        self.seg = ctk.CTkSegmentedButton(
            kepala, values=["Detail Langkah", "Plaintext"], command=self._tab, font=fnt(12),
            fg_color=NEUTRAL, selected_color=BLUE, selected_hover_color=BLUE_H,
            unselected_color=NEUTRAL, unselected_hover_color=NEUTRAL_H, text_color=INK)
        self.seg.set("Detail Langkah")
        self.seg.grid(row=0, column=1, padx=(0, 10))
        self.btn_copy = tombol(kepala, "Copy", self._salin, "neutral", width=70, height=32,
                               state="disabled")
        self.btn_copy.grid(row=0, column=2, padx=(0, 6))
        self.btn_dl_lap = tombol(kepala, "Download Report", self._unduh_laporan, "blue",
                                 width=140, height=32, state="disabled")
        self.btn_dl_lap.grid(row=0, column=3)
        self.output = kotak_teks(k, mono=True, wrap="none", state="disabled")
        self.output.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 16))

    # ================================================================ logika
    def _tampil_awal(self):
        isi_readonly(self.output,
                     "Pilih algoritma (atau Auto-detect), tempel ciphertext tanpa kunci, lalu klik Run Analysis.\n\n"
                     "Di sini akan tampil langkah demi langkah cara kunci dan plaintext ditemukan:\n"
                     "  Caesar    : coba 26 geseran\n"
                     "  Vigenere  : Kasiski, Index of Coincidence, frekuensi per kolom, serangan kamus\n"
                     "  Playfair  : serangan kamus\n"
                     "  Hill      : known-plaintext (K = C x P^-1) atau serangan statistik\n"
                     "  Stream    : brute force 256 seed LCG\n"
                     "  OTP       : penjelasan mengapa tidak dapat dipecahkan\n")

    def _ganti_algoritma(self):
        kode = NAMA_ANALISIS[self.algo_var.get()]
        self.lbl_hint.configure(text=HINT_ANALISIS[kode])
        self.btn_wordlist.configure(state="normal" if kode in ("auto", "2", "3") else "disabled")

    def _upload_input(self):
        p = filedialog.askopenfilename(
            parent=self.app, title="Pilih file ciphertext (.txt)",
            filetypes=[("Text file", "*.txt"), ("Semua file", "*.*")])
        if not p:
            return
        try:
            ukuran = os.path.getsize(p)
            with open(p, "rb") as f:
                mentah = f.read(BATAS_PRATINJAU * 4)
        except OSError as e:
            self.app.toast.tampil(pesan_error(e), "error")
            return
        pratinjau = mentah.decode("utf-8-sig", errors="replace")[:BATAS_PRATINJAU]
        if ukuran > len(mentah) or len(pratinjau) >= BATAS_PRATINJAU:
            pratinjau += "\n\n... (pratinjau dipotong; seluruh isi file tetap dianalisis)"
        self.file_path = p
        isi_readonly(self.input, pratinjau)
        self.lbl_file.configure(
            text=f"{os.path.basename(p)}  ({fmt_ukuran(ukuran)}) - pratinjau, tidak bisa diedit",
            text_color=BLUE_INK)
        self.btn_hapus_file.grid()
        self.app.toast.tampil(f"File dimuat: {os.path.basename(p)}", "info")

    def _hapus_file(self):
        self.file_path = None
        self.input.configure(state="normal")
        self.input.delete("1.0", "end")
        self.lbl_file.configure(text="Belum ada file - tempel ciphertext di atas", text_color=MUTED)
        self.btn_hapus_file.grid_remove()

    def _upload_wordlist(self):
        p = filedialog.askopenfilename(
            parent=self.app, title="Pilih wordlist (.txt, satu kata per baris)",
            filetypes=[("Text file", "*.txt"), ("Semua file", "*.*")])
        if not p:
            return
        try:
            jumlah = len(baca_teks(p).split())
        except Exception as e:                              # noqa: BLE001
            self.app.toast.tampil(pesan_error(e), "error")
            return
        if jumlah == 0:
            self.app.toast.tampil("Wordlist kosong.", "error")
            return
        self.wordlist_path = p
        extra = f" (dipakai {MAKS_KAMUS:,} pertama)" if jumlah > MAKS_KAMUS else ""
        self.lbl_wordlist.configure(text=f"{os.path.basename(p)}: {jumlah:,} kata{extra}",
                                    text_color=BLUE_INK)
        self.btn_hapus_wl.grid()

    def _hapus_wordlist(self):
        self.wordlist_path = None
        self.lbl_wordlist.configure(text="Opsional: daftar kata kunci untuk serangan kamus",
                                    text_color=MUTED)
        self.btn_hapus_wl.grid_remove()

    # ---- proses
    def _run(self):
        if self.running:
            return
        teks = None if self.file_path else self.input.get("1.0", "end-1c")
        if not self.file_path and not teks.strip():
            self.app.toast.tampil("Tempel ciphertext atau unggah file .txt terlebih dahulu.", "error")
            return
        mentah = self.ent_offset.get().strip()
        try:
            offset = int(mentah) if mentah else 0
            if offset < 0:
                raise ValueError
        except ValueError:
            self.app.toast.tampil("Posisi crib harus bilangan bulat >= 0 (indeks huruf pertama, mulai 0).",
                                  "error")
            return
        pilihan = NAMA_ANALISIS[self.algo_var.get()]
        bahasa = PILIHAN_BAHASA[self.bahasa_var.get()]
        crib = self.ent_crib.get().strip()
        wl = self.wordlist_path
        fp = self.file_path

        self._bersihkan_hasil()
        self.running = True
        self.btn_run.configure(state="disabled", text="Analyzing...")
        isi_readonly(self.output, "Menganalisis... (serangan Hill/Playfair bisa memakan beberapa detik)")
        self.app.jalankan_tugas(
            lambda: jalankan_analisis(pilihan, teks, fp, bahasa, crib, offset, wl),
            self._selesai, self._gagal)

    def _selesai(self, h):
        self.running = False
        self.btn_run.configure(state="normal", text="Run Analysis")
        self.hasil = h
        self.laporan = h["laporan"]
        teks = h["teks_hasil"]
        if len(teks) > BATAS_TAMPIL:
            teks = teks[:BATAS_TAMPIL] + f"\n\n... (ditampilkan {BATAS_TAMPIL:,} dari {len(h['teks_hasil']):,} karakter)"
        self.plain_tampil = teks or "(plaintext tidak dapat dipulihkan)"

        self.nilai["algo"].configure(text=h["algoritma"])
        self.nilai["metode"].configure(text=h["metode"])
        if h["kunci"] is None:
            self.nilai["kunci"].configure(text="tidak dapat ditentukan", text_color="#8A2B25")
        else:
            k = h["kunci"]
            self.nilai["kunci"].configure(text=k if len(k) <= 60 else k[:57] + "...",
                                          text_color=INK)
        self.nilai["yakin"].configure(text=h["yakin"] or "-")
        self.nilai["dicoba"].configure(text=f"{h['dicoba']:,}")
        self.nilai["waktu"].configure(text=fmt_durasi(h["waktu_total_s"]))
        self.btn_copy.configure(state="normal")
        self.btn_dl_lap.configure(state="normal")
        if h["kunci"] is not None:
            self.btn_copy_key.configure(state="normal")
            self.btn_dl_key.configure(state="normal")
        if h["bytes_hasil"] is not None:
            self.btn_dl_plain.configure(state="normal")
        self.seg.set("Detail Langkah")
        self._tab("Detail Langkah")

        if h["kunci"] is None:
            self.app.toast.tampil("Kunci tidak dapat ditentukan. Lihat Detail Langkah untuk alasannya.",
                                  "info")
        elif (h["yakin"] or "").startswith("Rendah"):
            self.app.toast.tampil(f"Kunci tebakan: {h['kunci']} - keyakinan rendah, periksa plaintext-nya.",
                                  "info")
        else:
            self.app.toast.tampil(f"Kunci ditemukan: {h['kunci']} (keyakinan {h['yakin']}).", "success")

    def _gagal(self, e):
        self.running = False
        self.btn_run.configure(state="normal", text="Run Analysis")
        self._tampil_awal()
        self.app.toast.tampil(pesan_error(e), "error")

    def _tab(self, nama):
        if nama == "Plaintext":
            self.output.configure(wrap="word")
            isi_readonly(self.output, self.plain_tampil if self.hasil else "")
        else:
            self.output.configure(wrap="none")
            isi_readonly(self.output, self.laporan if self.hasil else "")

    def _bersihkan_hasil(self):
        self.hasil = None
        self.laporan = self.plain_tampil = ""
        for lbl in self.nilai.values():
            lbl.configure(text="-", text_color=INK)
        for b in (self.btn_copy, self.btn_dl_lap, self.btn_copy_key, self.btn_dl_key,
                  self.btn_dl_plain):
            b.configure(state="disabled")

    def _reset(self):
        if self.running:
            return
        self._hapus_file()
        self._hapus_wordlist()
        self.ent_crib.delete(0, "end")
        self.ent_offset.delete(0, "end")
        self._bersihkan_hasil()
        self.seg.set("Detail Langkah")
        self.output.configure(wrap="none")
        self._tampil_awal()

    # ---- keluaran
    def _salin(self):
        if not self.hasil:
            return
        teks = self.hasil["teks_hasil"] if self.seg.get() == "Plaintext" else self.laporan
        self.app.clipboard_clear()
        self.app.clipboard_append(teks)
        self.app.toast.tampil("Disalin ke clipboard.", "success", 2000)

    def _salin_kunci(self):
        if self.hasil and self.hasil["kunci"] is not None:
            self.app.clipboard_clear()
            self.app.clipboard_append(self.hasil["kunci"])
            self.app.toast.tampil("Kunci disalin ke clipboard.", "success", 2000)

    def _simpan(self, judul, nama_awal, tulis):
        path = filedialog.asksaveasfilename(
            parent=self.app, title=judul, initialfile=nama_awal, defaultextension=".txt",
            filetypes=[("Text file", "*.txt"), ("Semua file", "*.*")])
        if not path:
            return
        try:
            tulis(path)
        except OSError as e:
            self.app.toast.tampil(f"Gagal menyimpan: {pesan_error(e)}", "error")
            return
        self.app.toast.tampil(f"Tersimpan: {path}", "success")

    def _unduh_kunci(self):
        h = self.hasil
        if h and h["kunci"] is not None:
            self._simpan("Simpan kunci", h["nama_kunci"] or "kunci_hasil_analisis.key.txt",
                         lambda p: tulis_teks(p, h["kunci"] + "\n"))

    def _unduh_plain(self):
        h = self.hasil
        if h and h["bytes_hasil"] is not None:
            self._simpan("Simpan plaintext", h["nama_hasil"], lambda p: tulis_bytes(p, h["bytes_hasil"]))

    def _unduh_laporan(self):
        if self.hasil:
            self._simpan("Simpan laporan analisis", "laporan_analisis.txt",
                         lambda p: tulis_teks(p, self.laporan + "\n"))


# ======================================================================
# JENDELA UTAMA
# ======================================================================
class CryptoZarApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CryptoZar")
        self.geometry("1260x820")
        self.minsize(1120, 740)
        self.configure(fg_color=BG)
        self.busy = False
        self.toast = Toast(self)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        sisi = ctk.CTkFrame(self, width=250, fg_color=SIDEBAR, corner_radius=0)
        sisi.grid(row=0, column=0, sticky="nsw")
        sisi.grid_propagate(False)
        kepala = ctk.CTkFrame(sisi, fg_color="transparent")
        kepala.pack(fill="x", padx=22, pady=(30, 30))
        self._logo = pil_ke_ctk(muat_b64(LOGO_PNG), 64)
        ctk.CTkLabel(kepala, image=self._logo, text="").pack(side="left")
        ctk.CTkLabel(kepala, text="CryptoZar", font=fnt(27, "bold"),
                     text_color=INK).pack(side="left", padx=(12, 0))
        self._emblem = pil_ke_ctk(muat_b64(EMBLEM_PNG), 220)
        ctk.CTkLabel(sisi, image=self._emblem, text="").pack(side="bottom", pady=(0, 24))

        isi = ctk.CTkFrame(self, fg_color=BG, corner_radius=0)
        isi.grid(row=0, column=1, sticky="nsew")
        isi.grid_columnconfigure(0, weight=1)
        isi.grid_rowconfigure(0, weight=1)

        self.halaman = {
            "Encrypt": HalamanKripto(isi, self, "encrypt"),
            "Decrypt": HalamanKripto(isi, self, "decrypt"),
            "Analyze": HalamanAnalisis(isi, self),
            "Demo": HalamanDemo(isi, self),
            "Benchmark": HalamanBenchmark(isi, self),
        }
        self.nav = {}
        for nama, hal in self.halaman.items():
            hal.grid(row=0, column=0, sticky="nsew")
            b = ctk.CTkButton(sisi, text=nama, anchor="w", height=44, corner_radius=12,
                              fg_color="transparent", hover_color=NAV_H, text_color=INK,
                              font=fnt(15), command=lambda n=nama: self.tampil(n))
            b.pack(fill="x", padx=16, pady=3)
            self.nav[nama] = b
        self.tampil("Encrypt")
        self._pasang_ikon()
        self.after(300, self._pasang_ikon)   

    def _pasang_ikon(self):
        """Ganti ikon kotak biru bawaan (pojok kiri atas jendela & taskbar) dengan logo."""
        try:
            from PIL import Image, ImageTk
            img = muat_b64(IKON_PNG)
            self._ikon_tk = ImageTk.PhotoImage(img.resize((64, 64), Image.LANCZOS))
            self.iconphoto(True, self._ikon_tk)
            if sys.platform.startswith("win"):
                ico = os.path.join(tempfile.gettempdir(), "cryptozar.ico")
                img.save(ico, format="ICO",
                         sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (256, 256)])
                self.iconbitmap(ico)
        except Exception:                             
            pass

    def tampil(self, nama):
        self.halaman[nama].tkraise()
        for n, b in self.nav.items():
            aktif = n == nama
            b.configure(fg_color=BLUE if aktif else "transparent",
                        text_color=BLUE_INK if aktif else INK,
                        font=fnt(15, "bold" if aktif else "normal"))

    def jalankan_tugas(self, fn, on_selesai, on_gagal, on_log=None):
        """Jalankan fn di thread terpisah agar jendela tetap responsif.
        Jika on_log diberikan, print() dari fn dialirkan ke on_log secara langsung."""
        q = queue.Queue()

        def kerja():
            try:
                if on_log:
                    with contextlib.redirect_stdout(_PenulisAntrean(q)):
                        hasil = fn()
                else:
                    hasil = fn()
                q.put(("selesai", hasil))
            except BaseException as e:                  # noqa: BLE001 - jangan sampai crash
                q.put(("gagal", e))

        threading.Thread(target=kerja, daemon=True).start()

        def cek():
            try:
                while True:
                    jenis, isi = q.get_nowait()
                    if jenis == "log":
                        on_log(isi)
                    elif jenis == "selesai":
                        on_selesai(isi)
                        return
                    else:
                        on_gagal(isi)
                        return
            except queue.Empty:
                pass
            self.after(60, cek)

        cek()


def main():
    if sys.platform.startswith("win"):
        try:                                 
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("cryptozar.app")
        except Exception:                     
            pass
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    CryptoZarApp().mainloop()


if __name__ == "__main__":
    main()
