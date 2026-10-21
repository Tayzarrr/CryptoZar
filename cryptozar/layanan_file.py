# CryptoZar — layanan_file
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.konfigurasi import ALGORITMA  # Mengimpor komponen yang dibutuhkan dari cryptozar.konfigurasi.
from cryptozar.file_io import baca_bytes  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.file_io import baca_hex  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.file_io import baca_teks  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.algoritma.caesar import caesar_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.caesar.
from cryptozar.algoritma.caesar import caesar_enkripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.caesar.
from cryptozar.algoritma.hill import hill_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.hill.
from cryptozar.algoritma.hill import hill_enkripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.hill.
from cryptozar.algoritma.hill import hill_parse_kunci  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.hill.
from cryptozar.algoritma.stream import keystream_lcg  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.stream.
from cryptozar.utilitas import normalisasi  # Mengimpor komponen yang dibutuhkan dari cryptozar.utilitas.
import os  # Memuat pustaka os.
from cryptozar.algoritma.otp import otp_buat_kunci  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.otp.
from cryptozar.file_io import path_hasil_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.algoritma.playfair import playfair_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.playfair.
from cryptozar.algoritma.playfair import playfair_enkripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.playfair.
import time  # Memuat pustaka time.
from cryptozar.file_io import tulis_bytes  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.file_io import tulis_hex  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.file_io import tulis_teks  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.algoritma.vigenere import vigenere_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.vigenere.
from cryptozar.algoritma.vigenere import vigenere_enkripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.vigenere.
from cryptozar.algoritma.otp import xor_bytes  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.otp.


