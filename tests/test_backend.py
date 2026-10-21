# Pengujian vektor algoritma dan integrasi layanan CryptoZar.
# Setiap baris kode diberi komentar penjelasan berbahasa Indonesia.
import contextlib  # Memuat pustaka contextlib.
import io  # Memuat pustaka io.
import tempfile  # Memuat pustaka tempfile.
import unittest  # Memuat pustaka unittest.
from pathlib import Path  # Mengimpor komponen yang dibutuhkan dari pathlib.
from cryptozar.algoritma.caesar import caesar_enkripsi, caesar_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.caesar.
from cryptozar.algoritma.vigenere import vigenere_enkripsi, vigenere_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.vigenere.
from cryptozar.algoritma.playfair import playfair_enkripsi, playfair_dekripsi, playfair_digraf  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.playfair.
from cryptozar.algoritma.hill import hill_parse_kunci, hill_enkripsi, hill_dekripsi  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.hill.
from cryptozar.algoritma.otp import xor_bytes  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.otp.
from cryptozar.algoritma.stream import keystream_lcg  # Mengimpor komponen yang dibutuhkan dari cryptozar.algoritma.stream.
from cryptozar.layanan_file import enkripsi_file, dekripsi_file  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_file.
from cryptozar.layanan_gui import jalankan_enkripsi, jalankan_dekripsi, kunci_acak  # Mengimpor komponen yang dibutuhkan dari cryptozar.layanan_gui.
from cryptozar.benchmark import ukur_beban_komputasi  # Mengimpor komponen yang dibutuhkan dari cryptozar.benchmark.


