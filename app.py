import streamlit as st
#halaman utama
st.title ('aplikasi perhitungan luas bangun datar')
st.header('buatan anak sistem informasi')

menu = st.sidebar.selectbox('Menu', ['luas persegi','luas segitiga','luas lingkaran'])
if menu == 'luas persegi':
    st.write('halaman untuk menghitung luas persegi')
    st.image('https://awsimages.detik.net.id/community/media/visual/2022/11/09/keliling-persegi_169.jpeg?w=600&q=90', caption='gambar persegi')
    sisi = st.number_input('silahkan masukan sisi', min_value=0,)
    if st.button('hitung'):
        luas = sisi * sisi
        st.write(f'luas persegi adalah {luas}')
    
    
elif menu == 'luas segitiga':
    st.write('halaman untuk menghitung luas segitiga')
elif menu == 'luas lingkaran':
    st.write('halaman untuk menghitung luas lingkaran')
    