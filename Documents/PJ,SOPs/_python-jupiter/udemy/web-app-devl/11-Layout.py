import streamlit as st
import numpy as np
import pandas as pd

st.title('Python and Streamlit')

#サイドバー
"""
st.sideber.write('レイアウト')
text = st.sidebar.text_input('あなたの趣味は')
condition = st.sidebar.slider('あなたの調子は', 0, 100, 50)

'あなたの趣味：', text
'コンディション：', condition 
"""

#2列表示
"""
st.write('レイアウト')

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
"""

#エクスパンダー
expander1= st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1内容を書く')
expander2= st.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')
expander3= st.beta_expander('問い合わせ3')
expander3.write('問い合わせ内容を書く')