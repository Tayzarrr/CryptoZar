# CryptoZar — layanan_gui
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.konfigurasi import ALFABET  # Mengimpor komponen yang dibutuhkan dari cryptozar.konfigurasi.
from cryptozar.konfigurasi import ALGORITMA  # Mengimpor komponen yang dibutuhkan dari cryptozar.konfigurasi.
from cryptozar.file_io import baca_bytes  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.file_io import baca_teks  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
import contextlib  # Memuat pustaka contextlib.
from cryptozar.layanan_file import dekripsi_file  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_file.
from cryptozar.demo import demo_belajar_kriptografi  # Mengimpor komponen yang dibutuhkan dari cryptozar.demo.
from cryptozar.layanan_file import enkripsi_file  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_file.
from cryptozar.algoritma.hill import hill_parse_kunci  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.hill.
import os  # Memuat pustaka os.
from cryptozar.algoritma.otp import otp_buat_kunci  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.otp.
import secrets  # Memuat pustaka secrets.
import shutil  # Memuat pustaka shutil.
import tempfile  # Memuat pustaka tempfile.
import time  # Memuat pustaka time.
from cryptozar.file_io import tulis_hex  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.file_io import tulis_teks  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.benchmark import ukur_beban_komputasi  # Mengimpor komponen yang dibutuhkan dari cryptozar.benchmark.
from cryptozar.algoritma.otp import xor_bytes  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.otp.


