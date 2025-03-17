import sqlite3

conn = sqlite3.connect('database/skincare.db')
cursor = conn.cursor()
cursor.execute("ALTER TABLE produk ADD COLUMN jenis_kulit TEXT")
conn.commit()
conn.close()
