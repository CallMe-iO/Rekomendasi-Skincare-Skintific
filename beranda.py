import pages.home
import streamlit as st

# Atur konfigurasi halaman
st.set_page_config(
    page_title="Sistem Diagnosa Skincare & Rekomendasi Sunscreen",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tampilan header di beranda
st.title("Selamat Datang di Sistem Diagnosa Skincare & Rekomendasi Sunscreen")
st.markdown("""
Selamat datang di aplikasi yang akan membantu Anda menemukan produk skincare dan sunscreen yang tepat!  
Sistem ini menggunakan metode forward chaining untuk mendiagnosa masalah kulit dan memberikan rekomendasi terbaik, bahkan dengan fallback jika tipe kulit khusus tidak memiliki produk.
""")

st.info("Pilih menu di sidebar untuk memulai diagnosa atau mendapatkan rekomendasi sunscreen secara langsung.")

# Panggil halaman utama dari folder pages/home.py
import pages.home

