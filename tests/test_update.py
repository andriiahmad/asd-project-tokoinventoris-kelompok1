"""Pengujian F4/F5 menggunakan atribut wajib."""
import contextlib
import io
import unittest
from unittest.mock import patch

from Fitur.update import ubah_harga, ubah_stok, update_harga, update_stok


class TestUpdate(unittest.TestCase):
    def setUp(self):
        self.produk = [{"kode_produk": "PRD001", "nama": "Beras", "kategori": "Sembako", "harga": 75000.0, "stok": 20}]

    def test_update_stok(self):
        produk, lama = ubah_stok(self.produk, "prd001", 0)
        self.assertEqual(lama, 20)
        self.assertEqual(produk["stok"], 0)

    def test_stok_negatif_ditolak(self):
        with self.assertRaises(ValueError):
            ubah_stok(self.produk, "PRD001", -1)

    def test_stok_desimal_ditolak(self):
        with self.assertRaises(ValueError):
            ubah_stok(self.produk, "PRD001", 1.5)

    def test_stok_bool_ditolak(self):
        with self.assertRaises(ValueError):
            ubah_stok(self.produk, "PRD001", True)

    def test_kode_tidak_ditemukan(self):
        self.assertIsNone(ubah_stok(self.produk, "PRD999", 5))
        self.assertIsNone(ubah_harga(self.produk, "PRD999", 10))

    def test_harga_desimal(self):
        produk, lama = ubah_harga(self.produk, "prd001", 85000.75)
        self.assertEqual(lama, 75000.0)
        self.assertEqual(produk["harga"], 85000.75)
        self.assertIsInstance(produk["harga"], float)

    def test_harga_tidak_valid(self):
        for harga in (0, -1, float("nan"), float("inf"), True):
            with self.subTest(harga=harga), self.assertRaises(ValueError):
                ubah_harga(self.produk, "PRD001", harga)

    @patch("builtins.input", side_effect=["PRD001", "9"])
    def test_pesan_update_stok(self, _):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            update_stok(self.produk)
        self.assertIn("Stok produk Beras berhasil diperbarui: 20 menjadi 9", out.getvalue())

    @patch("builtins.input", side_effect=["PRD001", "90000"])
    def test_pesan_update_harga(self, _):
        with contextlib.redirect_stdout(io.StringIO()) as out:
            update_harga(self.produk)
        self.assertIn("Harga produk Beras berhasil diperbarui: Rp 75.000,00 menjadi Rp 90.000,00", out.getvalue())


if __name__ == "__main__":
    unittest.main()
