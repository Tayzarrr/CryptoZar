<div align="center">
  <img src="cryptozar/assets/logo.png" alt="Logo CryptoZar" width="112">
  <h1>CryptoZar</h1>
  <p><strong>Eksplorasi kriptografi melalui aplikasi desktop yang interaktif.</strong></p>
  <p>6 algoritma · Enkripsi & dekripsi · Demo pembelajaran · Benchmark</p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+">
    <img src="https://img.shields.io/badge/GUI-CustomTkinter-6B84DE" alt="CustomTkinter">
    <img src="https://img.shields.io/badge/Struktur-Modular-1F5A3A" alt="Struktur modular">
    <img src="https://img.shields.io/badge/Project-Edukasi-AD8155" alt="Proyek edukasi">
  </p>
  <p><a href="#mulai-cepat">Mulai cepat</a> · <a href="#algoritma">Algoritma</a> · <a href="#struktur-proyek">Struktur proyek</a> · <a href="PANDUAN_GITHUB.md">Panduan GitHub</a></p>
</div>

---

## Tentang CryptoZar

**CryptoZar** merupakan aplikasi pembelajaran kriptografi berbasis Python dengan antarmuka desktop bernuansa pastel. Pengguna dapat mengenkripsi dan mendekripsi teks, mengolah file, membuat kunci acak, serta mengamati perbandingan beban komputasi algoritma.

Versi ini memisahkan program asli menjadi modul berdasarkan tanggung jawabnya. Setiap baris kode Python diberi komentar berbahasa Indonesia; docstring tetap dipertahankan sebagai penjelasan fungsi. Logo, emblem, dan ikon disimpan sebagai file PNG terpisah.

## Fitur utama

| Fitur | Kemampuan |
| :--- | :--- |
| 🔐 Encrypt & Decrypt | Memproses teks ketikan atau file menggunakan algoritma terpilih |
| 🎲 Random Key | Membuat kunci sesuai format masing-masing algoritma |
| 📂 File Processing | Membaca input, menampilkan pratinjau, serta menyimpan hasil dan kunci |
| 📖 Demo | Menampilkan contoh alur enkripsi dan dekripsi enam algoritma |
| 📊 Benchmark | Mengukur waktu, memori, ukuran kunci, dan ukuran ciphertext; ekspor CSV |
| 🖥️ Desktop GUI | Empat halaman: Encrypt, Decrypt, Demo, dan Benchmark |
| 🧩 Modular | Algoritma, layanan, tampilan, dan aset dapat dipelajari secara terpisah |

## Algoritma

| Algoritma | Bentuk kunci | Cara kerja singkat |
| :--- | :--- | :--- |
| Caesar | Bilangan bulat; geseran efektif modulo 26 | Menggeser setiap huruf alfabet |
| Vigenere | Kata berisi huruf A–Z | Menggeser huruf dengan kunci yang berulang |
| Playfair | Kata; I dan J digabung | Mengolah pasangan huruf pada tabel 5 × 5 |
| Hill | 4 atau 9 bilangan | Mengalikan blok huruf dengan matriks 2 × 2 atau 3 × 3 modulo 26 |
| One-Time Pad | Byte acak sepanjang pesan; ditampilkan sebagai hex | Menggabungkan pesan dan pad menggunakan XOR |
| Stream Cipher (LCG) | Seed bilangan bulat, efektif modulo 256 | Membentuk keystream LCG dan melakukan XOR |

**Perilaku data yang perlu dipahami:** Caesar, Vigenere, Playfair, dan Hill menormalisasi teks menjadi A–Z; spasi, angka, dan tanda baca dibuang. Playfair mengubah J menjadi I dan dapat menambahkan huruf pengisi X/Q. Hill menambahkan X agar panjang teks sesuai ukuran blok. Huruf pengisi tersebut tidak dihapus otomatis saat dekripsi. OTP dan Stream memproses byte, sehingga dekripsi dengan kunci yang sesuai mengembalikan isi file aslinya. Ciphertext kedua algoritma ini disimpan dalam format hex.

## Mulai cepat

Gunakan **Python 3.10 atau lebih baru** dengan dukungan Tkinter. Di Windows, jalankan perintah berikut melalui **PowerShell** dari folder yang berisi `main.py`:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

Aktivasi virtual environment tidak diperlukan. Cara ini juga menghindari kendala execution policy pada `Activate.ps1`.

Alternatif titik masuk, tetap dari folder proyek:

```powershell
.\.venv\Scripts\python.exe -m cryptozar
```

Jika perintah `py` tidak tersedia, gunakan `python` untuk membuat virtual environment. Jika `tkinter` tidak ditemukan, gunakan instalasi Python yang menyertakan komponen Tcl/Tk.

## Alur penggunaan

1. Buka halaman **Encrypt** dan pilih algoritma.
2. Ketik pesan atau pilih file input. File contoh tersedia di `contoh/pesan.txt`.
3. Isi kunci atau gunakan **Generate Random Key**.
4. Jalankan proses, lalu simpan hasil dan kunci jika diperlukan.
5. Buka **Decrypt**, pilih algoritma yang sama, masukkan ciphertext dan kunci, lalu jalankan dekripsi.
6. Gunakan **Demo** untuk melihat contoh dan **Benchmark** untuk membandingkan beban komputasi.

