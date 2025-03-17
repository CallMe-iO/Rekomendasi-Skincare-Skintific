from models import forward_chaining

def skincare_api(skin_type):
    """
    API rekomendasi sunscreen saja.
    Mengembalikan produk sunscreen untuk skin_type yang dipilih,
    ditambah produk dengan jenis "Semua Jenis Kulit" secara otomatis.
    """
    return forward_chaining.recommend_sunscreen(skin_type)
