import streamlit as st

st.title("""Perhitungan TDS""")

st.write('---')
st.title('TDS')

A = st.number_input('Masukkan berat cawan (mg)')
B = st.number_input('Masukkan nilai berat sampel pada cawan (mg)')
V = st.number_input('Masukkan volume sampel (L)')

tombol = st.button('Hitung nilai TDS')

if tombol:
    nilai_TDS = ((B-A)/V)*(100/100)
    st.success(f'Nilai TDS adalah {nilai_TDS}')
