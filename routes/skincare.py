from models import forward_chaining

def skincare_api(skin_type):
    """
    API rekomendasi sunscreen.
    """
    return forward_chaining.recommend_sunscreen(skin_type)
