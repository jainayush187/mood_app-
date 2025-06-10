import streamlit as st
import datetime

st.title("😊 My Interactive Mood App")

if 'mood_log' not in st.session_state:
    st.session_state.mood_log = []

mood = st.radio("आपका आज का मूड कैसा है?", ("😊 Happy", "😢 Sad", "😐 Neutral"))

if st.button("सेव करें"):
    today = datetime.date.today().strftime("%d-%m-%Y")
    st.session_state.mood_log.append({"date": today, "mood": mood})
    st.success(f"आपका मूड '{mood}' सेव हो गया!")

if st.session_state.mood_log:
    st.write("### आपके पिछले मूड्स:")
    for entry in reversed(st.session_state.mood_log):
        st.write(f"{entry['date']} : {entry['mood']}")
else:
    st.write("कोई मूड रिकॉर्ड नहीं मिला। अभी रिकॉर्ड करें।")
