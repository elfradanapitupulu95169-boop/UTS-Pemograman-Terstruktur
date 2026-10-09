from perpustakaan_pkg.fileio import FileHandler
from perpustakaan_pkg.proccesing import PerpustakaanManager
from perpustakaan_pkg.validasi import validasi_tahun, validasi_non_kosong, InvalidDataError

def main():
    file_db = "koleksi_buku.txt"
    handler = FileHandler(file_db)
    handler.inisialisasi_file()

    # Contoh Penambahan Data Baru
    try:
        judul = validasi_non_kosong("Sistem Informasi Lanjutan", "Judul")
        pengarang = validasi_non_kosong("Eko", "Pengarang")
        tahun = validasi_tahun("2024")
        stok = 8
        
        line = f"B03;{judul};{pengarang};{tahun};{stok}"
        handler.tambah_buku(line)
    except (InvalidDataError, AssertionError) as e:
        print(f"Gagal menambahkan data: {e}")

    # Membaca & Mengolah Data
    buku_list = handler.baca_semua_buku()
    manager = PerpustakaanManager(buku_list)

    # Menghasilkan Laporan
    laporan = manager.hasilkan_ringkasan_laporan(batas_stok_minimal=5)
    handler.tulis_laporan("laporan_perpustakaan.txt", laporan)

    print("Program perpustakaan berhasil dijalankan. Laporan telah dibuat.")

if __name__ == "__main__":
    main()