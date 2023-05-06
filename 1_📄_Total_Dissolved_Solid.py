import streamlit as st

st.set_page_config(page_title = "TOTAL DISSOLVED SOLID")

st.title("TOTAL DISSOLVED SOLID")

st.header("Prinsip Kerja")
st.markdown("""Analisis Total Dissolved Solid atau residu terlarut dalam air permukaan dilakukan dengan cara menimbang berat residu sampel yang lolos dari kertas saring berpori< 0,45 μm dan telah dikeringkan pada suhu 103-105°C hingga diperoleh bobot tetap.""")

st.header("Tujuan Praktikum : Mengetabui kadar Toral Dissolved solid dalam laratan")

st.header("Alat dan Bahan")
st.markdown("""1. Pinggan penguap yang terbuat dari porselen atau platina atau silica berkualitas tinggi
2. Penangas air
3. Oven untuk pemanasan pada suhu 103-105°C 
4. Desikator
5. Neraca analitik
6. Pipet volumetrik 25 ml
7. Cawan Goch atau alat penyaring lain yang dilengkapi pengisap atau penekan
8. Kertas saring berpori 0,45 μm
9. Tempat khusus untuk menaruh kertas saring
10. Penjepit""")

st.header("Cara Kerja")
st.markdown("""1. Timbang pinggan penguap kosong yang telah di pansakan di oven menggunakan neraca analitik
2. Kocok sampel air permukaan
3. Saring sampel air
4. Pipet 25 ml filtrat hasil penyaringan dan masukkan ke dalam pinggan penguap kosong yang telah ditimbang
5. Panaskan dengan penangas air hingga kering, setelah kering lap bagian luar pinggan dengan alkohol
6. Masukkan pinggan penguap ke dalam oven dan panaskan pada suhu 103-105°C selama 1 jam
7. Keluarkan pinggan penguap dan masukkan ke dalam desikator selama 15 menit atau sampai dingin
8. Timbang pinggan penguap yang sudah dingin.""")

st.header("Perhitungan")

st.latex(r'''
    Bobot TDS \left(\frac{mg}{ml}\right) = 
    \frac{\left(A-B\right) 1000}{volume sampel \left(ml\right)}
    ''')

st.markdown("""Keterangan: \n
A = Berat cawan berisi residu terlatur dalam (mg) \n
B = Berat cawan kosong (mg) \n
1000 = Konversi dari mL ke L""")