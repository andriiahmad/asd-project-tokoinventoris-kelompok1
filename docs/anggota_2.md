# Dokumentasi Anggota 2 — F3 dan F6

Mengacu pada **Brief Project Tema 1 — Tahap 1 (Array & Struct)**, halaman 8–9.

## F3 — Cari Produk

File: `Fitur/pencarian.py`.

- Operator memilih mode **kode** (1) atau **nama** (2), kemudian mengetik kata kunci.
- Pencarian **kode** memakai perbandingan **exact match** (`kode_produk`), maksimal satu hasil.
- Pencarian **nama** memakai **partial match** (`nama`), dapat menghasilkan banyak produk.
- Kedua mode mengabaikan perbedaan kapital. Kata kunci kosong ditolak.
- Hasil ditampilkan dengan `tampilkan_produk` (format tabel sama seperti F2), plus jumlah hasil.
- Jika tidak ditemukan, tampilkan `Produk dengan [kode/nama] '[kata kunci]' tidak ditemukan.`

## F6 — Hapus Produk

File: `Fitur/penghapusan.py`.

- Operator memasukkan kode produk lengkap.
- Jika ditemukan, program menampilkan **nama produk** sebelum meminta `y/n`.
- Jawaban `y` menghapus produk dari list. Jawaban lain membatalkan penghapusan.
- Jika tidak ditemukan, program menampilkan `Produk dengan kode '[kode]' tidak ditemukan.`
- Hapus hanya mengubah data **in-memory**.

## Struktur data wajib

Setiap item berupa dictionary dengan key `kode_produk`, `nama`, `kategori`, `harga`, `stok`. Jangan mengganti key dengan `kode` atau `nama_barang` karena lima key tersebut wajib sesuai brief halaman 5.

## Pengujian

Jalankan seluruh unit test dari root proyek:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Test F3/F6 berada di `tests/test_pencarian_penghapusan.py`, termasuk exact-match kode, partial-match nama, mode invalid, kata kunci kosong, hasil tidak ditemukan, penghapusan berhasil, dan penghapusan dibatalkan.
