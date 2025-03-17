import streamlit as st
from routes import diagnosis

st.title("Sistem Diagnosa Skincare & Rekomendasi Sunscreen")
st.write("Selamat datang! Pilih jenis kulit dan masalah kulit Anda untuk mendapatkan rekomendasi yang cerdas dan mendekati ideal.")

st.sidebar.title("Navigasi")
option = st.sidebar.selectbox("Pilih Menu", ["Diagnosis & Rekomendasi"])

if option == "Diagnosis & Rekomendasi":
    st.header("Diagnosis & Rekomendasi Skincare + Sunscreen")
    skin_types = ["Berminyak", "Kering", "Kombinasi", "Semua Jenis Kulit", "Sensitif", "Kulit Berjerawat"]
    selected_skin_type = st.radio("Pilih Jenis Kulit Anda", skin_types)
    
    skin_issues_options = [
        "Jerawat", "Kulit Berminyak", "Komedo", "Skin Barrier Bermasalah", 
        "Dehidrasi", "Kemerahan", "Kulit Bertekstur", "Kusam", 
        "Penuaan Dini", "Noda Hitam", "Bintik Hitam", "Warna Kulit Tidak Merata", 
        "Tekstur Tidak Merata", "Iritasi"
    ]
    selected_skin_issues = st.multiselect("Pilih Masalah Kulit (minimal 2, maksimal 3)", skin_issues_options)
    
    if st.button("Diagnosa & Rekomendasi"):
        if len(selected_skin_issues) < 2 or len(selected_skin_issues) > 3:
            st.error("Silakan pilih minimal 2 dan maksimal 3 masalah kulit.")
        else:
            with st.spinner("Mendiagnosa..."):
                recs = diagnosis.diagnosis_api(selected_skin_type, selected_skin_issues)
                skincare_recs = recs.get("skincare", [])
                sunscreen_recs = recs.get("sunscreen", [])
                
                st.subheader("Rekomendasi Skincare")
                if skincare_recs:
                    for prod in skincare_recs:
                        st.image(prod['gambar_path'], width=200)
                        st.subheader(prod['nama'])
                        st.write(prod['deskripsi'])
                        st.write(f"Harga: {prod['harga']}")
                        st.markdown("---")
                else:
                    st.warning("Tidak ada rekomendasi skincare yang cocok.")
                
                st.subheader("Rekomendasi Sunscreen")
                if sunscreen_recs:
                    for prod in sunscreen_recs:
                        st.image(prod['gambar_path'], width=200)
                        st.subheader(prod['nama'])
                        st.write(prod['deskripsi'])
                        st.write(f"Harga: {prod['harga']}")
                        st.markdown("---")
                else:
                    st.warning("Tidak ada rekomendasi sunscreen yang cocok.")
                    
