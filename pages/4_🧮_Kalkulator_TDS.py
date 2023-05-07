import streamlit as st

st.title("""Perhitungan TDS""")

st.write('---')
st.title('TDS')

A = st.number_input('Masukkan berat cawan (mg)')
B = st.number_input('Masukkan nilai berat sampel pada cawan (g)')
V = st.number_input('Masukkan volume sampel (mL)')

tombol = st.button('Hitung nilai TDS')

if tombol:
    nilai_TDS = (B-A) / V * 1000
    st.success(f'Nilai TDS adalah {nilai_TDS}')
    
st.write('---')
st.header('Baku Mutu Standar TDS')
st.markdown("""Baku mutu standar TDS dapat bervariasi tergantung pada kebutuhan dan regulasi yang berlaku di suatu daerah atau negara. Namun, umumnya baku mutu standar TDS ditetapkan dalam satuan mg/L atau ppm (bagian per juta) dan berkisar antara 500-1000 mg/L untuk air minum dan berkisar antara 1000-3000 mg/L untuk air permukaan dan limbah industri""")
