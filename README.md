# Pembagian Tugas Kelompok — Sistem Manajemen Toko / Inventori

**Mata kuliah:** Algoritma dan Struktur Data  
**Tema:** 1 — Sistem Manajemen Toko / Inventori  
**Jumlah anggota:** 3 orang  
**Bahasa:** Python 3.8+  
**Antarmuka:** CLI (terminal)  
**Tahap saat ini:** Tahap 1 — Array & Struct (*list of dict*)

## Anggota Kelompok

| No. | Nama | NIM | Peran |
| --- | --- | --- | --- |
| 1 | [ Wijaya Eka Saputra ] | [25083000019] | Fondasi dan Data Produk |
| 2 | [Nama Anggota 2] | [NIM 2] | Pencarian dan Penghapusan |
| 3 | [Nama Anggota 3] | [NIM 3] | Pembaruan dan Integrasi CLI |

## Pembagian Tugas Tahap 1 (UTS)

### Anggota 1 — Fondasi Sistem & Manajemen Data Produk

**Fitur wajib:** F1 (Tambah Produk Baru) dan F2 (Tampilkan Semua Produk).  
**File utama:** `produk.py`.

- [ ] Membuat penyimpanan data **Array of Struct**, yaitu `list` yang memuat `dict` produk.
- [ ] Menetapkan lima atribut wajib: `kode_produk` (`str`), `nama` (`str`), `kategori` (`str`), `harga` (`float`), dan `stok` (`int`).
- [ ] Mengimplementasikan **F1 — Tambah Produk Baru** dengan validasi:
  - Kode tidak kosong dan unik/tidak duplikat.
  - Nama dan kategori tidak kosong.
  - Harga merupakan angka dan lebih dari 0.
  - Stok merupakan bilangan bulat dan tidak negatif.
- [ ] Mengimplementasikan **F2 — Tampilkan Semua Produk** dalam tabel berkolom No, Kode, Nama, Kategori, Harga, dan Stok.
- [ ] Menangani kasus daftar kosong dengan pesan yang jelas.
- [ ] Menyediakan fungsi bantu untuk akses data produk yang bisa digunakan modul lain.
- [ ] Mengisi bagian deskripsi dan model data di `README.md`.

### Anggota 2 — Pencarian & Penghapusan Produk

**Fitur wajib:** F3 (Cari Produk) dan F6 (Hapus Produk).  
**File utama:** `pencarian.py` dan `hapus.py`.

- [ ] Mengimplementasikan **F3 — Cari Produk**:
  - Cari berdasarkan kode produk dengan **exact match**.
  - Cari berdasarkan nama dengan **partial match** dan tampilkan semua kecocokan.
  - Validasi kata kunci tidak kosong.
  - Tampilkan jumlah hasil atau pesan jika produk tidak ditemukan.
- [ ] Mengimplementasikan **F6 — Hapus Produk**:
  - Cari produk dari kode yang dimasukkan.
  - Tampilkan nama produk sebelum penghapusan.
  - Minta konfirmasi `y/n`; jangan hapus jika dibatalkan.
  - Tampilkan pesan untuk kode yang tidak ditemukan.
- [ ] Menguji kasus tepi: pencarian kosong, banyak hasil, kode tidak ditemukan, dan pembatalan hapus.
- [ ] Mengisi daftar fitur dan skenario pengujian di `README.md`.

### Anggota 3 — Pembaruan Produk & Integrasi Sistem

**Fitur wajib:** F4 (Update Stok Produk) dan F5 (Update Harga Produk).  
**File utama:** `update.py` dan `main.py`.

- [ ] Mengimplementasikan **F4 — Update Stok Produk**:
  - Cari produk berdasarkan kode yang sudah ada.
  - **Ganti** stok dengan nilai baru (bukan menambahkan stok).
  - Validasi bilangan bulat dan tidak negatif.
  - Tampilkan nilai stok lama dan nilai stok baru.
- [ ] Mengimplementasikan **F5 — Update Harga Produk**:
  - Cari produk berdasarkan kode yang sudah ada.
  - Validasi harga baru berupa angka dan lebih dari 0.
  - Tampilkan harga lama dan harga baru.
- [ ] Membuat menu CLI pada `main.py` untuk seluruh fitur F1–F6 dan opsi keluar.
- [ ] Mengintegrasikan modul agar berbagi **daftar produk yang sama**, bukan salinan data terpisah.
- [ ] Memastikan aplikasi bisa dijalankan dengan `python main.py`.
- [ ] Mengisi cara menjalankan dan pembagian tugas di `README.md`.

## Tanggung Jawab Bersama

- [ ] Membuat repository GitHub sesuai format `asd-project-[tema]-[nama kelompok]`.
- [ ] Mendaftarkan ketiga anggota sebagai collaborator.
- [ ] Melakukan pengujian seluruh fitur F1–F6, validasi input, dan integrasi antarmodul.
- [ ] Mereview kode agar modular, nama fungsi/variabel deskriptif, dan tidak banyak duplikasi.
- [ ] Melengkapi `README.md` dengan nama/NIM anggota, deskripsi sistem, cara menjalankan, fitur, dan pembagian tugas.
- [ ] **Setiap anggota melakukan commit dengan akun GitHub masing-masing**, dengan pesan deskriptif dan secara bertahap.
- [ ] Memastikan tidak memakai library eksternal atau database untuk Tahap 1. Data cukup disimpan dalam memori selama program berjalan.

## Struktur Folder yang Disarankan

> Ini merupakan rancangan pembagian file, bukan struktur yang diwajibkan dosen. File dapat disesuaikan saat integrasi.

```text
asd-project-toko-kelompok1/
├── main.py          # Anggota 3: menu utama dan integrasi
├── produk.py        # Anggota 1: data produk, tambah, tampilkan
├── pencarian.py     # Anggota 2: pencarian produk
├── hapus.py         # Anggota 2: penghapusan produk
├── update.py        # Anggota 3: update stok dan harga
├── README.md        # Dokumentasi bersama
└── PEMBAGIAN_TUGAS.md
```

**Kontrak antarmodul:** Semua operasi menerima objek `daftar_produk` yang sama agar penambahan, pembaruan, dan penghapusan terlihat konsisten di setiap fitur.

## Rencana Lanjutan Setelah UTS (Tentatif)

| Anggota | Usulan tanggung jawab |
| --- | --- |
| 1 | Linked List (riwayat transaksi) dan Sorting |
| 2 | Stack (undo) dan Tree (kategori produk) |
| 3 | Queue (antrian checkout) dan integrasi antarmodul |

> Pembagian Tahap 2–5 **belum final**. Detailnya mengikuti addendum dosen setelah UTS.

## Ketentuan Penilaian Checkpoint UTS

| Komponen | Bobot |
| --- | ---: |
| Kelengkapan 6 fitur dan validasi | 40% |
| Kualitas kode | 25% |
| Dokumentasi README | 20% |
| Progres bertahap di GitHub | 15% |

**Catatan:** Tanggal checkpoint UTS pada brief adalah **19 Oktober 2026**. Pastikan kembali kepada dosen jika ada jadwal/perpanjangan terbaru.

**Acuan:** *Brief Project Tema 1 — Sistem Manajemen Toko / Inventori*, Tahap 1, bagian Ketentuan Kelompok; Entitas Utama & Atribut; Fitur Wajib; Spesifikasi Teknis; dan Rubrik Penilaian.
