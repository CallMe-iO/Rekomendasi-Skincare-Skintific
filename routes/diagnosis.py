from models import forward_chaining

def diagnosis_api(skin_type, skin_issues):
    """
    API diagnosis untuk skincare.
    Mengembalikan produk rekomendasi berdasarkan forward chaining.
    """
    return forward_chaining.diagnose_skincare(skin_type, skin_issues)
