from models import data_loader

def diagnose_skincare(skin_type, selected_issues):
    """
    Diagnosis skincare:
    - Ambil produk dengan kategori 'skincare' dan jenis kulit sesuai.
    - Rekomendasikan produk jika seluruh issues produk (jika ada) merupakan subset dari input user.
    """
    produk_list = data_loader.get_produk_by_category_and_skin(skin_type, 'skincare')
    recommendations = []
    input_issues = set(issue.lower() for issue in selected_issues)
    
    for prod in produk_list:
        if prod["issues"]:
            if set(prod["issues"]).issubset(input_issues):
                recommendations.append(prod)
    return recommendations

def recommend_sunscreen(skin_type):
    """
    Rekomendasi sunscreen:
    - Ambil produk dengan kategori 'sunscreen' berdasarkan jenis kulit.
    - Jika tidak ada, fallback ke produk dengan jenis kulit "Semua Jenis Kulit".
    """
    recs = data_loader.get_produk_by_category_and_skin(skin_type, 'sunscreen')
    if not recs:
        recs = data_loader.get_produk_by_category_and_skin("Semua Jenis Kulit", 'sunscreen')
    return recs

def get_recommendations(skin_type, selected_issues):
    """
    Gabungan rekomendasi:
      - Diagnosis skincare berdasarkan input issues.
      - Rekomendasi sunscreen (dengan fallback) berdasarkan jenis kulit.
    """
    skincare_recs = diagnose_skincare(skin_type, selected_issues)
    sunscreen_recs = recommend_sunscreen(skin_type)
    return {"skincare": skincare_recs, "sunscreen": sunscreen_recs}
