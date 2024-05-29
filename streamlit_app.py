# Streamlitライブラリをインポート
import streamlit as st

# タイトルと説明
st.title('古文単語ガチャ')

st.write('古文単語をランダムに表示して、勉強をサポートします！')
st.write('がんばってください！')

# Load the data
@st.cache
def load_data():
    return pd.read_excel("古文単語リスト.xlsx")

st.latex("")


