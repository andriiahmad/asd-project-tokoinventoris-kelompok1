"""Pengujian F1/F2 terhadap spesifikasi brief Tahap 1."""
import contextlib
import io
import unittest
from unittest.mock import patch

from Fitur.produk import tambah_produk, tampilkan_produk, format_rupiah, cari_kode_produk


class TestProduk(unittest.TestCase):
    def setUp(self):
        self.produk = [{"kode_produk": "PRD001", "nama": "Beras", "kategori": "Sembako", "harga": 75000.0, "stok": 20}]

    def test_cari_kode_tepat(self):
        self.assertIs(cari_kode_produk(self.produk, "prd001"), self.produk[0])
        self.assertIsNone(cari_kode_produk(self.produk, "PRD00"))

    @patch("builtins.input", side_effect=["PRD002", "Minyak", "Sembako", "18000.5", "0"])
    def test_tambah_semua_atribut_wajib(self, _):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            tambah_produk(self.produk)
        self.assertEqual(len(self.produk), 2)
        self.assertEqual(set(self.produk[1]), {"kode_produk", "nama", "kategori", "harga", "stok"})
        self.assertEqual(self.produk[1]["harga"], 18000.5)
        self.assertIsInstance(self.produk[1]["harga"], float)
        self.assertEqual(self.produk[1]["stok"], 0)
        self.assertIn("Produk Minyak berhasil ditambahkan.", out.getvalue())

    @patch("builtins.input", side_effect=["", "PRD001", "prd001", "PRD003", "", "Teh", "", "Minuman", "0", "abc", "inf", "15000", "-1", "2.5", "3"])
    def test_validasi_komprehensif(self, _):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            tambah_produk(self.produk)
        self.assertEqual(self.produk[-1]["kode_produk"], "PRD003")
        self.assertEqual(self.produk[-1]["nama"], "Teh")
        self.assertEqual(self.produk[-1]["harga"], 15000.0)
        self.assertEqual(self.produk[-1]["stok"], 3)
        self.assertIn("sudah digunakan", out.getvalue())

    def test_tampilan_kosong(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            tampilkan_produk([])
        self.assertIn("Belum ada produk yang tersimpan.", out.getvalue())

    def test_tabel_6_kolom_dengan_no(self):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            tampilkan_produk(self.produk)
        header = out.getvalue().splitlines()[1]
        for name in ["No", "Kode", "Nama", "Kategori", "Harga", "Stok"]:
            self.assertIn(name, header)
        self.assertIn("Rp 75.000,00", out.getvalue())

    def test_format_rupiah(self):
        self.assertEqual(format_rupiah(12345.5), "Rp 12.345,50")


if __name__ == "__main__":
    unittest.main()
