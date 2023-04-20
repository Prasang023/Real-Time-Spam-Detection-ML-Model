import tweepy
import streamlit as st
from model import result

consumer_key = st.secrets["consumer_key"]
consumer_secret = st.secrets["consumer_secret"]
access_key = st.secrets["access_key"]
access_secret = st.secrets["access_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

st.title('Real-Time Spam Detection Machine Learning Model')

submit = st.button('Show Result')

if submit:
    tweets_list = api.user_timeline()
    for tweet in tweets_list:
        check = result(tweet.text)
        st.subheader(tweet.in_reply_to_screen_name)
        st.caption(tweet.created_at)
        st.text(tweet.text)
        st.subheader(check)
        st.divider()

    st.success('Executed Successfully')
    st.balloons()
