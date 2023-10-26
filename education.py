import pickle
import streamlit as st

model = pickle.load(open('estimasi-wages-by-education-in-the-usa.sav', 'rb'))

st.title('Estimasi Upah Sarjana Pendidikan di AS')

year = st.number_input('Input Tahun')
less_than_hs = st.number_input('Input kurang dari sekolah menengah atas')
high_school = st.number_input('Input sekolah menengah atas')
some_college = st.number_input('Input beberapa perguruan tinggi')
advanced_degree = st.number_input('Input gelar lanjutan')
men_less_than_hs = st.number_input(
    'Input laki laki kurang dari sekolah menengah atas')
men_high_school = st.number_input('Input laki laki sekolah menengah atas')
men_some_college = st.number_input('Input laki laki beberapa perguruan tinggi')
men_bachelors_degree = st.number_input('Input gelar sarjana laki-laki')
men_advanced_degree = st.number_input('Input gelar lanjutan laki laki')
women_less_than_hs = st.number_input(
    'Input perempuan kurang dari sekolah menengah atas')
women_high_school = st.number_input('Input perempuan sekolah menengah atas')
women_some_college = st.number_input(
    'Input perempuan beberapa perguruan tinggi')
women_bachelors_degree = st.number_input('Input gelar sarjana perempuan')
women_advanced_degree = st.number_input('Input gelar lanjutan perempuan')

predict = ''

if st.button('Estimasi Upah Sarjana Pendidikan di AS'):
    predict = model.predict(
        [[year, less_than_hs, high_school, some_college, advanced_degree, men_less_than_hs, men_high_school, men_some_college, men_bachelors_degree,
          men_advanced_degree, women_less_than_hs, women_high_school, women_some_college, women_bachelors_degree, women_advanced_degree]]
    )
    st.write('Estimasi Upah : ', predict)
