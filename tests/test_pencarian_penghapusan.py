"""Pengujian F3/F6 sesuai pilihan mode dan konfirmasi."""
import contextlib
import io
import unittest
from unittest.mock import patch

from Fitur.pencarian import cari_produk, cari_barang
from Fitur.penghapusan import hapus_produk, hapus_barang


class TestCariHapus(unittest.TestCase):
    def setUp(self):
        self.produk = [
            {"kode_produk": "PRD001", "nama": "Minyak Goreng", "kategori": "Sembako", "harga": 15000.0, "stok": 10},
            {"kode_produk": "PRD002", "nama": "Kacang Goreng", "kategori": "Makanan", "harga": 5000.0, "stok": 5},
            {"kode_produk": "PRD003", "nama": "Sabun", "kategori": "Perlengkapan", "harga": 4000.0, "stok": 2},
        ]

    def test_pencarian_kode_exact(self):
        self.assertEqual(cari_produk(self.produk, "kode", "prd001"), [self.produk[0]])
        self.assertEqual(cari_produk(self.produk, "kode", "PRD00"), [])

    def test_pencarian_nama_partial(self):
        self.assertEqual(len(cari_produk(self.produk, "nama", "GORENG")), 2)

    def test_kata_kunci_kosong(self):
        self.assertEqual(cari_produk(self.produk, "nama", " "), [])

    def test_data_kosong(self):
        self.assertEqual(cari_produk([], "kode", "PRD001"), [])

    @patch("builtins.input", side_effect=["1", "PRD001"])
    def test_cli_mode_kode(self, _):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            cari_barang(self.produk)
        self.assertIn("Ditemukan 1 produk.", out.getvalue())

    @patch("builtins.input", side_effect=["2", "goreng"])
    def test_cli_mode_nama(self, _):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            cari_barang(self.produk)
        self.assertIn("Ditemukan 2 produk.", out.getvalue())

    @patch("builtins.input", side_effect=["1", "PRD00"])
    def test_pesan_tidak_ditemukan(self, _):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            cari_barang(self.produk)
        self.assertIn("Produk dengan kode 'PRD00' tidak ditemukan.", out.getvalue())

    @patch("builtins.input", return_value="3")
    def test_mode_tidak_valid(self, _):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            cari_barang(self.produk)
        self.assertIn("Mode pencarian tidak valid", out.getvalue())

    def test_hapus_berdasarkan_kode(self):
        self.assertEqual(hapus_produk(self.produk, "prd003")["nama"], "Sabun")
        self.assertEqual(len(self.produk), 2)

    def test_hapus_tidak_ditemukan(self):
        self.assertIsNone(hapus_produk(self.produk, "PRD00"))
        self.assertEqual(len(self.produk), 3)

    @patch("builtins.input", side_effect=["PRD001", "n"])
    def test_batal_hapus(self, _):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            hapus_barang(self.produk)
        self.assertIn("Penghapusan dibatalkan.", out.getvalue())
        self.assertEqual(len(self.produk), 3)

    @patch("builtins.input", side_effect=["PRD001", "y"])
    def test_konfirmasi_hapus(self, _):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            hapus_barang(self.produk)
        self.assertIn("Produk Minyak Goreng berhasil dihapus dari sistem.", out.getvalue())
        self.assertEqual(len(self.produk), 2)


if __name__ == "__main__":
    unittest.main()
