import streamlit as st

st.title("""Perhitungan TSS""")

st.write('---')
st.title('TSS')

A = st.number_input('Masukkan nilai berat kertas saring (mg) atau berat cawan + kertas saring')
B = st.number_input('Masukkan nilai berat sampel pada kertas saring (g) atau berat cawan sampel + kertas saring residu setelah pemanasan')
V = st.number_input('Masukkan nilai volume sampel (mL)')

tombol = st.button('Hitung nilai TSS')

if tombol:
    nilai_TSS = (B-A) / V * 1000
    st.success(f'Nilai TSS adalah {nilai_TSS}')

st.write('---')
st.header('Baku Mutu Standar TSS')
st.markdown("""Baku mutu standar TSS dapat berbeda-beda tergantung pada kebutuhan dan regulasi yang berlaku di suatu daerah atau negara. Namun, umumnya baku mutu standar TSS ditetapkan dalam satuan mg/L atau ppm (bagian per juta) dan berkisar antara 30-50 mg/L untuk air permukaan dan 100-300 mg/L untuk limbah domestik dan industri.""")
