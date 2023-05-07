import streamlit as st

st.title('Perhitungan TS')

st.write('---')
st.title('TS')


A = st.number_input('Masukkan nilai berat cawan akhir + residu(g)')
B = st.number_input('Masukkan nilai berat cawan (g)')
V = st.number_input('Masukkan nilai volume (mL)')

tombol = st.button('Hitung nilai TS')

if tombol:
    nilai_TS = ((A-B*1000)/(v/1000)
    st.success(f'Nilai TS adalah {nilai_TS}')
