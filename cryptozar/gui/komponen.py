# CryptoZar — gui.komponen
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from cryptozar.gui.tema import BLUE  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BLUE_H  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BLUE_INK  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import BORDER  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import CARD  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import FIELD  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import INK  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import MINT  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import MINT_H  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import MINT_INK  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import MUTED  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import NEUTRAL  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import NEUTRAL_H  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import PRIMARY  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import PRIMARY_H  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
from cryptozar.gui.tema import TOAST  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
import base64  # Memuat pustaka base64.
import customtkinter as ctk  # Memuat pustaka customtkinter as ctk.
from cryptozar.gui.tema import fnt  # Mengimpor komponen yang dibutuhkan dari cryptozar.gui.tema.
import io  # Memuat pustaka io.


def muat_b64(data):  # Mendefinisikan fungsi muat_b64 dengan parameter yang tertulis.
    from PIL import Image  # Mengimpor komponen yang dibutuhkan dari PIL.

    return Image.open(io.BytesIO(base64.b64decode(data))).convert("RGBA")  # Mengembalikan Image.open(io.BytesIO(base64.b64decode(data))).convert("RGBA").


def pil_ke_ctk(img, lebar):  # Mendefinisikan fungsi pil_ke_ctk dengan parameter yang tertulis.
    tinggi = round(img.height * lebar / img.width)  # Menghitung atau menyiapkan round(img.height * lebar / img.width), lalu menyimpannya pada tinggi.
    return ctk.CTkImage(light_image=img, dark_image=img, size=(lebar, tinggi))  # Mengembalikan ctk.CTkImage(light_image=img, dark_image=img, size=(lebar, tinggi)).


