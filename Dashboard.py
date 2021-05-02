# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 19:44:02 2021

@author: C.F_Lin
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandasql import sqldf

@st.cache
def load_data():
    df = pd.read_csv("C:/Users/C.F_Lin/Desktop/資料.csv")
    return df
#df.rename(columns={"單位代號": "Orgcode"},inplace=True)

df = load_data()
user = st.text_input("請輸入員編")
mapping = dict(zip(df["員編"],df["單位代號"]))
try:
    user_org = mapping[user]
    st.write(user,user_org)
    query = "SELECT 單位代號 FROM df WHERE 單位代號 LIKE \""+user_org+"%\";"
    org = st.selectbox(
        "選擇單位",list(sqldf(query)['單位代號'].unique()))
    graph_proceed = st.button("產生圖表")
    sns.set(font=['sans-serif'])
    sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})
    if graph_proceed:
        st.header("單位人力概況")
        df_org = sqldf("SELECT * FROM df WHERE 單位代號 LIKE \""+org+"%\";")
        df_summary = pd.DataFrame(columns=['單位','在職人數','留停人數','合計'])
        N_1 = len(df_org[df_org["在職狀況代碼"]==1])
        N_3 = len(df_org[df_org["在職狀況代碼"]==3])
        row = {'單位': org, '在職人數': N_1, '留停人數': N_3, '合計':N_1+N_3}
        df_summary = df_summary.append(row,ignore_index=True).set_index('單位')
        st.table(df_summary)
        df2 = sqldf("SELECT COUNT(員編) AS 人數,性別 FROM df_org GROUP BY 性別;"
    )
        fig,ax = plt.subplots()
        ax = sns.barplot(df2["性別"],df2["人數"]/df2["人數"].sum())
        ax.set_ylabel("")
        st.pyplot(fig)
        df3 = sqldf("SELECT COUNT(員編) AS 人數,職稱 FROM df_org GROUP BY 職稱;"
    )
        fig,ax = plt.subplots()
        ax = sns.barplot(df3["職稱"],df3["人數"]/df3["人數"].sum())
        ax.set_ylabel("")
        st.pyplot(fig)       
except:
    st.warning("查無此員編！")
