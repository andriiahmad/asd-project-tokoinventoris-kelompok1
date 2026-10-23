"""Entry point CLI proyek semester Tahap 1 (Array of Struct)."""

import os
import sys

from Fitur.pencarian import cari_barang
from Fitur.penghapusan import hapus_barang
from Fitur.produk import tambah_produk, tampilkan_produk
from Fitur.update import update_harga, update_stok

# Seluruh produk disimpan dalam satu list; tidak ada database/file penyimpanan.
daftar_produk = []

MENU = [
    ("1", "Tambah Produk"),
    ("2", "Tampilkan Semua Produk"),
    ("3", "Cari Produk"),
    ("4", "Update Stok Produk"),
    ("5", "Update Harga Produk"),
    ("6", "Hapus Produk"),
    ("0", "Keluar"),
]


def bersihkan_terminal():
    if sys.stdout.isatty() and (os.name == "nt" or os.environ.get("TERM")):
        os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        print("\n=== TOKO BORIA — SISTEM MANAJEMEN INVENTORI ===")
        for nomor, nama in MENU:
            print(f"[{nomor}] {nama}")
        pilihan = input("Pilih menu: ").strip()
        bersihkan_terminal()
        if pilihan == "0":
            print("Terima kasih telah menggunakan sistem inventori.")
            break
        elif pilihan == "1":
            tambah_produk(daftar_produk)
        elif pilihan == "2":
            tampilkan_produk(daftar_produk)
        elif pilihan == "3":
            cari_barang(daftar_produk)
        elif pilihan == "4":
            update_stok(daftar_produk)
        elif pilihan == "5":
            update_harga(daftar_produk)
        elif pilihan == "6":
            hapus_barang(daftar_produk)
        else:
            print("Pilihan tidak tersedia. Masukkan 0 sampai 6.")
        input("\nTekan Enter untuk kembali ke menu...")


if __name__ == "__main__":
    main()
