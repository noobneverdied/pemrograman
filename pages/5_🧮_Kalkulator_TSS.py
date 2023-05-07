import streamlit as st

st.title("""Perhitungan TSS""")

st.write('---')
st.title('TSS')

A = st.number_input('Masukkan nilai berat kertas saring (g) atau berat cawan + kertas saring')
B = st.number_input('Masukkan nilai berat sampel pada kertas saring (g) atau berat cawan sampel + kertas saring residu setelah pemanasan')
V = st.number_input('Masukkan nilai volume sampel (mL)')

tombol = st.button('Hitung nilai TSS')

if tombol:
    nilai_TSS = ((B-A*1000)/(V/1000))
    st.success(f'Nilai TSS adalah {nilai_TSS}')
