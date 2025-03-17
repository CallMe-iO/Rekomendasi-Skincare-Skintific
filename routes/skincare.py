from models import forward_chaining, data_loader

def skincare_api(skin_type):
    """
    API untuk rekomendasi sunscreen.
    """
    product_ids = forward_chaining.recommend_sunscreen(skin_type)
    if product_ids:
        products = data_loader.get_produk_by_ids(product_ids)
        return products
    else:
        return []