def kartu(master, **kw):  # Mendefinisikan fungsi kartu dengan parameter yang tertulis.
    return ctk.CTkFrame(  # Mengembalikan ctk.CTkFrame(.
        master, fg_color=CARD, corner_radius=16, border_width=1, border_color=BORDER, **kw  # Menyusun bagian ekspresi master, fg_color=CARD, corner_radius=16, border_width=1, border_color=BORDER, **kw.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.


def tombol(master, teks, perintah, gaya="neutral", **kw):  # Mendefinisikan fungsi tombol dengan parameter yang tertulis.
    warna = {  # Menghitung atau menyiapkan {'neutral': (NEUTRAL, NEUTRAL_H, INK), 'blue': (BLUE, BLUE_H, BLUE_INK), 'mint': (MINT, MINT_H, MINT_INK), 'pr, lalu menyimpannya pada warna.
        "neutral": (NEUTRAL, NEUTRAL_H, INK),  # Menghitung atau menyiapkan {'neutral': (NEUTRAL, NEUTRAL_H, INK), 'blue': (BLUE, BLUE_H, BLUE_INK), 'mint': (MINT, MINT_H, MINT_INK), 'pr, lalu menyimpannya pada warna.
        "blue": (BLUE, BLUE_H, BLUE_INK),  # Menghitung atau menyiapkan {'neutral': (NEUTRAL, NEUTRAL_H, INK), 'blue': (BLUE, BLUE_H, BLUE_INK), 'mint': (MINT, MINT_H, MINT_INK), 'pr, lalu menyimpannya pada warna.
        "mint": (MINT, MINT_H, MINT_INK),  # Menghitung atau menyiapkan {'neutral': (NEUTRAL, NEUTRAL_H, INK), 'blue': (BLUE, BLUE_H, BLUE_INK), 'mint': (MINT, MINT_H, MINT_INK), 'pr, lalu menyimpannya pada warna.
        "primary": (PRIMARY, PRIMARY_H, "#FFFFFF"),  # Menghitung atau menyiapkan {'neutral': (NEUTRAL, NEUTRAL_H, INK), 'blue': (BLUE, BLUE_H, BLUE_INK), 'mint': (MINT, MINT_H, MINT_INK), 'pr, lalu menyimpannya pada warna.
        "ghost": ("transparent", NEUTRAL, MUTED),  # Menghitung atau menyiapkan {'neutral': (NEUTRAL, NEUTRAL_H, INK), 'blue': (BLUE, BLUE_H, BLUE_INK), 'mint': (MINT, MINT_H, MINT_INK), 'pr, lalu menyimpannya pada warna.
    }[gaya]  # Menghitung atau menyiapkan {'neutral': (NEUTRAL, NEUTRAL_H, INK), 'blue': (BLUE, BLUE_H, BLUE_INK), 'mint': (MINT, MINT_H, MINT_INK), 'pr, lalu menyimpannya pada warna.
    kw.setdefault("height", 38)  # Memanggil kw.setdefault untuk menjalankan operasi dengan argumen yang diberikan.
    kw.setdefault("corner_radius", 10)  # Memanggil kw.setdefault untuk menjalankan operasi dengan argumen yang diberikan.
    kw.setdefault("font", fnt(13, "bold" if gaya == "primary" else "normal"))  # Memanggil kw.setdefault untuk menjalankan operasi dengan argumen yang diberikan.
    return ctk.CTkButton(  # Mengembalikan ctk.CTkButton(.
        master,  # Menyusun bagian ekspresi master,.
        text=teks,  # Menyusun bagian ekspresi text=teks,.
        command=perintah,  # Menyusun bagian ekspresi command=perintah,.
        fg_color=warna[0],  # Menyusun bagian ekspresi fg_color=warna[0],.
        hover_color=warna[1],  # Menyusun bagian ekspresi hover_color=warna[1],.
        text_color=warna[2],  # Menyusun bagian ekspresi text_color=warna[2],.
        text_color_disabled="#B9B3A5",  # Menyusun bagian ekspresi text_color_disabled="#B9B3A5",.
        **kw  # Menyusun bagian ekspresi **kw.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.


def kotak_teks(master, mono=False, wrap="word", **kw):  # Mendefinisikan fungsi kotak_teks dengan parameter yang tertulis.
    return ctk.CTkTextbox(  # Mengembalikan ctk.CTkTextbox(.
        master,  # Menyusun bagian ekspresi master,.
        fg_color=FIELD,  # Menyusun bagian ekspresi fg_color=FIELD,.
        border_width=1,  # Menyusun bagian ekspresi border_width=1,.
        border_color=BORDER,  # Menyusun bagian ekspresi border_color=BORDER,.
        text_color=INK,  # Menyusun bagian ekspresi text_color=INK,.
        corner_radius=12,  # Menyusun bagian ekspresi corner_radius=12,.
        wrap=wrap,  # Menyusun bagian ekspresi wrap=wrap,.
        font=fnt(12 if mono else 13, mono=mono),  # Menyusun bagian ekspresi font=fnt(12 if mono else 13, mono=mono),.
        **kw  # Menyusun bagian ekspresi **kw.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.


def isi_readonly(tb, teks):  # Mendefinisikan fungsi isi_readonly dengan parameter yang tertulis.
    tb.configure(state="normal")  # Memanggil tb.configure untuk memperbarui konfigurasi widget.
    tb.delete("1.0", "end")  # Memanggil tb.delete untuk menghapus isi pada rentang yang ditentukan.
    tb.insert("1.0", teks)  # Memanggil tb.insert untuk menyisipkan teks atau elemen.
    tb.configure(state="disabled")  # Memanggil tb.configure untuk memperbarui konfigurasi widget.


class Toast:  # Mendefinisikan kelas Toast untuk mengelompokkan data dan perilaku.
    """Notifikasi singkat di kanan-bawah jendela (klik untuk menutup)."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.

    def __init__(self, root):  # Mendefinisikan fungsi __init__ dengan parameter yang tertulis.
        self.root = root  # Menghitung atau menyiapkan root, lalu menyimpannya pada self.root.
        self.frame = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada self.frame.
        self._job = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada self._job.

    def tutup(self):  # Mendefinisikan fungsi tutup dengan parameter yang tertulis.
        if self._job:  # Menjalankan blok hanya jika self._job.
            try:  # Memulai operasi yang dapat menghasilkan exception.
                self.root.after_cancel(self._job)  # Memanggil self.root.after_cancel untuk menjalankan operasi dengan argumen yang diberikan.
            except Exception:  # Menangani exception Exception.
                pass  # Membiarkan blok kosong tanpa operasi tambahan.
            self._job = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada self._job.
        if self.frame is not None:  # Menjalankan blok hanya jika self.frame is not None.
            self.frame.destroy()  # Memanggil self.frame.destroy untuk menjalankan operasi dengan argumen yang diberikan.
            self.frame = None  # Menghitung atau menyiapkan None, lalu menyimpannya pada self.frame.

    def tampil(self, pesan, jenis="info", ms=None):  # Mendefinisikan fungsi tampil dengan parameter yang tertulis.
        self.tutup()  # Memanggil self.tutup untuk menjalankan operasi dengan argumen yang diberikan.
        bg, garis, teks = TOAST[jenis]  # Menghitung atau menyiapkan TOAST[jenis], lalu menyimpannya pada (bg, garis, teks).
        judul = {"success": "Berhasil", "error": "Gagal", "info": "Info"}[jenis]  # Menghitung atau menyiapkan {'success': 'Berhasil', 'error': 'Gagal', 'info': 'Info'}[jenis], lalu menyimpannya pada judul.
        f = ctk.CTkFrame(  # Menghitung atau menyiapkan ctk.CTkFrame(self.root, fg_color=bg, corner_radius=14, border_width=1, border_color=garis), lalu menyimpannya pada f.
            self.root, fg_color=bg, corner_radius=14, border_width=1, border_color=garis  # Menghitung atau menyiapkan ctk.CTkFrame(self.root, fg_color=bg, corner_radius=14, border_width=1, border_color=garis), lalu menyimpannya pada f.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        ctk.CTkLabel(f, text=judul, font=fnt(13, "bold"), text_color=teks, anchor="w").pack(  # Memanggil ctk.CTkLabel(f, text=judul, font=fnt(13, 'bold'), text_color=teks, anchor='w').pack untuk menempatkan widget dengan tata letak pack.
            fill="x", padx=18, pady=(12, 0)  # Memanggil ctk.CTkLabel(f, text=judul, font=fnt(13, 'bold'), text_color=teks, anchor='w').pack untuk menempatkan widget dengan tata letak pack.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        ctk.CTkLabel(  # Memanggil ctk.CTkLabel(f, text=pesan, font=fnt(12), text_color=teks, anchor='w', justify='left', wraplength=360).pack untuk menempatkan widget dengan tata letak pack.
            f,  # Memanggil ctk.CTkLabel(f, text=pesan, font=fnt(12), text_color=teks, anchor='w', justify='left', wraplength=360).pack untuk menempatkan widget dengan tata letak pack.
            text=pesan,  # Memanggil ctk.CTkLabel(f, text=pesan, font=fnt(12), text_color=teks, anchor='w', justify='left', wraplength=360).pack untuk menempatkan widget dengan tata letak pack.
            font=fnt(12),  # Memanggil ctk.CTkLabel(f, text=pesan, font=fnt(12), text_color=teks, anchor='w', justify='left', wraplength=360).pack untuk menempatkan widget dengan tata letak pack.
            text_color=teks,  # Memanggil ctk.CTkLabel(f, text=pesan, font=fnt(12), text_color=teks, anchor='w', justify='left', wraplength=360).pack untuk menempatkan widget dengan tata letak pack.
            anchor="w",  # Memanggil ctk.CTkLabel(f, text=pesan, font=fnt(12), text_color=teks, anchor='w', justify='left', wraplength=360).pack untuk menempatkan widget dengan tata letak pack.
            justify="left",  # Memanggil ctk.CTkLabel(f, text=pesan, font=fnt(12), text_color=teks, anchor='w', justify='left', wraplength=360).pack untuk menempatkan widget dengan tata letak pack.
            wraplength=360,  # Memanggil ctk.CTkLabel(f, text=pesan, font=fnt(12), text_color=teks, anchor='w', justify='left', wraplength=360).pack untuk menempatkan widget dengan tata letak pack.
        ).pack(fill="x", padx=18, pady=(2, 12))  # Memanggil ctk.CTkLabel(f, text=pesan, font=fnt(12), text_color=teks, anchor='w', justify='left', wraplength=360).pack untuk menempatkan widget dengan tata letak pack.
        f.place(relx=1.0, rely=1.0, anchor="se", x=-24, y=-24)  # Memanggil f.place untuk menjalankan operasi dengan argumen yang diberikan.
        f.lift()  # Memanggil f.lift untuk menjalankan operasi dengan argumen yang diberikan.
        for w in (f, *f.winfo_children()):  # Mengulangi proses untuk w in (f, *f.winfo_children()).
            w.bind("<Button-1>", lambda _e: self.tutup())  # Memanggil w.bind untuk menghubungkan peristiwa dengan fungsi penangan.
        self.frame = f  # Menghitung atau menyiapkan f, lalu menyimpannya pada self.frame.
        self._job = self.root.after(ms or (7000 if jenis == "error" else 3500), self.tutup)  # Menghitung atau menyiapkan self.root.after(ms or (7000 if jenis == 'error' else 3500), self.tutup), lalu menyimpannya pada self._job.


class BarisMetrik(ctk.CTkFrame):  # Mendefinisikan kelas BarisMetrik untuk mengelompokkan data dan perilaku.

    def __init__(self, master, judul, warna):  # Mendefinisikan fungsi __init__ dengan parameter yang tertulis.
        super().__init__(master, fg_color="transparent")  # Memanggil super().__init__ untuk menjalankan operasi dengan argumen yang diberikan.
        self.grid_columnconfigure(0, weight=1)  # Memanggil self.grid_columnconfigure untuk menjalankan operasi dengan argumen yang diberikan.
        ctk.CTkLabel(self, text=judul, font=fnt(13), text_color=INK, anchor="w").grid(  # Memanggil ctk.CTkLabel(self, text=judul, font=fnt(13), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
            row=0, column=0, sticky="w"  # Memanggil ctk.CTkLabel(self, text=judul, font=fnt(13), text_color=INK, anchor='w').grid untuk menempatkan widget pada baris dan kolom.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.nilai = ctk.CTkLabel(  # Menghitung atau menyiapkan ctk.CTkLabel(self, text='-', font=fnt(13, 'bold'), text_color=INK, anchor='e'), lalu menyimpannya pada self.nilai.
            self, text="-", font=fnt(13, "bold"), text_color=INK, anchor="e"  # Menghitung atau menyiapkan ctk.CTkLabel(self, text='-', font=fnt(13, 'bold'), text_color=INK, anchor='e'), lalu menyimpannya pada self.nilai.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.nilai.grid(row=0, column=1, sticky="e")  # Memanggil self.nilai.grid untuk menempatkan widget pada baris dan kolom.
        self.bar = ctk.CTkProgressBar(  # Menghitung atau menyiapkan ctk.CTkProgressBar(self, height=6, corner_radius=3, fg_color='#E4DDCB', progress_color=warna), lalu menyimpannya pada self.bar.
            self, height=6, corner_radius=3, fg_color="#E4DDCB", progress_color=warna  # Menghitung atau menyiapkan ctk.CTkProgressBar(self, height=6, corner_radius=3, fg_color='#E4DDCB', progress_color=warna), lalu menyimpannya pada self.bar.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        self.bar.set(0)  # Memanggil self.bar.set untuk memperbarui nilai.
        self.bar.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(4, 0))  # Memanggil self.bar.grid untuk menempatkan widget pada baris dan kolom.

    def set(self, teks, frak):  # Mendefinisikan fungsi set dengan parameter yang tertulis.
        self.nilai.configure(text=teks)  # Memanggil self.nilai.configure untuk memperbarui konfigurasi widget.
        self.bar.set(frak)  # Memanggil self.bar.set untuk memperbarui nilai.
