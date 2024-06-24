#!/usr/bin/env python
# coding: utf-8

# # Library

# In[35]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.dates as mdates
import datetime
sns.set(style='dark')


# # Data Frame

# ## All Data

# In[7]:


all_data = pd.read_csv("https://raw.githubusercontent.com/Topofajar/Bangkit_Proyek-Analisis-Data_Topofajar/main/Bangkit_Dashbord/all_data%20(7).csv")
all_data.tail()


# In[8]:


# Mengurutkan all_data berdasarkan date time
all_data.sort_values(by="datetime", inplace=True)
all_data.reset_index(inplace=True)
all_data.head(10)


# # Data Frame Total Polutaan

# In[37]:


polutan_name = ["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"]
station = ["Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan", "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", "Wanliu", "Wanshouxigong"]
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'brown', 'pink', 'teal', 'lime']
number_sta = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)


# In[10]:


def create_df_total_polutan(data) :
    df_total_polutan = data.groupby(['year','station']).sum()
    df_total_polutan.reset_index(inplace=True)
    df_total_polutan = pd.melt(df_total_polutan, id_vars=['year', 'station'], value_vars=polutan_name,
                        var_name='pollutant', value_name='sum_value')
    return df_total_polutan


# In[11]:


df_total_polutan = create_df_total_polutan(all_data)


# ## Data Frame Tren PM2.5 dan PM10

# In[12]:


month_tren_df = all_data[(all_data["datetime"] >= "2017-02-01 02:00:00") & 
                (all_data["datetime"] <= "2017-02-28 02:00:00")]
week_tren_df = all_data[(all_data["datetime"] >= "2017-02-21 02:00:00") & 
                (all_data["datetime"] <= "2017-02-28 02:00:00")]


# # Komponen Filter

# In[43]:


with st.sidebar:
    # Menambahkan logo
    st.image("https://raw.githubusercontent.com/mff29/AnalisisDataWithPython-Fuad/main/logo.jpeg")

    # Feedback
    text = st.text_area("Bagaimana kualitas udara di lingkungan sekitarmu?")
    st.write(text)
    


# # Pembuatan Dashboard

# ## Tren Polusi semua tahun

# In[24]:


def visual_tahunan(loc):
    fig, ax = plt.subplots(figsize=(12, 5))
    filtered_df = df_total_polutan[df_total_polutan['station'] == loc]
    sns.barplot(data=filtered_df, x="year", y="sum_value", hue="pollutant", ax=ax, errwidth=0)

    # Menambahkan judul dan label sumbu
    ax.set_title('Total Polutan per tahun di '+loc)
    ax.set_xlabel('Tahun', size=13)
    ax.set_ylabel('Total Konsentrasi (ug/m^3)', size=13)
    ax.legend()

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)


# In[44]:


def tren_tahunan():
    st.subheader('Pantauan Polusi Udara Tahunan')
    st.subheader('Pilih Kota :')
    col1, col2, col3 = st.columns(3)

    with col1:
        Aotizhongxin = st.checkbox('Aotizhongxin')
        Dingling = st.checkbox('Dingling')
        Changping = st.checkbox('Changping')
        Dongsi = st.checkbox('Dongsi')

    with col2:
        Guanyuan = st.checkbox('Guanyuan')
        Gucheng = st.checkbox('Gucheng')
        Huairou = st.checkbox('Huairou')
        Nongzhanguan = st.checkbox('Nongzhanguan')

    with col3:
        Shunyi = st.checkbox('Shunyi')
        Tiantan = st.checkbox('Tiantan')
        Wanliu = st.checkbox('Wanliu')
        Wanshouxigong = st.checkbox('Wanshouxigong')
        

    if Aotizhongxin:
        visual_tahunan("Aotizhongxin")
        
    if Dingling:
        visual_tahunan("Dingling")
        
    if Changping:
        visual_tahunan("Changping")
    
    if Dongsi:
        visual_tahunan("Dongsi")
        
    if Guanyuan:
        visual_tahunan("Guanyuan")
        
    if Gucheng:
        visual_tahunan("Gucheng")
        
    if Huairou:
        visual_tahunan("Huairou")
        
    if Nongzhanguan:
        visual_tahunan("Nongzhanguan")
        
    if Shunyi:
        visual_tahunan("Shunyi")
    
    if Tiantan:
        visual_tahunan("Tiantan")
        
    if Wanliu:
        visual_tahunan("Wanliu")
        
    if Wanshouxigong:
        visual_tahunan("Wanshouxigong")


# ## Tren Polutan PM2.5 & PM10

# In[41]:


def visual_tren_bulan (name_polut) :
    fig, ax = plt.subplots(figsize=(12, 5))
    for i,loc in zip(number_sta,station):
        filtered_df = month_tren_df[month_tren_df['station'] == loc]
        plt.plot(filtered_df['datetime'], filtered_df[name_polut], label=loc,color=colors[i % len(colors)])

    plt.title('Tren Konsentrasi '+name_polut+' Bulan Februari 2017', size=20)
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xlabel('Date',size=13)
    plt.ylabel('Konsentrasi '+name_polut+' (ug/m^3)',size=13)
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)

def visual_tren_minggu (name_polut) :
    fig, ax = plt.subplots(figsize=(12, 5))
    for i,loc in zip(number_sta,station):
        filtered_df = week_tren_df[week_tren_df['station'] == loc]
        plt.plot(filtered_df['datetime'], filtered_df[name_polut], label=loc,color=colors[i % len(colors)])

    plt.title('Tren Konsentrasi '+name_polut+' Minggu Ini', size=20)
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xlabel('Date',size=13)
    plt.ylabel('Konsentrasi '+name_polut+' (ug/m^3)',size=13)
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)


# In[15]:


def tren_PM25 ():
    st.subheader('Treen Polutan PM2.5 Bulan Februari 2017')
    col1, col2 = st.columns(2)

    with col1:
        total_pol = month_tren_df['PM2.5'].sum()
        st.metric("Total Polutan", value=round(total_pol, 2))

    with col2:
        mean_pol = month_tren_df['PM2.5'].mean()
        st.metric("Rata-Rata Polutan", value=round(mean_pol, 2))

    Bulanan = st.checkbox('Report PM2.5 satu bulan terakhir')
    Mingguan = st.checkbox('Report PM2.5 satu minggu terakhir')

    if Bulanan:
        visual_tren_bulan ('PM2.5')

    if Mingguan:
        visual_tren_minggu ('PM2.5')


# In[42]:


def tren_PM10():
    st.subheader('Treen Polutan PM10 Bulan Februari 2017')
    col1, col2 = st.columns(2)

    with col1:
        total_pol = month_tren_df['PM10'].sum()
        st.metric("Total Polutan", value=round(total_pol, 2))

    with col2:
        mean_pol = month_tren_df['PM10'].mean()
        st.metric("Rata-Rata Polutan", value=round(mean_pol, 2))

    Bulanan1 = st.checkbox('Report PM10 satu bulan terakhir')
    Mingguan1 = st.checkbox('Report PM10 satu minggu terakhir')

    if Bulanan1:
        visual_tren_bulan ('PM10')

    if Mingguan1:
        visual_tren_minggu ('PM10')


# ## Tab

# In[ ]:


st.title('Pantauan Polusi Udara')
tab1, tab2, tab3 = st.tabs(["Tren PM2.5", "Tren PM10", "Tren Tahunan"])
 
with tab1:
    tren_PM25()
with tab2:
    tren_PM10() 
with tab3:
    tren_tahunan()

