# CryptoZar — gui.tema
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
import customtkinter as ctk  # Memuat pustaka customtkinter as ctk.
from tkinter import font as tkfont  # Mengimpor komponen yang dibutuhkan dari tkinter.

BG = "#EDE6D6"  # Menghitung atau menyiapkan '#EDE6D6', lalu menyimpannya pada BG.

SIDEBAR = "#E0D7C2"  # Menghitung atau menyiapkan '#E0D7C2', lalu menyimpannya pada SIDEBAR.

NAV_H = "#D3C9B2"  # Menghitung atau menyiapkan '#D3C9B2', lalu menyimpannya pada NAV_H.

METRIK_BG = "#F8F4EA"  # Menghitung atau menyiapkan '#F8F4EA', lalu menyimpannya pada METRIK_BG.

CARD = "#FFFFFF"  # Menghitung atau menyiapkan '#FFFFFF', lalu menyimpannya pada CARD.

BORDER = "#D9CFB8"  # Menghitung atau menyiapkan '#D9CFB8', lalu menyimpannya pada BORDER.

FIELD = "#FBF9F3"  # Menghitung atau menyiapkan '#FBF9F3', lalu menyimpannya pada FIELD.

INK = "#2D2A26"  # Menghitung atau menyiapkan '#2D2A26', lalu menyimpannya pada INK.

MUTED = "#7A7366"  # Menghitung atau menyiapkan '#7A7366', lalu menyimpannya pada MUTED.

BLUE = "#D9E0F7"  # Menghitung atau menyiapkan '#D9E0F7', lalu menyimpannya pada BLUE.

BLUE_H = "#C6D0F1"  # Menghitung atau menyiapkan '#C6D0F1', lalu menyimpannya pada BLUE_H.

BLUE_INK = "#2B3A67"  # Menghitung atau menyiapkan '#2B3A67', lalu menyimpannya pada BLUE_INK.

MINT = "#CDEBDA"  # Menghitung atau menyiapkan '#CDEBDA', lalu menyimpannya pada MINT.

MINT_H = "#B9E0CB"  # Menghitung atau menyiapkan '#B9E0CB', lalu menyimpannya pada MINT_H.

MINT_INK = "#1F5A3A"  # Menghitung atau menyiapkan '#1F5A3A', lalu menyimpannya pada MINT_INK.

PRIMARY = "#6B84DE"  # Menghitung atau menyiapkan '#6B84DE', lalu menyimpannya pada PRIMARY.

PRIMARY_H = "#566FCB"  # Menghitung atau menyiapkan '#566FCB', lalu menyimpannya pada PRIMARY_H.

NEUTRAL = "#F1EDE0"  # Menghitung atau menyiapkan '#F1EDE0', lalu menyimpannya pada NEUTRAL.

NEUTRAL_H = "#E7E1D0"  # Menghitung atau menyiapkan '#E7E1D0', lalu menyimpannya pada NEUTRAL_H.

TOAST = {  # Menghitung atau menyiapkan {'success': ('#DDF3E6', '#B5DEC6', '#1F5A3A'), 'error': ('#FBE3E1', '#EFB9B4', '#8A2B25'), 'info': ('#E3E9FA',, lalu menyimpannya pada TOAST.
    "success": ("#DDF3E6", "#B5DEC6", "#1F5A3A"),  # Menghitung atau menyiapkan {'success': ('#DDF3E6', '#B5DEC6', '#1F5A3A'), 'error': ('#FBE3E1', '#EFB9B4', '#8A2B25'), 'info': ('#E3E9FA',, lalu menyimpannya pada TOAST.
    "error": ("#FBE3E1", "#EFB9B4", "#8A2B25"),  # Menghitung atau menyiapkan {'success': ('#DDF3E6', '#B5DEC6', '#1F5A3A'), 'error': ('#FBE3E1', '#EFB9B4', '#8A2B25'), 'info': ('#E3E9FA',, lalu menyimpannya pada TOAST.
    "info": ("#E3E9FA", "#BFCBF0", "#2B3A67"),  # Menghitung atau menyiapkan {'success': ('#DDF3E6', '#B5DEC6', '#1F5A3A'), 'error': ('#FBE3E1', '#EFB9B4', '#8A2B25'), 'info': ('#E3E9FA',, lalu menyimpannya pada TOAST.
}  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

