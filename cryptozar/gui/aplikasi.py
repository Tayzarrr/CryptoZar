# CryptoZar — gui.aplikasi
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.gui.tema import BG  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BLUE  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BLUE_INK  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.aset import EMBLEM_PNG  # Mengimpor komponen yang dibutuhkan dari cryptozar.aset.
from cryptozar.gui.halaman_log import HalamanBenchmark  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.halaman_log.
from cryptozar.gui.halaman_log import HalamanDemo  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.halaman_log.
from cryptozar.gui.halaman_kripto import HalamanKripto  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.halaman_kripto.
from cryptozar.aset import IKON_PNG  # Mengimpor komponen yang dibutuhkan dari cryptozar.aset.
from cryptozar.gui.tema import INK  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.aset import LOGO_PNG  # Mengimpor komponen yang dibutuhkan dari cryptozar.aset.
from cryptozar.gui.tema import NAV_H  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import SIDEBAR  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.komponen import Toast  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
from cryptozar.layanan_gui import _PenulisAntrean  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_gui.
import contextlib  # Memuat pustaka contextlib.
import customtkinter as ctk  # Memuat pustaka customtkinter as ctk.
from cryptozar.gui.tema import fnt  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.komponen import muat_b64  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
import os  # Memuat pustaka os.
from cryptozar.gui.komponen import pil_ke_ctk  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
import queue  # Memuat pustaka queue.
import sys  # Memuat pustaka sys.
import tempfile  # Memuat pustaka tempfile.
import threading  # Memuat pustaka threading.


