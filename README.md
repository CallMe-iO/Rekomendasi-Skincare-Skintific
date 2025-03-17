/skincare_diagnosis_system
│── /assets
│   ├── /images
│   │   ├── /symptoms (gambar gejala)
│   │   ├── /diseases (gambar penyakit)
│   │   ├── /skincare (gambar skincare)
│── /database
│   ├── setup_database.py   # Script untuk setup database SQLite
│   ├── database.db         # File database SQLite
│── /models
│   ├── forward_chaining.py # Implementasi FC tanpa bobot & dengan bobot
│── /routes
│   ├── diagnosis.py        # Endpoint diagnosis
│   ├── skincare.py         # Endpoint daftar skincare
│── /pages
│   ├── home.py             # Halaman utama (Streamlit)
│── app.py                  # Entry point Streamlit
│── requirements.txt        # Dependency Python
│── README.md               # Dokumentasi proyek
