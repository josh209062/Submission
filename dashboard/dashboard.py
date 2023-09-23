import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
sns.set(style='dark')
print('Pandas Version: ',pd.__version__)
print('Seaborn version: ',sns.__version__)
print('Streamlit Version', st.__version__)
print('Numpy Version', np.__version__)
def workingday_df(df):
    workingday = df.groupby(by='workingday').cnt.sum().reset_index()
    workingday.rename(columns={'cnt':'sum'}, inplace=True)

    return workingday.sort_values(by='sum', ascending=False)

def holiday_df(df):
    holiday = df.groupby(by='holiday').cnt.sum().reset_index()
    holiday.rename(columns={'cnt':'sum'}, inplace=True)

    return holiday.sort_values(by='sum', ascending=False)

def weathersit_df(df):
    weathers = df.groupby(by='weathersit').cnt.sum().reset_index()
    weathers.rename(columns={'cnt':'sum'}, inplace=True)

    return weathers.sort_values(by='sum', ascending=False)

def season_df(df): 
    seasons = df.groupby(by='season').cnt.sum().reset_index()
    seasons.rename(columns={'cnt':'sum'}, inplace=True)

    return seasons.sort_values(by='sum', ascending=False)

def month_df(df):
    months = df.groupby(by='mnth').cnt.sum().reset_index()
    months.rename(columns={'cnt':'sum'}, inplace=True) 

    return months.sort_values(by='sum', ascending=False)

def sidebar(df):
    df['dteday'] = pd.to_datetime(df['dteday'])
    min = df['dteday'].min()
    max = df['dteday'].max()

    with st.sidebar:
        #st.image('#')
        def on_change():
            st.session_state.date = date

        date = st.date_input(
            label="Pilih Rentang Waktu",
            min_value=min,
            max_value=max,
            value=[min, max],
            on_change=on_change
        )
    return date

def workingday_chart(df):
    st.subheader('Penggunaan Bike-Sharing berdasarkan Working Day')
    df['sum'] = df['sum'] / 1000
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x='workingday',
        y='sum',
        data = df,
        ax=ax
    )
    ax.set_title("Nuber of Bike-Sharing by Working Day \n in thousand", loc="center", fontsize=30)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=30)
    st.pyplot(fig)

def holiday_chart(df):
    st.subheader('Penggunaan Bike-Sharing berdasarkan Holiday')
    df['sum'] = df['sum'] / 1000
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x='holiday',
        y='sum',
        data = df,
        ax=ax
    )
    ax.set_title("Nuber of Bike-Sharing by Holiday \n in thousand", loc="center", fontsize=30)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=30)
    st.pyplot(fig)

def weathersit_chart(df):
    st.subheader('Penggunaan Bike-Sharing berdasarkan Weathersit')
    df['sum'] = df['sum'] / 1000
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x='sum',
        y='weathersit',
        data = df,
        ax=ax
    )
    ax.set_title("Nuber of Bike-Sharing by Weathersit \n in thousand", loc="center", fontsize=30)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=30)
    st.pyplot(fig)

def season_chart(df):
    st.subheader('Penggunaan Bike-Sharing berdasarkan Season')
    fig, ax = plt.subplots(figsize=(20, 10))

    plt.pie(
        x='sum',
        labels='season',
        data = df
    )
    plt.title("Nuber of Bike-Sharing by Season \n in thousand", loc="center", fontsize=30)
    st.pyplot(fig)

def month_chart(df):
    st.subheader('Penggunaan Bike-Sharing berdasarkan Month')
    df['sum'] = df['sum'] / 1000
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.barplot(
        x='mnth',
        y='sum',
        data = df,
        ax=ax
    )
    ax.set_title("Nuber of Bike-Sharing by Month \n in thousand", loc="center", fontsize=30)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=30)
    st.pyplot(fig)

df = pd.read_csv('dashboard/data_clean.csv')

date = sidebar(df)

if(len(date) == 2):
    main_df = df[(df["dteday"] >= str(date[0])) & (df["dteday"] <= str(date[1]))]
else:
    main_df = df[(df["dteday"] >= str(st.session_state.date[0])) & (df["dteday"] <= str(st.session_state.date[1]))]

st.header(':sparkles: Dashboard Bike-Sharing :sparkles:')

working_day_df = workingday_df(main_df)
workingday_chart(working_day_df)

holi_day_df = holiday_df(main_df)
holiday_chart(holi_day_df)

weathersits_df = weathersit_df(main_df)
weathersit_chart(weathersits_df)

seasons_df = season_df(main_df)
season_chart(seasons_df)

months_df = month_df(main_df)
month_chart(months_df)
