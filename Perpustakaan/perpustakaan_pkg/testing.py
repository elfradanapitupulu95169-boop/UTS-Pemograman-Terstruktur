import unittest
from perpustakaan_pkg.proccesing import PerpustakaanManager
from perpustakaan_pkg.validasi import validasi_tahun, InvalidDataError

class TestPerpustakaan(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {"id": "B01", "judul": "Pemrograman Python", "pengarang": "Andi", "tahun": 2021, "stok": 10},
            {"id": "B02", "judul": "Struktur Data", "pengarang": "Budi", "tahun": 2019, "stok": 2}
        ]
        self.manager = PerpustakaanManager(self.sample_data)

    def test_hitung_total_stok(self):
        self.assertEqual(self.manager.hitung_total_stok(), 12)

    def test_hitung_total_stok_with_args(self):
        self.assertEqual(self.manager.hitung_total_stok(5, 3), 20)

    def test_urutkan_buku(self):
        hasil = self.manager.urutkan_buku_berdasarkan_tahun()
        self.assertEqual(hasil[0]["id"], "B01")

    def test_validasi_tahun_valid(self):
        self.assertEqual(validasi_tahun(2020), 2020)

    def test_validasi_tahun_invalid(self):
        with self.assertRaises(InvalidDataError):
            validasi_tahun(3000)

if __name__ == "__main__":
    unittest.main()