# CryptoZar — gui.halaman_kripto
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.gui.tema import BATAS_KUNCI  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BATAS_PRATINJAU  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BATAS_TAMPIL  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BG  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BLUE  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BLUE_INK  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BORDER  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.komponen import BarisMetrik  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
from cryptozar.gui.tema import CARD  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import INK  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import METRIK_BG  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import MUTED  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import NAMA_ALGO  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import NEUTRAL  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import NEUTRAL_H  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.konfigurasi import PROMPT_KUNCI  # Mengimpor komponen yang dibutuhkan dari cryptozar.konfigurasi.
from cryptozar.file_io import baca_hex  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.file_io import baca_teks  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
import customtkinter as ctk  # Memuat pustaka customtkinter as ctk.
from tkinter import filedialog  # Mengimpor komponen yang dibutuhkan dari tkinter.
from cryptozar.gui.format_pesan import fmt_durasi  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.format_pesan.
from cryptozar.gui.format_pesan import fmt_ukuran  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.format_pesan.
from cryptozar.gui.tema import fnt  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.format_pesan import frak_log  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.format_pesan.
from cryptozar.gui.komponen import isi_readonly  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
from cryptozar.layanan_gui import jalankan_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_gui.
from cryptozar.layanan_gui import jalankan_enkripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_gui.
from cryptozar.gui.komponen import kartu  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
from cryptozar.gui.komponen import kotak_teks  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
from cryptozar.layanan_gui import kunci_acak  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_gui.
import os  # Memuat pustaka os.
from cryptozar.gui.format_pesan import pesan_error  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.format_pesan.
from cryptozar.gui.komponen import tombol  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
from cryptozar.file_io import tulis_bytes  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.
from cryptozar.file_io import tulis_teks  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.


