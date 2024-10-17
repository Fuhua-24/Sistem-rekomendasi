import streamlit as st 
import pickle
import requests

jurnal = pickle.load(open("jurnal_list.pkl", 'rb'))
similariti = pickle.load(open("similarity.pkl", 'rb'))
jurnal_list=jurnal['title'].values

st.header("rekomendasi Jurnal")
selectvalue=st.selectbox("select jurnal from dropdown", jurnal_list)