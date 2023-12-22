import pickle
import streamlit as st
import pandas as pd

with st.sidebar:
    st.markdown("# Prediksi :oncoming_automobile:")
    st.write("Hello, I'm a Car Sales Price Prediction Dashboard!")
    st.write("Made by Group 1 Science :rocket:")

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title(':car: Car Sales Price Prediction :oncoming_automobile:')
st.markdown(":oncoming_automobile: Mari Kita Memprediksi Harga Mobil :oncoming_automobile:")

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Km Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input Engine Size')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi harga mobil bekas dalam Ponds: ', predict)
    st.write ('Estimasi harga mobil bekas dalam IDR (Juta): ',predict*19643)
