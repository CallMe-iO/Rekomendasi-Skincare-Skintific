import streamlit as st
from routes import diagnosis, skincare

st.title("Sistem Diagnosa Skincare & Rekomendasi Sunscreen")
st.write("Selamat datang! Pilih menu di samping untuk mulai.")

st.sidebar.title("Navigasi")
option = st.sidebar.selectbox("Pilih Menu", ["Diagnosis Skincare", "Rekomendasi Sunscreen"])

if option == "Diagnosis Skincare":
    st.header("Diagnosis Skincare")
    # Pilihan jenis kulit
    skin_types = ["Berminyak", "Kombinasi", "Semua Jenis Kulit", "Sensitif", "Kulit Berjerawat"]
    selected_skin_type = st.radio("Pilih Jenis Kulit Anda", skin_types)
    
    # Pilihan masalah kulit (minimal 2, maksimal 3)
    skin_issues_options = ["Jerawat", "Komedo", "Pori-pori besar", "Kulit kering", "Bekas jerawat"]
    selected_skin_issues = st.multiselect("Pilih Masalah Kulit (minimal 2, maksimal 3)", skin_issues_options)
    
    if st.button("Diagnosa Skincare"):
        if len(selected_skin_issues) < 2 or len(selected_skin_issues) > 3:
            st.error("Silakan pilih minimal 2 dan maksimal 3 masalah kulit.")
        else:
            with st.spinner("Mendiagnosa..."):
                recommendations = diagnosis.diagnosis_api(selected_skin_type, selected_skin_issues)
                if recommendations:
                    st.success("Rekomendasi ditemukan!")
                    for prod in recommendations:
                        st.image(prod['gambar_path'], width=200)
                        st.subheader(prod['nama'])
                        st.write(prod['deskripsi'])
                        st.write(f"Harga: {prod['harga']}")
                        st.markdown("---")
                else:
                    st.warning("Tidak ada rekomendasi yang cocok.")
                    
elif option == "Rekomendasi Sunscreen":
    st.header("Rekomendasi Sunscreen")
    skin_types = ["Berminyak", "Kombinasi", "Semua Jenis Kulit", "Sensitif", "Kulit Berjerawat"]
    selected_skin_type = st.radio("Pilih Jenis Kulit Anda", skin_types)
    
    if st.button("Rekomendasikan Sunscreen"):
        with st.spinner("Mencari rekomendasi..."):
            recommendations = skincare.skincare_api(selected_skin_type)
            if recommendations:
                st.success("Rekomendasi sunscreen ditemukan!")
                for prod in recommendations:
                    st.image(prod['gambar_path'], width=200)
                    st.subheader(prod['nama'])
                    st.write(prod['deskripsi'])
                    st.write(f"Harga: {prod['harga']}")
                    st.markdown("---")
            else:
                st.warning("Tidak ada rekomendasi sunscreen yang cocok.")
