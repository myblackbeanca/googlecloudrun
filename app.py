# YOUR PYTHON CODE USED TO CREATE YOUR STREAMLIT APP

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from textblob import TextBlob
import time

# Set page config
st.set_page_config(
    page_title="Multi-Function App",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a feature",
    ["Home", "Data Visualization", "Text Analysis", "File Upload & Analysis", "Interactive Calculator"]
)

# Home Page
if page == "Home":
    st.title("🎯 Welcome to Multi-Function App!")
    st.markdown("""
    This app demonstrates various Streamlit features:
    - 📊 **Data Visualization**: Create interactive charts
    - 📝 **Text Analysis**: Analyze sentiment and text properties
    - 📁 **File Upload & Analysis**: Upload and analyze CSV files
    - 🧮 **Interactive Calculator**: Perform basic calculations
    """)
    
    # Progress bar demo
    if st.button("Show Progress Demo"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        st.success("Completed!")

# Data Visualization Page
elif page == "Data Visualization":
    st.title("📊 Data Visualization")
    
    # Generate sample data
    chart_type = st.selectbox("Select Chart Type", ["Line", "Bar", "Scatter"])
    
    # Generate random data
    dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
    values = np.random.randn(30).cumsum()
    df = pd.DataFrame({'Date': dates, 'Value': values})
    
    if chart_type == "Line":
        fig = px.line(df, x='Date', y='Value', title='Interactive Line Chart')
    elif chart_type == "Bar":
        fig = px.bar(df, x='Date', y='Value', title='Interactive Bar Chart')
    else:
        fig = px.scatter(df, x='Date', y='Value', title='Interactive Scatter Plot')
    
    st.plotly_chart(fig, use_container_width=True)

# Text Analysis Page
elif page == "Text Analysis":
    st.title("📝 Text Analysis")
    
    text_input = st.text_area("Enter text for analysis:", height=150)
    if text_input:
        blob = TextBlob(text_input)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Sentiment Polarity", f"{blob.sentiment.polarity:.2f}")
        with col2:
            st.metric("Sentiment Subjectivity", f"{blob.sentiment.subjectivity:.2f}")
        with col3:
            st.metric("Word Count", len(text_input.split()))
        
        st.subheader("Word Statistics")
        words = text_input.split()
        word_freq = pd.Series(words).value_counts()
        st.bar_chart(word_freq.head(10))

# File Upload Page
elif page == "File Upload & Analysis":
    st.title("📁 File Upload & Analysis")
    
    uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(df.head())
        
        st.subheader("Data Statistics")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Numerical Columns Summary:")
            st.write(df.describe())
        with col2:
            st.write("Missing Values:")
            st.write(df.isnull().sum())

# Interactive Calculator
elif page == "Interactive Calculator":
    st.title("🧮 Interactive Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number:", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number:", value=0.0)
    
    operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])
    
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        else:
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero!")
                result = None
        
        if result is not None:
            st.success(f"Result: {result}")