def enkripsi_file(kode, path_in, kunci_str=None):  # Mendefinisikan fungsi enkripsi_file dengan parameter yang tertulis.
    """Enkripsi file .txt. Mengembalikan dict berisi ringkasan hasil."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    nama_tampil, nama_file = ALGORITMA[kode]  # Menghitung atau menyiapkan ALGORITMA[kode], lalu menyimpannya pada (nama_tampil, nama_file).
    base = os.path.splitext(path_in)[0]  # Menghitung atau menyiapkan os.path.splitext(path_in)[0], lalu menyimpannya pada base.
    out_path = f"{base}_{nama_file}.enc.txt"  # Menghitung atau menyiapkan f'{base}_{nama_file}.enc.txt', lalu menyimpannya pada out_path.
    info = {  # Menghitung atau menyiapkan {'algoritma': nama_tampil, 'path_in': path_in, 'out_path': out_path, 'kunci_path': None}, lalu menyimpannya pada info.
        "algoritma": nama_tampil,  # Menghitung atau menyiapkan {'algoritma': nama_tampil, 'path_in': path_in, 'out_path': out_path, 'kunci_path': None}, lalu menyimpannya pada info.
        "path_in": path_in,  # Menghitung atau menyiapkan {'algoritma': nama_tampil, 'path_in': path_in, 'out_path': out_path, 'kunci_path': None}, lalu menyimpannya pada info.
        "out_path": out_path,  # Menghitung atau menyiapkan {'algoritma': nama_tampil, 'path_in': path_in, 'out_path': out_path, 'kunci_path': None}, lalu menyimpannya pada info.
        "kunci_path": None,  # Menghitung atau menyiapkan {'algoritma': nama_tampil, 'path_in': path_in, 'out_path': out_path, 'kunci_path': None}, lalu menyimpannya pada info.
    }  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    if kode in ("1", "2", "3", "4"):  # Menjalankan blok hanya jika kode in ("1", "2", "3", "4").
        teks = baca_teks(path_in)  # Menghitung atau menyiapkan baca_teks(path_in), lalu menyimpannya pada teks.
        info["ukuran_in"] = len(teks.encode("utf-8"))  # Menghitung atau menyiapkan len(teks.encode('utf-8')), lalu menyimpannya pada info['ukuran_in'].
        if kode == "1":  # Menjalankan blok hanya jika kode == "1".
            try:  # Memulai operasi yang dapat menghasilkan exception.
                k = int(kunci_str)  # Menghitung atau menyiapkan int(kunci_str), lalu menyimpannya pada k.
            except (TypeError, ValueError):  # Menangani exception (TypeError, ValueError).
                raise ValueError("Kunci Caesar harus berupa bilangan bulat.")  # Menghentikan proses dengan exception ValueError("Kunci Caesar harus berupa bilangan bulat.").
            t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
            cipher = caesar_enkripsi(teks, k)  # Menghitung atau menyiapkan caesar_enkripsi(teks, k), lalu menyimpannya pada cipher.
            info["kunci_tampil"] = str(k % 26)  # Menghitung atau menyiapkan str(k % 26), lalu menyimpannya pada info['kunci_tampil'].
        elif kode == "2":  # Memeriksa kondisi alternatif kode == "2".
            t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
            cipher = vigenere_enkripsi(teks, kunci_str)  # Menghitung atau menyiapkan vigenere_enkripsi(teks, kunci_str), lalu menyimpannya pada cipher.
            info["kunci_tampil"] = normalisasi(kunci_str)  # Menghitung atau menyiapkan normalisasi(kunci_str), lalu menyimpannya pada info['kunci_tampil'].
        elif kode == "3":  # Memeriksa kondisi alternatif kode == "3".
            t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
            cipher = playfair_enkripsi(teks, kunci_str)  # Menghitung atau menyiapkan playfair_enkripsi(teks, kunci_str), lalu menyimpannya pada cipher.
            info["kunci_tampil"] = normalisasi(kunci_str).replace("J", "I")  # Menghitung atau menyiapkan normalisasi(kunci_str).replace('J', 'I'), lalu menyimpannya pada info['kunci_tampil'].
        else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
            M = hill_parse_kunci(kunci_str)  # Menghitung atau menyiapkan hill_parse_kunci(kunci_str), lalu menyimpannya pada M.
            t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
            cipher = hill_enkripsi(teks, M)  # Menghitung atau menyiapkan hill_enkripsi(teks, M), lalu menyimpannya pada cipher.
            info["kunci_tampil"] = str(M)  # Menghitung atau menyiapkan str(M), lalu menyimpannya pada info['kunci_tampil'].
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000  # Menghitung atau menyiapkan (time.perf_counter() - t0) * 1000, lalu menyimpannya pada info['waktu_ms'].
        tulis_teks(out_path, cipher)  # Memanggil tulis_teks untuk menjalankan operasi dengan argumen yang diberikan.
        info["cipher_tampil"] = cipher  # Menghitung atau menyiapkan cipher, lalu menyimpannya pada info['cipher_tampil'].
        info["ukuran_cipher"] = len(cipher)  # Menghitung atau menyiapkan len(cipher), lalu menyimpannya pada info['ukuran_cipher'].
        if not cipher:  # Menjalankan blok hanya jika not cipher.
            raise ValueError("File tidak berisi huruf A-Z sehingga tidak ada yang dienkripsi.")  # Menghentikan proses dengan exception ValueError("File tidak berisi huruf A-Z sehingga tidak ada yang dienkripsi.").
    elif kode == "5":  # Memeriksa kondisi alternatif kode == "5".
        data = baca_bytes(path_in)  # Menghitung atau menyiapkan baca_bytes(path_in), lalu menyimpannya pada data.
        info["ukuran_in"] = len(data)  # Menghitung atau menyiapkan len(data), lalu menyimpannya pada info['ukuran_in'].
        t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
        kunci = otp_buat_kunci(len(data))  # Menghitung atau menyiapkan otp_buat_kunci(len(data)), lalu menyimpannya pada kunci.
        c = xor_bytes(data, kunci)  # Menghitung atau menyiapkan xor_bytes(data, kunci), lalu menyimpannya pada c.
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000  # Menghitung atau menyiapkan (time.perf_counter() - t0) * 1000, lalu menyimpannya pada info['waktu_ms'].
        kunci_path = f"{base}_otp.key.txt"  # Menghitung atau menyiapkan f'{base}_otp.key.txt', lalu menyimpannya pada kunci_path.
        tulis_hex(kunci_path, kunci)  # Memanggil tulis_hex untuk menjalankan operasi dengan argumen yang diberikan.
        tulis_hex(out_path, c)  # Memanggil tulis_hex untuk menjalankan operasi dengan argumen yang diberikan.
        info["kunci_path"] = kunci_path  # Menghitung atau menyiapkan kunci_path, lalu menyimpannya pada info['kunci_path'].
        info["kunci_tampil"] = kunci.hex()  # Menghitung atau menyiapkan kunci.hex(), lalu menyimpannya pada info['kunci_tampil'].
        info["cipher_tampil"] = c.hex()  # Menghitung atau menyiapkan c.hex(), lalu menyimpannya pada info['cipher_tampil'].
        info["ukuran_cipher"] = len(c)  # Menghitung atau menyiapkan len(c), lalu menyimpannya pada info['ukuran_cipher'].
    else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
        try:  # Memulai operasi yang dapat menghasilkan exception.
            seed = int(kunci_str) % 256  # Menghitung atau menyiapkan int(kunci_str) % 256, lalu menyimpannya pada seed.
        except (TypeError, ValueError):  # Menangani exception (TypeError, ValueError).
            raise ValueError("Seed harus berupa bilangan bulat 0-255.")  # Menghentikan proses dengan exception ValueError("Seed harus berupa bilangan bulat 0-255.").
        data = baca_bytes(path_in)  # Menghitung atau menyiapkan baca_bytes(path_in), lalu menyimpannya pada data.
        info["ukuran_in"] = len(data)  # Menghitung atau menyiapkan len(data), lalu menyimpannya pada info['ukuran_in'].
        t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
        s = keystream_lcg(seed, len(data))  # Menghitung atau menyiapkan keystream_lcg(seed, len(data)), lalu menyimpannya pada s.
        c = xor_bytes(data, s)  # Menghitung atau menyiapkan xor_bytes(data, s), lalu menyimpannya pada c.
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000  # Menghitung atau menyiapkan (time.perf_counter() - t0) * 1000, lalu menyimpannya pada info['waktu_ms'].
        tulis_hex(out_path, c)  # Memanggil tulis_hex untuk menjalankan operasi dengan argumen yang diberikan.
        info["kunci_tampil"] = f"seed = {seed}"  # Menghitung atau menyiapkan f'seed = {seed}', lalu menyimpannya pada info['kunci_tampil'].
        info["keystream_tampil"] = s.hex()  # Menghitung atau menyiapkan s.hex(), lalu menyimpannya pada info['keystream_tampil'].
        info["cipher_tampil"] = c.hex()  # Menghitung atau menyiapkan c.hex(), lalu menyimpannya pada info['cipher_tampil'].
        info["ukuran_cipher"] = len(c)  # Menghitung atau menyiapkan len(c), lalu menyimpannya pada info['ukuran_cipher'].
    return info  # Mengembalikan info.


def dekripsi_file(kode, path_cipher, kunci_str=None):  # Mendefinisikan fungsi dekripsi_file dengan parameter yang tertulis.
    """Dekripsi file hasil enkripsi. Untuk OTP, kunci_str = path file kunci."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    nama_tampil, _ = ALGORITMA[kode]  # Menghitung atau menyiapkan ALGORITMA[kode], lalu menyimpannya pada (nama_tampil, _).
    out_path = path_hasil_dekripsi(path_cipher)  # Menghitung atau menyiapkan path_hasil_dekripsi(path_cipher), lalu menyimpannya pada out_path.
    info = {"algoritma": nama_tampil, "path_in": path_cipher, "out_path": out_path}  # Menghitung atau menyiapkan {'algoritma': nama_tampil, 'path_in': path_cipher, 'out_path': out_path}, lalu menyimpannya pada info.
    if kode in ("1", "2", "3", "4"):  # Menjalankan blok hanya jika kode in ("1", "2", "3", "4").
        cipher = baca_teks(path_cipher)  # Menghitung atau menyiapkan baca_teks(path_cipher), lalu menyimpannya pada cipher.
        if kode == "1":  # Menjalankan blok hanya jika kode == "1".
            try:  # Memulai operasi yang dapat menghasilkan exception.
                k = int(kunci_str)  # Menghitung atau menyiapkan int(kunci_str), lalu menyimpannya pada k.
            except (TypeError, ValueError):  # Menangani exception (TypeError, ValueError).
                raise ValueError("Kunci Caesar harus berupa bilangan bulat.")  # Menghentikan proses dengan exception ValueError("Kunci Caesar harus berupa bilangan bulat.").
            t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
            plain = caesar_dekripsi(cipher, k)  # Menghitung atau menyiapkan caesar_dekripsi(cipher, k), lalu menyimpannya pada plain.
        elif kode == "2":  # Memeriksa kondisi alternatif kode == "2".
            t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
            plain = vigenere_dekripsi(cipher, kunci_str)  # Menghitung atau menyiapkan vigenere_dekripsi(cipher, kunci_str), lalu menyimpannya pada plain.
        elif kode == "3":  # Memeriksa kondisi alternatif kode == "3".
            t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
            plain = playfair_dekripsi(cipher, kunci_str)  # Menghitung atau menyiapkan playfair_dekripsi(cipher, kunci_str), lalu menyimpannya pada plain.
        else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
            M = hill_parse_kunci(kunci_str)  # Menghitung atau menyiapkan hill_parse_kunci(kunci_str), lalu menyimpannya pada M.
            t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
            plain = hill_dekripsi(cipher, M)  # Menghitung atau menyiapkan hill_dekripsi(cipher, M), lalu menyimpannya pada plain.
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000  # Menghitung atau menyiapkan (time.perf_counter() - t0) * 1000, lalu menyimpannya pada info['waktu_ms'].
        tulis_teks(out_path, plain)  # Memanggil tulis_teks untuk menjalankan operasi dengan argumen yang diberikan.
        info["plain_tampil"] = plain  # Menghitung atau menyiapkan plain, lalu menyimpannya pada info['plain_tampil'].
    elif kode == "5":  # Memeriksa kondisi alternatif kode == "5".
        c = baca_hex(path_cipher)  # Menghitung atau menyiapkan baca_hex(path_cipher), lalu menyimpannya pada c.
        kunci = baca_hex(kunci_str)  # Menghitung atau menyiapkan baca_hex(kunci_str), lalu menyimpannya pada kunci.
        if len(kunci) != len(c):  # Menjalankan blok hanya jika len(kunci) != len(c).
            raise ValueError(  # Menghentikan proses dengan exception ValueError(.
                f"Panjang kunci ({len(kunci)} byte) tidak sama dengan ciphertext ({len(c)} byte)."  # Menyusun bagian ekspresi f"Panjang kunci ({len(kunci)} byte) tidak sama dengan ciphertext ({len(c)} byte).".
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
        data = xor_bytes(c, kunci)  # Menghitung atau menyiapkan xor_bytes(c, kunci), lalu menyimpannya pada data.
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000  # Menghitung atau menyiapkan (time.perf_counter() - t0) * 1000, lalu menyimpannya pada info['waktu_ms'].
        tulis_bytes(out_path, data)  # Memanggil tulis_bytes untuk menjalankan operasi dengan argumen yang diberikan.
        info["plain_tampil"] = data.decode("utf-8", errors="replace")  # Menghitung atau menyiapkan data.decode('utf-8', errors='replace'), lalu menyimpannya pada info['plain_tampil'].
    else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
        try:  # Memulai operasi yang dapat menghasilkan exception.
            seed = int(kunci_str) % 256  # Menghitung atau menyiapkan int(kunci_str) % 256, lalu menyimpannya pada seed.
        except (TypeError, ValueError):  # Menangani exception (TypeError, ValueError).
            raise ValueError("Seed harus berupa bilangan bulat 0-255.")  # Menghentikan proses dengan exception ValueError("Seed harus berupa bilangan bulat 0-255.").
        c = baca_hex(path_cipher)  # Menghitung atau menyiapkan baca_hex(path_cipher), lalu menyimpannya pada c.
        t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
        s = keystream_lcg(seed, len(c))  # Menghitung atau menyiapkan keystream_lcg(seed, len(c)), lalu menyimpannya pada s.
        data = xor_bytes(c, s)  # Menghitung atau menyiapkan xor_bytes(c, s), lalu menyimpannya pada data.
        info["waktu_ms"] = (time.perf_counter() - t0) * 1000  # Menghitung atau menyiapkan (time.perf_counter() - t0) * 1000, lalu menyimpannya pada info['waktu_ms'].
        tulis_bytes(out_path, data)  # Memanggil tulis_bytes untuk menjalankan operasi dengan argumen yang diberikan.
        info["plain_tampil"] = data.decode("utf-8", errors="replace")  # Menghitung atau menyiapkan data.decode('utf-8', errors='replace'), lalu menyimpannya pada info['plain_tampil'].
    return info  # Mengembalikan info.
