import sqlite3
import os

# Pastikan folder database ada
if not os.path.exists("database"):
    os.makedirs("database")

DB_PATH = "database/skincare.db"

def drop_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS produk_masalah")
    cursor.execute("DROP TABLE IF EXISTS produk")
    cursor.execute("DROP TABLE IF EXISTS jenis_kulit")
    cursor.execute("DROP TABLE IF EXISTS masalah_kulit")
    conn.commit()
    conn.close()

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Tabel jenis_kulit
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jenis_kulit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL UNIQUE
    )
    ''')
    
    # Tabel masalah_kulit
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS masalah_kulit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL UNIQUE
    )
    ''')
    
    # Tabel produk
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produk (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        jenis_kulit_id INTEGER NOT NULL,
        deskripsi TEXT,
        harga TEXT,
        gambar_path TEXT,
        kategori TEXT,  -- 'skincare' atau 'sunscreen'
        FOREIGN KEY (jenis_kulit_id) REFERENCES jenis_kulit(id)
    )
    ''')
    
    # Tabel relasi produk dan masalah kulit
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produk_masalah (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produk_id INTEGER NOT NULL,
        masalah_kulit_id INTEGER NOT NULL,
        FOREIGN KEY (produk_id) REFERENCES produk(id),
        FOREIGN KEY (masalah_kulit_id) REFERENCES masalah_kulit(id)
    )
    ''')
    
    conn.commit()
    conn.close()

def insert_reference_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Data jenis kulit
    skin_types = ["Berminyak", "Kering", "Kombinasi", "Semua Jenis Kulit", "Sensitif", "Kulit Berjerawat"]
    for st in skin_types:
        cursor.execute("INSERT OR IGNORE INTO jenis_kulit (nama) VALUES (?)", (st,))
    
    # Data masalah kulit
    skin_issues = [
        "Jerawat", "Kulit Berminyak", "Komedo", "Skin Barrier Bermasalah",
        "Dehidrasi", "Kemerahan", "Kulit Bertekstur", "Kusam",
        "Penuaan Dini", "Noda Hitam", "Bintik Hitam",
        "Warna Kulit Tidak Merata", "Tekstur Tidak Merata", "Iritasi"
    ]
    for issue in skin_issues:
        cursor.execute("INSERT OR IGNORE INTO masalah_kulit (nama) VALUES (?)", (issue,))
    
    conn.commit()
    conn.close()

