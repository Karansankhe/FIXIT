import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

st.title('Call Transcript Sentiment Analysis')

# Basic Authentication
st.sidebar.header('Login')
username = st.sidebar.text_input('Username')
password = st.sidebar.text_input('Password', type='password')

auth = HTTPBasicAuth(username, password)

if st.sidebar.button('Login'):
    if username and password:
        response = requests.get('http://127.0.0.1:5000/upload', auth=auth)
        if response.status_code == 200:
            st.sidebar.success('Login Successful')
        else:
            st.sidebar.error('Invalid Credentials')
    else:
        st.sidebar.warning('Please enter username and password')

uploaded_file = st.file_uploader('Upload call transcript', type=['txt'])

if uploaded_file is not None:
    if st.button('Submit'):
        with st.spinner('Analyzing sentiment...'):
            response = requests.post(
                'http://127.0.0.1:5000/upload',
                files={'file': uploaded_file},
                auth=auth
            )
            if response.status_code == 200:
                result = response.json()
                transcript = result.get('transcript')
                sentiment = result.get('sentiment', {})
                
                st.subheader('Uploaded Transcript')
                st.text_area('Transcript Content', transcript, height=300)
                
                if 'error' in sentiment:
                    st.error(f"Error: {sentiment['error']}")
                else:
                    st.subheader('Sentiment Analysis Result')
                    st.write(f"Label: {sentiment['label']}")
                    st.write(f"Score: {sentiment['score']:.2f}")
                    
                    # Prepare data for visualization
                    labels = ['Positive', 'Negative', 'Neutral']
                    scores = [0, 0, 0]  # Initialize scores for each label

                    # Set the score for the label present in sentiment analysis result
                    if sentiment['label'] == 'POSITIVE':
                        scores[0] = sentiment['score']
                    elif sentiment['label'] == 'NEGATIVE':
                        scores[1] = sentiment['score']
                    else:
                        scores[2] = sentiment['score']

                    # Pie Chart Visualization
                    fig, ax = plt.subplots()
                    if any(scores):  # Ensure there are non-zero values to plot
                        ax.pie(scores, labels=labels, autopct='%1.1f%%', colors=['green', 'red', 'gray'])
                        ax.set_title('Sentiment Distribution')
                    else:
                        ax.text(0.5, 0.5, 'No data to display', horizontalalignment='center', verticalalignment='center')

                    st.pyplot(fig)
                    
                    # Horizontal Bar Chart Visualization
                    fig, ax = plt.subplots()
                    if any(scores):  # Ensure there are non-zero values to plot
                        bars = ax.barh(labels, scores, color=['green', 'red', 'gray'])
                        ax.set_xlabel('Score')
                        ax.set_title('Sentiment Scores')

                        # Adding value labels on the bars
                        for bar in bars:
                            width = bar.get_width()
                            ax.text(width, bar.get_y() + bar.get_height()/2, f'{width:.2f}', va='center')
                    else:
                        ax.text(0.5, 0.5, 'No data to display', horizontalalignment='center', verticalalignment='center')

                    st.pyplot(fig)
                    
                    # Word Cloud Visualization
                    fig, ax = plt.subplots()
                    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(transcript)
                    ax.imshow(wordcloud, interpolation='bilinear')
                    ax.axis('off')
                    st.subheader('Word Cloud of Transcript')
                    st.pyplot(fig)
                    
                    # Additional Bar Chart for Sentiment Score Distribution
                    fig, ax = plt.subplots()
                    distribution_labels = ['Positive', 'Negative', 'Neutral']
                    distribution_scores = scores
                    bars = ax.bar(distribution_labels, distribution_scores, color=['green', 'red', 'gray'])
                    ax.set_ylabel('Score')
                    ax.set_title('Sentiment Score Distribution')

                    # Adding value labels on the bars
                    for bar in bars:
                        height = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width()/2.0, height, f'{height:.2f}', ha='center', va='bottom')
                    
                    st.pyplot(fig)
            else:
                st.error('Failed to analyze sentiment')
