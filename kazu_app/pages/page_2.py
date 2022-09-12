import streamlit as st
import datetime

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
    # 日付???
    start_date = st.date_input(
        '開始日',
        datetime.date(2022, 7, 1)
    )

    # カラーピッカー
    color = st.color_picker('テーマカラー', '#00f900')


    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書籍を送りました!')
        st.text(f'あなたは{age_category}ですね')
        st.text(f'好きな母音:{",".join(hobby)}')
