import streamlit as st

st.title("Selamat Datang di Web New York Informatika")
st.write(
    "ngoding seru bersama Zaina Valerie"
)
st.image("0c934f12-60da-4204-9bd5-61536b770ce1.jpeg")

st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
    