class CryptoZarApp(ctk.CTk):  # Mendefinisikan kelas CryptoZarApp untuk mengelompokkan data dan perilaku.

    def __init__(self):  # Mendefinisikan fungsi __init__ dengan parameter yang tertulis.
        super().__init__()  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
        self.title("CryptoZar")  # Memanggil self.title untuk menjalankan operasi dengan argumen yang diberikan.
        self.geometry("1260x820")  # Memanggil self.geometry untuk menjalankan operasi dengan argumen yang diberikan.
        self.minsize(1120, 740)  # Memanggil self.minsize untuk menjalankan operasi dengan argumen yang diberikan.
        self.configure(fg_color=BG)  # Memanggil self.configure untuk memperbarui konfigurasi widget.
        self.busy = False  # Menandai aplikasi siap menerima pekerjaan baru.
        self.toast = Toast(self)  # Menghitung atau menyiapkan Toast(self), lalu menyimpannya pada self.toast.
        self.grid_columnconfigure(1, weight=1)  # Memanggil self.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        self.grid_rowconfigure(0, weight=1)  # Memanggil self.grid_rowconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        sisi = ctk.CTkFrame(self, width=250, fg_color=SIDEBAR, corner_radius=0)  # Menghitung atau menyiapkan ctk.CTkFrame(self, width=250, fg_color=SIDEBAR, corner_radius=0), lalu menyimpannya pada sisi.
        sisi.grid(row=0, column=0, sticky="nsw")  # Memanggil sisi.grid untuk menempatkan widget pada baris dan kolom.
        sisi.grid_propagate(False)  # Memanggil sisi.grid_propagate untuk menjalankan operasi dengan argumen yang diberikan.
        kepala = ctk.CTkFrame(sisi, fg_color="transparent")  # Menghitung atau menyiapkan ctk.CTkFrame(sisi, fg_color='transparent'), lalu menyimpannya pada kepala.
        kepala.pack(fill="x", padx=22, pady=(30, 30))  # Memanggil kepala.pack untuk menempatkan widget dengan tata letak pack.
        self._logo = pil_ke_ctk(muat_b64(LOGO_PNG), 64)  # Menghitung atau menyiapkan pil_ke_ctk(muat_b64(LOGO_PNG), 64), lalu menyimpannya pada self._logo.
        ctk.CTkLabel(kepala, image=self._logo, text="").pack(side="left")  # Memanggil ctk.CTkLabel(kepala, image=self._logo, text='').pack untuk menempatkan widget dengan tata letak pack.
        ctk.CTkLabel(kepala, text="CryptoZar", font=fnt(27, "bold"), text_color=INK).pack(  # Memanggil ctk.CTkLabel(kepala, text='CryptoZar', font=fnt(27, 'bold'), text_color=INK).pack untuk menempatkan widget dengan tata letak pack.
            side="left", padx=(12, 0)  # Memanggil ctk.CTkLabel(kepala, text='CryptoZar', font=fnt(27, 'bold'), text_color=INK).pack untuk menempatkan widget dengan tata letak pack.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self._emblem = pil_ke_ctk(muat_b64(EMBLEM_PNG), 220)  # Menghitung atau menyiapkan pil_ke_ctk(muat_b64(EMBLEM_PNG), 220), lalu menyimpannya pada self._emblem.
        ctk.CTkLabel(sisi, image=self._emblem, text="").pack(side="bottom", pady=(0, 24))  # Memanggil ctk.CTkLabel(sisi, image=self._emblem, text='').pack untuk menempatkan widget dengan tata letak pack.
        isi = ctk.CTkFrame(self, fg_color=BG, corner_radius=0)  # Menghitung atau menyiapkan ctk.CTkFrame(self, fg_color=BG, corner_radius=0), lalu menyimpannya pada isi.
        isi.grid(row=0, column=1, sticky="nsew")  # Memanggil isi.grid untuk menempatkan widget pada baris dan kolom.
        isi.grid_columnconfigure(0, weight=1)  # Memanggil isi.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        isi.grid_rowconfigure(0, weight=1)  # Memanggil isi.grid_rowconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        self.halaman = {  # Menghitung atau menyiapkan {'Encrypt': HalamanKripto(isi, self, 'encrypt'), 'Decrypt': HalamanKripto(isi, self, 'decrypt'), 'Demo': Halam, lalu menyimpannya pada self.halaman.
            "Encrypt": HalamanKripto(isi, self, "encrypt"),  # Menghitung atau menyiapkan {'Encrypt': HalamanKripto(isi, self, 'encrypt'), 'Decrypt': HalamanKripto(isi, self, 'decrypt'), 'Demo': Halam, lalu menyimpannya pada self.halaman.
            "Decrypt": HalamanKripto(isi, self, "decrypt"),  # Menghitung atau menyiapkan {'Encrypt': HalamanKripto(isi, self, 'encrypt'), 'Decrypt': HalamanKripto(isi, self, 'decrypt'), 'Demo': Halam, lalu menyimpannya pada self.halaman.
            "Demo": HalamanDemo(isi, self),  # Menghitung atau menyiapkan {'Encrypt': HalamanKripto(isi, self, 'encrypt'), 'Decrypt': HalamanKripto(isi, self, 'decrypt'), 'Demo': Halam, lalu menyimpannya pada self.halaman.
            "Benchmark": HalamanBenchmark(isi, self),  # Menghitung atau menyiapkan {'Encrypt': HalamanKripto(isi, self, 'encrypt'), 'Decrypt': HalamanKripto(isi, self, 'decrypt'), 'Demo': Halam, lalu menyimpannya pada self.halaman.
        }  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.nav = {}  # Menghitung atau menyiapkan {}, lalu menyimpannya pada self.nav.
        for nama, hal in self.halaman.items():  # Mengulangi proses untuk nama, hal in self.halaman.items().
            hal.grid(row=0, column=0, sticky="nsew")  # Memanggil hal.grid untuk menempatkan widget pada baris dan kolom.
            b = ctk.CTkButton(  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
                sisi,  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
                text=nama,  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
                anchor="w",  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
                height=44,  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
                corner_radius=12,  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
                fg_color="transparent",  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
                hover_color=NAV_H,  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
                text_color=INK,  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
                font=fnt(15),  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
                command=lambda n=nama: self.tampil(n),  # Menghitung atau menyiapkan ctk.CTkButton(sisi, text=nama, anchor='w', height=44, corner_radius=12, fg_color='transparent', hover_color=NA, lalu menyimpannya pada b.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
            b.pack(fill="x", padx=16, pady=3)  # Memanggil b.pack untuk menempatkan widget dengan tata letak pack.
            self.nav[nama] = b  # Menghitung atau menyiapkan b, lalu menyimpannya pada self.nav[nama].
        self.tampil("Encrypt")  # Memanggil self.tampil untuk menjalankan operasi dengan argumen yang diberikan.
        self._pasang_ikon()  # Memanggil self._pasang_ikon untuk menjalankan operasi dengan argumen yang diberikan.
        self.after(300, self._pasang_ikon)  # Memanggil self.after untuk menjadwalkan callback.

    def _pasang_ikon(self):  # Mendefinisikan fungsi _pasang_ikon dengan parameter yang tertulis.
        """Ganti ikon kotak biru bawaan (pojok kiri atas jendela & taskbar) dengan logo."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
        try:  # Memulai operasi yang dapat menghasilkan exception.
            from PIL import Image, ImageTk  # Mengimpor komponen yang dibutuhkan dari PIL.

            img = muat_b64(IKON_PNG)  # Menghitung atau menyiapkan muat_b64(IKON_PNG), lalu menyimpannya pada img.
            self._ikon_tk = ImageTk.PhotoImage(img.resize((64, 64), Image.LANCZOS))  # Menghitung atau menyiapkan ImageTk.PhotoImage(img.resize((64, 64), Image.LANCZOS)), lalu menyimpannya pada self._ikon_tk.
            self.iconphoto(True, self._ikon_tk)  # Memanggil self.iconphoto untuk menjalankan operasi dengan argumen yang diberikan.
            if sys.platform.startswith("win"):  # Menjalankan blok hanya jika sys.platform.startswith("win").
                ico = os.path.join(tempfile.gettempdir(), "cryptozar.ico")  # Menghitung atau menyiapkan os.path.join(tempfile.gettempdir(), 'cryptozar.ico'), lalu menyimpannya pada ico.
                img.save(  # Memanggil img.save untuk menjalankan operasi dengan argumen yang diberikan.
                    ico,  # Memanggil img.save untuk menjalankan operasi dengan argumen yang diberikan.
                    format="ICO",  # Memanggil img.save untuk menjalankan operasi dengan argumen yang diberikan.
                    sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (256, 256)],  # Memanggil img.save untuk menjalankan operasi dengan argumen yang diberikan.
                )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
                self.iconbitmap(ico)  # Memanggil self.iconbitmap untuk menjalankan operasi dengan argumen yang diberikan.
        except Exception:  # Menangani exception Exception.
            pass  # Membiarkan blok kosong tanpa operasi tambahan.

    def tampil(self, nama):  # Mendefinisikan fungsi tampil dengan parameter yang tertulis.
        self.halaman[nama].tkraise()  # Memanggil self.halaman[nama].tkraise untuk menjalankan operasi dengan argumen yang diberikan.
        for n, b in self.nav.items():  # Mengulangi proses untuk n, b in self.nav.items().
            aktif = n == nama  # Menghitung atau menyiapkan n == nama, lalu menyimpannya pada aktif.
            b.configure(  # Memanggil b.configure untuk memperbarui konfigurasi widget.
                fg_color=BLUE if aktif else "transparent",  # Memanggil b.configure untuk memperbarui konfigurasi widget.
                text_color=BLUE_INK if aktif else INK,  # Memanggil b.configure untuk memperbarui konfigurasi widget.
                font=fnt(15, "bold" if aktif else "normal"),  # Memanggil b.configure untuk memperbarui konfigurasi widget.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

    def jalankan_tugas(self, fn, on_selesai, on_gagal, on_log=None):  # Mendefinisikan fungsi jalankan_tugas dengan parameter yang tertulis.
        """Jalankan fn di thread terpisah agar jendela tetap responsif.
        Jika on_log diberikan, print() dari fn dialirkan ke on_log secara langsung."""
        q = queue.Queue()  # Menghitung atau menyiapkan queue.Queue(), lalu menyimpannya pada q.

        def kerja():  # Mendefinisikan fungsi kerja dengan parameter yang tertulis.
            try:  # Memulai operasi yang dapat menghasilkan exception.
                if on_log:  # Menjalankan blok hanya jika on_log.
                    with contextlib.redirect_stdout(_PenulisAntrean(q)):  # Mengelola sumber daya atau konteks contextlib.redirect_stdout(_PenulisAntrean(q)).
                        hasil = fn()  # Menghitung atau menyiapkan fn(), lalu menyimpannya pada hasil.
                else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
                    hasil = fn()  # Menghitung atau menyiapkan fn(), lalu menyimpannya pada hasil.
                q.put(("selesai", hasil))  # Memanggil q.put untuk menjalankan operasi dengan argumen yang diberikan.
            except BaseException as e:  # Menangani exception BaseException as e.
                q.put(("gagal", e))  # Memanggil q.put untuk menjalankan operasi dengan argumen yang diberikan.

        threading.Thread(target=kerja, daemon=True).start()  # Memanggil threading.Thread(target=kerja, daemon=True).start untuk menjalankan operasi dengan argumen yang diberikan.

        def cek():  # Mendefinisikan fungsi cek dengan parameter yang tertulis.
            try:  # Memulai operasi yang dapat menghasilkan exception.
                while True:  # Mengulangi blok selama True.
                    jenis, isi = q.get_nowait()  # Menghitung atau menyiapkan q.get_nowait(), lalu menyimpannya pada (jenis, isi).
                    if jenis == "log":  # Menjalankan blok hanya jika jenis == "log".
                        on_log(isi)  # Memanggil on_log untuk menjalankan operasi dengan argumen yang diberikan.
                    elif jenis == "selesai":  # Memeriksa kondisi alternatif jenis == "selesai".
                        on_selesai(isi)  # Memanggil on_selesai untuk menjalankan operasi dengan argumen yang diberikan.
                        return  # Mengembalikan kendali ke pemanggil.
                    else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
                        on_gagal(isi)  # Memanggil on_gagal untuk menjalankan operasi dengan argumen yang diberikan.
                        return  # Mengembalikan kendali ke pemanggil.
            except queue.Empty:  # Menangani exception queue.Empty.
                pass  # Membiarkan blok kosong tanpa operasi tambahan.
            self.after(60, cek)  # Memanggil self.after untuk menjadwalkan callback.

        cek()  # Memanggil cek untuk menjalankan operasi dengan argumen yang diberikan.