class HalamanKripto(ctk.CTkFrame):  # Mendefinisikan kelas HalamanKripto untuk mengelompokkan data dan perilaku.

    def __init__(self, master, app, mode):  # Mendefinisikan fungsi __init__ dengan parameter yang tertulis.
        super().__init__(master, fg_color=BG, corner_radius=0)  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
        self.app = app  # Menghitung atau menyiapkan app, lalu menyimpannya pada self.app.
        self.mode = mode  # Menghitung atau menyiapkan mode, lalu menyimpannya pada self.mode.
        self.file_path = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada self.file_path.
        self.key_full = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada self.key_full.
        self.hasil = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada self.hasil.
        self.running = False  # Menghitung atau menyiapkan False, lalu menyimpannya pada self.running.
        enc = mode == "encrypt"  # Menghitung atau menyiapkan mode == 'encrypt', lalu menyimpannya pada enc.
        self.teks_run = "Run Encryption" if enc else "Run Decryption"  # Menghitung atau menyiapkan 'Run Encryption' if enc else 'Run Decryption', lalu menyimpannya pada self.teks_run.
        self.grid_columnconfigure(0, weight=3, uniform="kol")  # Memanggil self.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        self.grid_columnconfigure(1, weight=2, uniform="kol")  # Memanggil self.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        self.grid_rowconfigure(1, weight=1)  # Memanggil self.grid_rowconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        ctk.CTkLabel(  # Memanggil ctk.CTkLabel(self, text='Encrypt' if enc else 'Decrypt', font=fnt(28, 'bold'), text_color=INK, anchor='w').gri untuk menjalankan operasi dengan argumen yang diberikan.
            self,  # Memanggil ctk.CTkLabel(self, text='Encrypt' if enc else 'Decrypt', font=fnt(28, 'bold'), text_color=INK, anchor='w').gri untuk menjalankan operasi dengan argumen yang diberikan.
            text="Encrypt" if enc else "Decrypt",  # Memanggil ctk.CTkLabel(self, text='Encrypt' if enc else 'Decrypt', font=fnt(28, 'bold'), text_color=INK, anchor='w').gri untuk menjalankan operasi dengan argumen yang diberikan.
            font=fnt(28, "bold"),  # Memanggil ctk.CTkLabel(self, text='Encrypt' if enc else 'Decrypt', font=fnt(28, 'bold'), text_color=INK, anchor='w').gri untuk menjalankan operasi dengan argumen yang diberikan.
            text_color=INK,  # Memanggil ctk.CTkLabel(self, text='Encrypt' if enc else 'Decrypt', font=fnt(28, 'bold'), text_color=INK, anchor='w').gri untuk menjalankan operasi dengan argumen yang diberikan.
            anchor="w",  # Memanggil ctk.CTkLabel(self, text='Encrypt' if enc else 'Decrypt', font=fnt(28, 'bold'), text_color=INK, anchor='w').gri untuk menjalankan operasi dengan argumen yang diberikan.
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=28, pady=(24, 10))  # Memanggil ctk.CTkLabel(self, text='Encrypt' if enc else 'Decrypt', font=fnt(28, 'bold'), text_color=INK, anchor='w').gri untuk menjalankan operasi dengan argumen yang diberikan.
        kiri = ctk.CTkFrame(self, fg_color="transparent")  # Menghitung atau menyiapkan ctk.CTkFrame(self, fg_color='transparent'), lalu menyimpannya pada kiri.
        kiri.grid(row=1, column=0, sticky="nsew", padx=(28, 10), pady=(0, 22))  # Memanggil kiri.grid untuk menempatkan widget pada baris dan kolom.
        kiri.grid_columnconfigure(0, weight=1)  # Memanggil kiri.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        kiri.grid_rowconfigure(0, weight=1)  # Memanggil kiri.grid_rowconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        kanan = ctk.CTkFrame(self, fg_color="transparent")  # Menghitung atau menyiapkan ctk.CTkFrame(self, fg_color='transparent'), lalu menyimpannya pada kanan.
        kanan.grid(row=1, column=1, sticky="nsew", padx=(10, 28), pady=(0, 22))  # Memanggil kanan.grid untuk menempatkan widget pada baris dan kolom.
        kanan.grid_columnconfigure(0, weight=1)  # Memanggil kanan.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        kanan.grid_rowconfigure(1, weight=1)  # Memanggil kanan.grid_rowconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        self._bangun_input(kiri)  # Memanggil self._bangun_input untuk menjalankan operasi dengan argumen yang diberikan.
        self._bangun_kunci(kiri)  # Memanggil self._bangun_kunci untuk menjalankan operasi dengan argumen yang diberikan.
        self._bangun_metrik(kanan)  # Memanggil self._bangun_metrik untuk menjalankan operasi dengan argumen yang diberikan.
        self._bangun_hasil(kanan)  # Memanggil self._bangun_hasil untuk menjalankan operasi dengan argumen yang diberikan.
        self._bangun_aksi(kanan)  # Memanggil self._bangun_aksi untuk menjalankan operasi dengan argumen yang diberikan.
        self._ganti_algoritma()  # Memanggil self._ganti_algoritma untuk menjalankan operasi dengan argumen yang diberikan.

    def _bangun_input(self, induk):  # Mendefinisikan fungsi _bangun_input dengan parameter yang tertulis.
        k = kartu(induk)  # Menghitung atau menyiapkan kartu(induk), lalu menyimpannya pada k.
        k.grid(row=0, column=0, sticky="nsew", pady=(0, 14))  # Memanggil k.grid untuk menempatkan widget pada baris dan kolom.
        k.grid_columnconfigure(0, weight=1)  # Memanggil k.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        k.grid_rowconfigure(3, weight=1)  # Memanggil k.grid_rowconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        pad = {"padx": 20}  # Menghitung atau menyiapkan {'padx': 20}, lalu menyimpannya pada pad.
        ctk.CTkLabel(  # Memanggil ctk.CTkLabel(k, text='Cryptography Algorithm', font=fnt(14, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
            k, text="Cryptography Algorithm", font=fnt(14, "bold"), text_color=INK, anchor="w"  # Memanggil ctk.CTkLabel(k, text='Cryptography Algorithm', font=fnt(14, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        ).grid(row=0, column=0, sticky="w", pady=(16, 6), **pad)  # Memanggil ctk.CTkLabel(k, text='Cryptography Algorithm', font=fnt(14, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        self.algo_var = ctk.StringVar(value="Caesar Cipher")  # Menghitung atau menyiapkan ctk.StringVar(value='Caesar Cipher'), lalu menyimpannya pada self.algo_var.
        ctk.CTkOptionMenu(  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            k,  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            values=list(NAMA_ALGO),  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            variable=self.algo_var,  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            command=lambda _v: self._ganti_algoritma(),  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            height=38,  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            corner_radius=10,  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            fg_color=NEUTRAL,  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            button_color=NEUTRAL_H,  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            button_hover_color="#DAD3BE",  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            text_color=INK,  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            dropdown_fg_color=CARD,  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            dropdown_hover_color=BLUE,  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            dropdown_text_color=INK,  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            font=fnt(13),  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            dropdown_font=fnt(13),  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
            anchor="w",  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
        ).grid(row=1, column=0, sticky="ew", **pad)  # Memanggil ctk.CTkOptionMenu(k, values=list(NAMA_ALGO), variable=self.algo_var, command=lambda _v: self._ganti_algoritma( untuk menjalankan operasi dengan argumen yang diberikan.
        judul = (  # Menghitung atau menyiapkan 'Enter Plaintext' if self.mode == 'encrypt' else 'Enter Ciphertext (hex untuk OTP / Stream)', lalu menyimpannya pada judul.
            "Enter Plaintext"  # Menghitung atau menyiapkan 'Enter Plaintext' if self.mode == 'encrypt' else 'Enter Ciphertext (hex untuk OTP / Stream)', lalu menyimpannya pada judul.
            if self.mode == "encrypt"  # Menjalankan blok hanya jika self.mode == "encrypt.
            else "Enter Ciphertext (hex untuk OTP / Stream)"  # Menghitung atau menyiapkan 'Enter Plaintext' if self.mode == 'encrypt' else 'Enter Ciphertext (hex untuk OTP / Stream)', lalu menyimpannya pada judul.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        ctk.CTkLabel(k, text=judul, font=fnt(14, "bold"), text_color=INK, anchor="w").grid(  # Memanggil ctk.CTkLabel(k, text=judul, font=fnt(14, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
            row=2, column=0, sticky="w", pady=(14, 6), **pad  # Memanggil ctk.CTkLabel(k, text=judul, font=fnt(14, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.input = kotak_teks(k, height=120)  # Menghitung atau menyiapkan kotak_teks(k, height=120), lalu menyimpannya pada self.input.
        self.input.grid(row=3, column=0, sticky="nsew", **pad)  # Memanggil self.input.grid untuk menempatkan widget pada baris dan kolom.
        baris = ctk.CTkFrame(k, fg_color="transparent")  # Menghitung atau menyiapkan ctk.CTkFrame(k, fg_color='transparent'), lalu menyimpannya pada baris.
        baris.grid(row=4, column=0, sticky="ew", pady=(10, 16), **pad)  # Memanggil baris.grid untuk menempatkan widget pada baris dan kolom.
        baris.grid_columnconfigure(1, weight=1)  # Memanggil baris.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        tombol(baris, "Upload .txt File", self._upload_input, "blue", width=150).grid(  # Memanggil tombol(baris, 'Upload .txt File', self._upload_input, 'blue', width=150).grid untuk menempatkan widget pada baris dan kolom.
            row=0, column=0  # Memanggil tombol(baris, 'Upload .txt File', self._upload_input, 'blue', width=150).grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.lbl_file = ctk.CTkLabel(  # Menghitung atau menyiapkan ctk.CTkLabel(baris, text='Belum ada file - ketik teks di atas atau unggah file', font=fnt(12), text_color=MUTE, lalu menyimpannya pada self.lbl_file.
            baris,  # Menghitung atau menyiapkan ctk.CTkLabel(baris, text='Belum ada file - ketik teks di atas atau unggah file', font=fnt(12), text_color=MUTE, lalu menyimpannya pada self.lbl_file.
            text="Belum ada file - ketik teks di atas atau unggah file",  # Menghitung atau menyiapkan ctk.CTkLabel(baris, text='Belum ada file - ketik teks di atas atau unggah file', font=fnt(12), text_color=MUTE, lalu menyimpannya pada self.lbl_file.
            font=fnt(12),  # Menghitung atau menyiapkan ctk.CTkLabel(baris, text='Belum ada file - ketik teks di atas atau unggah file', font=fnt(12), text_color=MUTE, lalu menyimpannya pada self.lbl_file.
            text_color=MUTED,  # Menghitung atau menyiapkan ctk.CTkLabel(baris, text='Belum ada file - ketik teks di atas atau unggah file', font=fnt(12), text_color=MUTE, lalu menyimpannya pada self.lbl_file.
            anchor="w",  # Menghitung atau menyiapkan ctk.CTkLabel(baris, text='Belum ada file - ketik teks di atas atau unggah file', font=fnt(12), text_color=MUTE, lalu menyimpannya pada self.lbl_file.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.lbl_file.grid(row=0, column=1, sticky="w", padx=12)  # Memanggil self.lbl_file.grid untuk menempatkan widget pada baris dan kolom.
        self.btn_hapus_file = tombol(  # Menghitung atau menyiapkan tombol(baris, 'Remove', self._hapus_file, 'ghost', width=70, height=30), lalu menyimpannya pada self.btn_hapus_file.
            baris, "Remove", self._hapus_file, "ghost", width=70, height=30  # Menghitung atau menyiapkan tombol(baris, 'Remove', self._hapus_file, 'ghost', width=70, height=30), lalu menyimpannya pada self.btn_hapus_file.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.btn_hapus_file.grid(row=0, column=2)  # Memanggil self.btn_hapus_file.grid untuk menempatkan widget pada baris dan kolom.
        self.btn_hapus_file.grid_remove()  # Memanggil self.btn_hapus_file.grid_remove untuk menjalankan operasi dengan argumen yang diberikan.

    def _bangun_kunci(self, induk):  # Mendefinisikan fungsi _bangun_kunci dengan parameter yang tertulis.
        k = kartu(induk)  # Menghitung atau menyiapkan kartu(induk), lalu menyimpannya pada k.
        k.grid(row=1, column=0, sticky="ew")  # Memanggil k.grid untuk menempatkan widget pada baris dan kolom.
        k.grid_columnconfigure(0, weight=1)  # Memanggil k.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        pad = {"padx": 20}  # Menghitung atau menyiapkan {'padx': 20}, lalu menyimpannya pada pad.
        ctk.CTkLabel(  # Memanggil ctk.CTkLabel(k, text='Key Configuration', font=fnt(16, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
            k, text="Key Configuration", font=fnt(16, "bold"), text_color=INK, anchor="w"  # Memanggil ctk.CTkLabel(k, text='Key Configuration', font=fnt(16, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(16, 0), **pad)  # Memanggil ctk.CTkLabel(k, text='Key Configuration', font=fnt(16, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        ctk.CTkLabel(  # Memanggil ctk.CTkLabel(k, text='Cryptographic Key (Manual Input)', font=fnt(13), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
            k, text="Cryptographic Key (Manual Input)", font=fnt(13), text_color=INK, anchor="w"  # Memanggil ctk.CTkLabel(k, text='Cryptographic Key (Manual Input)', font=fnt(13), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        ).grid(row=1, column=0, columnspan=2, sticky="w", pady=(2, 6), **pad)  # Memanggil ctk.CTkLabel(k, text='Cryptographic Key (Manual Input)', font=fnt(13), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        self.keybox = kotak_teks(k, mono=True, height=84, wrap="char")  # Menghitung atau menyiapkan kotak_teks(k, mono=True, height=84, wrap='char'), lalu menyimpannya pada self.keybox.
        self.keybox.grid(row=2, column=0, sticky="nsew", padx=(20, 10))  # Memanggil self.keybox.grid untuk menempatkan widget pada baris dan kolom.
        sisi = ctk.CTkFrame(k, fg_color="transparent")  # Menghitung atau menyiapkan ctk.CTkFrame(k, fg_color='transparent'), lalu menyimpannya pada sisi.
        sisi.grid(row=2, column=1, sticky="n", padx=(0, 20))  # Memanggil sisi.grid untuk menempatkan widget pada baris dan kolom.
        self.btn_gen = tombol(  # Menghitung atau menyiapkan tombol(sisi, 'Generate Random Key', self._generate_kunci, 'mint', width=190), lalu menyimpannya pada self.btn_gen.
            sisi, "Generate Random Key", self._generate_kunci, "mint", width=190  # Menghitung atau menyiapkan tombol(sisi, 'Generate Random Key', self._generate_kunci, 'mint', width=190), lalu menyimpannya pada self.btn_gen.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.btn_gen.grid(row=0, column=0, pady=(0, 6))  # Memanggil self.btn_gen.grid untuk menempatkan widget pada baris dan kolom.
        tombol(sisi, "Upload Key File", self._upload_kunci, "neutral", width=190).grid(  # Memanggil tombol(sisi, 'Upload Key File', self._upload_kunci, 'neutral', width=190).grid untuk menempatkan widget pada baris dan kolom.
            row=1, column=0, pady=(0, 6)  # Memanggil tombol(sisi, 'Upload Key File', self._upload_kunci, 'neutral', width=190).grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        tombol(sisi, "Clear Key", self._hapus_kunci, "ghost", width=190, height=28).grid(  # Memanggil tombol(sisi, 'Clear Key', self._hapus_kunci, 'ghost', width=190, height=28).grid untuk menempatkan widget pada baris dan kolom.
            row=2, column=0  # Memanggil tombol(sisi, 'Clear Key', self._hapus_kunci, 'ghost', width=190, height=28).grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.lbl_hint = ctk.CTkLabel(  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='', font=fnt(12), text_color=MUTED, anchor='w', justify='left', wraplength=470), lalu menyimpannya pada self.lbl_hint.
            k,  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='', font=fnt(12), text_color=MUTED, anchor='w', justify='left', wraplength=470), lalu menyimpannya pada self.lbl_hint.
            text="",  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='', font=fnt(12), text_color=MUTED, anchor='w', justify='left', wraplength=470), lalu menyimpannya pada self.lbl_hint.
            font=fnt(12),  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='', font=fnt(12), text_color=MUTED, anchor='w', justify='left', wraplength=470), lalu menyimpannya pada self.lbl_hint.
            text_color=MUTED,  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='', font=fnt(12), text_color=MUTED, anchor='w', justify='left', wraplength=470), lalu menyimpannya pada self.lbl_hint.
            anchor="w",  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='', font=fnt(12), text_color=MUTED, anchor='w', justify='left', wraplength=470), lalu menyimpannya pada self.lbl_hint.
            justify="left",  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='', font=fnt(12), text_color=MUTED, anchor='w', justify='left', wraplength=470), lalu menyimpannya pada self.lbl_hint.
            wraplength=470,  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='', font=fnt(12), text_color=MUTED, anchor='w', justify='left', wraplength=470), lalu menyimpannya pada self.lbl_hint.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.lbl_hint.grid(row=3, column=0, columnspan=2, sticky="w", pady=(8, 16), **pad)  # Memanggil self.lbl_hint.grid untuk menempatkan widget pada baris dan kolom.

    def _bangun_metrik(self, induk):  # Mendefinisikan fungsi _bangun_metrik dengan parameter yang tertulis.
        k = ctk.CTkFrame(  # Menghitung atau menyiapkan ctk.CTkFrame(induk, fg_color=METRIK_BG, corner_radius=16, border_width=1, border_color=BORDER), lalu menyimpannya pada k.
            induk, fg_color=METRIK_BG, corner_radius=16, border_width=1, border_color=BORDER  # Menghitung atau menyiapkan ctk.CTkFrame(induk, fg_color=METRIK_BG, corner_radius=16, border_width=1, border_color=BORDER), lalu menyimpannya pada k.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        k.grid(row=0, column=0, sticky="ew", pady=(0, 14))  # Memanggil k.grid untuk menempatkan widget pada baris dan kolom.
        k.grid_columnconfigure(0, weight=1)  # Memanggil k.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        ctk.CTkLabel(  # Memanggil ctk.CTkLabel(k, text='Performance Metrics', font=fnt(18, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
            k, text="Performance Metrics", font=fnt(18, "bold"), text_color=INK, anchor="w"  # Memanggil ctk.CTkLabel(k, text='Performance Metrics', font=fnt(18, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(16, 8))  # Memanggil ctk.CTkLabel(k, text='Performance Metrics', font=fnt(18, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        self.m_proses = BarisMetrik(k, "Processing Time (ms)", "#8FA2E6")  # Menghitung atau menyiapkan BarisMetrik(k, 'Processing Time (ms)', '#8FA2E6'), lalu menyimpannya pada self.m_proses.
        self.m_thr = BarisMetrik(k, "Throughput (KB/s)", "#8FA2E6")  # Menghitung atau menyiapkan BarisMetrik(k, 'Throughput (KB/s)', '#8FA2E6'), lalu menyimpannya pada self.m_thr.
        self.m_ukuran = BarisMetrik(k, "File Size", "#7CCBA0")  # Menghitung atau menyiapkan BarisMetrik(k, 'File Size', '#7CCBA0'), lalu menyimpannya pada self.m_ukuran.
        self.m_total = BarisMetrik(k, "Time Taken", "#7CCBA0")  # Menghitung atau menyiapkan BarisMetrik(k, 'Time Taken', '#7CCBA0'), lalu menyimpannya pada self.m_total.
        for i, m in enumerate((self.m_proses, self.m_thr, self.m_ukuran, self.m_total), 1):  # Mengulangi proses untuk i, m in enumerate((self.m_proses, self.m_thr, self.m_ukuran, self.m_total), 1).
            m.grid(row=i, column=0, sticky="ew", padx=20, pady=(0, 9 if i < 4 else 18))  # Memanggil m.grid untuk menempatkan widget pada baris dan kolom.

    def _bangun_hasil(self, induk):  # Mendefinisikan fungsi _bangun_hasil dengan parameter yang tertulis.
        k = kartu(induk)  # Menghitung atau menyiapkan kartu(induk), lalu menyimpannya pada k.
        k.grid(row=1, column=0, sticky="nsew", pady=(0, 14))  # Memanggil k.grid untuk menempatkan widget pada baris dan kolom.
        k.grid_columnconfigure(0, weight=1)  # Memanggil k.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        k.grid_rowconfigure(2, weight=1)  # Memanggil k.grid_rowconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        ctk.CTkLabel(  # Memanggil ctk.CTkLabel(k, text='Results Area', font=fnt(18, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
            k, text="Results Area", font=fnt(18, "bold"), text_color=INK, anchor="w"  # Memanggil ctk.CTkLabel(k, text='Results Area', font=fnt(18, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=(16, 0))  # Memanggil ctk.CTkLabel(k, text='Results Area', font=fnt(18, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        ctk.CTkLabel(k, text="Output Results", font=fnt(13), text_color=MUTED, anchor="w").grid(  # Memanggil ctk.CTkLabel(k, text='Output Results', font=fnt(13), text_color=MUTED, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
            row=1, column=0, sticky="w", padx=20, pady=(0, 6)  # Memanggil ctk.CTkLabel(k, text='Output Results', font=fnt(13), text_color=MUTED, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.btn_copy = tombol(  # Menghitung atau menyiapkan tombol(k, 'Copy to Clipboard', self._salin, 'neutral', width=140, height=30, state='disabled'), lalu menyimpannya pada self.btn_copy.
            k,  # Menghitung atau menyiapkan tombol(k, 'Copy to Clipboard', self._salin, 'neutral', width=140, height=30, state='disabled'), lalu menyimpannya pada self.btn_copy.
            "Copy to Clipboard",  # Menghitung atau menyiapkan tombol(k, 'Copy to Clipboard', self._salin, 'neutral', width=140, height=30, state='disabled'), lalu menyimpannya pada self.btn_copy.
            self._salin,  # Menghitung atau menyiapkan tombol(k, 'Copy to Clipboard', self._salin, 'neutral', width=140, height=30, state='disabled'), lalu menyimpannya pada self.btn_copy.
            "neutral",  # Menghitung atau menyiapkan tombol(k, 'Copy to Clipboard', self._salin, 'neutral', width=140, height=30, state='disabled'), lalu menyimpannya pada self.btn_copy.
            width=140,  # Menghitung atau menyiapkan tombol(k, 'Copy to Clipboard', self._salin, 'neutral', width=140, height=30, state='disabled'), lalu menyimpannya pada self.btn_copy.
            height=30,  # Menghitung atau menyiapkan tombol(k, 'Copy to Clipboard', self._salin, 'neutral', width=140, height=30, state='disabled'), lalu menyimpannya pada self.btn_copy.
            state="disabled",  # Menghitung atau menyiapkan tombol(k, 'Copy to Clipboard', self._salin, 'neutral', width=140, height=30, state='disabled'), lalu menyimpannya pada self.btn_copy.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.btn_copy.grid(row=1, column=1, sticky="e", padx=(0, 20), pady=(0, 6))  # Memanggil self.btn_copy.grid untuk menempatkan widget pada baris dan kolom.
        self.output = kotak_teks(k, mono=True, wrap="char", height=90, state="disabled")  # Menghitung atau menyiapkan kotak_teks(k, mono=True, wrap='char', height=90, state='disabled'), lalu menyimpannya pada self.output.
        self.output.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20)  # Memanggil self.output.grid untuk menempatkan widget pada baris dan kolom.
        self.lbl_judul_hasil = ctk.CTkLabel(  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='Encryption Result' if self.mode == 'encrypt' else 'Decryption Result', font=fnt(13, 'bol, lalu menyimpannya pada self.lbl_judul_hasil.
            k,  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='Encryption Result' if self.mode == 'encrypt' else 'Decryption Result', font=fnt(13, 'bol, lalu menyimpannya pada self.lbl_judul_hasil.
            text="Encryption Result" if self.mode == "encrypt" else "Decryption Result",  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='Encryption Result' if self.mode == 'encrypt' else 'Decryption Result', font=fnt(13, 'bol, lalu menyimpannya pada self.lbl_judul_hasil.
            font=fnt(13, "bold"),  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='Encryption Result' if self.mode == 'encrypt' else 'Decryption Result', font=fnt(13, 'bol, lalu menyimpannya pada self.lbl_judul_hasil.
            text_color=INK,  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='Encryption Result' if self.mode == 'encrypt' else 'Decryption Result', font=fnt(13, 'bol, lalu menyimpannya pada self.lbl_judul_hasil.
            anchor="w",  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='Encryption Result' if self.mode == 'encrypt' else 'Decryption Result', font=fnt(13, 'bol, lalu menyimpannya pada self.lbl_judul_hasil.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.lbl_judul_hasil.grid(  # Memanggil self.lbl_judul_hasil.grid untuk menempatkan widget pada baris dan kolom.
            row=3, column=0, columnspan=2, sticky="w", padx=20, pady=(10, 0)  # Memanggil self.lbl_judul_hasil.grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.lbl_ringkas = ctk.CTkLabel(  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='File size: -\nTime taken: -\nStatus: menunggu proses', font=fnt(12), text_color=INK, anc, lalu menyimpannya pada self.lbl_ringkas.
            k,  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='File size: -\nTime taken: -\nStatus: menunggu proses', font=fnt(12), text_color=INK, anc, lalu menyimpannya pada self.lbl_ringkas.
            text="File size: -\nTime taken: -\nStatus: menunggu proses",  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='File size: -\nTime taken: -\nStatus: menunggu proses', font=fnt(12), text_color=INK, anc, lalu menyimpannya pada self.lbl_ringkas.
            font=fnt(12),  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='File size: -\nTime taken: -\nStatus: menunggu proses', font=fnt(12), text_color=INK, anc, lalu menyimpannya pada self.lbl_ringkas.
            text_color=INK,  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='File size: -\nTime taken: -\nStatus: menunggu proses', font=fnt(12), text_color=INK, anc, lalu menyimpannya pada self.lbl_ringkas.
            anchor="w",  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='File size: -\nTime taken: -\nStatus: menunggu proses', font=fnt(12), text_color=INK, anc, lalu menyimpannya pada self.lbl_ringkas.
            justify="left",  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='File size: -\nTime taken: -\nStatus: menunggu proses', font=fnt(12), text_color=INK, anc, lalu menyimpannya pada self.lbl_ringkas.
            wraplength=360,  # Menghitung atau menyiapkan ctk.CTkLabel(k, text='File size: -\nTime taken: -\nStatus: menunggu proses', font=fnt(12), text_color=INK, anc, lalu menyimpannya pada self.lbl_ringkas.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.lbl_ringkas.grid(row=4, column=0, columnspan=2, sticky="w", padx=20, pady=(2, 8))  # Memanggil self.lbl_ringkas.grid untuk menempatkan widget pada baris dan kolom.
        baris = ctk.CTkFrame(k, fg_color="transparent")  # Menghitung atau menyiapkan ctk.CTkFrame(k, fg_color='transparent'), lalu menyimpannya pada baris.
        baris.grid(row=5, column=0, columnspan=2, sticky="ew", padx=20, pady=(0, 16))  # Memanggil baris.grid untuk menempatkan widget pada baris dan kolom.
        self.btn_dl = tombol(  # Menghitung atau menyiapkan tombol(baris, 'Download Result', self._unduh_hasil, 'blue', width=150, state='disabled'), lalu menyimpannya pada self.btn_dl.
            baris, "Download Result", self._unduh_hasil, "blue", width=150, state="disabled"  # Menghitung atau menyiapkan tombol(baris, 'Download Result', self._unduh_hasil, 'blue', width=150, state='disabled'), lalu menyimpannya pada self.btn_dl.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.btn_dl.grid(row=0, column=0, padx=(0, 8))  # Memanggil self.btn_dl.grid untuk menempatkan widget pada baris dan kolom.
        self.btn_dlkey = tombol(  # Menghitung atau menyiapkan tombol(baris, 'Download Key', self._unduh_kunci, 'neutral', width=130, state='disabled'), lalu menyimpannya pada self.btn_dlkey.
            baris, "Download Key", self._unduh_kunci, "neutral", width=130, state="disabled"  # Menghitung atau menyiapkan tombol(baris, 'Download Key', self._unduh_kunci, 'neutral', width=130, state='disabled'), lalu menyimpannya pada self.btn_dlkey.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        if self.mode == "encrypt":  # Menjalankan blok hanya jika self.mode == "encrypt".
            self.btn_dlkey.grid(row=0, column=1)  # Memanggil self.btn_dlkey.grid untuk menempatkan widget pada baris dan kolom.

    def _bangun_aksi(self, induk):  # Mendefinisikan fungsi _bangun_aksi dengan parameter yang tertulis.
        baris = ctk.CTkFrame(induk, fg_color="transparent")  # Menghitung atau menyiapkan ctk.CTkFrame(induk, fg_color='transparent'), lalu menyimpannya pada baris.
        baris.grid(row=2, column=0, sticky="ew")  # Memanggil baris.grid untuk menempatkan widget pada baris dan kolom.
        baris.grid_columnconfigure(0, weight=1)  # Memanggil baris.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        self.btn_run = tombol(baris, self.teks_run, self._run, "primary", height=44)  # Menghitung atau menyiapkan tombol(baris, self.teks_run, self._run, 'primary', height=44), lalu menyimpannya pada self.btn_run.
        self.btn_run.grid(row=0, column=0, sticky="ew", padx=(0, 8))  # Memanggil self.btn_run.grid untuk menempatkan widget pada baris dan kolom.
        tombol(  # Memanggil tombol(baris, 'Reset Input', self._reset, 'neutral', height=44, width=120, border_width=1, border_color=BORDER untuk menjalankan operasi dengan argumen yang diberikan.
            baris,  # Memanggil tombol(baris, 'Reset Input', self._reset, 'neutral', height=44, width=120, border_width=1, border_color=BORDER untuk menjalankan operasi dengan argumen yang diberikan.
            "Reset Input",  # Memanggil tombol(baris, 'Reset Input', self._reset, 'neutral', height=44, width=120, border_width=1, border_color=BORDER untuk menjalankan operasi dengan argumen yang diberikan.
            self._reset,  # Memanggil tombol(baris, 'Reset Input', self._reset, 'neutral', height=44, width=120, border_width=1, border_color=BORDER untuk menjalankan operasi dengan argumen yang diberikan.
            "neutral",  # Memanggil tombol(baris, 'Reset Input', self._reset, 'neutral', height=44, width=120, border_width=1, border_color=BORDER untuk menjalankan operasi dengan argumen yang diberikan.
            height=44,  # Memanggil tombol(baris, 'Reset Input', self._reset, 'neutral', height=44, width=120, border_width=1, border_color=BORDER untuk menjalankan operasi dengan argumen yang diberikan.
            width=120,  # Memanggil tombol(baris, 'Reset Input', self._reset, 'neutral', height=44, width=120, border_width=1, border_color=BORDER untuk menjalankan operasi dengan argumen yang diberikan.
            border_width=1,  # Memanggil tombol(baris, 'Reset Input', self._reset, 'neutral', height=44, width=120, border_width=1, border_color=BORDER untuk menjalankan operasi dengan argumen yang diberikan.
            border_color=BORDER,  # Memanggil tombol(baris, 'Reset Input', self._reset, 'neutral', height=44, width=120, border_width=1, border_color=BORDER untuk menjalankan operasi dengan argumen yang diberikan.
        ).grid(row=0, column=1)  # Memanggil tombol(baris, 'Reset Input', self._reset, 'neutral', height=44, width=120, border_width=1, border_color=BORDER untuk menjalankan operasi dengan argumen yang diberikan.

    def kode(self):  # Mendefinisikan fungsi kode dengan parameter yang tertulis.
        return NAMA_ALGO[self.algo_var.get()]  # Mengembalikan NAMA_ALGO[self.algo_var.get()].

    def _ganti_algoritma(self):  # Mendefinisikan fungsi _ganti_algoritma dengan parameter yang tertulis.
        kode = self.kode()  # Menghitung atau menyiapkan self.kode(), lalu menyimpannya pada kode.
        enc = self.mode == "encrypt"  # Menghitung atau menyiapkan self.mode == 'encrypt', lalu menyimpannya pada enc.
        if kode == "5":  # Menjalankan blok hanya jika kode == "5".
            hint = (  # Menghitung atau menyiapkan 'Kunci dibangkitkan otomatis sepanjang pesan jika dikosongkan. Atau klik Generate / unggah kunci hex sendiri.', lalu menyimpannya pada hint.
                "Kunci dibangkitkan otomatis sepanjang pesan jika dikosongkan. Atau klik Generate / unggah kunci hex sendiri."  # Menghitung atau menyiapkan 'Kunci dibangkitkan otomatis sepanjang pesan jika dikosongkan. Atau klik Generate / unggah kunci hex sendiri.', lalu menyimpannya pada hint.
                if enc  # Menjalankan blok hanya jika en.
                else "Tempel kunci OTP (hex) atau unggah file .key.txt. Panjangnya harus sama dengan ciphertext."  # Menghitung atau menyiapkan 'Kunci dibangkitkan otomatis sepanjang pesan jika dikosongkan. Atau klik Generate / unggah kunci hex sendiri.', lalu menyimpannya pada hint.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
            label, contoh = PROMPT_KUNCI[kode]  # Menghitung atau menyiapkan PROMPT_KUNCI[kode], lalu menyimpannya pada (label, contoh).
            hint = f"{label}. Contoh: {contoh}"  # Menghitung atau menyiapkan f'{label}. Contoh: {contoh}', lalu menyimpannya pada hint.
        self.lbl_hint.configure(text=hint)  # Memanggil self.lbl_hint.configure untuk memperbarui konfigurasi widget.
        self.btn_gen.configure(state="normal" if enc else "disabled")  # Memanggil self.btn_gen.configure untuk memperbarui konfigurasi widget.

    def _teks_input(self):  # Mendefinisikan fungsi _teks_input dengan parameter yang tertulis.
        return self.input.get("1.0", "end-1c")  # Mengembalikan self.input.get("1.0", "end-1c").

    def _upload_input(self):  # Mendefinisikan fungsi _upload_input dengan parameter yang tertulis.
        p = filedialog.askopenfilename(  # Menghitung atau menyiapkan filedialog.askopenfilename(parent=self.app, title='Pilih file .txt', filetypes=[('Text file', '*.txt'), ('Semu, lalu menyimpannya pada p.
            parent=self.app,  # Menghitung atau menyiapkan filedialog.askopenfilename(parent=self.app, title='Pilih file .txt', filetypes=[('Text file', '*.txt'), ('Semu, lalu menyimpannya pada p.
            title="Pilih file .txt",  # Menghitung atau menyiapkan filedialog.askopenfilename(parent=self.app, title='Pilih file .txt', filetypes=[('Text file', '*.txt'), ('Semu, lalu menyimpannya pada p.
            filetypes=[("Text file", "*.txt"), ("Semua file", "*.*")],  # Menghitung atau menyiapkan filedialog.askopenfilename(parent=self.app, title='Pilih file .txt', filetypes=[('Text file', '*.txt'), ('Semu, lalu menyimpannya pada p.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        if not p:  # Menjalankan blok hanya jika not p.
            return  # Mengembalikan kendali ke pemanggil.
        try:  # Memulai operasi yang dapat menghasilkan exception.
            ukuran = os.path.getsize(p)  # Menghitung atau menyiapkan os.path.getsize(p), lalu menyimpannya pada ukuran.
            with open(p, "rb") as f:  # Mengelola sumber daya atau konteks open(p, "rb") as f.
                mentah = f.read(BATAS_PRATINJAU * 4)  # Menghitung atau menyiapkan f.read(BATAS_PRATINJAU * 4), lalu menyimpannya pada mentah.
        except OSError as e:  # Menangani exception OSError as e.
            self.app.toast.tampil(pesan_error(e), "error")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
            return  # Mengembalikan kendali ke pemanggil.
        pratinjau = mentah.decode("utf-8-sig", errors="replace")[:BATAS_PRATINJAU]  # Menghitung atau menyiapkan mentah.decode('utf-8-sig', errors='replace')[:BATAS_PRATINJAU], lalu menyimpannya pada pratinjau.
        if ukuran > len(mentah) or len(pratinjau) >= BATAS_PRATINJAU:  # Menjalankan blok hanya jika ukuran > len(mentah) or len(pratinjau) >= BATAS_PRATINJAU.
            pratinjau += "\n\n... (pratinjau dipotong; seluruh isi file tetap diproses)"  # Menghitung atau menyiapkan '\n\n... (pratinjau dipotong; seluruh isi file tetap diproses)', lalu menyimpannya pada pratinjau.
        self.file_path = p  # Menghitung atau menyiapkan p, lalu menyimpannya pada self.file_path.
        isi_readonly(self.input, pratinjau)  # Memanggil isi_readonly untuk menjalankan operasi dengan argumen yang diberikan.
        self.lbl_file.configure(  # Memanggil self.lbl_file.configure untuk memperbarui konfigurasi widget.
            text=f"{os.path.basename(p)}  ({fmt_ukuran(ukuran)}) - pratinjau, tidak bisa diedit",  # Memanggil self.lbl_file.configure untuk memperbarui konfigurasi widget.
            text_color=BLUE_INK,  # Memanggil self.lbl_file.configure untuk memperbarui konfigurasi widget.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.btn_hapus_file.grid()  # Memanggil self.btn_hapus_file.grid untuk menempatkan widget pada baris dan kolom.
        self.app.toast.tampil(f"File dimuat: {os.path.basename(p)}", "info")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.

    def _hapus_file(self):  # Mendefinisikan fungsi _hapus_file dengan parameter yang tertulis.
        self.file_path = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada self.file_path.
        self.input.configure(state="normal")  # Memanggil self.input.configure untuk memperbarui konfigurasi widget.
        self.input.delete("1.0", "end")  # Memanggil self.input.delete untuk menghapus isi pada rentang yang ditentukan.
        self.lbl_file.configure(  # Memanggil self.lbl_file.configure untuk memperbarui konfigurasi widget.
            text="Belum ada file - ketik teks di atas atau unggah file", text_color=MUTED  # Memanggil self.lbl_file.configure untuk memperbarui konfigurasi widget.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.btn_hapus_file.grid_remove()  # Memanggil self.btn_hapus_file.grid_remove untuk menjalankan operasi dengan argumen yang diberikan.

    def set_kunci(self, teks):  # Mendefinisikan fungsi set_kunci dengan parameter yang tertulis.
        self.keybox.configure(state="normal")  # Memanggil self.keybox.configure untuk memperbarui konfigurasi widget.
        self.keybox.delete("1.0", "end")  # Memanggil self.keybox.delete untuk menghapus isi pada rentang yang ditentukan.
        if len(teks) > BATAS_KUNCI:  # Menjalankan blok hanya jika len(teks) > BATAS_KUNCI.
            self.key_full = teks  # Menghitung atau menyiapkan teks, lalu menyimpannya pada self.key_full.
            self.keybox.insert(  # Memanggil self.keybox.insert untuk menyisipkan teks atau elemen.
                "1.0",  # Memanggil self.keybox.insert untuk menyisipkan teks atau elemen.
                teks[:200]  # Memanggil self.keybox.insert untuk menyisipkan teks atau elemen.
                + f"...\n[Kunci panjang: {len(teks):,} karakter - tersimpan penuh di memori]",  # Memanggil self.keybox.insert untuk menyisipkan teks atau elemen.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
            self.keybox.configure(state="disabled")  # Memanggil self.keybox.configure untuk memperbarui konfigurasi widget.
        else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
            self.key_full = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada self.key_full.
            self.keybox.insert("1.0", teks)  # Memanggil self.keybox.insert untuk menyisipkan teks atau elemen.

    def get_kunci(self):  # Mendefinisikan fungsi get_kunci dengan parameter yang tertulis.
        if self.key_full is not None:  # Menjalankan blok hanya jika self.key_full is not None.
            return self.key_full  # Mengembalikan self.key_full.
        return self.keybox.get("1.0", "end-1c").strip()  # Mengembalikan self.keybox.get("1.0", "end-1c").strip().

    def _hapus_kunci(self):  # Mendefinisikan fungsi _hapus_kunci dengan parameter yang tertulis.
        self.set_kunci("")  # Memanggil self.set_kunci untuk menjalankan operasi dengan argumen yang diberikan.

    def _generate_kunci(self):  # Mendefinisikan fungsi _generate_kunci dengan parameter yang tertulis.
        kode = self.kode()  # Menghitung atau menyiapkan self.kode(), lalu menyimpannya pada kode.
        n = 0  # Menghitung atau menyiapkan 0, lalu menyimpannya pada n.
        if kode == "5":  # Menjalankan blok hanya jika kode == "5".
            if self.file_path:  # Menjalankan blok hanya jika self.file_path.
                try:  # Memulai operasi yang dapat menghasilkan exception.
                    n = os.path.getsize(self.file_path)  # Menghitung atau menyiapkan os.path.getsize(self.file_path), lalu menyimpannya pada n.
                except OSError as e:  # Menangani exception OSError as e.
                    self.app.toast.tampil(pesan_error(e), "error")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
                    return  # Mengembalikan kendali ke pemanggil.
            else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
                n = len(self._teks_input().encode("utf-8"))  # Menghitung atau menyiapkan len(self._teks_input().encode('utf-8')), lalu menyimpannya pada n.
            if n == 0:  # Menjalankan blok hanya jika n == 0.
                self.app.toast.tampil(  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
                    "Isi teks atau unggah file dulu - panjang kunci OTP harus sama dengan panjang pesan.",  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
                    "info",  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
                )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
                return  # Mengembalikan kendali ke pemanggil.
        self.set_kunci(kunci_acak(kode, n))  # Memanggil self.set_kunci untuk menjalankan operasi dengan argumen yang diberikan.
        self.app.toast.tampil("Kunci acak dibuat.", "success")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.

    def _upload_kunci(self):  # Mendefinisikan fungsi _upload_kunci dengan parameter yang tertulis.
        p = filedialog.askopenfilename(  # Menghitung atau menyiapkan filedialog.askopenfilename(parent=self.app, title='Pilih file kunci', filetypes=[('Text file', '*.txt'), ('Sem, lalu menyimpannya pada p.
            parent=self.app,  # Menghitung atau menyiapkan filedialog.askopenfilename(parent=self.app, title='Pilih file kunci', filetypes=[('Text file', '*.txt'), ('Sem, lalu menyimpannya pada p.
            title="Pilih file kunci",  # Menghitung atau menyiapkan filedialog.askopenfilename(parent=self.app, title='Pilih file kunci', filetypes=[('Text file', '*.txt'), ('Sem, lalu menyimpannya pada p.
            filetypes=[("Text file", "*.txt"), ("Semua file", "*.*")],  # Menghitung atau menyiapkan filedialog.askopenfilename(parent=self.app, title='Pilih file kunci', filetypes=[('Text file', '*.txt'), ('Sem, lalu menyimpannya pada p.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        if not p:  # Menjalankan blok hanya jika not p.
            return  # Mengembalikan kendali ke pemanggil.
        try:  # Memulai operasi yang dapat menghasilkan exception.
            if self.kode() == "5":  # Menjalankan blok hanya jika self.kode() == "5".
                teks = baca_hex(p).hex()  # Menghitung atau menyiapkan baca_hex(p).hex(), lalu menyimpannya pada teks.
            else:  # Menjalankan alternatif ketika kondisi sebelumnya tidak terpenuhi.
                teks = " ".join(baca_teks(p).split())  # Menghitung atau menyiapkan ' '.join(baca_teks(p).split()), lalu menyimpannya pada teks.
        except Exception as e:  # Menangani exception Exception as e.
            self.app.toast.tampil(pesan_error(e), "error")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
            return  # Mengembalikan kendali ke pemanggil.
        if not teks:  # Menjalankan blok hanya jika not teks.
            self.app.toast.tampil("File kunci kosong.", "error")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
            return  # Mengembalikan kendali ke pemanggil.
        self.set_kunci(teks)  # Memanggil self.set_kunci untuk menjalankan operasi dengan argumen yang diberikan.
        self.app.toast.tampil(f"Kunci dimuat dari {os.path.basename(p)}", "info")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.

    def _run(self):  # Mendefinisikan fungsi _run dengan parameter yang tertulis.
        if self.running:  # Menjalankan blok hanya jika self.running.
            return  # Mengembalikan kendali ke pemanggil.
        kode = self.kode()  # Menghitung atau menyiapkan self.kode(), lalu menyimpannya pada kode.
        teks = None if self.file_path else self._teks_input()  # Menghitung atau menyiapkan None if self.file_path else self._teks_input(), lalu menyimpannya pada teks.
        if not self.file_path and (not teks):  # Menjalankan blok hanya jika not self.file_path and (not teks).
            self.app.toast.tampil(  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
                "Masukkan teks atau unggah file .txt terlebih dahulu.", "error"  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
            return  # Mengembalikan kendali ke pemanggil.
        kunci = self.get_kunci()  # Menghitung atau menyiapkan self.get_kunci(), lalu menyimpannya pada kunci.
        enc = self.mode == "encrypt"  # Menghitung atau menyiapkan self.mode == 'encrypt', lalu menyimpannya pada enc.
        if not kunci and (not (enc and kode == "5")):  # Menjalankan blok hanya jika not kunci and (not (enc and kode == "5")).
            self.app.toast.tampil(  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
                "Kunci masih kosong. Isi kunci, unggah file kunci, atau klik Generate Random Key.",  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
                "error",  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
            return  # Mengembalikan kendali ke pemanggil.
        self._bersihkan_hasil()  # Memanggil self._bersihkan_hasil untuk menjalankan operasi dengan argumen yang diberikan.
        self.running = True  # Menghitung atau menyiapkan True, lalu menyimpannya pada self.running.
        self.btn_run.configure(state="disabled", text="Processing...")  # Memanggil self.btn_run.configure untuk memperbarui konfigurasi widget.
        self.lbl_ringkas.configure(text="File size: -\nTime taken: -\nStatus: memproses...")  # Memanggil self.lbl_ringkas.configure untuk memperbarui konfigurasi widget.
        fn = jalankan_enkripsi if enc else jalankan_dekripsi  # Menghitung atau menyiapkan jalankan_enkripsi if enc else jalankan_dekripsi, lalu menyimpannya pada fn.
        self.app.jalankan_tugas(  # Memanggil self.app.jalankan_tugas untuk menjalankan operasi dengan argumen yang diberikan.
            lambda: fn(kode, teks, self.file_path, kunci), self._selesai, self._gagal  # Memanggil self.app.jalankan_tugas untuk menjalankan operasi dengan argumen yang diberikan.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

    def _selesai(self, h):  # Mendefinisikan fungsi _selesai dengan parameter yang tertulis.
        self.running = False  # Menghitung atau menyiapkan False, lalu menyimpannya pada self.running.
        self.btn_run.configure(state="normal", text=self.teks_run)  # Memanggil self.btn_run.configure untuk memperbarui konfigurasi widget.
        self.hasil = h  # Menghitung atau menyiapkan h, lalu menyimpannya pada self.hasil.
        teks = h["teks_hasil"]  # Menghitung atau menyiapkan h['teks_hasil'], lalu menyimpannya pada teks.
        if len(teks) > BATAS_TAMPIL:  # Menjalankan blok hanya jika len(teks) > BATAS_TAMPIL.
            teks = (  # Menghitung atau menyiapkan teks[:BATAS_TAMPIL] + f"\n\n... (ditampilkan {BATAS_TAMPIL:,} dari {len(h['teks_hasil']):,} karakter; gunakan , lalu menyimpannya pada teks.
                teks[:BATAS_TAMPIL]  # Menghitung atau menyiapkan teks[:BATAS_TAMPIL] + f"\n\n... (ditampilkan {BATAS_TAMPIL:,} dari {len(h['teks_hasil']):,} karakter; gunakan , lalu menyimpannya pada teks.
                + f"\n\n... (ditampilkan {BATAS_TAMPIL:,} dari {len(h['teks_hasil']):,} karakter; gunakan Download Result untuk hasil lengkap)"  # Menghitung atau menyiapkan teks[:BATAS_TAMPIL] + f"\n\n... (ditampilkan {BATAS_TAMPIL:,} dari {len(h['teks_hasil']):,} karakter; gunakan , lalu menyimpannya pada teks.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        isi_readonly(self.output, teks)  # Memanggil isi_readonly untuk menjalankan operasi dengan argumen yang diberikan.
        ms = h["waktu_ms"]  # Menghitung atau menyiapkan h['waktu_ms'], lalu menyimpannya pada ms.
        thr = h["ukuran_in"] / 1024 / (ms / 1000) if ms > 0 else None  # Menghitung atau menyiapkan h['ukuran_in'] / 1024 / (ms / 1000) if ms > 0 else None, lalu menyimpannya pada thr.
        self.m_proses.set(f"{ms:,.4f}", frak_log(ms, 0.01, 5000))  # Memanggil self.m_proses.set untuk memperbarui nilai.
        self.m_thr.set(f"{thr:,.1f}" if thr else "-", frak_log(thr, 10, 1000000.0))  # Memanggil self.m_thr.set untuk memperbarui nilai.
        self.m_ukuran.set(fmt_ukuran(h["ukuran_in"]), frak_log(h["ukuran_in"], 10, 100000000.0))  # Memanggil self.m_ukuran.set untuk memperbarui nilai.
        self.m_total.set(  # Memanggil self.m_total.set untuk memperbarui nilai.
            fmt_durasi(h["waktu_total_s"]), frak_log(h["waktu_total_s"], 0.001, 30)  # Memanggil self.m_total.set untuk memperbarui nilai.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.lbl_ringkas.configure(  # Memanggil self.lbl_ringkas.configure untuk memperbarui konfigurasi widget.
            text=f"Algorithm: {h['algoritma']}\nFile size: {fmt_ukuran(h['ukuran_in'])} (input) -> {fmt_ukuran(h['ukuran_out'])} (output)\nTime taken: {fmt_durasi(h['waktu_total_s'])}\nStatus: Success"  # Memanggil self.lbl_ringkas.configure untuk memperbarui konfigurasi widget.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.btn_copy.configure(state="normal")  # Memanggil self.btn_copy.configure untuk memperbarui konfigurasi widget.
        self.btn_dl.configure(state="normal")  # Memanggil self.btn_dl.configure untuk memperbarui konfigurasi widget.
        if h["kunci_simpan"]:  # Menjalankan blok hanya jika h["kunci_simpan"].
            self.btn_dlkey.configure(state="normal")  # Memanggil self.btn_dlkey.configure untuk memperbarui konfigurasi widget.
        aksi = "Enkripsi" if self.mode == "encrypt" else "Dekripsi"  # Menghitung atau menyiapkan 'Enkripsi' if self.mode == 'encrypt' else 'Dekripsi', lalu menyimpannya pada aksi.
        pesan = f"{aksi} selesai dalam {ms:.3f} ms."  # Menghitung atau menyiapkan f'{aksi} selesai dalam {ms:.3f} ms.', lalu menyimpannya pada pesan.
        if (  # Menjalankan blok hanya jika .
            self.mode == "encrypt"  # Menyusun bagian ekspresi self.mode == "encrypt".
            and h["algoritma"].startswith("One-Time")  # Menyusun bagian ekspresi and h["algoritma"].startswith("One-Time").
            and (not self.get_kunci())  # Menyusun bagian ekspresi and (not self.get_kunci()).
        ):  # Menyusun bagian ekspresi ):.
            pesan += " Kunci OTP dibangkitkan otomatis - simpan lewat Download Key!"  # Menghitung atau menyiapkan ' Kunci OTP dibangkitkan otomatis - simpan lewat Download Key!', lalu menyimpannya pada pesan.
        self.app.toast.tampil(pesan, "success")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.

    def _gagal(self, e):  # Mendefinisikan fungsi _gagal dengan parameter yang tertulis.
        self.running = False  # Menghitung atau menyiapkan False, lalu menyimpannya pada self.running.
        self.btn_run.configure(state="normal", text=self.teks_run)  # Memanggil self.btn_run.configure untuk memperbarui konfigurasi widget.
        msg = pesan_error(e)  # Menghitung atau menyiapkan pesan_error(e), lalu menyimpannya pada msg.
        self.lbl_ringkas.configure(text=f"File size: -\nTime taken: -\nStatus: Failed")  # Memanggil self.lbl_ringkas.configure untuk memperbarui konfigurasi widget.
        self.app.toast.tampil(msg, "error")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.

    def _bersihkan_hasil(self):  # Mendefinisikan fungsi _bersihkan_hasil dengan parameter yang tertulis.
        self.hasil = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada self.hasil.
        isi_readonly(self.output, "")  # Memanggil isi_readonly untuk menjalankan operasi dengan argumen yang diberikan.
        for m in (self.m_proses, self.m_thr, self.m_ukuran, self.m_total):  # Mengulangi proses untuk m in (self.m_proses, self.m_thr, self.m_ukuran, self.m_total).
            m.set("-", 0)  # Memanggil m.set untuk memperbarui nilai.
        for b in (self.btn_copy, self.btn_dl, self.btn_dlkey):  # Mengulangi proses untuk b in (self.btn_copy, self.btn_dl, self.btn_dlkey).
            b.configure(state="disabled")  # Memanggil b.configure untuk memperbarui konfigurasi widget.
        self.lbl_ringkas.configure(text="File size: -\nTime taken: -\nStatus: menunggu proses")  # Memanggil self.lbl_ringkas.configure untuk memperbarui konfigurasi widget.

    def _reset(self):  # Mendefinisikan fungsi _reset dengan parameter yang tertulis.
        if self.running:  # Menjalankan blok hanya jika self.running.
            return  # Mengembalikan kendali ke pemanggil.
        self._hapus_file()  # Memanggil self._hapus_file untuk menjalankan operasi dengan argumen yang diberikan.
        self.set_kunci("")  # Memanggil self.set_kunci untuk menjalankan operasi dengan argumen yang diberikan.
        self._bersihkan_hasil()  # Memanggil self._bersihkan_hasil untuk menjalankan operasi dengan argumen yang diberikan.

    def _salin(self):  # Mendefinisikan fungsi _salin dengan parameter yang tertulis.
        if not self.hasil:  # Menjalankan blok hanya jika not self.hasil.
            return  # Mengembalikan kendali ke pemanggil.
        self.app.clipboard_clear()  # Memanggil self.app.clipboard_clear untuk menjalankan operasi dengan argumen yang diberikan.
        self.app.clipboard_append(self.hasil["teks_hasil"])  # Memanggil self.app.clipboard_append untuk menjalankan operasi dengan argumen yang diberikan.
        self.app.toast.tampil("Hasil disalin ke clipboard.", "success", 2000)  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.

    def _simpan(self, judul, nama_awal, tulis):  # Mendefinisikan fungsi _simpan dengan parameter yang tertulis.
        path = filedialog.asksaveasfilename(  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama_awal, defaultextension='.txt', fil, lalu menyimpannya pada path.
            parent=self.app,  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama_awal, defaultextension='.txt', fil, lalu menyimpannya pada path.
            title=judul,  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama_awal, defaultextension='.txt', fil, lalu menyimpannya pada path.
            initialfile=nama_awal,  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama_awal, defaultextension='.txt', fil, lalu menyimpannya pada path.
            defaultextension=".txt",  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama_awal, defaultextension='.txt', fil, lalu menyimpannya pada path.
            filetypes=[("Text file", "*.txt"), ("Semua file", "*.*")],  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama_awal, defaultextension='.txt', fil, lalu menyimpannya pada path.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        if not path:  # Menjalankan blok hanya jika not path.
            return  # Mengembalikan kendali ke pemanggil.
        try:  # Memulai operasi yang dapat menghasilkan exception.
            tulis(path)  # Memanggil tulis untuk menjalankan operasi dengan argumen yang diberikan.
        except OSError as e:  # Menangani exception OSError as e.
            self.app.toast.tampil(f"Gagal menyimpan: {pesan_error(e)}", "error")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
            return  # Mengembalikan kendali ke pemanggil.
        self.app.toast.tampil(f"Tersimpan: {path}", "success")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.

    def _unduh_hasil(self):  # Mendefinisikan fungsi _unduh_hasil dengan parameter yang tertulis.
        if self.hasil:  # Menjalankan blok hanya jika self.hasil.
            h = self.hasil  # Menghitung atau menyiapkan self.hasil, lalu menyimpannya pada h.
            self._simpan(  # Memanggil self._simpan untuk menjalankan operasi dengan argumen yang diberikan.
                "Simpan hasil", h["nama_hasil"], lambda p: tulis_bytes(p, h["bytes_hasil"])  # Memanggil self._simpan untuk menjalankan operasi dengan argumen yang diberikan.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

    def _unduh_kunci(self):  # Mendefinisikan fungsi _unduh_kunci dengan parameter yang tertulis.
        if self.hasil and self.hasil["kunci_simpan"]:  # Menjalankan blok hanya jika self.hasil and self.hasil["kunci_simpan"].
            h = self.hasil  # Menghitung atau menyiapkan self.hasil, lalu menyimpannya pada h.
            self._simpan(  # Memanggil self._simpan untuk menjalankan operasi dengan argumen yang diberikan.
                "Simpan kunci",  # Memanggil self._simpan untuk menjalankan operasi dengan argumen yang diberikan.
                h["nama_kunci"],  # Memanggil self._simpan untuk menjalankan operasi dengan argumen yang diberikan.
                lambda p: tulis_teks(p, h["kunci_simpan"] + "\n"),  # Memanggil self._simpan untuk menjalankan operasi dengan argumen yang diberikan.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
