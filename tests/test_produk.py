"""Pengujian F1/F2, validasi input, dan konsistensi format."""

import contextlib
import io
import unittest
from unittest.mock import patch

from Fitur.produk import buat_kode_barang, format_rupiah, tambah_barang, tampilkan_barang


class TestProduk(unittest.TestCase):
    def setUp(self):
        self.barang = [
            {"kode": "BRG001", "nama_barang": "Beras", "kategori": "Sembako", "harga": 75000, "stok": 20},
            {"kode": "BRG002", "nama_barang": "Minyak", "kategori": "Sembako", "harga": 18000, "stok": 35},
        ]

    def test_kode_berurutan(self):
        self.assertEqual(buat_kode_barang(self.barang), "BRG003")

    def test_kode_barang_kosong(self):
        self.assertEqual(buat_kode_barang([]), "BRG001")

    def test_kode_setelah_999(self):
        self.assertEqual(buat_kode_barang([{"kode": "BRG999"}]), "BRG1000")

    def test_kode_tidak_mengulang_kode_terakhir_yang_ada(self):
        self.assertEqual(buat_kode_barang([{"kode": "BRG001"}, {"kode": "BRG003"}]), "BRG004")

    def test_format_rupiah_bulat(self):
        self.assertEqual(format_rupiah(12345), "Rp12.345")

    def test_format_rupiah_angka_sangat_besar(self):
        self.assertEqual(format_rupiah(10 ** 100), "Rp" + f"{10 ** 100:,}".replace(",", "."))

    def test_format_rupiah_desimal(self):
        self.assertEqual(format_rupiah(12345.5), "Rp12.345,50")

    def test_tampil_barang_kosong(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            tampilkan_barang([])
        self.assertIn("Belum ada data barang", output.getvalue())

    def test_tampil_barang_berisi(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            tampilkan_barang(self.barang)
        self.assertIn("Rp75.000", output.getvalue())
        self.assertIn("BRG002", output.getvalue())

    @patch("builtins.input", side_effect=["Roti", "Makanan", "12000", "0"])
    def test_tambah_barang(self, _mock):
        with contextlib.redirect_stdout(io.StringIO()):
            tambah_barang(self.barang)
        self.assertEqual(self.barang[-1]["kode"], "BRG003")
        self.assertEqual(self.barang[-1]["stok"], 0)

    @patch("builtins.input", side_effect=["", " Teh ", "", "Minuman", "0", "-1", "12a", "10000", "-2", "x", "8"])
    def test_validasi_input_tambah(self, _mock):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            tambah_barang(self.barang)
        self.assertEqual(self.barang[-1]["nama_barang"], "Teh")
        self.assertEqual(self.barang[-1]["harga"], 10000)
        self.assertEqual(self.barang[-1]["stok"], 8)
        self.assertIn("tidak boleh kosong", output.getvalue())


if __name__ == "__main__":
    unittest.main()
