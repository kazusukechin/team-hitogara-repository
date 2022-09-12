import streamlit as st
from PIL import Image

st.title('MPP01')
st.caption('これはテストアプリです')

image = Image.open('./data/スクリーンショット01.png')
st.image(image,width = 150)
