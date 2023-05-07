import streamlit as st

st.title("""Perhitungan TDS""")

st.write('---')
st.title('TDS')

A = st.number_input('Masukkan berat cawan (g)')
B = st.number_input('Masukkan nilai berat sampel pada cawan (g)')
V = st.number_input('Masukkan volume sampel (mL)')

tombol = st.button('Hitung nilai TDS')

if tombol:
    nilai_TDS = ((B-A *1000)/(V/1000))
    st.success(f'Nilai TDS adalah {nilai_TDS}')
