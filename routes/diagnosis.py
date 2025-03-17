from models import forward_chaining, data_loader

def diagnosis_api(skin_type, skin_issues):
    """
    API diagnosis untuk skincare.
    Mengembalikan data produk rekomendasi berdasarkan forward chaining.
    """
    product_ids = forward_chaining.diagnose_skincare(skin_type, skin_issues)
    if product_ids:
        products = data_loader.get_produk_by_ids(product_ids)
        return products
    else:
        return []
