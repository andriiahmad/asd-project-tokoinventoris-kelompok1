# Anggota 2 — F3 Cari Barang dan F6 Hapus Barang

## Lingkup
- F3: Linear search terhadap `list of dict` berdasarkan kode atau sebagian nama (tanpa membedakan huruf besar/kecil).
- F6: Hapus berdasarkan kode produk unik; CLI menampilkan data dan meminta konfirmasi `y` sebelum menghapus.
- Seluruh perubahan bersifat in-memory. Tidak ada database maupun dependensi eksternal.

## Struktur data
Produk memakai kunci `kode`, `nama_barang`, `kategori`, `harga`, `stok` sesuai `main.py`.

## Penggunaan
Dari folder root:

```bash
python main.py
```

Pilih menu 3 untuk cari, atau menu 6 untuk hapus. Pencarian nama bisa menghasilkan beberapa produk, sedangkan penghapusan memerlukan kode yang tepat. Jawaban selain `y` membatalkan penghapusan.

## Pengujian
```bash
python -m unittest discover -s tests -v
```

Pengujian meliputi pencarian berdasarkan kode/nama, input kosong, data tidak ditemukan, penghapusan, dan konfirmasi/batal pada CLI.
