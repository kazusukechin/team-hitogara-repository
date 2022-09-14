import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import csv
import time
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import base64

st.title('機械学習による予測パート')
st.write('# 結果')

# 以下サイドバー部分
st.sidebar.markdown("### 機械学習に用いるcsvファイルを入力してください")
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files=False)

if uploaded_files:

    st.sidebar.write("## 以下の情報を入力してください")
    weight = st.sidebar.number_input('体重(kg)', 10, 300, 60)
    height = st.sidebar.number_input('身長(cm)', 10, 300, 170)
    bmi = (weight / (height**2 / 10000))

    st.sidebar.write("### 飲酒量")
    al_5per_500ml = st.sidebar.slider('5%500ml(缶)', 0, 30, 1)
    al_5per_350ml = st.sidebar.slider('5%350ml(缶)', 0, 30, 1)
    al_wine = st.sidebar.number_input('ワイン(ml)', 0, 10000, 0)

    al_total = al_5per_500ml * 5 * 5 + al_5per_350ml * 3.5 * 5 + al_wine * 0.15
    # al_in_body_per = al_total / 833 / weight / 10

    # モデリング
    df = pd.read_csv(uploaded_files)
    df_columns = df.columns
    # これで何回目か測ることができる
    csv_len = len(df)
    ex = ['体重', '身長', 'BMI', '5%ロング缶', '5%ショート缶', 'ワイン', '総アルコール量']
    ob = ['血中アルコール濃度']

    execute = st.sidebar.button("情報入力完了")
    lr = linear_model.LinearRegression()

    # 予測機器
    if execute:
        # 学習
        df_ex = df[ex]
        df_ob = df[ob]
        X_train = df_ex.values
        y_train = df_ob.values
        # 予測
        X_test = pd.DataFrame([], columns=['体重', '身長', 'BMI', '5%ロング缶', '5%ショート缶', 'ワイン', '総アルコール量'])
        record = pd.Series([weight, height, bmi, al_5per_500ml, al_5per_350ml, al_wine, al_total], index=X_test.columns)
        X_test = X_test.append(record, ignore_index=True)
        lr.fit(X_train, y_train)
        y_pred = lr.predict(X_test)
        st.write('あなたの血中アルコール濃度はおそらく', y_pred[0][0], '%ほどです。')

        # 症状提言
        if (y_pred[0][0] < 0.02):
            drunk_stage = 'のみたりてない期'
            shoujyou = '飲み足りていない'
        elif (y_pred[0][0] < 0.05) and (y_pred[0][0] >= 0.02):
            drunk_stage = '爽快期'
            shoujyou = '爽やかな気分になる、皮膚が赤くなる、陽気になる、判断力が少し鈍る'
        elif (y_pred[0][0] < 0.1) and (y_pred[0][0] >= 0.05):
            drunk_stage = 'ほろ酔い期'
            shoujyou = 'ほろ酔い気分になる、手の動きが活発になる、理性が失われる、体温が上がる、脈がはやくなる'
        elif (y_pred[0][0] < 0.15) and (y_pred[0][0] >= 0.1):
            drunk_stage = '酩酊初期'
            shoujyou = '気が大きくなる、大声でがなりたてる、怒りっぽくなる、立てばふらつく'
        elif (y_pred[0][0] < 0.30) and (y_pred[0][0] >= 0.15):
            drunk_stage = '酩酊期'
            shoujyou = '千鳥足になる、何度も同じことを喋る、呼吸が速くなる、吐き気がおこる'
        elif (y_pred[0][0] < 0.40) and (y_pred[0][0] >= 0.30):
            drunk_stage = '泥酔期'
            shoujyou = 'まともに立てない、記憶がはっきりしない、言葉がめちゃくちゃになる'
        elif (y_pred[0][0] < 0.50) and (y_pred[0][0] >= 0.40):
            drunk_stage = '昏睡期'
            shoujyou = '揺り動かしても起きない、大小便は垂れ流し、呼吸はゆっくりと深い、死亡'
        else:
            drunk_stage = '非常に危ない状態'
            shoujyou = '死亡。いますぐ救急車を呼んでください。'
        st.write('あなたは今', drunk_stage, 'です。')
        st.write('以下のような症状が見られるはずです。')
        st.write(shoujyou)

        # dfに行追加
        y_pred = float(y_pred)
        df.loc[csv_len] = [weight, height, bmi, al_5per_500ml, al_5per_350ml, al_wine, al_total, y_pred]

        # df.to_csv("data_al.csv")
        csv_al = df.to_csv(index=False)  
        b64 = base64.b64encode(csv_al.encode()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="result.csv">download</a>'
        st.markdown(f"ダウンロードする {href}", unsafe_allow_html=True)
