def baca_suhu(nama_file):
    data_suhu = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                if baris.strip():
                    hari, suhu_str = baris.strip().split(";")
                    data_suhu.append({
                        "hari": hari.strip(),
                        "suhu": int(suhu_str.strip())
                    })
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan!")
        return []
    return data_suhu


def analisis_suhu(data_suhu, *args, **kwargs):
    if not data_suhu:
        return {}

    suhu_list = list(map(lambda item: item["suhu"], data_suhu))
    rata_rata = sum(suhu_list) / len(suhu_list)

    tertinggi = max(data_suhu, key=lambda item: item["suhu"])
    terendah = min(data_suhu, key=lambda item: item["suhu"])
    batas_panas = kwargs.get("batas_panas", 32)

    laporan_detail = []
    jumlah_panas = 0
    for item in data_suhu:
        kategori = "Panas" if item["suhu"] >= batas_panas else "Normal"
        if kategori == "Panas":
            jumlah_panas += 1
        laporan_detail.append({
            "hari": item["hari"],
            "suhu": item["suhu"],
            "kategori": kategori
        })

    return {
        "rata_rata": rata_rata,
        "tertinggi": tertinggi,
        "terendah": terendah,
        "jumlah_panas": jumlah_panas,
        "detail": laporan_detail
    }

def tulis_laporan(hasil_analisis, file_output):
    if not hasil_analisis:
        return
    with open(file_output, "w") as file:
        file.write("=== LAPORAN ANALISIS SUHU ===\n")
        file.write(f"Rata-rata Suhu  : {hasil_analisis['rata_rata']:.2f}°C\n")
        file.write(f"Suhu Tertinggi   : {hasil_analisis['tertinggi']['suhu']}°C ({hasil_analisis['tertinggi']['hari']})\n")
        file.write(f"Suhu Terendah    : {hasil_analisis['terendah']['suhu']}°C ({hasil_analisis['terendah']['hari']})\n")
        file.write(f"Jumlah Hari Panas: {hasil_analisis['jumlah_panas']} hari\n\n")
        file.write("Detail Harian:\n")
        for detail in hasil_analisis["detail"]:
            file.write(f"- {detail['hari']}: {detail['suhu']}°C [{detail['kategori']}]\n")

    print("\n--- ISI FILE LAPORAN ---")
    with open(file_output, "r") as file:
        print(file.read())


if __name__ == "__main__":
    data = baca_suhu("suhu.txt")
    if data:
        hasil = analisis_suhu(data, batas_panas=32)
        tulis_laporan(hasil, "laporan_suhu.txt")