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
from sklearn.preprocessing import LabelEncoder

st.title('MVP01')
st.caption('これは最初のプロトタイプです')

# # 以下をサイドバーに表示
# st.sidebar.markdown("### 機械学習に用いるcsvファイルを入力してください")
# # ファイルアップロード
# uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files=False)

# if uploaded_files:
#     df = pd.read_csv(uploaded_files)
#     df_columns = df.columns
#     # データフレームを表示
#     st.markdown("### 入力データ")
#     st.dataframe(df.style.highlight_max(axis=0))
#     # matplotlibで可視化。X軸,Y軸を選択できる
#     st.markdown("### 可視化 単変量")
#     # データフレームのカラムを選択オプションに設定する
#     x = st.selectbox("X軸", df_columns)
#     y = st.selectbox("Y軸", df_columns)
#     # 選択した変数を用いてmtplotlibで可視化
#     fig = plt.figure(figsize=(12, 8))
#     plt.scatter(df[x], df[y])
#     plt.xlabel(x, fontsize=18)
#     plt.ylabel(y, fontsize=18)
#     st.pyplot(fig)

#     # seabornのペアプロットで可視化。複数の変数を選択できる。
#     st.markdown("### 可視化 ペアプロット")
#     # データフレームのカラムを選択肢にする。複数選択
#     item = st.multiselect("可視化するカラム", df_columns)
#     # 散布図の色分け基準を１つ選択する。カテゴリ変数を想定
#     hue = st.selectbox("色の基準", df_columns)
    
#     # 実行ボタン（なくてもよいが、その場合、処理を進めるまでエラー画面が表示されてしまう）
#     execute_pairplot = st.button("ペアプロット描画")
#     # 実行ボタンを押したら下記を表示
#     if execute_pairplot:
#             df_sns = df[item]
#             df_sns["hue"] = df[hue]
            
#             # streamlit上でseabornのペアプロットを表示させる
#             fig = sns.pairplot(df_sns, hue="hue")
#             st.pyplot(fig)


#     st.markdown("### モデリング")
#     # 説明変数は複数選択式
#     ex = st.multiselect("説明変数を選択してください（複数選択可）", df_columns)

#     # 目的変数は一つ
#     ob = st.selectbox("目的変数を選択してください", df_columns)

#     # 機械学習のタイプを選択する。
#     ml_menu = st.selectbox("実施する機械学習のタイプを選択してください", ["重回帰分析","ロジスティック回帰分析"])
    
#     # 機械学習のタイプにより以下の処理が分岐
#     if ml_menu == "重回帰分析":
#             st.markdown("#### 機械学習を実行します")
#             execute = st.button("実行")
            
#             lr = linear_model.LinearRegression()
#             # 実行ボタンを押したら下記が進む
#             if execute:
#                   df_ex = df[ex]
#                   df_ob = df[ob]
#                   X_train, X_test, y_train, y_test = train_test_split(df_ex.values, df_ob.values, test_size = 0.3)
#                   lr.fit(X_train, y_train)
#                   # プログレスバー（ここでは、やってる感だけ）
#                   my_bar = st.progress(0)
                  
#                   for percent_complete in range(100):
#                         time.sleep(0.02)
#                         my_bar.progress(percent_complete + 1)
                  
#                   # metricsで指標を強調表示させる
#                   col1, col2 = st.columns(2)
#                   col1.metric(label="トレーニングスコア", value=lr.score(X_train, y_train))
#                   col2.metric(label="テストスコア", value=lr.score(X_test, y_test))
                  
#     # ロジスティック回帰分析を選択した場合
#     elif ml_menu == "ロジスティック回帰分析":
#             st.markdown("#### 機械学習を実行します")
#             execute = st.button("実行")
            
#             lr = LogisticRegression()

#             # 実行ボタンを押したら下記が進む
#             if execute:
#                 df_ex = df[ex]
#                 df_ob = df[ob]
#                 X_train, X_test, y_train, y_test = train_test_split(df_ex.values, df_ob.values, test_size = 0.3)
#                 lr.fit(X_train, y_train)
#                 # プログレスバー（ここでは、やってる感だけ）
#                 my_bar = st.progress(0)
#                 for percent_complete in range(100):
#                         time.sleep(0.02)
#                         my_bar.progress(percent_complete + 1)

#                 col1, col2 = st.columns(2)
#                 col1.metric(label="トレーニングスコア", value=lr.score(X_train, y_train))
#                 col2.metric(label="テストスコア", value=lr.score(X_test, y_test))

# 入力フォーム
st.subheader('以下を入力してください')

with st.form(key='profile_form'):
    weight = st.number_input('体重(kg)')
    long_5per = st.number_input('5%ロング缶(500ml)')
    short_5per = st.number_input('5%ショート缶(350ml)')
    long_7per = st.number_input('7%ロング缶(500ml)')
    short_7per = st.number_input('7%ショート缶(350ml)')
    long_9per = st.number_input('9%ロング缶(500ml)')
    short_9per = st.number_input('9%ショート缶(350ml)')
    calculation_btn = st.form_submit_button('計算')
    cancel_btn = st.form_submit_button('キャンセル')

    alcohol_sum = long_5per*500*5+short_5per*350*5+long_7per*500*7+short_7per*350*7+long_9per*500*9+short_9per*350*9
    if weight != 0:
        alcohol_per_inbody = alcohol_sum/833/weight/10

    if calculation_btn:
        st.text(f'あなたのアルコール血中濃度は{alcohol_per_inbody}%です。')
        if (alcohol_per_inbody < 0.02):
            drunk_stage = 'のみたりてない期'
            shoujyou = '飲み足りていない'
        elif (alcohol_per_inbody < 0.05) and (alcohol_per_inbody >= 0.02):
            drunk_stage = '爽快期'
            shoujyou = '爽やかな気分になる、皮膚が赤くなる、陽気になる、判断力が少し鈍る'
        elif (alcohol_per_inbody < 0.1) and (alcohol_per_inbody >= 0.05):
            drunk_stage = 'ほろ酔い期'
            shoujyou = 'ほろ酔い気分になる、手の動きが活発になる、理性が失われる、体温が上がる、脈がはやくなる'
        elif (alcohol_per_inbody < 0.05) and (alcohol_per_inbody >= 0.02):
            drunk_stage = '酩酊初期'
            shoujyou = '気が大きくなる、大声でがなりたてる、怒りっぽくなる、立てばふらつく'
        elif (alcohol_per_inbody < 0.05) and (alcohol_per_inbody >= 0.02):
            drunk_stage = '酩酊期'
            shoujyou = '千鳥足になる、何度も同じことを喋る、呼吸が速くなる、吐き気がおこる'
        elif (alcohol_per_inbody < 0.05) and (alcohol_per_inbody >= 0.02):
            drunk_stage = '泥酔期'
            shoujyou = 'まともに立てない、記憶がはっきりしない、言葉がめちゃくちゃになる'
        elif (alcohol_per_inbody < 0.05) and (alcohol_per_inbody >= 0.02):
            drunk_stage = '昏睡期'
            shoujyou = '揺り動かしても起きない、大小便は垂れ流し、呼吸はゆっくりと深い、死亡'
        st.text(f'あなたは今{drunk_stage}です。以下のような症状が見られるはずです。')
        st.text(f'{shoujyou}')
        with open('./data/記録.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow([weight, alcohol_per_inbody, drunk_stage])
        if alcohol_per_inbody >= 0.5:
            st.text(f'あなたは飲み過ぎです。いますぐ病院に行きましょう')


