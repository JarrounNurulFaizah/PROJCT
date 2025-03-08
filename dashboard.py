import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Bike Sharing", page_icon="🚴", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/hour.csv")
    return df

df = load_data()

# Judul Dashboard
st.title("🚲 Dashboard Analisis Bike Sharing")

# Sidebar Menu
st.sidebar.header("🔍 Pilih Analisis")
option = st.sidebar.radio("Pilih Analisis:", ["Pengaruh Musim", "Jam Puncak Peminjaman"])

# --- Analisis 1: Pengaruh Musim ---
if option == "Pengaruh Musim":
    st.subheader("🌦️ Pengaruh Musim terhadap Jumlah Peminjaman Sepeda")

    # Grupkan data berdasarkan musim
    seasonal_counts = df.groupby("season")["cnt"].mean().reset_index()

    # Mapping nama musim
    season_map = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
    seasonal_counts["season"] = seasonal_counts["season"].map(season_map)

    # Visualisasi dengan Plotly
    fig = px.bar(seasonal_counts, x="season", y="cnt", 
                 color="season", 
                 color_discrete_map={"Semi": "blue", "Panas": "orange", "Gugur": "green", "Dingin": "red"},
                 labels={"cnt": "Rata-rata Peminjaman", "season": "Musim"},
                 title="Rata-rata Peminjaman Sepeda Berdasarkan Musim")

    # Menampilkan grafik di Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Insight
    st.write("📌 **Insight:**")
    st.write("- Musim panas memiliki jumlah peminjaman tertinggi.")
    st.write("- Musim dingin memiliki jumlah peminjaman terendah, kemungkinan karena cuaca ekstrem.")

# --- Analisis 2: Jam Puncak Peminjaman ---
elif option == "Jam Puncak Peminjaman":
    st.subheader("⏰ Jam Puncak Peminjaman Sepeda")

    # Grupkan data berdasarkan jam
    hourly_counts = df.groupby("hr")["cnt"].mean().reset_index()

    # Visualisasi dengan Plotly
    fig = px.line(hourly_counts, x="hr", y="cnt", markers=True,
                  labels={"cnt": "Rata-rata Peminjaman", "hr": "Jam dalam Sehari"},
                  title="Tren Peminjaman Sepeda per Jam")

    # Menampilkan grafik di Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Insight
    st.write("📌 **Insight:**")
    st.write("- Peminjaman sepeda mencapai puncaknya pada jam **08:00 dan 17:00**.")
    st.write("- Pola ini menunjukkan bahwa banyak pengguna menggunakan sepeda untuk **perjalanan kerja**.")

# Footer
st.markdown("---")
st.markdown("📊 **Dashboard dibuat oleh [Jarro'un Nurul Faizah]** | 🚀 Data: Bike Sharing Dataset")
