"""F6: hapus barang berdasarkan kode unik dengan konfirmasi."""

from Fitur.produk import tampilkan_barang


def hapus_produk(barang, kode):
    """Hapus produk sesuai kode; kembalikan True jika berhasil."""
    kode = kode.strip().casefold()
    if not kode:
        return False
    for index, produk in enumerate(barang):
        if produk["kode"].casefold() == kode:
            barang.pop(index)
            return True
    return False


def hapus_barang(barang):
    """Antarmuka CLI penghapusan dengan konfirmasi."""
    kode = input("Masukkan kode barang yang akan dihapus: ").strip()
    if not kode:
        print("Kode barang tidak boleh kosong.")
        return
    produk = next(
        (item for item in barang if item["kode"].casefold() == kode.casefold()),
        None,
    )
    if produk is None:
        print("Barang tidak ditemukan.")
        return

    tampilkan_barang([produk])
    konfirmasi = input("Yakin ingin menghapus barang ini? (y/n): ").strip().casefold()
    if konfirmasi != "y":
        print("Penghapusan dibatalkan.")
        return

    if hapus_produk(barang, kode):
        print("Barang berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")
