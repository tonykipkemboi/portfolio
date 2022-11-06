import streamlit as st
import time


def surprised() -> None:
    st.image('../assets/Snowflake_Inc.-Logo.wine.png',
             use_column_width=True)
    st.subheader(
        'I am a Developer Relations Engineer working on Streamlit🎈 @Snowflake❄️')
    st.write('I am beyond excited to start the new role woring on an open-source product that I love with a great team!', on_click=st.snow())
    snowflake, streamlit = st.columns(2)

    with snowflake:
        st.info('What is Snowflake?')
        st.video('https://www.youtube.com/watch?v=xojAXXRo_S0')
    st.subheader(
        'I share my thoughts on why I am making the switch to DevRel in [my latest article](https://townee.hashnode.dev/preview/63640dbabb0b328aa172548c)!')

    with streamlit:
        st.info(
            'Learn about Streamlit in Snowflake!')
        st.video('https://www.youtube.com/watch?v=e8kZQDKeNwk&t=3s')


with st.empty():
    _, col2, _ = st.columns(3)
    with col2:
        st.button('LET IT SNOW!', on_click=surprised)
