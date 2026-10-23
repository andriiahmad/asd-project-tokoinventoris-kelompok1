# Toko Inventoris

Sistem manajemen inventaris toko sederhana berbasis CLI dengan Python. Aplikasi ini memungkinkan pengguna menambah, menampilkan, mencari, memperbarui stok/harga, dan menghapus data barang secara in-memory.

## Persyaratan
- Python 3.8+

## Cara Menjalankan
1. Clone repository ini.
2. Buka terminal di folder proyek.
3. Jalankan:

```bash
python main.py
```

## Fitur
- F1: Tambah barang
- F2: Tampilkan semua data
- F3: Cari data barang berdasarkan kode atau sebagian nama
- F4: Update stok barang
- F5: Update harga barang
- F6: Hapus barang dengan konfirmasi
- F0: Keluar aplikasi

### Aturan validasi
- Kode barang unik dan ditampilkan dalam format `BRG###`.
- Nama barang dan kategori tidak boleh kosong.
- Harga harus bernilai numerik dan lebih dari 0.
- Stok harus bilangan bulat dan tidak boleh negatif.
- Penghapusan memerlukan konfirmasi `y`.

## Struktur Folder
```text
uts-toko-inventoris/
├── Fitur/
│   ├── pencarian.py
│   ├── penghapusan.py
│   ├── produk.py
│   └── update.py
├── tests/
│   ├── test_pencarian_penghapusan.py
│   └── test_update.py
├── main.py
├── README.md
├── .gitignore
└── docs/
    └── anggota_2.md
```

## Data Kelompok
| Nama | NIM | Tugas |
|---|---:|---|
| Andri Ahmad Iksan Ramadhani | 25083000012 | Anggota 1 / F1-F2 |
| Excel Bilqissiano | 25083000016 | Anggota 2 / F3-F6 |
| Wijaya Eka Saputra | 25083000019 | Anggota 3 / F4-F5 dan integrasi CLI |

## Cara Menjalankan Pengujian
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Batasan
- Data disimpan di memori (in-memory) dan akan hilang setelah program ditutup.
- Tidak menggunakan database atau dependency eksternal.

