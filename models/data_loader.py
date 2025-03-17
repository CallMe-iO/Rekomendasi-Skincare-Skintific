import sqlite3

def get_connection():
    conn = sqlite3.connect('database/skincare.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_produk_by_ids(ids):
    conn = get_connection()
    cursor = conn.cursor()
    placeholders = ','.join(['?'] * len(ids))
    query = f"SELECT * FROM produk WHERE id IN ({placeholders})"
    cursor.execute(query, ids)
    rows = cursor.fetchall()
    conn.close()
    # Konversi hasil ke dalam list dictionary
    products = [dict(row) for row in rows]
    return products

def get_rules_by_kategori(kategori):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aturan WHERE kategori = ?", (kategori,))
    rows = cursor.fetchall()
    conn.close()
    rules = [dict(row) for row in rows]
    return rules
