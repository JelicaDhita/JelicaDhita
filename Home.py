import pickle
import streamlit as st
import pandas as pd

with st.sidebar:
    st.markdown("# Home page :oncoming_automobile:")
    st.write("Hello, I'm a Car Sales Price Prediction Dashboard!")
    st.write("Made by Group 1 Science :rocket:")
    
st.title(':car: Car Sales Price Prediction :oncoming_automobile: :scales:')
st.markdown(f"""
            <div style="text-align:center;">Tren konsumen yang cepat berubah, perubahan kondisi ekonomi, dan faktor-faktor eksternal lainnya membuat sulit untuk menghasilkan prediksi harga penjualan mobil yang akurat dengan metode tradisional. Solusi ini dirancang untuk menghasilkan prediksi harga penjualan mobil dengan tepat, produsen dan dealer mobil dapat memperoleh informasi tentang harga penjualan mobil secara akurat.
            </div>
        """, unsafe_allow_html=True)

