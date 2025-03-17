import sqlite3

DB_PATH = "database/skincare.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_produk_issues(produk_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
        SELECT m.nama
        FROM produk_masalah pm
        JOIN masalah_kulit m ON pm.masalah_kulit_id = m.id
        WHERE pm.produk_id = ?
    '''
    cursor.execute(query, (produk_id,))
    rows = cursor.fetchall()
    conn.close()
    return [row["nama"].lower() for row in rows]

def get_produk_by_category_and_skin(skin_type, kategori):
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
        SELECT p.id, p.nama, p.deskripsi, p.harga, p.gambar_path, p.kategori
        FROM produk p
        JOIN jenis_kulit j ON p.jenis_kulit_id = j.id
        WHERE lower(j.nama) = ? AND p.kategori = ?
    '''
    cursor.execute(query, (skin_type.lower(), kategori))
    rows = cursor.fetchall()
    conn.close()
    
    produk_list = []
    for row in rows:
        prod = dict(row)
        prod["issues"] = get_produk_issues(prod["id"])
        produk_list.append(prod)
    return produk_list
