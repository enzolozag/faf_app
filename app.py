import streamlit as st

st.title('Hello fella')

video = open('SAOKO.mp4','rb')

video_bytes = video.read()
st.video(video_bytes)