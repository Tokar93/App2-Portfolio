import streamlit as st

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