import os

class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath

    def inisialisasi_file(self):
        try:
            with open(self.filepath, "x") as f:
                f.write("id;judul;pengarang;tahun;stok\n")
        except FileExistsError:
            pass

    def tambah_buku(self, data_line):
        with open(self.filepath, "a") as f:
            f.write(data_line + "\n")

    def baca_semua_buku(self):
        buku_list = []
        try:
            with open(self.filepath, "r") as f:
                header = next(f, None)
                for baris in f:
                    if baris.strip():
                        try:
                            b_id, judul, pengarang, tahun, stok = baris.strip().split(";")
                            buku_list.append({
                                "id": b_id,
                                "judul": judul,
                                "pengarang": pengarang,
                                "tahun": int(tahun),
                                "stok": int(stok)
                            })
                        except ValueError:
                            continue  # Melewati baris corrupt
        except FileNotFoundError:
            print("File data buku tidak ditemukan!")
        return buku_list

    def tulis_laporan(self, path_laporan, konten):
        with open(path_laporan, "w") as f:
            f.write(konten)