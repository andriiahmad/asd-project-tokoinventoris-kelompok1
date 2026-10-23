# Sistem Manajemen Toko Inventori — Toko Boria

Proyek UTS Algoritma dan Struktur Data: sistem inventori toko berbasis **Python CLI**, menggunakan **array of struct** yang direpresentasikan sebagai **`list of dict`**. Data disimpan **in-memory** (tanpa database); perubahan data akan hilang setelah aplikasi ditutup.

## Persyaratan

- Python **3.8+**
- Git (hanya untuk clone/pull/push)
- Tanpa dependensi pihak ketiga atau `pip install`

## Menjalankan program

```bash
git clone https://github.com/andriiahmad/uts-toko-inventoris.git
cd uts-toko-inventoris
python main.py
```

Jika Windows tidak mengenali `python`, gunakan `py main.py`. Jika sudah pernah clone, jalankan `git pull origin main` dari direktori proyek untuk memperoleh perubahan terbaru.

## Menu & fitur

| Menu | Fitur | Implementasi |
|---|---|---|
| 1 | Tambah barang (F1) | Validasi nama, kategori, harga, stok, dan kode unik |
| 2 | Tampilkan semua data (F2) | Tabel inventori + format rupiah |
| 3 | Cari barang (F3) | Linear search berdasarkan kode/sebagian nama, tanpa membedakan kapital |
| 4 | Update stok (F4) | Cari berdasarkan kode, stok bilangan bulat >= 0 |
| 5 | Update harga (F5) | Cari berdasarkan kode, harga > 0 |
| 6 | Hapus barang (F6) | Cari berdasarkan kode tepat dan konfirmasi `y` |
| 0 | Keluar | Mengakhiri aplikasi |

### Model data

Contoh item pada satu list bersama `Barang`:

```python
{
    "kode": "BRG001",
    "nama_barang": "Beras Premium 5 kg",
    "kategori": "Sembako",
    "harga": 75000,
    "stok": 20
}
```

Kode baru dibuat berurutan berdasarkan **nomor terbesar yang masih tersimpan**: `BRG001`, `BRG002`, ... `BRG1000`. Lebar minimal tiga digit; nomor yang sudah dihapus tidak otomatis digunakan kembali. Harga tampil sebagai rupiah dengan pemisah ribuan Indonesia, misalnya `Rp75.000` atau `Rp12.345,50`.

**Catatan input harga:** F1 menerima rupiah bilangan bulat. F5 juga menerima nilai desimal dengan tanda titik (contoh `12345.50`), dibulatkan ke dua angka desimal. Masukkan angka tanpa simbol `Rp` dan tanpa pemisah ribuan.

## Struktur repository

```text
uts-toko-inventoris/
├── .github/workflows/tests.yml  # Otomasi pengujian
├── .gitignore
├── Fitur/
│   ├── pencarian.py             # F3
│   ├── penghapusan.py           # F6
│   ├── produk.py                # F1–F2
│   └── update.py                # F4–F5
├── docs/
│   └── anggota_2.md
├── tests/
│   ├── test_integrasi_cli.py
│   ├── test_pencarian_penghapusan.py
│   ├── test_produk.py
│   └── test_update.py
├── main.py                      # Entry point / menu CLI
└── README.md
```

## Pengujian

Dari direktori root repository:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Pengujian mencakup F1–F6, kondisi data kosong, input tidak valid, kode unik, pencarian tanpa membedakan kapital, penghapusan dengan/batal konfirmasi, format rupiah, serta simulasi end-to-end CLI. Workflow GitHub Actions menjalankan rangkaian tes otomatis untuk Python 3.8 dan 3.13 pada push ke `main` atau pull request.

## Anggota kelompok

| Nama | NIM | Tanggung jawab |
|---|---|---|
| Andri Ahmad Iksan Ramadhani | 25083000012 | Anggota 1 — F1 & F2 |
| Excel Bilqissiano | 25083000016 | Anggota 2 — F3 & F6 |
| Wijaya Eka Saputra | 25083000019 | Anggota 3 — F4, F5 & integrasi CLI |

## Batasan

- Aplikasi adalah CLI untuk kebutuhan pembelajaran, **bukan** sistem produksi.
- Data tidak disimpan secara permanen dan akan kembali ke data awal setelah program dijalankan ulang.
- Menggunakan **Python Standard Library saja**.
- File `.pyc` dan `__pycache__` merupakan cache hasil eksekusi, bukan source code, sehingga diabaikan oleh Git.
