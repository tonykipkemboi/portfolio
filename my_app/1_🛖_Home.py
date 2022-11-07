import streamlit as st
from PIL import Image


# Configures the default settings of the page
st.set_page_config(page_title="Tony Kipkemboi | DevRel Engineer",
                   page_icon="🎈",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

#  ---HEADER---
st.markdown("# Tony Kipkemboi")
st.markdown("## ex-Data Engineer and Tech Content Creator")
st.markdown("""
    I write articles about Data, Python, Blockchain and related topics. The articles are mostly hosted on the [Hashnode](https://townee.hashnode.dev/) platform. I also create video content hosted on [YouTube](https://www.youtube.com/c/TonyKipkemboi). Feel free to follow and subscribe for updates on future releases. 
""")
st.write('---')
st.subheader('My recent articles...')
with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image("https://townee.hashnode.dev/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1662677533071%2FE7f0dP14x.png%3Fw%3D1600%26h%3D840%26fit%3Dcrop%26crop%3Dentropy%26auto%3Dcompress%2Cformat%26format%3Dwebp&w=1920&q=75")

    with text_col:
        st.subheader(
            "How to Query The Graph Protocol for On-Chain Data using Python")
        st.write("""
            A step-by-step guide on querying Subgraphs using Python, GraphQL, and Subgrounds
            
            The goal is for you to be able to query any Subgraph data using Python and understand the two querying methods.
            
            """)
        st.markdown(
            "[Read more...](https://townee.hashnode.dev/how-to-query-the-graph-protocol-for-on-chain-data-using-python)")

with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image(
            "https://townee.hashnode.dev/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Funsplash%2FYOCDD-D4oOM%2Fupload%2Fv1659634275969%2FzsFL1gRcQ.jpeg%3Fw%3D1600%26h%3D840%26fit%3Dcrop%26crop%3Dentropy%26auto%3Dcompress%2Cformat%26format%3Dwebp&w=1920&q=75")

    with text_col:
        st.subheader("What is a Governance Token?")
        st.write("""
            Analogical explanation of governance tokens
            
            There are several models for DAO membership, but I will focus on Token-Based Membership. One means you can be a member of a DAO is by trading tokens in a decentralized exchange.
            
            """)
        st.markdown(
            "[Read more...](https://townee.hashnode.dev/what-is-a-governance-token)")

st.write('---')
st.subheader('My recent videos...')

with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image(Image.open('./assets/Thumbnail_1.png'))

    with text_col:
        st.subheader(
            "Learn how to create a Python Virtual Environment for👏 the👏LAST👏TIME👏 (Beginner Friendly)")
        st.write("""
            In this demo, I cover:
            - what is a python virtual environment 
            - how to set it up 
            - activate it, and 
            - deactivate it
            """)
        st.markdown(
            "[Watch here...](https://youtu.be/vqnpYf7grro)")

with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image(Image.open('./assets/Thumbnail_2.png'))

    with text_col:
        st.subheader(
            "How I Made $132.10 with 83 Lines of Python! 🤯")
        st.write("""
            In this video, I share my first web3 hackathon experience and how I won a piece of the bounty price for my project. 

            These are links to various topics I mention in the video:
            - Gitcoin: https://gitcoin.co
            - Codeless Conduct: https://codelessconduct.org/
            - MVRV Dashboard: https://share.streamlit.io/tonykipkemboi/mvrvdashboardapp/main/app.py
            """)
        st.markdown(
            "[Watch here...](https://youtu.be/vqnpYf7grro)")

st.write('---')
