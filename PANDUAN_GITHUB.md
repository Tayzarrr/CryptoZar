# Panduan PowerShell — CryptoZar

Repository tujuan: https://github.com/Tayzarrr/CryptoZar

ZIP berisi folder `CryptoZar_Modular`. Simpan ZIP di Downloads sebelum menjalankan contoh di bawah. Perintah ini menambahkan versi modular ke repository yang sudah ada dan mempertahankan riwayat Git. File lama yang tidak berbenturan tetap ada.

## 1. Ekstrak ZIP

```powershell
Set-Location "$env:USERPROFILE\Downloads"
Expand-Archive -LiteralPath ".\CryptoZar_Modular.zip" -DestinationPath ".\CryptoZar_Hasil" -Force
Test-Path ".\CryptoZar_Hasil\CryptoZar_Modular\main.py"
```

Hasil `Test-Path` harus `True`. Jika ZIP tersimpan di folder lain, ganti lokasi pada `Set-Location`.

## 2. Clone repository yang sudah ada

```powershell
git --version
git clone https://github.com/Tayzarrr/CryptoZar.git CryptoZar-GitHub
if ($LASTEXITCODE -ne 0) { throw "Clone gagal. Periksa koneksi, akses repository, atau nama folder tujuan." }
Set-Location ".\CryptoZar-GitHub"
git remote -v
git status
```

Jika folder `CryptoZar-GitHub` sudah ada, gunakan folder tujuan lain yang belum ada dan sesuaikan langkah selanjutnya. Jangan menginisialisasi repository baru di folder hasil ekstrak karena repository GitHub sudah memiliki riwayat.

## 3. Buat branch dan salin isi proyek

```powershell
git switch -c refactor/modular-komentar
if ($LASTEXITCODE -ne 0) { throw "Gagal membuat branch. Periksa git status dan nama branch." }
$sumberCryptoZar = (Resolve-Path "..\CryptoZar_Hasil\CryptoZar_Modular").Path
Get-ChildItem -LiteralPath $sumberCryptoZar -Force | Copy-Item -Destination . -Recurse -Force
Get-ChildItem -Force
git status --short
```

`main.py`, `README.md`, `requirements.txt`, dan folder `cryptozar` harus langsung berada di folder repository. README lama akan diganti dengan README yang ada di ZIP. Perintah penyalinan juga menyertakan `.gitignore` dan `.gitattributes`.

## 4. Jalankan dan periksa program

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe main.py
```

Coba halaman Encrypt, Decrypt, Demo, dan Benchmark. Tutup jendela aplikasi untuk kembali ke PowerShell. Kode Python berada di file `.py`; yang diketik pada PowerShell adalah perintah menjalankannya.

## 5. Stage, commit, dan push

```powershell
git add -- main.py cryptozar tests contoh requirements.txt README.md PANDUAN_GITHUB.md CATATAN_PEMISAHAN.md .gitignore .gitattributes
git diff --cached --stat
git status
git commit -m "Refactor CryptoZar menjadi modular dengan komentar dan dokumentasi"
if ($LASTEXITCODE -ne 0) { throw "Commit gagal. Periksa pesan Git sebelum push." }
git push -u origin refactor/modular-komentar
```

Jika Git meminta identitas, isi identitas Git milikmu lalu ulangi commit:

```powershell
git config user.name "NAMA_GITHUB_KAMU"
git config user.email "EMAIL_GITHUB_KAMU"
```

Jika autentikasi diminta, ikuti login GitHub yang ditampilkan Git Credential Manager/browser. Password akun GitHub tidak dipakai sebagai password HTTPS Git; jika Git meminta token, gunakan Personal Access Token sebagai kredensial lokal dan jangan masukkan ke file proyek.

## 6. Buat pull request lalu merge

1. Buka https://github.com/Tayzarrr/CryptoZar.
2. Klik **Compare & pull request** atau buka tab **Pull requests → New pull request**.
3. Pilih base branch utama repository (`main` atau `master`, sesuai yang tampil) dan compare `refactor/modular-komentar`.
4. Judul: **Refactor CryptoZar: modularisasi, komentar per baris, dan README**.
5. Isi deskripsi: “Memisahkan algoritma, layanan file, GUI, dan aset. Menambahkan komentar berbahasa Indonesia, dokumentasi penggunaan, serta pengujian backend.” Tambahkan hasil pengujian aktual pada komputermu.
6. Klik **Create pull request**, tinjau perubahannya, lalu **Merge pull request → Confirm merge** jika pemeriksaan/aturan repository mengizinkan.

Jika GitHub CLI (`gh`) sudah dipasang dan login, langkah membuat PR dapat diganti dengan:

```powershell
gh pr create --title "Refactor CryptoZar: modularisasi, komentar per baris, dan README" --body "Memisahkan algoritma, layanan file, GUI, dan aset. Menambahkan komentar per baris, README, dan pengujian backend."
```

Setelah merge, perbarui salinan lokal; gunakan nama branch utama yang terlihat di repository:

```powershell
git fetch origin
git switch main
git pull --ff-only origin main
```

Jika branch utamanya `master`, ganti kedua `main` di atas dengan `master`.

## Kendala umum

| Pesan/kondisi | Tindakan |
| --- | --- |
| `git` tidak dikenali | Instal Git for Windows dan buka ulang PowerShell |
| `py` tidak dikenali | Gunakan `python` yang terpasang atau perbaiki instalasi Python |
| `ModuleNotFoundError: customtkinter` | Instal requirements dengan Python `.venv` yang sama |
| `No module named cryptozar` | Jalankan dari folder yang berisi `main.py` dan folder `cryptozar` |
| `LF will be replaced by CRLF` | Peringatan konversi akhir baris; periksa `git status` dan lanjutkan bila tidak ada error |
| `Permission denied` / `403` saat push | Login dengan akun yang mempunyai izin push; jika tidak memiliki izin, gunakan fork dan PR |
| Branch sudah ada | Gunakan nama branch baru atau lanjutkan branch yang sesuai setelah memeriksa `git status` |
| Push ditolak karena branch remote berbeda | Periksa `git status` dan riwayat remote; jangan menggunakan force push secara sembarang |

Untuk pembaruan berikutnya, edit file pada clone yang sama, jalankan pengujian, lalu buat commit dan push pada branch kerja.
