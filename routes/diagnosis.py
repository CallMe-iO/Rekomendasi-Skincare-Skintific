from models import forward_chaining

def diagnosis_api(skin_type, skin_issues):
    """
    API diagnosis gabungan untuk skincare & sunscreen.
    Fungsi ini mengembalikan dictionary dengan key:
      - "skincare": list rekomendasi produk skincare
      - "sunscreen": list rekomendasi produk sunscreen (dengan fallback ke "Semua Jenis Kulit")
    """
    return forward_chaining.get_recommendations(skin_type, skin_issues)
