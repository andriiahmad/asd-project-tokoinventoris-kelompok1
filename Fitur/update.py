"""F4 dan F5: pembaruan atribut stok dan harga produk."""

import math

from Fitur.produk import cari_kode_produk, format_rupiah


def ubah_stok(daftar_produk, kode_produk, stok_baru):
    """Ubah stok; kembalikan (produk, stok_lama) atau None."""
    if type(stok_baru) is not int or stok_baru < 0:
        raise ValueError("Stok harus bilangan bulat tidak negatif.")
    produk = cari_kode_produk(daftar_produk, kode_produk)
    if produk is None:
        return None
    stok_lama = produk["stok"]
    produk["stok"] = stok_baru
    return produk, stok_lama


def ubah_harga(daftar_produk, kode_produk, harga_baru):
    """Ubah harga; kembalikan (produk, harga_lama) atau None."""
    if isinstance(harga_baru, bool) or not isinstance(harga_baru, (int, float)):
        raise ValueError("Harga harus berupa angka lebih dari 0.")
    try:
        harga_float = float(harga_baru)
    except OverflowError:
        raise ValueError("Harga harus berupa angka lebih dari 0.")
    if not math.isfinite(harga_float) or harga_float <= 0:
        raise ValueError("Harga harus berupa angka lebih dari 0.")
    produk = cari_kode_produk(daftar_produk, kode_produk)
    if produk is None:
        return None
    harga_lama = produk["harga"]
    produk["harga"] = harga_float
    return produk, harga_lama


def update_stok(daftar_produk):
    kode = input("Kode produk yang diperbarui stoknya: ").strip()
    produk = cari_kode_produk(daftar_produk, kode)
    if produk is None:
        print(f"Produk dengan kode '{kode}' tidak ditemukan.")
        return
    try:
        stok_baru = int(input("Masukkan stok baru: ").strip())
        hasil = ubah_stok(daftar_produk, kode, stok_baru)
    except ValueError as error:
        print(f"Input tidak valid: {error}")
        return
    produk, stok_lama = hasil
    print(f"Stok produk {produk['nama']} berhasil diperbarui: {stok_lama} menjadi {produk['stok']}.")


def update_harga(daftar_produk):
    kode = input("Kode produk yang diperbarui harganya: ").strip()
    produk = cari_kode_produk(daftar_produk, kode)
    if produk is None:
        print(f"Produk dengan kode '{kode}' tidak ditemukan.")
        return
    try:
        harga_baru = float(input("Masukkan harga baru: ").strip())
        hasil = ubah_harga(daftar_produk, kode, harga_baru)
    except ValueError as error:
        print(f"Input tidak valid: {error}")
        return
    produk, harga_lama = hasil
    print(f"Harga produk {produk['nama']} berhasil diperbarui: {format_rupiah(harga_lama)} menjadi {format_rupiah(produk['harga'])}.")
