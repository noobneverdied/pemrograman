import streamlit as st

st.title("""Perhitungan TSS""")

st.write('---')
st.title('TSS')

A = st.number_input('Masukkan nilai berat kertas saring (mg) atau berat cawan + kertas saring')
B = st.number_input('Masukkan nilai berat sampel pada kertas saring (mg) atau berat cawan sampel + kertas saring residu setelah pemanasan')
V = st.number_input('Masukkan nilai volume sampel (L)')

tombol = st.button('Hitung nilai TSS')

if tombol:
    nilai_TSS = ((B-A)/V)*(100/100)
    st.success(f'Nilai TSS adalah {nilai_TSS}')
