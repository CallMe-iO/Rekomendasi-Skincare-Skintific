import sqlite3
import os

# Pastikan folder database sudah ada
if not os.path.exists("database"):
    os.makedirs("database")

def create_tables():
    conn = sqlite3.connect('database/skincare.db')
    cursor = conn.cursor()
    
    # Tabel jenis_kulit
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jenis_kulit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipe TEXT NOT NULL,
        description TEXT
    )
    ''')
    
    # Tabel masalah_kulit
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS masalah_kulit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        description TEXT
    )
    ''')
    
    # Tabel produk
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produk (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        deskripsi TEXT,
        harga TEXT,
        gambar_path TEXT,
        kategori TEXT  -- 'skincare' atau 'sunscreen'
    )
    ''')
    
    # Tabel aturan (rules)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS aturan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kategori TEXT,  -- 'skincare' atau 'sunscreen'
        skin_type TEXT,
        skin_issues TEXT,  -- daftar masalah kulit dipisahkan koma; bisa NULL untuk sunscreen
        rekomendasi_produk_ids TEXT,  -- daftar ID produk (dipisah koma)
        deskripsi TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

def insert_dummy_data():
    conn = sqlite3.connect('database/skincare.db')
    cursor = conn.cursor()
    
    # Data jenis kulit
    jenis_kulit_data = [
        ('Berminyak', 'Kulit yang berminyak dan rentan terhadap jerawat.'),
        ('Kombinasi', 'Kulit kombinasi antara berminyak dan kering.'),
        ('Semua Jenis Kulit', 'Cocok untuk semua jenis kulit.'),
        ('Sensitif', 'Kulit yang mudah iritasi.'),
        ('Kulit Berjerawat', 'Kulit dengan masalah jerawat.')
    ]
    cursor.executemany('INSERT INTO jenis_kulit (tipe, description) VALUES (?, ?)', jenis_kulit_data)
    
    # Data masalah kulit
    masalah_kulit_data = [
        ('Jerawat', 'Masalah jerawat di wajah.'),
        ('Komedo', 'Masalah komedo pada kulit.'),
        ('Pori-pori besar', 'Pori-pori wajah tampak besar.'),
        ('Kulit kering', 'Kulit terasa kering dan dehidrasi.'),
        ('Bekas jerawat', 'Bekas jerawat yang sulit hilang.')
    ]
    cursor.executemany('INSERT INTO masalah_kulit (nama, description) VALUES (?, ?)', masalah_kulit_data)
    
    # Data produk
    produk_data = [
        # Produk untuk skincare diagnosis
        ('Acid Acne Gel Cleanser', 'Membersihkan jerawat dan komedo dengan formula AHA/BHA.', 'Rp 150.000', 'assets/images/skincare/acid_acne_gel.jpg', 'skincare'),
        ('Aqua Light Daily Sunscreen SPF35 PA+++', 'Melindungi kulit dari sinar UV dengan tekstur ringan.', 'Rp 200.000', 'assets/images/skincare/aqua_light_sunscreen.jpg', 'skincare'),
        # Produk untuk sunscreen (berdasarkan jenis kulit)
        ('Aqua Light Daily Sunscreen SPF35 PA+++', 'Sunscreen khusus untuk kulit Berminyak.', 'Rp 200.000', 'assets/images/skincare/aqua_light_sunscreen.jpg', 'sunscreen'),
        ('Matte Finish Sunscreen SPF30', 'Sunscreen dengan hasil matte untuk kulit Kombinasi.', 'Rp 210.000', 'assets/images/skincare/matte_finish_sunscreen.jpg', 'sunscreen'),
        ('Universal Sunscreen SPF50', 'Sunscreen yang cocok untuk Semua Jenis Kulit.', 'Rp 220.000', 'assets/images/skincare/universal_sunscreen.jpg', 'sunscreen'),
        ('Sensitive Skin Sunscreen SPF30', 'Sunscreen lembut untuk kulit Sensitif.', 'Rp 230.000', 'assets/images/skincare/sensitive_sunscreen.jpg', 'sunscreen'),
        ('Acne-prone Sunscreen SPF40', 'Sunscreen untuk kulit Berjerawat yang tidak menyumbat pori.', 'Rp 240.000', 'assets/images/skincare/acne_prone_sunscreen.jpg', 'sunscreen')
    ]
    cursor.executemany('INSERT INTO produk (nama, deskripsi, harga, gambar_path, kategori) VALUES (?, ?, ?, ?, ?)', produk_data)
    
    # Aturan untuk skincare diagnosis (mempertimbangkan jenis kulit dan masalah kulit)
    # Contoh: Jika kulit Berminyak dan masalah kulit mencakup Jerawat dan Komedo, rekomendasi adalah kombinasi produk.
    aturan_data = [
        ('skincare', 'Berminyak', 'Jerawat,Komedo', '1,2', 'Paket rekomendasi untuk kulit Berminyak dengan jerawat dan komedo.')
        # Tambahkan aturan lain sesuai logika yang diinginkan.
    ]
    cursor.executemany('INSERT INTO aturan (kategori, skin_type, skin_issues, rekomendasi_produk_ids, deskripsi) VALUES (?, ?, ?, ?, ?)', aturan_data)
    
    # Aturan untuk sunscreen (hanya berdasarkan jenis kulit)
    sunscreen_rules = [
        ('sunscreen', 'Berminyak', None, '3', 'Sunscreen untuk kulit Berminyak.'),
        ('sunscreen', 'Kombinasi', None, '4', 'Sunscreen untuk kulit Kombinasi.'),
        ('sunscreen', 'Semua Jenis Kulit', None, '5', 'Sunscreen untuk Semua Jenis Kulit.'),
        ('sunscreen', 'Sensitif', None, '6', 'Sunscreen untuk kulit Sensitif.'),
        ('sunscreen', 'Kulit Berjerawat', None, '7', 'Sunscreen untuk kulit Berjerawat.')
    ]
    cursor.executemany('INSERT INTO aturan (kategori, skin_type, skin_issues, rekomendasi_produk_ids, deskripsi) VALUES (?, ?, ?, ?, ?)', sunscreen_rules)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    insert_dummy_data()
    print("Database setup completed!")