NAMA_ALGO = {  # Menghitung atau menyiapkan {'Caesar Cipher': '1', 'Vigenere Cipher': '2', 'Playfair Cipher': '3', 'Hill Cipher': '4', 'One-Time Pad': '5', lalu menyimpannya pada NAMA_ALGO.
    "Caesar Cipher": "1",  # Menghitung atau menyiapkan {'Caesar Cipher': '1', 'Vigenere Cipher': '2', 'Playfair Cipher': '3', 'Hill Cipher': '4', 'One-Time Pad': '5', lalu menyimpannya pada NAMA_ALGO.
    "Vigenere Cipher": "2",  # Menghitung atau menyiapkan {'Caesar Cipher': '1', 'Vigenere Cipher': '2', 'Playfair Cipher': '3', 'Hill Cipher': '4', 'One-Time Pad': '5', lalu menyimpannya pada NAMA_ALGO.
    "Playfair Cipher": "3",  # Menghitung atau menyiapkan {'Caesar Cipher': '1', 'Vigenere Cipher': '2', 'Playfair Cipher': '3', 'Hill Cipher': '4', 'One-Time Pad': '5', lalu menyimpannya pada NAMA_ALGO.
    "Hill Cipher": "4",  # Menghitung atau menyiapkan {'Caesar Cipher': '1', 'Vigenere Cipher': '2', 'Playfair Cipher': '3', 'Hill Cipher': '4', 'One-Time Pad': '5', lalu menyimpannya pada NAMA_ALGO.
    "One-Time Pad": "5",  # Menghitung atau menyiapkan {'Caesar Cipher': '1', 'Vigenere Cipher': '2', 'Playfair Cipher': '3', 'Hill Cipher': '4', 'One-Time Pad': '5', lalu menyimpannya pada NAMA_ALGO.
    "Stream Cipher (LCG)": "6",  # Menghitung atau menyiapkan {'Caesar Cipher': '1', 'Vigenere Cipher': '2', 'Playfair Cipher': '3', 'Hill Cipher': '4', 'One-Time Pad': '5', lalu menyimpannya pada NAMA_ALGO.
}  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

BATAS_TAMPIL = 100000  # Menghitung atau menyiapkan 100000, lalu menyimpannya pada BATAS_TAMPIL.

BATAS_PRATINJAU = 20000  # Menghitung atau menyiapkan 20000, lalu menyimpannya pada BATAS_PRATINJAU.

BATAS_KUNCI = 3000  # Menghitung atau menyiapkan 3000, lalu menyimpannya pada BATAS_KUNCI.

_cache_font = {}  # Menghitung atau menyiapkan {}, lalu menyimpannya pada _cache_font.


def _pilih_font(kandidat, cadangan):  # Mendefinisikan fungsi _pilih_font dengan parameter yang tertulis.
    ada = set(tkfont.families())  # Menghitung atau menyiapkan set(tkfont.families()), lalu menyimpannya pada ada.
    for k in kandidat:  # Mengulangi proses untuk k in kandidat.
        if k in ada:  # Menjalankan blok hanya jika k in ada.
            return k  # Mengembalikan k.
    return cadangan  # Mengembalikan cadangan.


