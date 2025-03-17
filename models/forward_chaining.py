from models import data_loader

def diagnose_skincare(skin_type, selected_issues):
    """
    Diagnosis skincare:
    - Ambil produk dengan kategori 'skincare' dan jenis kulit sesuai.
    - Rekomendasikan produk jika semua issues produk (jika ada) merupakan subset dari input user.
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
    - Ambil produk dengan kategori 'sunscreen' dan jenis kulit sesuai.
    """
    produk_list = data_loader.get_produk_by_category_and_skin(skin_type, 'sunscreen')
    return produk_list
