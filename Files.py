import streamlit as st
import pandas as pd

#-------------------------------------------------------------------

st.subheader('Uploading CSV File')
df=st.file_uploader('Upload the csv file: ', type=['csv','xlsx'])


st.subheader('Loading CSV File')
df=pd.read_csv('Products.csv')
st.write('first 5 rows: \n')

# check if file exists then show.

if df is not None:
    st.table(df.head())

#st.write('All rows: \n')
#st.table(df)
    
#-------------------------------------------------------------------


st.subheader('Loading image File')
st.image('img.png')

st.subheader('Uploading image File')
img_file=st.file_uploader('Upload the image file: ', type=['png','jpeg'])

if img_file is not None:
    st.image(img_file)
    
#-------------------------------------------------------------------

st.subheader('Uploading video File')
video_file=st.file_uploader('Upload the video file: ', type=['mkv','mp4'])

if video_file is not None:
    st.video(video_file,start_time= 0)

#-------------------------------------------------------------------

st.subheader('Uploading Audio File')
audio_file=st.file_uploader('Upload the Audio file: ', type=['mp3','wav'])

if audio_file is not None:
    st.audio(audio_file.read())

#-------------------------------------------------------------------
