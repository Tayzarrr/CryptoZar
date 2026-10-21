# Catatan pemisahan program

Sumber: `CryptoZar(AplikasiEnkripsi)(1).py` (identik dengan lampiran pertama).

- Fungsi dan kelas dipindahkan berdasarkan tanggung jawab, memakai impor eksplisit.
- Enam algoritma mempunyai file masing-masing.
- Data gambar base64 dikeluarkan menjadi tiga PNG; `aset.py` menyediakan adaptor agar pemuat gambar asli tetap kompatibel.
- `main.py` dan `python -m cryptozar` menjadi titik masuk baru.
- Kode diberi komentar penjelasan dalam bahasa Indonesia. Baris kosong bukan instruksi; docstring tetap berupa dokumentasi literal.
- Logika dan format hasil algoritma dipertahankan. Pengukuran benchmark mengikuti implementasi sumber, termasuk estimasi waktu dekripsi Stream.
- Tambahan proyek: requirements, contoh pesan, pengujian, README, panduan GitHub, gitignore, dan gitattributes.

## Verifikasi dan batasnya

Struktur sintaksis fungsi/kelas dibandingkan dengan sumber asli melalui AST, sehingga komentar dan pemindahan file tidak mengubah isi instruksi. Pengujian fungsional memeriksa algoritma dan integrasi layanan. Aset gambar dibandingkan dengan bytes hasil decode dari sumber.

Lingkungan pembuatan tidak memiliki layar desktop untuk menjalankan jendela GUI secara visual. Lakukan pemeriksaan empat halaman di Windows melalui langkah pada README.
