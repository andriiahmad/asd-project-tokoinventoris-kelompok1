"""Operasi F1 dan F2 menggunakan Array of Struct (list of dict)."""

import math


def cari_kode_produk(daftar_produk, kode_produk):
    """Cari kode unik secara persis tanpa membedakan kapital."""
    kode_normal = kode_produk.strip().casefold()
    for produk in daftar_produk:
        if produk["kode_produk"].casefold() == kode_normal:
            return produk
    return None


def format_rupiah(harga):
    """Tampilkan nilai rupiah dengan dua digit desimal."""
    nilai = f"{harga:,.2f}"
    return "Rp " + nilai.replace(",", "_").replace(".", ",").replace("_", ".")


def tambah_produk(daftar_produk):
    """Minta lima atribut produk; ulangi input hingga valid."""
    while True:
        kode_produk = input("Kode produk: ").strip()
        if not kode_produk:
            print("Kode produk tidak boleh kosong.")
        elif cari_kode_produk(daftar_produk, kode_produk) is not None:
            print("Kode produk sudah digunakan. Masukkan kode lain.")
        else:
            break

    while True:
        nama = input("Nama produk: ").strip()
        if nama:
            break
        print("Nama produk tidak boleh kosong.")

    while True:
        kategori = input("Kategori: ").strip()
        if kategori:
            break
        print("Kategori tidak boleh kosong.")

    while True:
        try:
            harga = float(input("Harga (Rp): ").strip())
            if not math.isfinite(harga) or harga <= 0:
                print("Harga harus berupa angka lebih dari 0.")
                continue
            break
        except ValueError:
            print("Harga harus berupa angka lebih dari 0.")

    while True:
        try:
            stok = int(input("Stok: ").strip())
            if stok < 0:
                print("Stok tidak boleh negatif.")
                continue
            break
        except ValueError:
            print("Stok harus berupa bilangan bulat.")

    daftar_produk.append({
        "kode_produk": kode_produk,
        "nama": nama,
        "kategori": kategori,
        "harga": harga,
        "stok": stok,
    })
    print(f"Produk {nama} berhasil ditambahkan.")


def tampilkan_produk(daftar_produk):
    """Tampilkan tabel No, Kode, Nama, Kategori, Harga, dan Stok."""
    if not daftar_produk:
        print("Belum ada produk yang tersimpan.")
        return

    judul = ["No", "Kode", "Nama", "Kategori", "Harga", "Stok"]
    baris = []
    for nomor, produk in enumerate(daftar_produk, start=1):
        baris.append([
            str(nomor), produk["kode_produk"], produk["nama"],
            produk["kategori"], format_rupiah(produk["harga"]), str(produk["stok"]),
        ])
    lebar = [max(len(judul[i]), *(len(b[i]) for b in baris)) for i in range(len(judul))]
    garis = "+" + "+".join("-" * (x + 2) for x in lebar) + "+"
    print(garis)
    print("|" + "|".join(f" {judul[i]:<{lebar[i]}} " for i in range(len(judul))) + "|")
    print(garis)
    for data in baris:
        print("|" + "|".join(f" {data[i]:<{lebar[i]}} " for i in range(len(judul))) + "|")
    print(garis)
