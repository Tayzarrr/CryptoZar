# 🔐 CryptoZar

## Aplikasi Enkripsi Modern Berbasis Python

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Cryptography](https://img.shields.io/badge/Domain-Cryptography-green.svg)
![GUI](https://img.shields.io/badge/Interface-CustomTkinter-orange.svg)

## 📌 Tentang Project

CryptoZar merupakan aplikasi desktop berbasis Python yang
mengimplementasikan berbagai algoritma kriptografi dalam satu platform
interaktif.

Aplikasi ini dibuat untuk mempelajari konsep keamanan informasi,
khususnya proses enkripsi dan dekripsi data menggunakan beberapa metode
cipher klasik hingga stream encryption.

## ✨ Fitur Utama

-   Enkripsi dan dekripsi teks maupun file
-   Dukungan 6 algoritma kriptografi
-   Antarmuka GUI modern menggunakan CustomTkinter
-   Pembangkitan kunci otomatis
-   Demo pembelajaran kriptografi
-   Benchmark performa algoritma

## 🔐 Algoritma yang Didukung

  Algoritma             Jenis
  --------------------- -----------------------
  Caesar Cipher         Substitution Cipher
  Vigenere Cipher       Polyalphabetic Cipher
  Playfair Cipher       Digraph Cipher
  Hill Cipher           Matrix Cipher
  One-Time Pad (OTP)    Symmetric Cipher
  Stream Cipher (LCG)   Stream Encryption

## 🏗️ Struktur Sistem

    CryptoZar
    │
    ├── Backend Cryptography Engine
    │   ├── Caesar Cipher
    │   ├── Vigenere Cipher
    │   ├── Playfair Cipher
    │   ├── Hill Cipher
    │   ├── One-Time Pad
    │   └── Stream Cipher
    │
    └── Graphical User Interface
        ├── Input Data
        ├── Pemilihan Algoritma
        ├── Key Management
        └── Result Visualization

## ⚙️ Teknologi

-   Python 3.x
-   CustomTkinter
-   Tkinter
-   CSV
-   Time Performance Measurement
-   Tracemalloc Memory Analysis
-   Secrets Random Generator

## 🚀 Instalasi

Clone repository:

``` bash
git clone https://github.com/Tayzarrr/CryptoZar.git
```

Masuk folder:

``` bash
cd CryptoZar
```

Install dependency:

``` bash
pip install customtkinter
```

Jalankan aplikasi:

``` bash
python CryptoZar.py
```

## 📊 Benchmark

CryptoZar menyediakan pengujian performa algoritma berdasarkan:

-   Waktu enkripsi
-   Waktu dekripsi
-   Penggunaan memori
-   Ukuran kunci
-   Ukuran ciphertext

Hasil pengujian dapat disimpan dalam bentuk CSV.

## 🎓 Mode Pembelajaran

Aplikasi menyediakan demo otomatis yang memperlihatkan proses:

    Plaintext
        ↓
    Encryption Algorithm
        ↓
    Ciphertext
        ↓
    Decryption
        ↓
    Plaintext kembali

## 📁 Struktur Repository

    CryptoZar
    │
    ├── CryptoZar.py
    ├── README.md
    ├── requirements.txt
    └── assets/
        └── screenshot.png

## 👨‍💻 Developer

**Andika Novanda Putra**

## 📌 Catatan

Project ini dibuat untuk tujuan edukasi. Algoritma cipher klasik sangat
baik untuk memahami konsep kriptografi, namun untuk keamanan industri
gunakan algoritma modern seperti AES, RSA, ECC, atau ChaCha20.

⭐ Jangan lupa memberikan star jika project ini bermanfaat.
