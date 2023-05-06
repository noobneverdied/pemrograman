import streamlit as st

st.set_page_config(page_title = "TOTAL SOLID")

st.title("TOTAL SOLID")

st.header("Prinsip Kerja")
st.markdown("""Total suspended solid atau padatan tersuspensi total (TSS) adalah residu dari padatan total yang tertahan oleh saringan dengan ukuran partikel maksimal 2μm atau lebih besar dari ukuran partikel koloid. """)

st.header("Tujuan Praktikum : Untuk mengetahui total padatan tersuspensi")

st.header("Alat dan Bahan")
st.markdown("""1. Timbang pinggan penguap kosong yang telah dipanaskan di oven menggunakan neraca analitik
2. Kocok sampel air permukaan
3. Pipet 25 ml sampel air dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
4. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan penguap dengan alkohol
5. Masukkan pinggan penguap kedalam oven dan panaskan pada suhu 103-105°C selama 1 jam
6. Keluarkan pinggan penguap dan masukkan menit atau sampai dingin kedalam desikator sela 19/73
7. Timbang pinggan penguap yang sudah dingin.""")

# st.header("Cara Kerja")
# st.markdown("""1. Timbang pinggan penguap kosong yang telah dipanaskan di oven menggunakan neraca analitik
# 2. Kocok sampel air permukaan
# 3. Pipet 25 ml sampel air dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
# 4. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan penguap dengan alkohol
# 5. Masukkan pinggan penguap kedalam oven dan panaskan pada suhu 103-105°C selama 1 jam
# 6. Keluarkan pinggan penguap dan masukkan menit atau sampai dingin kedalam desikator sela 19/73
# 7. Timbang pinggan penguap yang sudah dingin.""")

st.header("Perhitungan")

st.latex(r'''
    Bobot TSS \left(\frac{mg}{ml}\right) = 
    \frac{\left(A-B\right) 1000}{volume sampel \left(ml\right)}
    ''')

st.markdown("""Keterangan: \n
A = Berat cawan berisi residu (mg) \n
B = Berat cawan kosong (mg) \n
1000 = Konversi dari mL ke L""")

