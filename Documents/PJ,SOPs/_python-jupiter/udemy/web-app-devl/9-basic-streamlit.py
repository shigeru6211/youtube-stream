import streamlit as st
import numpy as np
import pandas as pd

st.title('StreamLit entry class')

st.write('DataFrame')

#df = pd.DataFrame({
#    '1列目': [1,2,3,4],
#   '2列目': [10,20,30,40]
#})

# Dynamicな表にはwrite/dataframe
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
# dataframeの方がオプションが多い
# st.dataframe(df.style.highlight_max(axis=0))

# Staticな表にはtable
# st.table(df.style.highlight_max(axis=0))

# Magic Command（マジックコマンド）
# Double quatation3つでテキストを書ける
# """
# # 章
# ## 節
# ### 項

# # Back quatationを3つで、コードの書式になる（Markdown表記）
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# グラフを書く（Chart）
# df = pd.DataFrame(
#     np.random.rand(20, 3), #縦20横3で乱数を入れる
#     columns=['a', 'b', 'c']
# )

# st.line_chart(df) #折れ線グラフ
# st.area_chart(df) #面グラフ
# st.bar_chart(df) #棒グラフ


# マップ
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69, 130.70], #縦20横3で乱数を入れる
#     columns=['lat', 'lon'] #緯度と経度をとる
# )
# # 
# st.map(df)

# #画像の表示
# from PIL import Image
# st.write('Display Image')

# img = Image.open('sample.jpg')
# st.image(img, caption='My Favorite', use_column_width=True)
# #参考 API reference > Display Media

