"""F6: hapus produk menggunakan kode unik dengan konfirmasi."""

from Fitur.produk import cari_kode_produk


def hapus_produk(daftar_produk, kode_produk):
    """Hapus berdasarkan kode tepat; kembalikan produk yang dihapus atau None."""
    produk = cari_kode_produk(daftar_produk, kode_produk)
    if produk is None:
        return None
    daftar_produk.remove(produk)
    return produk


def hapus_barang(daftar_produk):
    kode = input("Masukkan kode produk yang akan dihapus: ").strip()
    if not kode:
        print("Kode produk tidak boleh kosong.")
        return
    produk = cari_kode_produk(daftar_produk, kode)
    if produk is None:
        print(f"Produk dengan kode '{kode}' tidak ditemukan.")
        return
    print(f"Produk yang akan dihapus: {produk['nama']} ({produk['kode_produk']})")
    konfirmasi = input("Yakin ingin menghapus? (y/n): ").strip().casefold()
    if konfirmasi != "y":
        print("Penghapusan dibatalkan.")
        return
    hapus_produk(daftar_produk, kode)
    print(f"Produk {produk['nama']} berhasil dihapus dari sistem.")
