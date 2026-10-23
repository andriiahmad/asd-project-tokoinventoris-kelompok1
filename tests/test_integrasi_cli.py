"""Skenario end-to-end: buat, tampil, cari, update, hapus, keluar."""
import contextlib
import io
import unittest
from unittest.mock import patch

import main as aplikasi


class TestCLI(unittest.TestCase):
    def test_semua_menu(self):
        daftar = []
        urutan = [
            "2", "",  # belum ada produk
            "1", "PRD001", "Minyak Goreng", "Sembako", "15000", "8", "",
            "2", "",
            "3", "1", "PRD001", "",
            "3", "2", "goreng", "",
            "4", "PRD001", "10", "",
            "5", "PRD001", "15500.5", "",
            "6", "PRD001", "n", "",
            "6", "PRD001", "y", "",
            "0",
        ]
        with patch.object(aplikasi, "daftar_produk", daftar), \
             patch.object(aplikasi, "bersihkan_terminal"), \
             patch("builtins.input", side_effect=urutan), \
             contextlib.redirect_stdout(io.StringIO()) as out:
            aplikasi.main()
        teks = out.getvalue()
        self.assertIn("Belum ada produk yang tersimpan.", teks)
        self.assertIn("Produk Minyak Goreng berhasil ditambahkan.", teks)
        self.assertIn("Ditemukan 1 produk.", teks)
        self.assertIn("Stok produk Minyak Goreng berhasil diperbarui: 8 menjadi 10", teks)
        self.assertIn("Rp 15.500,50", teks)
        self.assertIn("Penghapusan dibatalkan.", teks)
        self.assertIn("Produk Minyak Goreng berhasil dihapus dari sistem.", teks)
        self.assertEqual(daftar, [])

    def test_pilihan_menu_tidak_valid(self):
        with patch.object(aplikasi, "daftar_produk", []), \
             patch.object(aplikasi, "bersihkan_terminal"), \
             patch("builtins.input", side_effect=["99", "", "0"]), \
             contextlib.redirect_stdout(io.StringIO()) as out:
            aplikasi.main()
        self.assertIn("Pilihan tidak tersedia", out.getvalue())


if __name__ == "__main__":
    unittest.main()