class TestAlgoritma(unittest.TestCase):  # Mendefinisikan kelas TestAlgoritma untuk mengelompokkan data dan perilaku.
    def test_caesar_vektor(self):  # Mendefinisikan fungsi test_caesar_vektor dengan parameter yang tertulis.
        self.assertEqual(caesar_enkripsi("BELAJAR KRIPTOGRAFI", 3), "EHODMDUNULSWRJUDIL")  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertEqual(caesar_dekripsi("DEFC", 3), "ABCZ")  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.

    def test_vigenere_vektor(self):  # Mendefinisikan fungsi test_vigenere_vektor dengan parameter yang tertulis.
        self.assertEqual(vigenere_enkripsi("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertEqual(vigenere_dekripsi("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.

    def test_vigenere_kunci_kosong(self):  # Mendefinisikan fungsi test_vigenere_kunci_kosong dengan parameter yang tertulis.
        with self.assertRaises(ValueError):  # Mengelola sumber daya atau konteks self.assertRaises(ValueError).
            vigenere_enkripsi("ABC", "123")  # Memanggil vigenere_enkripsi untuk menjalankan operasi dengan argumen yang diberikan.

    def test_playfair_vektor(self):  # Mendefinisikan fungsi test_playfair_vektor dengan parameter yang tertulis.
        plain = "HIDETHEGOLDINTHETREESTUMP"  # Menghitung atau menyiapkan 'HIDETHEGOLDINTHETREESTUMP', lalu menyimpannya pada plain.
        cipher = "BMODZBXDNABEKUDMUIXMMOUVIF"  # Menghitung atau menyiapkan 'BMODZBXDNABEKUDMUIXMMOUVIF', lalu menyimpannya pada cipher.
        self.assertEqual(playfair_enkripsi(plain, "PLAYFAIR EXAMPLE"), cipher)  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertEqual(  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
            playfair_dekripsi(cipher, "PLAYFAIR EXAMPLE"), "HIDETHEGOLDINTHETREXESTUMP"  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.

    def test_playfair_pengisi(self):  # Mendefinisikan fungsi test_playfair_pengisi dengan parameter yang tertulis.
        prepared = "".join(a + b for a, b in playfair_digraf("JXX BALLOON"))  # Menghitung atau menyiapkan ''.join((a + b for a, b in playfair_digraf('JXX BALLOON'))), lalu menyimpannya pada prepared.
        cipher = playfair_enkripsi("JXX BALLOON", "MONARCHY")  # Menghitung atau menyiapkan playfair_enkripsi('JXX BALLOON', 'MONARCHY'), lalu menyimpannya pada cipher.
        self.assertEqual(playfair_dekripsi(cipher, "MONARCHY"), prepared)  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.

    def test_playfair_panjang_ganjil(self):  # Mendefinisikan fungsi test_playfair_panjang_ganjil dengan parameter yang tertulis.
        with self.assertRaises(ValueError):  # Mengelola sumber daya atau konteks self.assertRaises(ValueError).
            playfair_dekripsi("ABC", "MONARCHY")  # Memanggil playfair_dekripsi untuk menjalankan operasi dengan argumen yang diberikan.

    def test_hill_2x2_padding(self):  # Mendefinisikan fungsi test_hill_2x2_padding dengan parameter yang tertulis.
        key = hill_parse_kunci("3 3 2 5")  # Menghitung atau menyiapkan hill_parse_kunci('3 3 2 5'), lalu menyimpannya pada key.
        self.assertEqual(hill_enkripsi("HELP", key), "HIAT")  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertEqual(hill_dekripsi(hill_enkripsi("HELLO", key), key), "HELLOX")  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.

    def test_hill_3x3_vektor(self):  # Mendefinisikan fungsi test_hill_3x3_vektor dengan parameter yang tertulis.
        key = hill_parse_kunci("6 24 1 13 16 10 20 17 15")  # Menghitung atau menyiapkan hill_parse_kunci('6 24 1 13 16 10 20 17 15'), lalu menyimpannya pada key.
        self.assertEqual(hill_enkripsi("ACT", key), "POH")  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertEqual(hill_dekripsi("POH", key), "ACT")  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.

    def test_hill_kunci_tidak_valid(self):  # Mendefinisikan fungsi test_hill_kunci_tidak_valid dengan parameter yang tertulis.
        for key in ("1 2 3", "2 4 2 4", "a b c d"):  # Mengulangi proses untuk key in ("1 2 3", "2 4 2 4", "a b c d").
            with self.subTest(key=key), self.assertRaises(ValueError):  # Mengelola sumber daya atau konteks self.subTest(key=key), self.assertRaises(ValueError).
                hill_parse_kunci(key)  # Memanggil hill_parse_kunci untuk menjalankan operasi dengan argumen yang diberikan.

    def test_xor_vektor(self):  # Mendefinisikan fungsi test_xor_vektor dengan parameter yang tertulis.
        self.assertEqual(xor_bytes(bytes([0, 255]), bytes([255, 15])), bytes([255, 240]))  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        with self.assertRaises(ValueError):  # Mengelola sumber daya atau konteks self.assertRaises(ValueError).
            xor_bytes(b"A", b"AB")  # Memanggil xor_bytes untuk menjalankan operasi dengan argumen yang diberikan.

    def test_stream_lcg(self):  # Mendefinisikan fungsi test_stream_lcg dengan parameter yang tertulis.
        self.assertEqual(keystream_lcg(77, 4), bytes([130, 139, 184, 153]))  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertEqual(keystream_lcg(77, 10), keystream_lcg(333, 10))  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.


class TestIntegrasi(unittest.TestCase):  # Mendefinisikan kelas TestIntegrasi untuk mengelompokkan data dan perilaku.
    def test_file_semua_algoritma(self):  # Mendefinisikan fungsi test_file_semua_algoritma dengan parameter yang tertulis.
        with tempfile.TemporaryDirectory() as tmp:  # Mengelola sumber daya atau konteks tempfile.TemporaryDirectory() as tmp.
            source = Path(tmp) / "pesan.txt"  # Menghitung atau menyiapkan Path(tmp) / 'pesan.txt', lalu menyimpannya pada source.
            source.write_text("BELAJAR KRIPTOGRAFI", encoding="utf-8")  # Memanggil source.write_text untuk menjalankan operasi dengan argumen yang diberikan.
            for code, key in [  # Mengulangi proses untuk code, key in .
                ("1", "3"),  # Menyusun bagian ekspresi ("1", "3"),.
                ("2", "SANDI"),  # Menyusun bagian ekspresi ("2", "SANDI"),.
                ("3", "MONARCHY"),  # Menyusun bagian ekspresi ("3", "MONARCHY"),.
                ("4", "3 3 2 5"),  # Menyusun bagian ekspresi ("4", "3 3 2 5"),.
                ("5", None),  # Menyusun bagian ekspresi ("5", None),.
                ("6", "77"),  # Menyusun bagian ekspresi ("6", "77"),.
            ]:  # Menyusun bagian ekspresi ]:.
                with self.subTest(code=code):  # Mengelola sumber daya atau konteks self.subTest(code=code).
                    result = enkripsi_file(code, str(source), key)  # Menghitung atau menyiapkan enkripsi_file(code, str(source), key), lalu menyimpannya pada result.
                    decoded = dekripsi_file(  # Menghitung atau menyiapkan dekripsi_file(code, result['out_path'], result['kunci_path'] if code == '5' else key), lalu menyimpannya pada decoded.
                        code, result["out_path"], result["kunci_path"] if code == "5" else key  # Menghitung atau menyiapkan dekripsi_file(code, result['out_path'], result['kunci_path'] if code == '5' else key), lalu menyimpannya pada decoded.
                    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
                    text = Path(decoded["out_path"]).read_text(encoding="utf-8")  # Menghitung atau menyiapkan Path(decoded['out_path']).read_text(encoding='utf-8'), lalu menyimpannya pada text.
                    expected = (  # Menghitung atau menyiapkan 'BELAJAR KRIPTOGRAFI' if code in ('5', '6') else 'BELAJARKRIPTOGRAFI', lalu menyimpannya pada expected.
                        "BELAJAR KRIPTOGRAFI" if code in ("5", "6") else "BELAJARKRIPTOGRAFI"  # Menghitung atau menyiapkan 'BELAJAR KRIPTOGRAFI' if code in ('5', '6') else 'BELAJARKRIPTOGRAFI', lalu menyimpannya pada expected.
                    )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
                    if code == "3":  # Menjalankan blok hanya jika code == "3".
                        expected = "BELAIARKRIPTOGRAFI"  # Menghitung atau menyiapkan 'BELAIARKRIPTOGRAFI', lalu menyimpannya pada expected.
                    self.assertEqual(text, expected)  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.

    def test_file_biner(self):  # Mendefinisikan fungsi test_file_biner dengan parameter yang tertulis.
        data = bytes(range(256)) + b"\x00\xff\r\n"  # Menghitung atau menyiapkan bytes(range(256)) + b'\x00\xff\r\n', lalu menyimpannya pada data.
        with tempfile.TemporaryDirectory() as tmp:  # Mengelola sumber daya atau konteks tempfile.TemporaryDirectory() as tmp.
            source = Path(tmp) / "binary.txt"  # Menghitung atau menyiapkan Path(tmp) / 'binary.txt', lalu menyimpannya pada source.
            source.write_bytes(data)  # Memanggil source.write_bytes untuk menjalankan operasi dengan argumen yang diberikan.
            for code, key in [("5", None), ("6", "77")]:  # Mengulangi proses untuk code, key in [("5", None), ("6", "77")].
                result = enkripsi_file(code, str(source), key)  # Menghitung atau menyiapkan enkripsi_file(code, str(source), key), lalu menyimpannya pada result.
                decoded = dekripsi_file(  # Menghitung atau menyiapkan dekripsi_file(code, result['out_path'], result['kunci_path'] if code == '5' else key), lalu menyimpannya pada decoded.
                    code, result["out_path"], result["kunci_path"] if code == "5" else key  # Menghitung atau menyiapkan dekripsi_file(code, result['out_path'], result['kunci_path'] if code == '5' else key), lalu menyimpannya pada decoded.
                )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
                self.assertEqual(Path(decoded["out_path"]).read_bytes(), data)  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.

    def test_layanan_gui_dan_otp_manual(self):  # Mendefinisikan fungsi test_layanan_gui_dan_otp_manual dengan parameter yang tertulis.
        for code, key in [  # Mengulangi proses untuk code, key in .
            ("1", "3"),  # Menyusun bagian ekspresi ("1", "3"),.
            ("2", "SANDI"),  # Menyusun bagian ekspresi ("2", "SANDI"),.
            ("3", "MONARCHY"),  # Menyusun bagian ekspresi ("3", "MONARCHY"),.
            ("4", "3 3 2 5"),  # Menyusun bagian ekspresi ("4", "3 3 2 5"),.
            ("5", "00010203"),  # Menyusun bagian ekspresi ("5", "00010203"),.
            ("6", "77"),  # Menyusun bagian ekspresi ("6", "77"),.
        ]:  # Menyusun bagian ekspresi ]:.
            result = jalankan_enkripsi(code, "ABCD", None, key)  # Menghitung atau menyiapkan jalankan_enkripsi(code, 'ABCD', None, key), lalu menyimpannya pada result.
            decoded = jalankan_dekripsi(  # Menghitung atau menyiapkan jalankan_dekripsi(code, result['teks_hasil'], None, result['kunci_simpan']), lalu menyimpannya pada decoded.
                code, result["teks_hasil"], None, result["kunci_simpan"]  # Menghitung atau menyiapkan jalankan_dekripsi(code, result['teks_hasil'], None, result['kunci_simpan']), lalu menyimpannya pada decoded.
            )  # Menutup susunan argumen atau koleksi yang dibuka pada baris sebelumnya.
            self.assertEqual(decoded["bytes_hasil"], b"ABCD")  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.

    def test_kunci_acak(self):  # Mendefinisikan fungsi test_kunci_acak dengan parameter yang tertulis.
        self.assertTrue(1 <= int(kunci_acak("1")) <= 25)  # Memanggil self.assertTrue untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertEqual(len(kunci_acak("2")), 8)  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertEqual(len(kunci_acak("3")), 8)  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertEqual(len(hill_parse_kunci(kunci_acak("4"))), 2)  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertEqual(len(bytes.fromhex(kunci_acak("5", 31))), 31)  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
        self.assertTrue(0 <= int(kunci_acak("6")) <= 255)  # Memanggil self.assertTrue untuk menjalankan operasi dengan argumen yang diberikan.

    def test_benchmark_csv(self):  # Mendefinisikan fungsi test_benchmark_csv dengan parameter yang tertulis.
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):  # Mengelola sumber daya atau konteks tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()).
            path = Path(tmp) / "benchmark.csv"  # Menghitung atau menyiapkan Path(tmp) / 'benchmark.csv', lalu menyimpannya pada path.
            ukur_beban_komputasi([32], ulang=1, csv_path=str(path))  # Memanggil ukur_beban_komputasi untuk menjalankan operasi dengan argumen yang diberikan.
            rows = path.read_text(encoding="utf-8").splitlines()  # Menghitung atau menyiapkan path.read_text(encoding='utf-8').splitlines(), lalu menyimpannya pada rows.
            self.assertEqual(len(rows), 8)  # Memanggil self.assertEqual untuk menjalankan operasi dengan argumen yang diberikan.
            self.assertIn("memori_puncak_kib", rows[0])  # Memanggil self.assertIn untuk menjalankan operasi dengan argumen yang diberikan.


if __name__ == "__main__":  # Menjalankan blok hanya jika __name__ == "__main__".
    unittest.main()  # Memanggil unittest.main untuk menjalankan operasi dengan argumen yang diberikan.
