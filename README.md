# Sistem Manajemen Toko / Inventori — Toko Boria

Proyek semester Algoritma dan Struktur Data, **Tema 1 / Tahap 1 (Array & Struct)**. Aplikasi ini membantu operator toko mengelola produk melalui Command Line Interface (CLI) Python menggunakan **Array of Struct** yang direpresentasikan sebagai satu `list of dict`. Tidak ada database atau penyimpanan file: data akan hilang saat aplikasi berhenti.

## Anggota kelompok dan pembagian tugas

| Anggota | NIM | Tanggung jawab |
|---|---|---|
| Andri Ahmad Iksan Ramadhani | 25083000012 | Anggota 1 — F1 Tambah Produk dan F2 Tampilkan Produk |
| Excel Bilqissiano | 25083000016 | Anggota 2 — F3 Cari Produk dan F6 Hapus Produk |
| Wijaya Eka Saputra | 25083000019 | Anggota 3 — F4 Update Stok, F5 Update Harga, integrasi CLI |

## Cara menjalankan

Persyaratan: **Python 3.8+** dan Git untuk mengunduh repository (tidak memerlukan `pip install`).

```bash
git clone https://github.com/andriiahmad/asd-project-tokoinventoris-kelompok1.git
cd asd-project-tokoinventoris-kelompok1
python main.py
```

Di Windows dapat memakai `py main.py` jika perintah `python` tidak tersedia. Jika repository sudah pernah di-clone, gunakan `git pull origin main` di folder proyek untuk memperbarui kode.

## Fitur Tahap 1

| Menu | Fitur | Deskripsi |
|---|---|---|
| 1 | F1 — Tambah Produk | Input `kode_produk`, `nama`, `kategori`, `harga`, `stok`. Kode unik dan wajib diinput operator. Validasi semua input. |
| 2 | F2 — Tampilkan Semua Produk | Tabel dengan kolom **No, Kode, Nama, Kategori, Harga, Stok**; pesan khusus jika data kosong. |
| 3 | F3 — Cari Produk | Pilih mode **kode** (exact match) atau **nama** (partial match); tampilkan detail dan jumlah hasil. |
| 4 | F4 — Update Stok | Ganti nilai stok produk berdasarkan kode; stok bilangan bulat dan tidak negatif. |
| 5 | F5 — Update Harga | Ganti harga produk berdasarkan kode; harga numerik lebih dari nol. |
| 6 | F6 — Hapus Produk | Cari berdasarkan kode, tampilkan nama, minta konfirmasi `y/n` sebelum menghapus. |
| 0 | Keluar | Mengakhiri aplikasi. |

### Struktur data

Setiap produk memiliki **lima nama atribut wajib** sebagaimana ditulis di brief halaman 5:

```python
produk = {
    "kode_produk": "PRD001",  # str, unik dan tidak kosong; format kode bebas
    "nama": "Minyak Goreng 1L",  # str, tidak kosong
    "kategori": "Sembako",    # str, tidak kosong
    "harga": 15000.0,         # float, > 0
    "stok": 50,              # int, >= 0
}

daftar_produk = [produk]     # list of dict
```

Kode produk **diinput manual**, bukan dibuat otomatis. Produk baru disimpan ke `daftar_produk` saat aplikasi dijalankan. Ketika program ditutup, data tidak tersimpan. Harga ditampilkan dalam rupiah, misalnya `Rp 15.000,00`; saat input harga, ketik angka saja, misalnya `15000` atau `15000.5`.

## Struktur file

```text
asd-project-tokoinventoris-kelompok1/
├── main.py
├── Fitur/
│   ├── produk.py                 # F1, F2, format tabel
│   ├── pencarian.py              # F3
│   ├── update.py                 # F4, F5
│   └── penghapusan.py            # F6
├── tests/
│   ├── test_produk.py
│   ├── test_pencarian_penghapusan.py
│   ├── test_update.py
│   └── test_integrasi_cli.py
├── docs/
│   └── anggota_2.md
├── .github/workflows/tests.yml
├── .gitignore
└── README.md
```

## Pengujian

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Unit test memeriksa validasi F1, seluruh kolom F2, kode exact/nama partial F3, perubahan stok dan harga F4/F5, konfirmasi F6, serta alur CLI terintegrasi. GitHub Actions menjalankan unit test pada push/PR.

## Catatan untuk checkpoint UTS

- Nama repository saat ini: `asd-project-tokoinventoris-kelompok1`, mengikuti pola `asd-project-[tema]-[nama kelompok]`.
- Semua anggota harus berstatus collaborator dan memiliki commit dari akun GitHub masing-masing. Verifikasi melalui pengaturan repository dan daftar kontribusi.
- Riwayat commit asli harus menunjukkan progres bertahap; jangan memalsukan atau mengubah tanggal commit.
- Fokus tahap ini adalah enam fitur Array of Struct. Linked List, Stack, Queue, Tree, dan Sorting dikerjakan pada tahap selanjutnya sesuai addendum dosen.
