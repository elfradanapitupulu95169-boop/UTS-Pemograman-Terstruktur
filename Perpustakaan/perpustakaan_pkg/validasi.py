class InvalidDataError(Exception):
    """Custom exception untuk menangani input data buku/peminjaman tidak valid."""
    pass

def validasi_tahun(tahun):
    try:
        thn = int(tahun)
        if thn < 1000 or thn > 2026:
            raise InvalidDataError("Tahun terbit tidak logis!")
        return thn
    except ValueError:
        raise InvalidDataError("Tahun harus berupa angka integer!")

def validasi_non_kosong(teks, nama_field):
    assert len(str(teks).strip()) > 0, f"Field {nama_field} tidak boleh kosong!"
    return str(teks).strip()