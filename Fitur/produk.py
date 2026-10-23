"""F1/F2: tambah dan tampilkan produk (list of dict)."""


def buat_kode_barang(barang):
    """Buat kode unik berurutan, BRG001 dan seterusnya."""
    nomor_terbesar = 0
    for produk in barang:
        kode = produk["kode"].upper()
        if kode.startswith("BRG") and kode[3:].isdigit():
            nomor_terbesar = max(nomor_terbesar, int(kode[3:]))
    return f"BRG{nomor_terbesar + 1:03d}"


def format_rupiah(nilai):
    """Format rupiah dengan pemisah ribuan dan desimal Indonesia."""
    if isinstance(nilai, int):
        angka = f"{nilai:,}"
    elif isinstance(nilai, float) and not nilai.is_integer():
        angka = f"{nilai:,.2f}"
    else:
        angka = f"{nilai:,.0f}"
    return "Rp" + angka.replace(",", "_").replace(".", ",").replace("_", ".")


def tampilkan_barang(barang):
    if not barang:
        print("Belum ada data barang.")
        return

    kolom = [
        ("kode", "Kode"),
        ("nama_barang", "Nama Barang"),
        ("kategori", "Kategori"),
        ("harga", "Harga"),
        ("stok", "Stok"),
    ]
    baris = []

    for produk in barang:
        harga = format_rupiah(produk["harga"])
        baris.append([
            produk["kode"],
            produk["nama_barang"],
            produk["kategori"],
            harga,
            str(produk["stok"]),
        ])

    lebar_kolom = [
        max(len(judul), *(len(data[i]) for data in baris))
        for i, (_, judul) in enumerate(kolom)
    ]
    garis = "+" + "+".join("-" * (lebar + 2) for lebar in lebar_kolom) + "+"

    print(garis)
    print("|" + "|".join(
        f" {judul:<{lebar_kolom[i]}} "
        for i, (_, judul) in enumerate(kolom)
    ) + "|")
    print(garis)

    for data in baris:
        print("|" + "|".join(
            f" {nilai:<{lebar_kolom[i]}} "
            for i, nilai in enumerate(data)
        ) + "|")

    print(garis)


def tambah_barang(barang):
    nama_barang = input("Nama barang: ").strip()
    while not nama_barang:
        print("Nama barang tidak boleh kosong.")
        nama_barang = input("Nama barang: ").strip()

    kategori = input("Kategori: ").strip()
    while not kategori:
        print("Kategori tidak boleh kosong.")
        kategori = input("Kategori: ").strip()

    while True:
        try:
            harga = int(input("Harga: "))
            if harga <= 0:
                print("Harga harus lebih dari 0.")
                continue
            break
        except ValueError:
            print("Harga harus berupa angka.")

    while True:
        try:
            stok = int(input("Stok: "))
            if stok < 0:
                print("Stok tidak boleh kurang dari 0.")
                continue
            break
        except ValueError:
            print("Stok harus berupa angka.")

    produk_baru = {
        "kode": buat_kode_barang(barang),
        "nama_barang": nama_barang,
        "kategori": kategori,
        "harga": harga,
        "stok": stok,
    }
    barang.append(produk_baru)
    print(f"Barang berhasil ditambahkan dengan kode {produk_baru['kode']}.")
