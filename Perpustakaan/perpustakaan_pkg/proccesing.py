class PerpustakaanManager:
    def __init__(self, data_buku):
        self.data_buku = data_buku

    def hitung_total_stok(self, *args):
        # Penggunaan *args untuk menambahkan bonus stok ekstra jika ada
        total = sum([b["stok"] for b in self.data_buku])
        total += sum(args)
        return total

    def buat_record_buku(self, **kwargs):
        # Penggunaan **kwargs untuk fleksibilitas atribut buku
        record = {
            "id": kwargs.get("id", "000"),
            "judul": kwargs.get("judul", "Tanpa Judul"),
            "pengarang": kwargs.get("pengarang", "Anonim"),
            "tahun": kwargs.get("tahun", 2000),
            "stok": kwargs.get("stok", 1)
        }
        return record

    def urutkan_buku_berdasarkan_tahun(self):
        # Penggunaan lambda pada sorted() buku
        return sorted(self.data_buku, key=lambda x: x["tahun"], reverse=True)

    def filter_buku_tersedia(self):
        # Penggunaan lambda pada filter() buku yang tersedia
        return list(filter(lambda x: x["stok"] > 0, self.data_buku))

    def hasilkan_ringkasan_laporan(self, batas_stok_minimal=5):
        # Penggunaan keyword argument suapya lebih fleksibel
        total = self.hitung_total_stok()
        buku_langka = list(filter(lambda x: x["stok"] < batas_stok_minimal, self.data_buku))
        
        laporan = "=== LAPORAN INVENTARIS PERPUSTAKAAN ===\n"
        laporan += f"Total Koleksi Stok: {total}\n"
        laporan += f"Jumlah Buku dengan Stok < {batas_stok_minimal}: {len(buku_langka)}\n\n"
        laporan += "Daftar Koleksi Terbaru:\n"
        for b in self.urutkan_buku_berdasarkan_tahun():
            laporan += f"- [{b['id']}] {b['judul']} ({b['tahun']}) - Stok: {b['stok']}\n"
        return laporan