def insert_produk_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Ambil mapping jenis kulit dan masalah kulit
    cursor.execute("SELECT id, nama FROM jenis_kulit")
    jenis_mapping = {row[1]: row[0] for row in cursor.fetchall()}
    
    cursor.execute("SELECT id, nama FROM masalah_kulit")
    masalah_mapping = {row[1]: row[0] for row in cursor.fetchall()}
    
    # Data produk (dictionary)
    produk_data = [
        {
            "nama": "3x Acid Acne Gel Cleanser",
            "jenis_kulit": "Berminyak",
            "issues": ["Jerawat", "Kulit Berminyak", "Komedo"],
            "deskripsi": "Membersihkan jerawat dan komedo dengan efektif.",
            "harga": "Rp150.000",
            "gambar_path": "assets/images/skincare/acid_acne_gel.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "5X Ceramide Pembersih pH Rendah",
            "jenis_kulit": "Kering",
            "issues": ["Skin Barrier Bermasalah", "Dehidrasi"],
            "deskripsi": "Membersihkan dengan formula pH rendah.",
            "harga": "Rp120.000",
            "gambar_path": "assets/images/skincare/ceramide_pembersih.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Amino Acid Gentle Cleansing Mousse",
            "jenis_kulit": "Kering",
            "issues": ["Skin Barrier Bermasalah", "Dehidrasi"],
            "deskripsi": "Mousse lembut untuk membersihkan kulit.",
            "harga": "Rp130.000",
            "gambar_path": "assets/images/skincare/amino_acid_mousse.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Panthenol Gentle Gel Cleanser",
            "jenis_kulit": "Kombinasi",
            "issues": ["Kulit Berminyak", "Komedo"],
            "deskripsi": "Gel cleanser yang lembut.",
            "harga": "Rp140.000",
            "gambar_path": "assets/images/skincare/panthenol_gel.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "5X CERAMIDE SOOTHING TONER",
            "jenis_kulit": "Kering",
            "issues": ["Skin Barrier Bermasalah", "Kemerahan"],
            "deskripsi": "Toner yang menenangkan kulit.",
            "harga": "Rp110.000",
            "gambar_path": "assets/images/skincare/ceramide_soothing_toner.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "4D Hyaluronic Acid Barrier Essence Toner",
            "jenis_kulit": "Kering",
            "issues": ["Dehidrasi", "Skin Barrier Bermasalah"],
            "deskripsi": "Essence toner dengan 4D Hyaluronic Acid.",
            "harga": "Rp160.000",
            "gambar_path": "assets/images/skincare/hyaluronic_essence.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Glycolic Acid Daily Clarifying Toner",
            "jenis_kulit": "Berminyak",
            "issues": ["Jerawat", "Komedo"],
            "deskripsi": "Toner pengelupasan dengan Glycolic Acid.",
            "harga": "Rp155.000",
            "gambar_path": "assets/images/skincare/glycolic_acid_toner.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "5X Ceramide Barrier Repair Moisture Gel",
            "jenis_kulit": "Semua Jenis Kulit",
            "issues": ["Skin Barrier Bermasalah", "Kemerahan", "Dehidrasi", "Kulit Bertekstur"],
            "deskripsi": "Gel pelembab dengan 5X Ceramide.",
            "harga": "Rp170.000",
            "gambar_path": "assets/images/skincare/ceramide_repair_gel.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Retinol Skin Renewal Moisturizer",
            "jenis_kulit": "Semua Jenis Kulit",
            "issues": ["Kusam", "Skin Barrier Bermasalah", "Penuaan Dini"],
            "deskripsi": "Moisturizer dengan Retinol untuk peremajaan kulit.",
            "harga": "Rp200.000",
            "gambar_path": "assets/images/skincare/retinol_moisturizer.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Sensitive Moisture Gel",
            "jenis_kulit": "Sensitif",
            "issues": ["Kemerahan", "Skin Barrier Bermasalah", "Dehidrasi"],
            "deskripsi": "Gel pelembab untuk kulit sensitif.",
            "harga": "Rp180.000",
            "gambar_path": "assets/images/skincare/sensitive_moisture.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Symwhite 377 Dark Spot Moisture Gel",
            "jenis_kulit": "Semua Jenis Kulit",
            "issues": ["Noda Hitam", "Bintik Hitam", "Penuaan Dini"],
            "deskripsi": "Gel untuk mengatasi noda hitam.",
            "harga": "Rp190.000",
            "gambar_path": "assets/images/skincare/symwhite_moisture.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Truffle Biome Skin Reborn Cream Gel Moisturizer",
            "jenis_kulit": "Sensitif",
            "issues": ["Jerawat", "Kemerahan", "Iritasi"],
            "deskripsi": "Moisturizer dengan Truffle Biome untuk kulit sensitif.",
            "harga": "Rp210.000",
            "gambar_path": "assets/images/skincare/truffle_reborn.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Symwhite 377 Dark Spot Serum",
            "jenis_kulit": "Semua Jenis Kulit",
            "issues": ["Bintik Hitam", "Warna Kulit Tidak Merata"],
            "deskripsi": "Serum untuk mencerahkan dan meratakan warna kulit.",
            "harga": "Rp220.000",
            "gambar_path": "assets/images/skincare/symwhite_serum.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Niacinamide Brightening Serum",
            "jenis_kulit": "Semua Jenis Kulit",
            "issues": ["Kusam", "Warna Kulit Tidak Merata"],
            "deskripsi": "Serum dengan Niacinamide untuk mencerahkan kulit.",
            "harga": "Rp230.000",
            "gambar_path": "assets/images/skincare/niacinamide_serum.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Retinol Skin Renewal Serum",
            "jenis_kulit": "Semua Jenis Kulit",
            "issues": ["Tekstur Tidak Merata", "Jerawat", "Penuaan Dini"],
            "deskripsi": "Serum dengan Retinol untuk regenerasi kulit.",
            "harga": "Rp240.000",
            "gambar_path": "assets/images/skincare/retinol_serum.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "Salicylic Acid Anti-Acne Serum",
            "jenis_kulit": "Kulit Berjerawat",
            "issues": ["Jerawat", "Bintik Hitam", "Skin Barrier Bermasalah"],
            "deskripsi": "Serum anti jerawat dengan Salicylic Acid.",
            "harga": "Rp250.000",
            "gambar_path": "assets/images/skincare/salicylic_serum.jpg",
            "kategori": "skincare"
        },
        {
            "nama": "5X Ceramide Skin Barrier Repair Serum",
            "jenis_kulit": "Semua Jenis Kulit",
            "issues": ["Skin Barrier Bermasalah", "Kemerahan"],
            "deskripsi": "Serum perbaikan skin barrier dengan 5X Ceramide.",
            "harga": "Rp260.000",
            "gambar_path": "assets/images/skincare/ceramide_repair_serum.jpg",
            "kategori": "skincare"
        },
        # Data sunscreen
        {
            "nama": "5X Ceramide Serum Sunscreen SPF50 PA++++",
            "jenis_kulit": "Semua Jenis Kulit",
            "issues": [],
            "deskripsi": "Sunscreen dengan perlindungan tinggi SPF50 PA++++.",
            "harga": "Rp270.000",
            "gambar_path": "assets/images/skincare/ceramide_sunscreen.jpg",
            "kategori": "sunscreen"
        },
        {
            "nama": "Aqua Light Daily Sunscreen SPF35 PA+++",
            "jenis_kulit": "Berminyak",
            "issues": [],
            "deskripsi": "Sunscreen ringan dengan perlindungan SPF35 PA+++.",
            "harga": "Rp280.000",
            "gambar_path": "assets/images/skincare/aqua_light_sunscreen.jpg",
            "kategori": "sunscreen"
        },
        {
            "nama": "Light Serum Sunscreen SPF50 PA++++",
            "jenis_kulit": "Berminyak",
            "issues": [],
            "deskripsi": "Sunscreen dengan finish ringan dan perlindungan SPF50 PA++++.",
            "harga": "Rp290.000",
            "gambar_path": "assets/images/skincare/light_serum_sunscreen.jpg",
            "kategori": "sunscreen"
        },
        {
            "nama": "Matte Fit Serum Sunscreen SPF50+ PA++++",
            "jenis_kulit": "Berminyak",
            "issues": [],
            "deskripsi": "Sunscreen dengan hasil matte dan perlindungan SPF50+ PA++++.",
            "harga": "Rp300.000",
            "gambar_path": "assets/images/skincare/matte_fit_sunscreen.jpg",
            "kategori": "sunscreen"
        },
        {
            "nama": "Outdoor Sunscreen Spray SPF50+ PA++++",
            "jenis_kulit": "Semua Jenis Kulit",
            "issues": [],
            "deskripsi": "Sunscreen spray untuk perlindungan luar ruangan.",
            "harga": "Rp310.000",
            "gambar_path": "assets/images/skincare/outdoor_sunscreen.jpg",
            "kategori": "sunscreen"
        }
    ]
    
    for prod in produk_data:
        jenis_id = jenis_mapping.get(prod["jenis_kulit"])
        cursor.execute('''
            INSERT INTO produk (nama, jenis_kulit_id, deskripsi, harga, gambar_path, kategori)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (prod["nama"], jenis_id, prod["deskripsi"], prod["harga"], prod["gambar_path"], prod["kategori"]))
        produk_id = cursor.lastrowid
        
        # Sisipkan relasi ke tabel produk_masalah (hanya untuk produk skincare)
        if prod["issues"]:
            for issue in prod["issues"]:
                masalah_id = masalah_mapping.get(issue)
                if masalah_id:
                    cursor.execute('''
                        INSERT INTO produk_masalah (produk_id, masalah_kulit_id)
                        VALUES (?, ?)
                    ''', (produk_id, masalah_id))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    drop_tables()      # Hapus tabel lama agar skema baru dipaksa dibuat ulang
    create_tables()
    insert_reference_data()
    insert_produk_data()
    print("Database setup completed!")