def fnt(ukuran=13, bobot="normal", mono=False):  # Mendefinisikan fungsi fnt dengan parameter yang tertulis.
    """Buat CTkFont; keluarga font dipilih sekali setelah jendela utama ada."""  # Menjelaskan tujuan modul, kelas, atau fungsi melalui docstring.
    if "sans" not in _cache_font:  # Menjalankan blok hanya jika "sans" not in _cache_font.
        _cache_font["sans"] = _pilih_font(  # Menghitung atau menyiapkan _pilih_font(('Inter', 'Segoe UI', 'SF Pro Text', 'Helvetica Neue', 'Roboto', 'Noto Sans', 'DejaVu Sans'), 'Hel, lalu menyimpannya pada _cache_font['sans'].
            (  # Menghitung atau menyiapkan _pilih_font(('Inter', 'Segoe UI', 'SF Pro Text', 'Helvetica Neue', 'Roboto', 'Noto Sans', 'DejaVu Sans'), 'Hel, lalu menyimpannya pada _cache_font['sans'].
                "Inter",  # Menghitung atau menyiapkan _pilih_font(('Inter', 'Segoe UI', 'SF Pro Text', 'Helvetica Neue', 'Roboto', 'Noto Sans', 'DejaVu Sans'), 'Hel, lalu menyimpannya pada _cache_font['sans'].
                "Segoe UI",  # Menghitung atau menyiapkan _pilih_font(('Inter', 'Segoe UI', 'SF Pro Text', 'Helvetica Neue', 'Roboto', 'Noto Sans', 'DejaVu Sans'), 'Hel, lalu menyimpannya pada _cache_font['sans'].
                "SF Pro Text",  # Menghitung atau menyiapkan _pilih_font(('Inter', 'Segoe UI', 'SF Pro Text', 'Helvetica Neue', 'Roboto', 'Noto Sans', 'DejaVu Sans'), 'Hel, lalu menyimpannya pada _cache_font['sans'].
                "Helvetica Neue",  # Menghitung atau menyiapkan _pilih_font(('Inter', 'Segoe UI', 'SF Pro Text', 'Helvetica Neue', 'Roboto', 'Noto Sans', 'DejaVu Sans'), 'Hel, lalu menyimpannya pada _cache_font['sans'].
                "Roboto",  # Menghitung atau menyiapkan _pilih_font(('Inter', 'Segoe UI', 'SF Pro Text', 'Helvetica Neue', 'Roboto', 'Noto Sans', 'DejaVu Sans'), 'Hel, lalu menyimpannya pada _cache_font['sans'].
                "Noto Sans",  # Menghitung atau menyiapkan _pilih_font(('Inter', 'Segoe UI', 'SF Pro Text', 'Helvetica Neue', 'Roboto', 'Noto Sans', 'DejaVu Sans'), 'Hel, lalu menyimpannya pada _cache_font['sans'].
                "DejaVu Sans",  # Menghitung atau menyiapkan _pilih_font(('Inter', 'Segoe UI', 'SF Pro Text', 'Helvetica Neue', 'Roboto', 'Noto Sans', 'DejaVu Sans'), 'Hel, lalu menyimpannya pada _cache_font['sans'].
            ),  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
            "Helvetica",  # Menghitung atau menyiapkan _pilih_font(('Inter', 'Segoe UI', 'SF Pro Text', 'Helvetica Neue', 'Roboto', 'Noto Sans', 'DejaVu Sans'), 'Hel, lalu menyimpannya pada _cache_font['sans'].
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
        _cache_font["mono"] = _pilih_font(  # Menghitung atau menyiapkan _pilih_font(('Cascadia Mono', 'Consolas', 'Menlo', 'SF Mono', 'DejaVu Sans Mono', 'Liberation Mono'), 'Courier, lalu menyimpannya pada _cache_font['mono'].
            (  # Menghitung atau menyiapkan _pilih_font(('Cascadia Mono', 'Consolas', 'Menlo', 'SF Mono', 'DejaVu Sans Mono', 'Liberation Mono'), 'Courier, lalu menyimpannya pada _cache_font['mono'].
                "Cascadia Mono",  # Menghitung atau menyiapkan _pilih_font(('Cascadia Mono', 'Consolas', 'Menlo', 'SF Mono', 'DejaVu Sans Mono', 'Liberation Mono'), 'Courier, lalu menyimpannya pada _cache_font['mono'].
                "Consolas",  # Menghitung atau menyiapkan _pilih_font(('Cascadia Mono', 'Consolas', 'Menlo', 'SF Mono', 'DejaVu Sans Mono', 'Liberation Mono'), 'Courier, lalu menyimpannya pada _cache_font['mono'].
                "Menlo",  # Menghitung atau menyiapkan _pilih_font(('Cascadia Mono', 'Consolas', 'Menlo', 'SF Mono', 'DejaVu Sans Mono', 'Liberation Mono'), 'Courier, lalu menyimpannya pada _cache_font['mono'].
                "SF Mono",  # Menghitung atau menyiapkan _pilih_font(('Cascadia Mono', 'Consolas', 'Menlo', 'SF Mono', 'DejaVu Sans Mono', 'Liberation Mono'), 'Courier, lalu menyimpannya pada _cache_font['mono'].
                "DejaVu Sans Mono",  # Menghitung atau menyiapkan _pilih_font(('Cascadia Mono', 'Consolas', 'Menlo', 'SF Mono', 'DejaVu Sans Mono', 'Liberation Mono'), 'Courier, lalu menyimpannya pada _cache_font['mono'].
                "Liberation Mono",  # Menghitung atau menyiapkan _pilih_font(('Cascadia Mono', 'Consolas', 'Menlo', 'SF Mono', 'DejaVu Sans Mono', 'Liberation Mono'), 'Courier, lalu menyimpannya pada _cache_font['mono'].
            ),  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
            "Courier",  # Menghitung atau menyiapkan _pilih_font(('Cascadia Mono', 'Consolas', 'Menlo', 'SF Mono', 'DejaVu Sans Mono', 'Liberation Mono'), 'Courier, lalu menyimpannya pada _cache_font['mono'].
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
    return ctk.CTkFont(  # Mengembalikan ctk.CTkFont(.
        family=_cache_font["mono" if mono else "sans"], size=ukuran, weight=bobot  # Menyusun bagian ekspresi family=_cache_font["mono" if mono else "sans"], size=ukuran, weight=bobot.
    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
