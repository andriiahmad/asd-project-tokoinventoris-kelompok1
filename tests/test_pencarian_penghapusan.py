"""Unit test F3 dan F6. Jalankan: python -m unittest discover -s tests -v"""

import unittest
from unittest.mock import patch

from Fitur.pencarian import cari_produk, cari_barang
from Fitur.penghapusan import hapus_produk, hapus_barang


class TestCariHapus(unittest.TestCase):
    def setUp(self):
        self.barang = [
            {"kode": "BRG001", "nama_barang": "Beras Premium", "kategori": "Sembako", "harga": 75000, "stok": 20},
            {"kode": "BRG002", "nama_barang": "Beras Merah", "kategori": "Sembako", "harga": 65000, "stok": 10},
            {"kode": "BRG003", "nama_barang": "Sabun Mandi", "kategori": "Perlengkapan", "harga": 5000, "stok": 40},
        ]

    def test_cari_kode(self):
        self.assertEqual(cari_produk(self.barang, "brg001"), [self.barang[0]])

    def test_cari_nama_sebagian(self):
        self.assertEqual(len(cari_produk(self.barang, "BERAS")), 2)

    def test_cari_tidak_ditemukan(self):
        self.assertEqual(cari_produk(self.barang, "kopi"), [])

    def test_cari_kosong(self):
        self.assertEqual(cari_produk(self.barang, "   "), [])

    def test_cari_data_kosong(self):
        self.assertEqual(cari_produk([], "beras"), [])

    def test_hapus_kode(self):
        self.assertTrue(hapus_produk(self.barang, "brg002"))
        self.assertEqual(len(self.barang), 2)
        self.assertFalse(any(p["kode"] == "BRG002" for p in self.barang))

    def test_hapus_tidak_ada(self):
        self.assertFalse(hapus_produk(self.barang, "BRG999"))
        self.assertEqual(len(self.barang), 3)

    def test_hapus_kode_kosong(self):
        self.assertFalse(hapus_produk(self.barang, " "))
        self.assertEqual(len(self.barang), 3)

    @patch("builtins.input", side_effect=["BRG001", "n"])
    def test_batal_hapus(self, _mock):
        hapus_barang(self.barang)
        self.assertEqual(len(self.barang), 3)

    @patch("builtins.input", side_effect=["BRG001", "y"])
    def test_konfirmasi_hapus(self, _mock):
        hapus_barang(self.barang)
        self.assertEqual(len(self.barang), 2)

    @patch("builtins.input", return_value="BERAS")
    def test_cli_cari(self, _mock):
        cari_barang(self.barang)
        self.assertEqual(len(self.barang), 3)


if __name__ == "__main__":
    unittest.main()
