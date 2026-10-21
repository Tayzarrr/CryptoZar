# CryptoZar — peluncur
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.gui.aplikasi import CryptoZarApp  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.aplikasi.
import customtkinter as ctk  # Memuat pustaka customtkinter as ctk.
import sys  # Memuat pustaka sys.


def main():  # Mendefinisikan fungsi main dengan parameter yang tertulis.
    if sys.platform.startswith("win"):  # Menjalankan blok hanya jika sys.platform.startswith("win").
        try:  # Memulai operasi yang dapat menghasilkan exception.
            import ctypes  # Memuat pustaka ctypes.

            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("cryptozar.app")  # Memanggil ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID untuk menjalankan operasi dengan argumen yang diberikan.
        except Exception:  # Menangani exception Exception.
            pass  # Membiarkan blok kosong tanpa operasi tambahan.
    ctk.set_appearance_mode("light")  # Memanggil ctk.set_appearance_mode untuk menjalankan operasi dengan argumen yang diberikan.
    ctk.set_default_color_theme("blue")  # Memanggil ctk.set_default_color_theme untuk menjalankan operasi dengan argumen yang diberikan.
    CryptoZarApp().mainloop()  # Memanggil CryptoZarApp().mainloop untuk menjalankan loop peristiwa jendela.
