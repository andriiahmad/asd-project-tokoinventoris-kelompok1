import os
from Fitur.produk import tambah_barang, tampilkan_barang
from Fitur.pencarian import cari_barang
from Fitur.penghapusan import hapus_barang


def bersihkan_terminal():
    os.system("cls" if os.name == "nt" else "clear")


Barang = [
    {
        "kode": "BRG001",
        "nama_barang": "Beras Premium 5 kg",
        "kategori": "Sembako",
        "harga": 75000,
        "stok": 20,
    },
    {
        "kode": "BRG002",
        "nama_barang": "Minyak Goreng 1 L",
        "kategori": "Sembako",
        "harga": 18000,
        "stok": 35,
    },
    {
        "kode": "BRG003",
        "nama_barang": "Gula Pasir 1 kg",
        "kategori": "Sembako",
        "harga": 16000,
        "stok": 25,
    },
    {
        "kode": "BRG004",
        "nama_barang": "Teh Celup 25 kantong",
        "kategori": "Minuman",
        "harga": 12000,
        "stok": 18,
    },
    {
        "kode": "BRG005",
        "nama_barang": "Sabun Mandi",
        "kategori": "Perlengkapan",
        "harga": 5000,
        "stok": 40,
    },
]

lebar = 54

menu = [
    ("1", "Tambah Barang", "Input produk baru"),
    ("2", "Tampilkan Semua Data", "Lihat semua inventaris"),
    ("3", "Cari Data Barang", "Temukan produk"),
    ("4", "Update Data Barang", "Ubah data produk"),
    ("5", "Filter Data Barang", "Saring produk"),
    ("6", "Hapus Data Barang", "Hapus produk"),
    ("0", "Keluar", "Tutup aplikasi"),
]

while True:
    print("+" + "=" * lebar + "+")
    print("|" + "TOKO BORIA".center(lebar) + "|")
    print("|" + "TOKO INVENTARIS".center(lebar) + "|")
    print("+" + "=" * lebar + "+")
    print("|" + "Selamat datang! Kelola stok toko dengan mudah.".center(lebar) + "|")
    print("+" + "=" * lebar + "+")
    print("|" + "MENU UTAMA".center(lebar) + "|")
    print("+" + "-" * lebar + "+")

    for nomor, nama, keterangan in menu:
        label = f"  [{nomor}]  {nama}"
        print("|" + f"{label:<30}{keterangan:>24}" + "|")
    print("+" + "=" * lebar + "+")
    pilihan = input("Masukkan nomor menu pilihan Anda: ")

    bersihkan_terminal()

    if pilihan == "0":
        print("Terima kasih sudah menggunakan Toko Boria.")
        break
    elif pilihan == "1":
        tambah_barang(Barang)
    elif pilihan == "2":
        tampilkan_barang(Barang)
    elif pilihan == "3":
        cari_barang(Barang)
    elif pilihan == "6":
        hapus_barang(Barang)
    else:
        print("Pilihan tidak tersedia. Silakan pilih menu 0 sampai 6.")

    input("\nTekan Enter untuk kembali ke menu...")
