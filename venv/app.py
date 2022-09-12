import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

st.title('MPP01')
st.caption('これはテストアプリです')

col1, col2 = st.columns(2)

with col1:


    st.subheader('自己紹介')
    st.text('私はほにゃららです。')

    code =  '''
    import streamlit as st

    st.title('MPP01')
    '''
    st.code(code,language = 'python')

# # 画像
# image = Image.open('スクリーンショット01.png')
# st.image(image,width = 150)

# # 動画
# video_file = open('画面収録01.mov','rb')
# video_bytes = video_file.read()
# st.video(video_bytes)

    with st.form(key='profile_form'):
        # テキストボックス
        name = st.text_input('名前')
        address = st.text_input('住所')

        # セレクトボックス(st.radioでラジオ)
        age_category = st.selectbox(
            '年齢層',
            ('子供(18歳未満)', '大人(18歳以上)')
        )
        # 複数選択
        hobby = st.multiselect(
            '趣味',
            ('あ', 'い', 'う', 'え', 'お')
        )

        # チェックボックス
        mail_subscribe = st.checkbox('メルマガ購読する')
        # スライダー
        height = st.slider('身長', min_value=110, max_value=210)
        # #　日付???
        # start_date = st.date_input(
        #     '開始日',
        #     datetime.date(2022, 7, 1)
        # )

        # カラーピッカー
        color = st.color_picker('テーマカラー', '#00f900')


        # ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')

        if submit_btn:
            st.text(f'ようこそ！{name}さん！{address}に書籍を送りました!')
            st.text(f'あなたは{age_category}ですね')
            st.text(f'好きな母音:{",".join(hobby)}')


# # テキストボックス
# name = st.text_input('名前')
# print(name)

# # ボタン
# submit_btn = st.button('送信')
# cancel_btn = st.button('キャンセル')
# print(f'submitbtn:{submit_btn}')
# print(f'cancelbtn:{cancel_btn}')

# if submit_btn:
#     st.text(f'ようこそ！{name}さん！')

# # BMI
# weight = st.number_input('体重(kg)')
# length = st.number_input('身長(m)')

# if length != 0:
#     bmi = (weight/(length**2))
# else:
#     st.text(f'設定を行なってください')

# calculation_btn = st.button('計算')
# if calculation_btn:
#     st.text(f'あなたのBMIは{bmi}です。')
#     if (bmi > 25):
#         st.text(f'痩せましょう！')
#     elif (bmi < 18):
#         st.text(f'太りましょう！')
#     else:
#         st.text(f'あなたは健康体です')


with col2:
    # データ分析関連
    df = pd.read_csv('平均気温.csv', index_col='月')
    # st.dataframe(df)
    # st.table(df)
    st.line_chart(df)
    st.bar_chart(df['2021年'])


    # # matplotlib
    # fig, ax = plt.subplots()
    # ax.plot(df.index, df['2021年'])
    # ax.set_title('matplotlib graph')
    # st.pyplot(fig)