# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('BMI計算')

weight=st.number_input("体重(kg)を入力",min_value=1)
height=st.number_input("身長(cm)を入力",min_value=1)


if st.button("計算:")
    st.write("あなたのBMIは"+str(w/h/100)**2)


