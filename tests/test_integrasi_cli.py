"""Uji integrasi alur menu 1 sampai 6 di entry point main()."""

import contextlib
import io
import unittest
from unittest.mock import patch

import main as aplikasi


class TestIntegrasiCLI(unittest.TestCase):
    def test_alur_seluruh_menu(self):
        barang = [dict(produk) for produk in aplikasi.Barang]
        masukan = [
            "1", "Susu UHT", "Minuman", "12000", "7", "",
            "2", "",
            "3", "susu", "",
            "4", "BRG006", "9", "",
            "5", "BRG006", "15000.5", "",
            "6", "BRG006", "y", "",
            "0",
        ]
        with patch.object(aplikasi, "Barang", barang), \
             patch.object(aplikasi, "bersihkan_terminal"), \
             patch("builtins.input", side_effect=masukan), \
             contextlib.redirect_stdout(io.StringIO()) as output:
            aplikasi.main()

        tulisan = output.getvalue()
        self.assertIn("BRG006", tulisan)
        self.assertIn("Ditemukan 1 barang", tulisan)
        self.assertIn("Stok berhasil diperbarui: 7 -> 9", tulisan)
        self.assertIn("Rp15.000,50", tulisan)
        self.assertIn("Barang berhasil dihapus", tulisan)
        self.assertIn("Terima kasih", tulisan)
        self.assertEqual(len(barang), 5)

    def test_pilihan_menu_invalid(self):
        with patch.object(aplikasi, "bersihkan_terminal"), \
             patch("builtins.input", side_effect=["x", "", "0"]), \
             contextlib.redirect_stdout(io.StringIO()) as output:
            aplikasi.main()
        self.assertIn("Pilihan tidak tersedia", output.getvalue())


if __name__ == "__main__":
    unittest.main()
