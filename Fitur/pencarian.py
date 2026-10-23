"""F3: pencarian kode tepat atau nama sebagian (linear search)."""

from Fitur.produk import tampilkan_produk


def cari_produk(daftar_produk, mode, kata_kunci):
    """Hasil berupa list; mode hanya 'kode' atau 'nama'."""
    kunci = kata_kunci.strip().casefold()
    if not kunci or mode not in ("kode", "nama"):
        return []
    if mode == "kode":
        return [p for p in daftar_produk if p["kode_produk"].casefold() == kunci]
    return [p for p in daftar_produk if kunci in p["nama"].casefold()]


def cari_barang(daftar_produk):
    """Tanyakan mode pencarian kemudian tampilkan hasil."""
    print("Mode pencarian: [1] Kode produk  [2] Nama produk")
    pilihan = input("Pilih mode (1/2): ").strip()
    if pilihan not in ("1", "2"):
        print("Mode pencarian tidak valid. Pilih 1 atau 2.")
        return
    mode = "kode" if pilihan == "1" else "nama"
    kata_kunci = input(f"Masukkan {mode} produk: ").strip()
    if not kata_kunci:
        print("Kata kunci tidak boleh kosong.")
        return
    hasil = cari_produk(daftar_produk, mode, kata_kunci)
    if not hasil:
        print(f"Produk dengan {mode} '{kata_kunci}' tidak ditemukan.")
        return
    print(f"Ditemukan {len(hasil)} produk.")
    tampilkan_produk(hasil)
