import streamlit as st

st.title('Perhitungan TS')

st.write('---')
st.title('TS')


A = st.number_input('Masukkan nilai berat cawan akhir + residu(mg)')
B = st.number_input('Masukkan nilai berat cawan (mg)')
V = st.number_input('Masukkan nilai volume (L)')

tombol = st.button('Hitung nilai TS')

if tombol:
    nilai_TS = ((A-B)/V)*(100/100)
    st.success(f'Nilai TS adalah {nilai_TS}')
