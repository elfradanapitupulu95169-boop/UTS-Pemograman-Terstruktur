import unittest
from Analisis_suhu import analisis_suhu

class TestSuhuAnalyzer(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Selasa", "suhu": 33},
            {"hari": "Rabu", "suhu": 29},
            {"hari": "Kamis", "suhu": 35}
        ]

    def test_hitung_rata_rata(self):
        hasil = analisis_suhu(self.sample_data)
        self.assertEqual(hasil["rata_rata"], 32.0)

    def test_suhu_tertinggi_dan_terendah(self):
        hasil = analisis_suhu(self.sample_data)
        self.assertEqual(hasil["tertinggi"]["hari"], "Kamis")
        self.assertEqual(hasil["terendah"]["hari"], "Rabu")

    def test_jumlah_hari_panas(self):
        hasil = analisis_suhu(self.sample_data, batas_panas=32)
        self.assertEqual(hasil["jumlah_panas"], 2)


if __name__ == "__main__":
    unittest.main()