def _hex_ke_bytes(teks, nama):  # Mendefinisikan fungsi _hex_ke_bytes dengan parameter yang tertulis.
    bersih = "".join(str(teks).split())  # Menghitung atau menyiapkan ''.join(str(teks).split()), lalu menyimpannya pada bersih.
    try:  # Memulai operasi yang dapat menghasilkan exception.
        return bytes.fromhex(bersih)  # Mengembalikan bytes.fromhex(bersih).
    except ValueError:  # Menangani exception ValueError.
        raise ValueError(  # Menghentikan proses dengan exception ValueError(.
            f"{nama} harus berupa heksadesimal yang valid (karakter 0-9 dan A-F, jumlah genap)."  # Menyusun bagian ekspresi f"{nama} harus berupa heksadesimal yang valid (karakter 0-9 dan A-F, jumlah genap).".
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.


def _siapkan_input(folder, teks, path_file, nama_default):  # Mendefinisikan fungsi _siapkan_input dengan parameter yang tertulis.
    """Salin file upload (atau tulis teks ketikan) ke folder sementara."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    if path_file:  # Menjalankan blok hanya jika path_file.
        tujuan = os.path.join(folder, os.path.basename(path_file))  # Menghitung atau menyiapkan os.path.join(folder, os.path.basename(path_file)), lalu menyimpannya pada tujuan.
        shutil.copyfile(path_file, tujuan)  # Memanggil shutil.copyfile untuk menjalankan operasi dengan argumen yang diberikan.
    else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
        tujuan = os.path.join(folder, nama_default)  # Menghitung atau menyiapkan os.path.join(folder, nama_default), lalu menyimpannya pada tujuan.
        tulis_teks(tujuan, teks)  # Memanggil tulis_teks untuk menjalankan operasi dengan argumen yang diberikan.
    return tujuan  # Mengembalikan tujuan.


def _enkripsi_otp_kunci_manual(path_in, kunci_hex):  # Mendefinisikan fungsi _enkripsi_otp_kunci_manual dengan parameter yang tertulis.
    """OTP dengan kunci yang disediakan pengguna (backend hanya membangkitkan kunci acak)."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    kunci = _hex_ke_bytes(kunci_hex, "Kunci OTP")  # Menghitung atau menyiapkan _hex_ke_bytes(kunci_hex, 'Kunci OTP'), lalu menyimpannya pada kunci.
    data = baca_bytes(path_in)  # Menghitung atau menyiapkan baca_bytes(path_in), lalu menyimpannya pada data.
    if len(kunci) != len(data):  # Menjalankan blok hanya jika len(kunci) != len(data).
        raise ValueError(  # Menghentikan proses dengan exception ValueError(.
            f"Panjang kunci OTP ({len(kunci)} byte) harus sama dengan panjang pesan ({len(data)} byte). Klik 'Generate Random Key' lagi, atau kosongkan kunci agar dibangkitkan otomatis."  # Menyusun bagian ekspresi f"Panjang kunci OTP ({len(kunci)} byte) harus sama dengan panjang pesan ({len(data)} byte). Klik 'Ge.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    out_path = f"{os.path.splitext(path_in)[0]}_otp.enc.txt"  # Menghitung atau menyiapkan f'{os.path.splitext(path_in)[0]}_otp.enc.txt', lalu menyimpannya pada out_path.
    t0 = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t0.
    c = xor_bytes(data, kunci)  # Menghitung atau menyiapkan xor_bytes(data, kunci), lalu menyimpannya pada c.
    waktu_ms = (time.perf_counter() - t0) * 1000  # Menghitung atau menyiapkan (time.perf_counter() - t0) * 1000, lalu menyimpannya pada waktu_ms.
    tulis_hex(out_path, c)  # Memanggil tulis_hex untuk menjalankan operasi dengan argumen yang diberikan.
    return {  # Mengembalikan {.
        "algoritma": ALGORITMA["5"][0],  # Menyusun bagian ekspresi "algoritma": ALGORITMA["5"][0],.
        "path_in": path_in,  # Menyusun bagian ekspresi "path_in": path_in,.
        "out_path": out_path,  # Menyusun bagian ekspresi "out_path": out_path,.
        "kunci_path": None,  # Menyusun bagian ekspresi "kunci_path": None,.
        "ukuran_in": len(data),  # Menyusun bagian ekspresi "ukuran_in": len(data),.
        "waktu_ms": waktu_ms,  # Menyusun bagian ekspresi "waktu_ms": waktu_ms,.
        "kunci_tampil": kunci.hex(),  # Menyusun bagian ekspresi "kunci_tampil": kunci.hex(),.
        "cipher_tampil": c.hex(),  # Menyusun bagian ekspresi "cipher_tampil": c.hex(),.
        "ukuran_cipher": len(c),  # Menyusun bagian ekspresi "ukuran_cipher": len(c),.
    }  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.


def jalankan_enkripsi(kode, teks, path_file, kunci):  # Mendefinisikan fungsi jalankan_enkripsi dengan parameter yang tertulis.
    """Enkripsi teks ketikan (teks) atau file (path_file). Mengembalikan dict hasil untuk GUI."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    t_awal = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t_awal.
    with tempfile.TemporaryDirectory(prefix="cryptozar_") as tmp:  # Mengelola sumber daya atau konteks tempfile.TemporaryDirectory(prefix="cryptozar_") as tmp.
        path_in = _siapkan_input(tmp, teks, path_file, "pesan.txt")  # Menghitung atau menyiapkan _siapkan_input(tmp, teks, path_file, 'pesan.txt'), lalu menyimpannya pada path_in.
        if kode == "5" and kunci:  # Menjalankan blok hanya jika kode == "5" and kunci.
            info = _enkripsi_otp_kunci_manual(path_in, kunci)  # Menghitung atau menyiapkan _enkripsi_otp_kunci_manual(path_in, kunci), lalu menyimpannya pada info.
        else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
            info = enkripsi_file(kode, path_in, kunci or None)  # Menghitung atau menyiapkan enkripsi_file(kode, path_in, kunci or None), lalu menyimpannya pada info.
        data_out = baca_bytes(info["out_path"])  # Menghitung atau menyiapkan baca_bytes(info['out_path']), lalu menyimpannya pada data_out.
        nama_hasil = os.path.basename(info["out_path"])  # Menghitung atau menyiapkan os.path.basename(info['out_path']), lalu menyimpannya pada nama_hasil.
        if kode == "5":  # Menjalankan blok hanya jika kode == "5".
            kunci_simpan = info["kunci_tampil"]  # Menghitung atau menyiapkan info['kunci_tampil'], lalu menyimpannya pada kunci_simpan.
        else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
            kunci_simpan = " ".join(str(kunci).split())  # Menghitung atau menyiapkan ' '.join(str(kunci).split()), lalu menyimpannya pada kunci_simpan.
        ukuran_in = info["ukuran_in"]  # Menghitung atau menyiapkan info['ukuran_in'], lalu menyimpannya pada ukuran_in.
    nama_kunci = nama_hasil[: -len(".enc.txt")] + ".key.txt"  # Menghitung atau menyiapkan nama_hasil[:-len('.enc.txt')] + '.key.txt', lalu menyimpannya pada nama_kunci.
    return {  # Mengembalikan {.
        "mode": "encrypt",  # Menyusun bagian ekspresi "mode": "encrypt",.
        "algoritma": info["algoritma"],  # Menyusun bagian ekspresi "algoritma": info["algoritma"],.
        "teks_hasil": info["cipher_tampil"],  # Menyusun bagian ekspresi "teks_hasil": info["cipher_tampil"],.
        "bytes_hasil": data_out,  # Menyusun bagian ekspresi "bytes_hasil": data_out,.
        "nama_hasil": nama_hasil,  # Menyusun bagian ekspresi "nama_hasil": nama_hasil,.
        "kunci_simpan": kunci_simpan,  # Menyusun bagian ekspresi "kunci_simpan": kunci_simpan,.
        "nama_kunci": nama_kunci,  # Menyusun bagian ekspresi "nama_kunci": nama_kunci,.
        "ukuran_in": ukuran_in,  # Menyusun bagian ekspresi "ukuran_in": ukuran_in,.
        "ukuran_out": len(data_out),  # Menyusun bagian ekspresi "ukuran_out": len(data_out),.
        "waktu_ms": info["waktu_ms"],  # Menyusun bagian ekspresi "waktu_ms": info["waktu_ms"],.
        "waktu_total_s": time.perf_counter() - t_awal,  # Menyusun bagian ekspresi "waktu_total_s": time.perf_counter() - t_awal,.
    }  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.


def jalankan_dekripsi(kode, teks, path_file, kunci):  # Mendefinisikan fungsi jalankan_dekripsi dengan parameter yang tertulis.
    """Dekripsi teks ketikan atau file. Untuk OTP, kunci = string hex."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    t_awal = time.perf_counter()  # Menghitung atau menyiapkan time.perf_counter(), lalu menyimpannya pada t_awal.
    with tempfile.TemporaryDirectory(prefix="cryptozar_") as tmp:  # Mengelola sumber daya atau konteks tempfile.TemporaryDirectory(prefix="cryptozar_") as tmp.
        path_in = _siapkan_input(tmp, teks, path_file, "pesan.enc.txt")  # Menghitung atau menyiapkan _siapkan_input(tmp, teks, path_file, 'pesan.enc.txt'), lalu menyimpannya pada path_in.
        ukuran_in = os.path.getsize(path_in)  # Menghitung atau menyiapkan os.path.getsize(path_in), lalu menyimpannya pada ukuran_in.
        if kode in ("5", "6"):  # Menjalankan blok hanya jika kode in ("5", "6").
            try:  # Memulai operasi yang dapat menghasilkan exception.
                bytes.fromhex("".join(baca_teks(path_in).split()))  # Memanggil bytes.fromhex untuk menjalankan operasi dengan argumen yang diberikan.
            except ValueError:  # Menangani exception ValueError.
                raise ValueError(  # Menghentikan proses dengan exception ValueError(.
                    "Ciphertext harus berupa heksadesimal yang valid (karakter 0-9 dan A-F, jumlah genap)."  # Menyusun bagian ekspresi "Ciphertext harus berupa heksadesimal yang valid (karakter 0-9 dan A-F, jumlah genap).".
                )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        if kode == "5":  # Menjalankan blok hanya jika kode == "5".
            kunci_bytes = _hex_ke_bytes(kunci, "Kunci OTP")  # Menghitung atau menyiapkan _hex_ke_bytes(kunci, 'Kunci OTP'), lalu menyimpannya pada kunci_bytes.
            path_kunci = os.path.join(tmp, "kunci.key.txt")  # Menghitung atau menyiapkan os.path.join(tmp, 'kunci.key.txt'), lalu menyimpannya pada path_kunci.
            tulis_hex(path_kunci, kunci_bytes)  # Memanggil tulis_hex untuk menjalankan operasi dengan argumen yang diberikan.
            info = dekripsi_file(kode, path_in, path_kunci)  # Menghitung atau menyiapkan dekripsi_file(kode, path_in, path_kunci), lalu menyimpannya pada info.
        else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
            info = dekripsi_file(kode, path_in, kunci)  # Menghitung atau menyiapkan dekripsi_file(kode, path_in, kunci), lalu menyimpannya pada info.
        data_out = baca_bytes(info["out_path"])  # Menghitung atau menyiapkan baca_bytes(info['out_path']), lalu menyimpannya pada data_out.
        nama_hasil = os.path.basename(info["out_path"])  # Menghitung atau menyiapkan os.path.basename(info['out_path']), lalu menyimpannya pada nama_hasil.
    return {  # Mengembalikan {.
        "mode": "decrypt",  # Menyusun bagian ekspresi "mode": "decrypt",.
        "algoritma": info["algoritma"],  # Menyusun bagian ekspresi "algoritma": info["algoritma"],.
        "teks_hasil": info["plain_tampil"],  # Menyusun bagian ekspresi "teks_hasil": info["plain_tampil"],.
        "bytes_hasil": data_out,  # Menyusun bagian ekspresi "bytes_hasil": data_out,.
        "nama_hasil": nama_hasil,  # Menyusun bagian ekspresi "nama_hasil": nama_hasil,.
        "kunci_simpan": None,  # Menyusun bagian ekspresi "kunci_simpan": None,.
        "nama_kunci": None,  # Menyusun bagian ekspresi "nama_kunci": None,.
        "ukuran_in": ukuran_in,  # Menyusun bagian ekspresi "ukuran_in": ukuran_in,.
        "ukuran_out": len(data_out),  # Menyusun bagian ekspresi "ukuran_out": len(data_out),.
        "waktu_ms": info["waktu_ms"],  # Menyusun bagian ekspresi "waktu_ms": info["waktu_ms"],.
        "waktu_total_s": time.perf_counter() - t_awal,  # Menyusun bagian ekspresi "waktu_total_s": time.perf_counter() - t_awal,.
    }  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.


def kunci_acak(kode, panjang_otp=0):  # Mendefinisikan fungsi kunci_acak dengan parameter yang tertulis.
    """Kunci acak yang valid untuk algoritma terpilih."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    if kode == "1":  # Menjalankan blok hanya jika kode == "1".
        return str(secrets.randbelow(25) + 1)  # Mengembalikan str(secrets.randbelow(25) + 1).
    if kode in ("2", "3"):  # Menjalankan blok hanya jika kode in ("2", "3").
        return "".join((secrets.choice(ALFABET) for _ in range(8)))  # Mengembalikan "".join((secrets.choice(ALFABET) for _ in range(8))).
    if kode == "4":  # Menjalankan blok hanya jika kode == "4".
        while True:  # Mengulangi blok selama True.
            angka = " ".join((str(secrets.randbelow(26)) for _ in range(4)))  # Menghitung atau menyiapkan ' '.join((str(secrets.randbelow(26)) for _ in range(4))), lalu menyimpannya pada angka.
            try:  # Memulai operasi yang dapat menghasilkan exception.
                hill_parse_kunci(angka)  # Memanggil hill_parse_kunci untuk menjalankan operasi dengan argumen yang diberikan.
                return angka  # Mengembalikan angka.
            except ValueError:  # Menangani exception ValueError.
                continue  # Melanjutkan ke iterasi berikutnya.
    if kode == "5":  # Menjalankan blok hanya jika kode == "5".
        return otp_buat_kunci(panjang_otp).hex()  # Mengembalikan otp_buat_kunci(panjang_otp).hex().
    return str(secrets.randbelow(256))  # Mengembalikan str(secrets.randbelow(256)).


@contextlib.contextmanager  # Menerapkan dekorator contextlib.contextmanager pada fungsi di bawahnya.
def _folder_sementara():  # Mendefinisikan fungsi _folder_sementara dengan parameter yang tertulis.
    """Pindah ke folder sementara agar file demo/benchmark tidak mengotori folder program."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    awal = os.getcwd()  # Menghitung atau menyiapkan os.getcwd(), lalu menyimpannya pada awal.
    with tempfile.TemporaryDirectory(prefix="cryptozar_") as tmp:  # Mengelola sumber daya atau konteks tempfile.TemporaryDirectory(prefix="cryptozar_") as tmp.
        os.chdir(tmp)  # Memanggil os.chdir untuk menjalankan operasi dengan argumen yang diberikan.
        try:  # Memulai operasi yang dapat menghasilkan exception.
            yield tmp  # Menyusun bagian ekspresi yield tmp.
        finally:  # Menjalankan pembersihan meskipun terjadi exception.
            os.chdir(awal)  # Mengembalikan direktori kerja ke lokasi sebelum konteks sementara.


def jalankan_demo():  # Mendefinisikan fungsi jalankan_demo dengan parameter yang tertulis.
    with _folder_sementara():  # Mengelola sumber daya atau konteks _folder_sementara().
        demo_belajar_kriptografi()  # Memanggil demo_belajar_kriptografi untuk menjalankan operasi dengan argumen yang diberikan.
    print(  # Memanggil print untuk menampilkan informasi.
        "\n[GUI] File hasil demo bersifat sementara dan dihapus otomatis setelah demo selesai."  # Memanggil print untuk menampilkan informasi.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.


def jalankan_benchmark(sertakan_1mib, ulang):  # Mendefinisikan fungsi jalankan_benchmark dengan parameter yang tertulis.
    ukuran = [1024, 10 * 1024, 100 * 1024] + ([1024 * 1024] if sertakan_1mib else [])  # Menghitung atau menyiapkan [1024, 10 * 1024, 100 * 1024] + ([1024 * 1024] if sertakan_1mib else []), lalu menyimpannya pada ukuran.
    nama_csv = "hasil_beban_komputasi.csv"  # Menghitung atau menyiapkan 'hasil_beban_komputasi.csv', lalu menyimpannya pada nama_csv.
    with _folder_sementara():  # Mengelola sumber daya atau konteks _folder_sementara().
        ukur_beban_komputasi(ukuran, ulang, nama_csv)  # Memanggil ukur_beban_komputasi untuk menjalankan operasi dengan argumen yang diberikan.
        return baca_teks(nama_csv)  # Mengembalikan baca_teks(nama_csv).


class _PenulisAntrean:  # Mendefinisikan kelas _PenulisAntrean untuk mengelompokkan data dan perilaku.
    """Pengganti sys.stdout: mengalirkan print() backend ke antrean untuk ditampilkan di GUI."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.

    encoding = "utf-8"  # Menghitung atau menyiapkan 'utf-8', lalu menyimpannya pada encoding.

    def __init__(self, q):  # Mendefinisikan fungsi __init__ dengan parameter yang tertulis.
        self.q = q  # Menghitung atau menyiapkan q, lalu menyimpannya pada self.q.

    def write(self, s):  # Mendefinisikan fungsi write dengan parameter yang tertulis.
        if s:  # Menjalankan blok hanya jika s.
            self.q.put(("log", s))  # Memanggil self.q.put untuk menjalankan operasi dengan argumen yang diberikan.
        return len(s)  # Mengembalikan len(s).

    def flush(self):  # Mendefinisikan fungsi flush dengan parameter yang tertulis.
        pass  # Membiarkan blok kosong tanpa operasi tambahan.

    def isatty(self):  # Mendefinisikan fungsi isatty dengan parameter yang tertulis.
        return False  # Mengembalikan False.
