# CryptoZar — aset
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
from pathlib import Path  # Mengimpor komponen yang dibutuhkan dari pathlib.
import base64  # Memuat pustaka base64.

_FOLDER = Path(__file__).resolve().parent / "assets"  # Menghitung atau menyiapkan Path(__file__).resolve().parent / 'assets', lalu menyimpannya pada _FOLDER.
LOGO_PNG = base64.b64encode((_FOLDER / "logo.png").read_bytes())  # Menghitung atau menyiapkan base64.b64encode((_FOLDER / 'logo.png').read_bytes()), lalu menyimpannya pada LOGO_PNG.
EMBLEM_PNG = base64.b64encode((_FOLDER / "emblem.png").read_bytes())  # Menghitung atau menyiapkan base64.b64encode((_FOLDER / 'emblem.png').read_bytes()), lalu menyimpannya pada EMBLEM_PNG.
IKON_PNG = base64.b64encode((_FOLDER / "ikon.png").read_bytes())  # Menghitung atau menyiapkan base64.b64encode((_FOLDER / 'ikon.png').read_bytes()), lalu menyimpannya pada IKON_PNG.
