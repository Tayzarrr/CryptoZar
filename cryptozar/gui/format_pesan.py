# CryptoZar — gui.format_pesan
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
import math  # Memuat pustaka math.


def fmt_ukuran(b):  # Mendefinisikan fungsi fmt_ukuran dengan parameter yang tertulis.
    if b < 1024:  # Menjalankan blok hanya jika b < 1024.
        return f"{b} B"  # Mengembalikan f"{b} B".
    if b < 1024 * 1024:  # Menjalankan blok hanya jika b < 1024 * 1024.
        return f"{b / 1024:.2f} KB"  # Mengembalikan f"{b / 1024:.2f} KB".
    return f"{b / (1024 * 1024):.2f} MB"  # Mengembalikan f"{b / (1024 * 1024):.2f} MB".


def fmt_durasi(detik):  # Mendefinisikan fungsi fmt_durasi dengan parameter yang tertulis.
    if detik < 1:  # Menjalankan blok hanya jika detik < 1.
        return f"{detik * 1000:.1f} ms"  # Mengembalikan f"{detik * 1000:.1f} ms".
    if detik < 60:  # Menjalankan blok hanya jika detik < 60.
        return f"{detik:.2f} s"  # Mengembalikan f"{detik:.2f} s".
    m, s = divmod(int(round(detik)), 60)  # Menghitung atau menyiapkan divmod(int(round(detik)), 60), lalu menyimpannya pada (m, s).
    return f"{m} m {s:02d} s"  # Mengembalikan f"{m} m {s:02d} s".


def frak_log(nilai, lo, hi):  # Mendefinisikan fungsi frak_log dengan parameter yang tertulis.
    """Posisi 0..1 pada skala logaritmik untuk panjang bilah metrik."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    if nilai is None or nilai <= 0:  # Menjalankan blok hanya jika nilai is None or nilai <= 0.
        return 0.0  # Mengembalikan 0.0.
    return max(0.03, min(1.0, math.log10(nilai / lo) / math.log10(hi / lo)))  # Mengembalikan max(0.03, min(1.0, math.log10(nilai / lo) / math.log10(hi / lo))).


def pesan_error(e):  # Mendefinisikan fungsi pesan_error dengan parameter yang tertulis.
    """Ubah exception menjadi pesan yang ramah untuk pengguna."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    if isinstance(e, UnicodeDecodeError):  # Menjalankan blok hanya jika isinstance(e, UnicodeDecodeError).
        return "File bukan teks UTF-8 yang valid. Pilih file .txt berformat teks."  # Mengembalikan "File bukan teks UTF-8 yang valid. Pilih file .txt berformat teks.".
    if isinstance(e, FileNotFoundError):  # Menjalankan blok hanya jika isinstance(e, FileNotFoundError).
        return "File tidak ditemukan. Pastikan file masih ada di lokasinya."  # Mengembalikan "File tidak ditemukan. Pastikan file masih ada di lokasinya.".
    if isinstance(e, PermissionError):  # Menjalankan blok hanya jika isinstance(e, PermissionError).
        return "Akses ke file ditolak oleh sistem."  # Mengembalikan "Akses ke file ditolak oleh sistem.".
    if isinstance(e, MemoryError):  # Menjalankan blok hanya jika isinstance(e, MemoryError).
        return "Memori tidak cukup untuk memproses data sebesar ini."  # Mengembalikan "Memori tidak cukup untuk memproses data sebesar ini.".
    if isinstance(e, (ValueError, OSError)):  # Menjalankan blok hanya jika isinstance(e, (ValueError, OSError)).
        return str(e)  # Mengembalikan str(e).
    return f"Terjadi kesalahan tak terduga ({type(e).__name__}): {e}"  # Mengembalikan f"Terjadi kesalahan tak terduga ({type(e).__name__}): {e}".