**Contoh Caesar:** pesan `BELAJAR KRIPTOGRAFI` dengan kunci `3` menghasilkan `EHODMDUNULSWRJUDIL`. Dekripsinya menghasilkan `BELAJARKRIPTOGRAFI` karena normalisasi menghapus spasi.

File kerja pada Demo dan Benchmark GUI bersifat sementara. Gunakan tombol penyimpanan hasil benchmark untuk menyimpan CSV secara permanen.

## Struktur proyek

| Lokasi | Tanggung jawab |
| :--- | :--- |
| `main.py` | Titik masuk aplikasi desktop |
| `cryptozar/__main__.py` | Mendukung `python -m cryptozar` |
| `cryptozar/peluncur.py` | Mengatur tema dan memulai aplikasi |
| `cryptozar/konfigurasi.py` | Daftar algoritma dan format kunci default |
| `cryptozar/utilitas.py` | Normalisasi dan konversi huruf/angka |
| `cryptozar/algoritma/caesar.py` | Caesar Cipher |
| `cryptozar/algoritma/vigenere.py` | Vigenere Cipher |
| `cryptozar/algoritma/playfair.py` | Playfair Cipher |
| `cryptozar/algoritma/hill.py` | Hill Cipher dan operasi matriks |
| `cryptozar/algoritma/otp.py` | XOR dan pembangkitan pad |
| `cryptozar/algoritma/stream.py` | Keystream LCG |
| `cryptozar/file_io.py` | Pembacaan dan penulisan teks, byte, dan hex |
| `cryptozar/layanan_file.py` | Alur enkripsi/dekripsi file enam algoritma |
| `cryptozar/layanan_gui.py` | Penghubung GUI dan backend, kunci acak, serta penyaluran log |
| `cryptozar/demo.py` | Skenario demonstrasi enam algoritma |
| `cryptozar/benchmark.py` | Pengukuran waktu, memori, dan ekspor CSV |
| `cryptozar/aset.py` | Adaptor pemuatan PNG untuk pemuat gambar asli |
| `cryptozar/assets/` | Logo, emblem, dan ikon PNG |
| `cryptozar/gui/tema.py` | Warna, batas tampilan, dan font |
| `cryptozar/gui/format_pesan.py` | Format ukuran/durasi dan pesan kesalahan |
| `cryptozar/gui/komponen.py` | Komponen GUI, notifikasi, dan baris metrik |
| `cryptozar/gui/halaman_kripto.py` | Halaman Encrypt dan Decrypt |
| `cryptozar/gui/halaman_log.py` | Halaman Demo dan Benchmark beserta kelas dasar log |
| `cryptozar/gui/aplikasi.py` | Jendela utama, navigasi, dan antrean tugas |
| `tests/` | Pengujian algoritma dan integrasi file |
| `PANDUAN_GITHUB.md` | Instruksi PowerShell untuk push dan pull request |

## Pengujian

Pengujian backend dapat dijalankan tanpa membuka GUI:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Suite mencakup vektor Caesar/Vigenere/Playfair/Hill yang diketahui, kunci tidak valid, round-trip file, data biner OTP/Stream, dan adaptor layanan GUI. Pengujian ini tidak menggantikan pemeriksaan visual jendela pada komputer pengguna.

## Memahami benchmark

Data uji dibangkitkan dengan seed tetap agar dapat diulang. Waktu dilaporkan sebagai median dari beberapa pengulangan; puncak memori Python diukur secara terpisah menggunakan `tracemalloc`. Hasil aktual dipengaruhi perangkat dan beban komputer.

Benchmark melaporkan tujuh konfigurasi karena Hill diuji dalam ukuran 2 × 2 dan 3 × 3. Kolom ciphertext OTP/Stream menghitung representasi hex (dua karakter per byte), tanpa newline file. Waktu dekripsi Stream pada kode asli merupakan estimasi dari waktu pembangkitan keystream ditambah XOR. Ukuran kunci adalah representasi konseptual pada benchmark, bukan ukuran penuh objek Python.

## Ruang lingkup pembelajaran

Algoritma klasik dan LCG pada proyek ini digunakan untuk pembelajaran. OTP memerlukan pad acak yang dirahasiakan dan hanya digunakan sekali; mode kunci manual bergantung pada kunci yang diberikan pengguna. Proyek ini mempertahankan perilaku algoritma dan pengukuran pada program sumber.

## Kontribusi dan pengembangan

Lihat [panduan GitHub](PANDUAN_GITHUB.md) untuk alur clone → branch → commit → push → pull request → merge. Jalankan pengujian sebelum mengirim perubahan.

---

<div align="center">
  <strong>CryptoZar · Pelajari prosesnya, pahami hasilnya.</strong><br>
  <sub>Python · CustomTkinter · Kriptografi</sub>
</div>
