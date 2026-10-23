"""F3: pencarian barang menggunakan linear search."""

from Fitur.produk import tampilkan_barang


def cari_produk(barang, kata_kunci):
    """Kembalikan semua produk dengan kode/nama yang cocok (case-insensitive)."""
    kata_kunci = kata_kunci.strip().casefold()
    if not kata_kunci:
        return []
    return [
        produk for produk in barang
        if kata_kunci in produk["kode"].casefold()
        or kata_kunci in produk["nama_barang"].casefold()
    ]


def cari_barang(barang):
    """Antarmuka CLI pencarian produk."""
    kata_kunci = input("Masukkan kode atau nama barang: ").strip()
    if not kata_kunci:
        print("Kata kunci tidak boleh kosong.")
        return
    hasil = cari_produk(barang, kata_kunci)
    if not hasil:
        print("Barang tidak ditemukan.")
        return
    print(f"Ditemukan {len(hasil)} barang:")
    tampilkan_barang(hasil)
