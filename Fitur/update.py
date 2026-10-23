import math

from Fitur.produk import format_rupiah


def cari_dengan_kode(barang, kode):
    """Cari satu produk berdasarkan kode, tanpa membedakan huruf besar/kecil."""
    kode = kode.strip().casefold()
    for produk in barang:
        if produk["kode"].casefold() == kode:
            return produk
    return None


def ubah_stok(barang, kode, stok_baru):
    """Kembalikan (stok_lama, stok_baru), atau None jika kode tidak ada."""
    if isinstance(stok_baru, bool) or not isinstance(stok_baru, int) or stok_baru < 0:
        raise ValueError("Stok harus bilangan bulat tidak negatif.")

    produk = cari_dengan_kode(barang, kode)
    if produk is None:
        return None

    stok_lama = produk["stok"]
    produk["stok"] = stok_baru
    return stok_lama, stok_baru


def ubah_harga(barang, kode, harga_baru):
    """Kembalikan (harga_lama, harga_baru), atau None jika kode tidak ada."""
    if isinstance(harga_baru, bool) or not isinstance(harga_baru, (int, float)):
        raise ValueError("Harga harus berupa angka positif.")

    if isinstance(harga_baru, int):
        nilai = harga_baru
    else:
        nilai = float(harga_baru)
        if not math.isfinite(nilai):
            raise ValueError("Harga harus berupa angka positif yang valid.")
        nilai = round(nilai, 2)
    if nilai <= 0:
        raise ValueError("Harga harus berupa angka positif yang valid.")

    if isinstance(nilai, float) and nilai.is_integer():
        nilai = int(nilai)

    produk = cari_dengan_kode(barang, kode)
    if produk is None:
        return None

    harga_lama = produk["harga"]
    produk["harga"] = nilai
    return harga_lama, nilai


def update_stok(barang):
    kode = input("Masukkan kode barang: ").strip()
    produk = cari_dengan_kode(barang, kode)
    if produk is None:
        print("Barang tidak ditemukan.")
        return

    print(f"Stok saat ini: {produk['stok']}")
    try:
        stok_baru = int(input("Masukkan stok baru: ").strip())
        lama, baru = ubah_stok(barang, kode, stok_baru)
    except ValueError as error:
        print(f"Input tidak valid: {error}")
        return

    print(f"Stok berhasil diperbarui: {lama} -> {baru}.")


def update_harga(barang):
    kode = input("Masukkan kode barang: ").strip()
    produk = cari_dengan_kode(barang, kode)
    if produk is None:
        print("Barang tidak ditemukan.")
        return

    print(f"Harga saat ini: {format_rupiah(produk['harga'])}")
    try:
        harga_baru = float(input("Masukkan harga baru: ").strip())
        lama, baru = ubah_harga(barang, kode, harga_baru)
    except ValueError as error:
        print(f"Input tidak valid: {error}")
        return

    print(f"Harga berhasil diperbarui: {format_rupiah(lama)} -> {format_rupiah(baru)}.")
