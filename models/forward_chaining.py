from models import data_loader

def diagnose_skincare(skin_type, skin_issues):
    """
    Forward chaining untuk mendiagnosis rekomendasi skincare.
    Input:
      skin_type: string (misal: 'Berminyak')
      skin_issues: list of strings (misal: ['Jerawat', 'Komedo'])
    Output:
      List of rekomendasi produk (ID produk)
    """
    rules = data_loader.get_rules_by_kategori('skincare')
    recommended_ids = []
    for rule in rules:
        # Cek kecocokan jenis kulit (case-insensitive)
        if rule['skin_type'].lower() == skin_type.lower():
            if rule['skin_issues']:
                # Pisahkan kondisi masalah kulit dari rule
                rule_issues = [issue.strip().lower() for issue in rule['skin_issues'].split(',')]
                input_issues = [issue.lower() for issue in skin_issues]
                # Pastikan semua kondisi pada rule terpenuhi oleh input
                if all(issue in input_issues for issue in rule_issues):
                    recommended_ids.extend([int(pid.strip()) for pid in rule['rekomendasi_produk_ids'].split(',')])
                    break  # Ambil rule pertama yang cocok
    return recommended_ids

def recommend_sunscreen(skin_type):
    """
    Forward chaining untuk merekomendasikan sunscreen (hanya berdasarkan jenis kulit).
    Input:
      skin_type: string
    Output:
      List of rekomendasi produk (ID produk)
    """
    rules = data_loader.get_rules_by_kategori('sunscreen')
    for rule in rules:
        if rule['skin_type'].lower() == skin_type.lower():
            return [int(pid.strip()) for pid in rule['rekomendasi_produk_ids'].split(',')]
    return []
