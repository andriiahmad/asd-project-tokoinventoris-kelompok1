import unittest

from Fitur.update import ubah_harga, ubah_stok


class TestUpdateBarang(unittest.TestCase):
    def setUp(self):
        self.barang = [
            {"kode": "BRG001", "nama_barang": "Beras", "kategori": "Sembako", "harga": 75000, "stok": 20}
        ]

    def test_stok_berubah(self):
        self.assertEqual(ubah_stok(self.barang, "BRG001", 8), (20, 8))
        self.assertEqual(self.barang[0]["stok"], 8)

    def test_stok_nol_diizinkan(self):
        ubah_stok(self.barang, "BRG001", 0)
        self.assertEqual(self.barang[0]["stok"], 0)

    def test_stok_negatif_ditolak(self):
        with self.assertRaises(ValueError):
            ubah_stok(self.barang, "BRG001", -2)

    def test_stok_desimal_ditolak(self):
        with self.assertRaises(ValueError):
            ubah_stok(self.barang, "BRG001", 2.5)

    def test_harga_berubah(self):
        self.assertEqual(ubah_harga(self.barang, "brg001", 85000), (75000, 85000))
        self.assertEqual(self.barang[0]["harga"], 85000)

    def test_harga_nol_ditolak(self):
        with self.assertRaises(ValueError):
            ubah_harga(self.barang, "BRG001", 0)

    def test_harga_nan_ditolak(self):
        with self.assertRaises(ValueError):
            ubah_harga(self.barang, "BRG001", float("nan"))

    def test_kode_tidak_ada(self):
        self.assertIsNone(ubah_stok(self.barang, "BRG999", 5))
        self.assertEqual(self.barang[0]["stok"], 20)


if __name__ == "__main__":
    unittest.main()
