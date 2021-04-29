#10 インタラクティブなウィジェット

import streamlit as st
import numpy as np
import pandas as pd

st.title('StreamLit entry class')

st.write('DataFrame')


#チェックボックスやスライダーなど
from PIL import Image
st.write('Display Image')

# #チェックボックス、trueの時に動作させる
if st.checkbox("Show Image"):
    img = Image.open('sample.jpg')
    st.image(img, caption='My Favorite', use_column_width=True)

# #セレクトボックス
option = st.selectbox(
    "あなたの好きな数字いれて",
    list(range(1, 11))
)
"あなたの好きな数字は、", option, "です"

#テキストボックス
option = st.text_input("趣味は？")
"あなたの趣味：", option

スライダー
condition = st.slider("あなたの調子は？", 0, 70, 35)
"コンディション：", condition
# 参考 API reference > display interactive widgets


