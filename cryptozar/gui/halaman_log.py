# CryptoZar — gui.halaman_log
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.gui.tema import BG  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BLUE  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BLUE_H  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import INK  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import MUTED  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import NEUTRAL  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import NEUTRAL_H  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
import customtkinter as ctk  # Memuat pustaka customtkinter as ctk.
from tkinter import filedialog  # Mengimpor komponen yang dibutuhkan dari tkinter.
from cryptozar.gui.tema import fnt  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.komponen import isi_readonly  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
from cryptozar.layanan_gui import jalankan_benchmark  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_gui.
from cryptozar.layanan_gui import jalankan_demo  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_gui.
from cryptozar.gui.komponen import kartu  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
from cryptozar.gui.komponen import kotak_teks  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
from cryptozar.gui.format_pesan import pesan_error  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.format_pesan.
from cryptozar.gui.komponen import tombol  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.komponen.
from cryptozar.file_io import tulis_teks  # Mengimpor komponen yang dibutuhkan dari cryptozar.file_io.


class HalamanLog(ctk.CTkFrame):  # Mendefinisikan kelas HalamanLog untuk mengelompokkan data dan perilaku.

    def __init__(self, master, app, judul, deskripsi, wrap):  # Mendefinisikan fungsi __init__ dengan parameter yang tertulis.
        super().__init__(master, fg_color=BG, corner_radius=0)  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
        self.app = app  # Menghitung atau menyiapkan app, lalu menyimpannya pada self.app.
        self.grid_columnconfigure(0, weight=1)  # Memanggil self.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        self.grid_rowconfigure(2, weight=1)  # Memanggil self.grid_rowconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        ctk.CTkLabel(self, text=judul, font=fnt(28, "bold"), text_color=INK, anchor="w").grid(  # Memanggil ctk.CTkLabel(self, text=judul, font=fnt(28, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
            row=0, column=0, sticky="w", padx=28, pady=(24, 10)  # Memanggil ctk.CTkLabel(self, text=judul, font=fnt(28, 'bold'), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        panel = kartu(self)  # Menghitung atau menyiapkan kartu(self), lalu menyimpannya pada panel.
        panel.grid(row=1, column=0, sticky="ew", padx=28, pady=(0, 14))  # Memanggil panel.grid untuk menempatkan widget pada baris dan kolom.
        panel.grid_columnconfigure(0, weight=1)  # Memanggil panel.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        ctk.CTkLabel(  # Memanggil ctk.CTkLabel(panel, text=deskripsi, font=fnt(13), text_color=MUTED, anchor='w', justify='left', wraplength=820 untuk menjalankan operasi dengan argumen yang diberikan.
            panel,  # Memanggil ctk.CTkLabel(panel, text=deskripsi, font=fnt(13), text_color=MUTED, anchor='w', justify='left', wraplength=820 untuk menjalankan operasi dengan argumen yang diberikan.
            text=deskripsi,  # Memanggil ctk.CTkLabel(panel, text=deskripsi, font=fnt(13), text_color=MUTED, anchor='w', justify='left', wraplength=820 untuk menjalankan operasi dengan argumen yang diberikan.
            font=fnt(13),  # Memanggil ctk.CTkLabel(panel, text=deskripsi, font=fnt(13), text_color=MUTED, anchor='w', justify='left', wraplength=820 untuk menjalankan operasi dengan argumen yang diberikan.
            text_color=MUTED,  # Memanggil ctk.CTkLabel(panel, text=deskripsi, font=fnt(13), text_color=MUTED, anchor='w', justify='left', wraplength=820 untuk menjalankan operasi dengan argumen yang diberikan.
            anchor="w",  # Memanggil ctk.CTkLabel(panel, text=deskripsi, font=fnt(13), text_color=MUTED, anchor='w', justify='left', wraplength=820 untuk menjalankan operasi dengan argumen yang diberikan.
            justify="left",  # Memanggil ctk.CTkLabel(panel, text=deskripsi, font=fnt(13), text_color=MUTED, anchor='w', justify='left', wraplength=820 untuk menjalankan operasi dengan argumen yang diberikan.
            wraplength=820,  # Memanggil ctk.CTkLabel(panel, text=deskripsi, font=fnt(13), text_color=MUTED, anchor='w', justify='left', wraplength=820 untuk menjalankan operasi dengan argumen yang diberikan.
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(16, 10))  # Memanggil ctk.CTkLabel(panel, text=deskripsi, font=fnt(13), text_color=MUTED, anchor='w', justify='left', wraplength=820 untuk menjalankan operasi dengan argumen yang diberikan.
        self.kontrol = ctk.CTkFrame(panel, fg_color="transparent")  # Menghitung atau menyiapkan ctk.CTkFrame(panel, fg_color='transparent'), lalu menyimpannya pada self.kontrol.
        self.kontrol.grid(row=1, column=0, sticky="w", padx=20, pady=(0, 10))  # Memanggil self.kontrol.grid untuk menempatkan widget pada baris dan kolom.
        self.progress = ctk.CTkProgressBar(  # Menghitung atau menyiapkan ctk.CTkProgressBar(panel, height=6, corner_radius=3, fg_color='#E4DDCB', progress_color='#8FA2E6', mode='indet, lalu menyimpannya pada self.progress.
            panel,  # Menghitung atau menyiapkan ctk.CTkProgressBar(panel, height=6, corner_radius=3, fg_color='#E4DDCB', progress_color='#8FA2E6', mode='indet, lalu menyimpannya pada self.progress.
            height=6,  # Menghitung atau menyiapkan ctk.CTkProgressBar(panel, height=6, corner_radius=3, fg_color='#E4DDCB', progress_color='#8FA2E6', mode='indet, lalu menyimpannya pada self.progress.
            corner_radius=3,  # Menghitung atau menyiapkan ctk.CTkProgressBar(panel, height=6, corner_radius=3, fg_color='#E4DDCB', progress_color='#8FA2E6', mode='indet, lalu menyimpannya pada self.progress.
            fg_color="#E4DDCB",  # Menghitung atau menyiapkan ctk.CTkProgressBar(panel, height=6, corner_radius=3, fg_color='#E4DDCB', progress_color='#8FA2E6', mode='indet, lalu menyimpannya pada self.progress.
            progress_color="#8FA2E6",  # Menghitung atau menyiapkan ctk.CTkProgressBar(panel, height=6, corner_radius=3, fg_color='#E4DDCB', progress_color='#8FA2E6', mode='indet, lalu menyimpannya pada self.progress.
            mode="indeterminate",  # Menghitung atau menyiapkan ctk.CTkProgressBar(panel, height=6, corner_radius=3, fg_color='#E4DDCB', progress_color='#8FA2E6', mode='indet, lalu menyimpannya pada self.progress.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.progress.set(0)  # Memanggil self.progress.set untuk memperbarui nilai.
        self.progress.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 16))  # Memanggil self.progress.grid untuk menempatkan widget pada baris dan kolom.
        hasil = kartu(self)  # Menghitung atau menyiapkan kartu(self), lalu menyimpannya pada hasil.
        hasil.grid(row=2, column=0, sticky="nsew", padx=28, pady=(0, 22))  # Memanggil hasil.grid untuk menempatkan widget pada baris dan kolom.
        hasil.grid_columnconfigure(0, weight=1)  # Memanggil hasil.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        hasil.grid_rowconfigure(0, weight=1)  # Memanggil hasil.grid_rowconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        self.output = kotak_teks(hasil, mono=True, wrap=wrap, state="disabled")  # Menghitung atau menyiapkan kotak_teks(hasil, mono=True, wrap=wrap, state='disabled'), lalu menyimpannya pada self.output.
        self.output.grid(row=0, column=0, sticky="nsew", padx=14, pady=14)  # Memanggil self.output.grid untuk menempatkan widget pada baris dan kolom.

    def tombol_run(self, teks, perintah):  # Mendefinisikan fungsi tombol_run dengan parameter yang tertulis.
        self.btn_run = tombol(self.kontrol, teks, perintah, "primary", width=170)  # Menghitung atau menyiapkan tombol(self.kontrol, teks, perintah, 'primary', width=170), lalu menyimpannya pada self.btn_run.
        self.btn_run.grid(row=0, column=0, padx=(0, 8))  # Memanggil self.btn_run.grid untuk menempatkan widget pada baris dan kolom.
        self._teks_run = teks  # Menghitung atau menyiapkan teks, lalu menyimpannya pada self._teks_run.

    def tambah(self, teks):  # Mendefinisikan fungsi tambah dengan parameter yang tertulis.
        self.output.configure(state="normal")  # Memanggil self.output.configure untuk memperbarui konfigurasi widget.
        self.output.insert("end", teks)  # Memanggil self.output.insert untuk menyisipkan teks atau elemen.
        self.output.see("end")  # Memanggil self.output.see untuk menjalankan operasi dengan argumen yang diberikan.
        self.output.configure(state="disabled")  # Memanggil self.output.configure untuk memperbarui konfigurasi widget.

    def mulai(self, fn, on_selesai):  # Mendefinisikan fungsi mulai dengan parameter yang tertulis.
        if self.app.busy:  # Menjalankan blok hanya jika self.app.busy.
            self.app.toast.tampil("Masih ada proses Demo/Benchmark yang berjalan.", "info")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
            return  # Mengembalikan kendali ke pemanggil.
        self.app.busy = True  # Menghitung atau menyiapkan True, lalu menyimpannya pada self.app.busy.
        isi_readonly(self.output, "")  # Memanggil isi_readonly untuk menjalankan operasi dengan argumen yang diberikan.
        self.btn_run.configure(state="disabled", text="Running...")  # Memanggil self.btn_run.configure untuk memperbarui konfigurasi widget.
        self.progress.start()  # Memanggil self.progress.start untuk menjalankan operasi dengan argumen yang diberikan.

        def selesai(hasil):  # Mendefinisikan fungsi selesai dengan parameter yang tertulis.
            self._akhir()  # Memanggil self._akhir untuk menjalankan operasi dengan argumen yang diberikan.
            on_selesai(hasil)  # Memanggil on_selesai untuk menjalankan operasi dengan argumen yang diberikan.

        def gagal(e):  # Mendefinisikan fungsi gagal dengan parameter yang tertulis.
            self._akhir()  # Memanggil self._akhir untuk menjalankan operasi dengan argumen yang diberikan.
            self.tambah(f"\n[ERROR] {pesan_error(e)}\n")  # Memanggil self.tambah untuk menjalankan operasi dengan argumen yang diberikan.
            self.app.toast.tampil(pesan_error(e), "error")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.

        self.app.jalankan_tugas(fn, selesai, gagal, on_log=self.tambah)  # Memanggil self.app.jalankan_tugas untuk menjalankan operasi dengan argumen yang diberikan.

    def _akhir(self):  # Mendefinisikan fungsi _akhir dengan parameter yang tertulis.
        self.app.busy = False  # Menghitung atau menyiapkan False, lalu menyimpannya pada self.app.busy.
        self.progress.stop()  # Memanggil self.progress.stop untuk menjalankan operasi dengan argumen yang diberikan.
        self.progress.set(0)  # Memanggil self.progress.set untuk memperbarui nilai.
        self.btn_run.configure(state="normal", text=self._teks_run)  # Memanggil self.btn_run.configure untuk memperbarui konfigurasi widget.

    def salin(self):  # Mendefinisikan fungsi salin dengan parameter yang tertulis.
        self.app.clipboard_clear()  # Memanggil self.app.clipboard_clear untuk menjalankan operasi dengan argumen yang diberikan.
        self.app.clipboard_append(self.output.get("1.0", "end-1c"))  # Memanggil self.app.clipboard_append untuk menjalankan operasi dengan argumen yang diberikan.
        self.app.toast.tampil("Output disalin ke clipboard.", "success", 2000)  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.

    def simpan(self, judul, nama, ekstensi, isi):  # Mendefinisikan fungsi simpan dengan parameter yang tertulis.
        if not isi:  # Menjalankan blok hanya jika not isi.
            self.app.toast.tampil("Belum ada data untuk disimpan. Jalankan dulu.", "info")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
            return  # Mengembalikan kendali ke pemanggil.
        path = filedialog.asksaveasfilename(  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama, defaultextension=ekstensi, filety, lalu menyimpannya pada path.
            parent=self.app,  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama, defaultextension=ekstensi, filety, lalu menyimpannya pada path.
            title=judul,  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama, defaultextension=ekstensi, filety, lalu menyimpannya pada path.
            initialfile=nama,  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama, defaultextension=ekstensi, filety, lalu menyimpannya pada path.
            defaultextension=ekstensi,  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama, defaultextension=ekstensi, filety, lalu menyimpannya pada path.
            filetypes=[(f"File {ekstensi}", f"*{ekstensi}"), ("Semua file", "*.*")],  # Menghitung atau menyiapkan filedialog.asksaveasfilename(parent=self.app, title=judul, initialfile=nama, defaultextension=ekstensi, filety, lalu menyimpannya pada path.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        if not path:  # Menjalankan blok hanya jika not path.
            return  # Mengembalikan kendali ke pemanggil.
        try:  # Memulai operasi yang dapat menghasilkan exception.
            tulis_teks(path, isi)  # Memanggil tulis_teks untuk menjalankan operasi dengan argumen yang diberikan.
        except OSError as e:  # Menangani exception OSError as e.
            self.app.toast.tampil(f"Gagal menyimpan: {pesan_error(e)}", "error")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
            return  # Mengembalikan kendali ke pemanggil.
        self.app.toast.tampil(f"Tersimpan: {path}", "success")  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.


class HalamanDemo(HalamanLog):  # Mendefinisikan kelas HalamanDemo untuk mengelompokkan data dan perilaku.

    def __init__(self, master, app):  # Mendefinisikan fungsi __init__ dengan parameter yang tertulis.
        super().__init__(  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
            master,  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
            app,  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
            "Demo",  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
            'Menjalankan demo_belajar_kriptografi(): pesan "BELAJAR KRIPTOGRAFI" dienkripsi lalu didekripsi dengan keenam algoritma, lengkap dengan kunci, ciphertext, dan waktu.',  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
            wrap="word",  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.tombol_run("Run Demo", self._run)  # Memanggil self.tombol_run untuk menjalankan operasi dengan argumen yang diberikan.
        tombol(self.kontrol, "Copy Output", self.salin, "neutral", width=120).grid(  # Memanggil tombol(self.kontrol, 'Copy Output', self.salin, 'neutral', width=120).grid untuk menempatkan widget pada baris dan kolom.
            row=0, column=1, padx=(0, 8)  # Memanggil tombol(self.kontrol, 'Copy Output', self.salin, 'neutral', width=120).grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        tombol(self.kontrol, "Save Log", self._simpan_log, "blue", width=110).grid(  # Memanggil tombol(self.kontrol, 'Save Log', self._simpan_log, 'blue', width=110).grid untuk menempatkan widget pada baris dan kolom.
            row=0, column=2  # Memanggil tombol(self.kontrol, 'Save Log', self._simpan_log, 'blue', width=110).grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

    def _run(self):  # Mendefinisikan fungsi _run dengan parameter yang tertulis.
        self.mulai(jalankan_demo, lambda _h: self.app.toast.tampil("Demo selesai.", "success"))  # Memanggil self.mulai untuk menjalankan operasi dengan argumen yang diberikan.

    def _simpan_log(self):  # Mendefinisikan fungsi _simpan_log dengan parameter yang tertulis.
        self.simpan(  # Memanggil self.simpan untuk menjalankan operasi dengan argumen yang diberikan.
            "Simpan log demo", "demo_cryptozar.txt", ".txt", self.output.get("1.0", "end-1c")  # Memanggil self.simpan untuk menjalankan operasi dengan argumen yang diberikan.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.


class HalamanBenchmark(HalamanLog):  # Mendefinisikan kelas HalamanBenchmark untuk mengelompokkan data dan perilaku.

    def __init__(self, master, app):  # Mendefinisikan fungsi __init__ dengan parameter yang tertulis.
        super().__init__(  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
            master,  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
            app,  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
            "Benchmark",  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
            "Menjalankan ukur_beban_komputasi(): waktu, memori puncak, dan ukuran kunci/ciphertext semua algoritma pada beberapa ukuran data (median dari beberapa kali ulang). Ukuran 1 MiB bisa memakan waktu cukup lama pada cipher klasik.",  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
            wrap="none",  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.csv_text = ""  # Menghitung atau menyiapkan '', lalu menyimpannya pada self.csv_text.
        self.tombol_run("Run Benchmark", self._run)  # Memanggil self.tombol_run untuk menjalankan operasi dengan argumen yang diberikan.
        self.sw = ctk.CTkSwitch(  # Menghitung atau menyiapkan ctk.CTkSwitch(self.kontrol, text='Sertakan 1 MiB', font=fnt(13), text_color=INK, progress_color='#8FA2E6'), lalu menyimpannya pada self.sw.
            self.kontrol,  # Menghitung atau menyiapkan ctk.CTkSwitch(self.kontrol, text='Sertakan 1 MiB', font=fnt(13), text_color=INK, progress_color='#8FA2E6'), lalu menyimpannya pada self.sw.
            text="Sertakan 1 MiB",  # Menghitung atau menyiapkan ctk.CTkSwitch(self.kontrol, text='Sertakan 1 MiB', font=fnt(13), text_color=INK, progress_color='#8FA2E6'), lalu menyimpannya pada self.sw.
            font=fnt(13),  # Menghitung atau menyiapkan ctk.CTkSwitch(self.kontrol, text='Sertakan 1 MiB', font=fnt(13), text_color=INK, progress_color='#8FA2E6'), lalu menyimpannya pada self.sw.
            text_color=INK,  # Menghitung atau menyiapkan ctk.CTkSwitch(self.kontrol, text='Sertakan 1 MiB', font=fnt(13), text_color=INK, progress_color='#8FA2E6'), lalu menyimpannya pada self.sw.
            progress_color="#8FA2E6",  # Menghitung atau menyiapkan ctk.CTkSwitch(self.kontrol, text='Sertakan 1 MiB', font=fnt(13), text_color=INK, progress_color='#8FA2E6'), lalu menyimpannya pada self.sw.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.sw.grid(row=0, column=1, padx=(14, 14))  # Memanggil self.sw.grid untuk menempatkan widget pada baris dan kolom.
        ctk.CTkLabel(self.kontrol, text="Ulang:", font=fnt(13), text_color=INK).grid(  # Memanggil ctk.CTkLabel(self.kontrol, text='Ulang:', font=fnt(13), text_color=INK).grid untuk menempatkan widget pada baris dan kolom.
            row=0, column=2, padx=(0, 6)  # Memanggil ctk.CTkLabel(self.kontrol, text='Ulang:', font=fnt(13), text_color=INK).grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.seg = ctk.CTkSegmentedButton(  # Menghitung atau menyiapkan ctk.CTkSegmentedButton(self.kontrol, values=['3', '5', '10'], font=fnt(13), fg_color=NEUTRAL, selected_color=B, lalu menyimpannya pada self.seg.
            self.kontrol,  # Menghitung atau menyiapkan ctk.CTkSegmentedButton(self.kontrol, values=['3', '5', '10'], font=fnt(13), fg_color=NEUTRAL, selected_color=B, lalu menyimpannya pada self.seg.
            values=["3", "5", "10"],  # Menghitung atau menyiapkan ctk.CTkSegmentedButton(self.kontrol, values=['3', '5', '10'], font=fnt(13), fg_color=NEUTRAL, selected_color=B, lalu menyimpannya pada self.seg.
            font=fnt(13),  # Menghitung atau menyiapkan ctk.CTkSegmentedButton(self.kontrol, values=['3', '5', '10'], font=fnt(13), fg_color=NEUTRAL, selected_color=B, lalu menyimpannya pada self.seg.
            fg_color=NEUTRAL,  # Menghitung atau menyiapkan ctk.CTkSegmentedButton(self.kontrol, values=['3', '5', '10'], font=fnt(13), fg_color=NEUTRAL, selected_color=B, lalu menyimpannya pada self.seg.
            selected_color=BLUE,  # Menghitung atau menyiapkan ctk.CTkSegmentedButton(self.kontrol, values=['3', '5', '10'], font=fnt(13), fg_color=NEUTRAL, selected_color=B, lalu menyimpannya pada self.seg.
            selected_hover_color=BLUE_H,  # Menghitung atau menyiapkan ctk.CTkSegmentedButton(self.kontrol, values=['3', '5', '10'], font=fnt(13), fg_color=NEUTRAL, selected_color=B, lalu menyimpannya pada self.seg.
            unselected_color=NEUTRAL,  # Menghitung atau menyiapkan ctk.CTkSegmentedButton(self.kontrol, values=['3', '5', '10'], font=fnt(13), fg_color=NEUTRAL, selected_color=B, lalu menyimpannya pada self.seg.
            unselected_hover_color=NEUTRAL_H,  # Menghitung atau menyiapkan ctk.CTkSegmentedButton(self.kontrol, values=['3', '5', '10'], font=fnt(13), fg_color=NEUTRAL, selected_color=B, lalu menyimpannya pada self.seg.
            text_color=INK,  # Menghitung atau menyiapkan ctk.CTkSegmentedButton(self.kontrol, values=['3', '5', '10'], font=fnt(13), fg_color=NEUTRAL, selected_color=B, lalu menyimpannya pada self.seg.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.seg.set("5")  # Memanggil self.seg.set untuk memperbarui nilai.
        self.seg.grid(row=0, column=3, padx=(0, 14))  # Memanggil self.seg.grid untuk menempatkan widget pada baris dan kolom.
        tombol(self.kontrol, "Copy Output", self.salin, "neutral", width=110).grid(  # Memanggil tombol(self.kontrol, 'Copy Output', self.salin, 'neutral', width=110).grid untuk menempatkan widget pada baris dan kolom.
            row=0, column=4, padx=(0, 8)  # Memanggil tombol(self.kontrol, 'Copy Output', self.salin, 'neutral', width=110).grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        tombol(self.kontrol, "Save CSV", self._simpan_csv, "blue", width=100).grid(  # Memanggil tombol(self.kontrol, 'Save CSV', self._simpan_csv, 'blue', width=100).grid untuk menempatkan widget pada baris dan kolom.
            row=0, column=5  # Memanggil tombol(self.kontrol, 'Save CSV', self._simpan_csv, 'blue', width=100).grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

    def _run(self):  # Mendefinisikan fungsi _run dengan parameter yang tertulis.
        besar = bool(self.sw.get())  # Menghitung atau menyiapkan bool(self.sw.get()), lalu menyimpannya pada besar.
        ulang = int(self.seg.get())  # Menghitung atau menyiapkan int(self.seg.get()), lalu menyimpannya pada ulang.
        self.csv_text = ""  # Menghitung atau menyiapkan '', lalu menyimpannya pada self.csv_text.

        def selesai(csv_text):  # Mendefinisikan fungsi selesai dengan parameter yang tertulis.
            self.csv_text = csv_text  # Menghitung atau menyiapkan csv_text, lalu menyimpannya pada self.csv_text.
            self.app.toast.tampil(  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
                "Benchmark selesai. Klik Save CSV untuk menyimpan tabel.", "success"  # Memanggil self.app.toast.tampil untuk menjalankan operasi dengan argumen yang diberikan.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

        self.mulai(lambda: jalankan_benchmark(besar, ulang), selesai)  # Memanggil self.mulai untuk menjalankan operasi dengan argumen yang diberikan.

    def _simpan_csv(self):  # Mendefinisikan fungsi _simpan_csv dengan parameter yang tertulis.
        self.simpan(  # Memanggil self.simpan untuk menjalankan operasi dengan argumen yang diberikan.
            "Simpan tabel benchmark", "hasil_beban_komputasi.csv", ".csv", self.csv_text  # Memanggil self.simpan untuk menjalankan operasi dengan argumen yang diberikan.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
