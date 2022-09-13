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

# 以下をサイドバーに表示
st.sidebar.markdown("### 機械学習に用いるcsvファイルを入力してください")
# ファイルアップロード
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files=False)

if uploaded_files:
        df = pd.read_csv(uploaded_files)
        df_columns = df.columns
    
        st.markdown("### モデリング")
        # 説明変数は複数選択式
        # ex = st.multiselect("説明変数を選択してください（複数選択可）", df_columns)
        ex = ['変数1', '変数2', '変数3', '変数4']

        # 目的変数は一つ
        # ob = st.selectbox("目的変数を選択してください", df_columns)
        ob = ['目的関数']

        # 機械学習のタイプを選択する。
        # ml_menu = st.selectbox("実施する機械学習のタイプを選択してください", ["重回帰分析","ロジスティック回帰分析"])
        ml_menu = "ロジスティック回帰分析"

        # 機械学習のタイプにより以下の処理が分岐
        if ml_menu == "重回帰分析":
                st.markdown("#### 機械学習を実行します")
                execute = st.button("実行")
                
                lr = linear_model.LinearRegression()
                # 実行ボタンを押したら下記が進む
                if execute:
                        df_ex = df[ex]
                        df_ob = df[ob]
                        X_train, X_test, y_train, y_test = train_test_split(df_ex.values, df_ob.values, test_size = 0.3)
                        lr.fit(X_train, y_train)
                        # プログレスバー（ここでは、やってる感だけ）
                        my_bar = st.progress(0)
                        
                        for percent_complete in range(100):
                                time.sleep(0.02)
                                my_bar.progress(percent_complete + 1)
                        
                        # metricsで指標を強調表示させる
                        col1, col2 = st.columns(2)
                        col1.metric(label="トレーニングスコア", value=lr.score(X_train, y_train))
                        col2.metric(label="テストスコア", value=lr.score(X_test, y_test))
                  
    # ロジスティック回帰分析を選択した場合
        elif ml_menu == "ロジスティック回帰分析":
                st.markdown("#### 機械学習を実行します")
                execute = st.button("実行")
                
                lr = LogisticRegression()

                # hensu_1 = st.number_input('変数1')
                # hensu_2 = st.number_input('変数2')
                # hensu_3 = st.number_input('変数3')
                # hensu_4 = st.number_input('変数4')
                hensu_1 = 4
                hensu_2 = 5
                hensu_3 = 6
                hensu_4 = 7
                aim = st.number_input('目的関数')

                # 実行ボタンを押したら下記が進む
                if execute:
                        df_ex = df[ex]
                        df_ob = df[ob]
                        # X_train, X_test, y_train, y_test = train_test_split(df_ex.values, df_ob.values, test_size = 0.3)
                        X_train = df_ex.values
                        y_train = df_ob.values
                        X_test = pd.DataFrame([], columns=['変数1', '変数2', '変数3', '変数4'])
                        record = pd.Series([hensu_1, hensu_2, hensu_3, hensu_4], index=X_test.columns)
                        X_test = X_test.append(record, ignore_index=True)

                        

                        lr.fit(X_train, y_train)
                        pred_probs = lr.predict(X_test)
                        st.write(pred_probs)
                        y_test = [pred_probs[0]]

                        # プログレスバー（ここでは、やってる感だけ）
                        my_bar = st.progress(0)
                        for percent_complete in range(100):
                                time.sleep(0.02)
                                my_bar.progress(percent_complete + 1)

                        col1, col2 = st.columns(2)
                        col1.metric(label="トレーニングスコア", value=lr.score(X_train, y_train))
                        col2.metric(label="テストスコア", value=lr.score(X_test, y_test))

                        ### 結果出力
                        st.write(pred_probs[0])
