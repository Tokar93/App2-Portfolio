import streamlit as st
import pandas as pd

st.set_page_config(page_title='My portfolio')

col1, col2 = st.columns(2)

with col1:
    st.image('images/makapaka.png')

with col2:
    st.title('Tomasz Tokarski')
    content = """
    Beginner programmer building his portfolio. Beginner programmer building his portfolio. Beginner programmer building his portfolio. Beginner programmer building his portfolio.
    Beginner programmer building his portfolio. Beginner programmer building his portfolio. Beginner programmer building his portfolio.
    """
    st.info(content)
intro = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(intro)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f'images/{row['image']}', width=300)
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f'images/{row['image']}', width=300)
        st.write(f'[Source Code]({row["url"]})')
