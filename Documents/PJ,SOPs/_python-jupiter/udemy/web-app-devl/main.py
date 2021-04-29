import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Python and Streamlit')


st.write('プログレスバーの表示')

'Start!'
latest_iteration = st.empty() #テキスト
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.03)
'Done!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


#エクスパンダー
expander1= st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1内容を書く')
expander2= st.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')
expander3= st.beta_expander('問い合わせ3')
expander3.write('問い合わせ内容を書く')