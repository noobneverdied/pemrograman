import streamlit as st

st.title('Perhitungan TS')

st.write('---')
st.title('TS')


A = st.number_input('Masukkan nilai berat cawan akhir + residu(mg)')
B = st.number_input('Masukkan nilai berat cawan (g)')
V = st.number_input('Masukkan nilai volume (mL)')

tombol = st.button('Hitung nilai TS')

if tombol:
    nilai_TS = (A-B) / V * 1000
    st.success(f'Nilai TS adalah {nilai_TS}')
    
    
st.write('---')
st.header('Baku Mutu Standar TS')
st.markdown("""Baku mutu standar TS dapat bervariasi tergantung pada kebutuhan dan regulasi yang berlaku di suatu daerah atau negara. Namun, umumnya baku mutu standar TS ditetapkan dalam satuan mg/L atau ppm (bagian per juta) dan berkisar antara 500-1000 mg/L untuk air permukaan dan 2000-4000 mg/L untuk limbah domestik dan industri.""")
