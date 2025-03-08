# 🚲 Dashboard Analisis Bike Sharing

## 📌 Deskripsi
Dashboard ini dibuat untuk menganalisis data peminjaman sepeda berdasarkan **musim** dan **jam dalam sehari** menggunakan dataset **Bike Sharing Dataset**. Dashboard ini dikembangkan dengan **Streamlit** dan menampilkan visualisasi interaktif menggunakan **Plotly**.

---

## 🛠️ Fitur Dashboard
✅ **Analisis Pengaruh Musim** terhadap jumlah peminjaman sepeda
✅ **Analisis Jam Puncak Peminjaman** dalam sehari
✅ **Visualisasi Interaktif** dengan **Plotly**
✅ **Sidebar Menu** untuk memilih analisis
✅ **Deskripsi & Insight Data** untuk memahami pola peminjaman

---

## 📂 Struktur Folder
```
|-- data/
|   |-- hour.csv  # Dataset peminjaman sepeda per jam
|   |-- day.csv   # Dataset peminjaman sepeda per hari
|
|-- dashboard.py  # Script utama untuk menjalankan dashboard
|-- README.md  # Dokumentasi proyek
|-- requirements.txt  # Daftar pustaka yang diperlukan
```

---

## 🚀 Cara Menjalankan Dashboard
### 1️⃣ **Persiapan Lingkungan**
Pastikan Python dan pustaka yang diperlukan telah terinstal. Jika belum, jalankan perintah berikut:
```bash
pip install -r requirements.txt
```

### 2️⃣ **Menjalankan Dashboard**
Jalankan perintah berikut di terminal:
```bash
streamlit run dashboard.py
```
Dashboard akan terbuka di browser secara otomatis.

---

## 📊 Hasil Analisis
### 🔹 **Pengaruh Musim terhadap Peminjaman Sepeda**
- Musim panas memiliki jumlah peminjaman tertinggi.
- Musim dingin memiliki jumlah peminjaman terendah.

### 🔹 **Jam Puncak Peminjaman Sepeda**
- Peminjaman sepeda mencapai puncaknya pada **08:00 dan 17:00**.
- Pola ini menunjukkan bahwa banyak pengguna menggunakan sepeda untuk **perjalanan kerja**.

---

## 🏗️ Teknologi yang Digunakan
- **Python** 🐍
- **Streamlit** 📊 (Framework untuk dashboard interaktif)
- **Plotly** 📈 (Visualisasi data interaktif)
- **Pandas** 📑 (Manipulasi data)

---

## 📌 Catatan
Jika terjadi error saat menjalankan **streamlit run dashboard.py**, pastikan:
- Semua pustaka sudah terinstal
- Struktur folder sesuai dengan dokumentasi ini

---

