import streamlit as st
from utils import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)

col2.image(Image.open('./assets/tony.png'))

st.header('Tony Kipkemboi')

st.info('Connect with me on the following platforms...')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/c/TonyKipkemboi',
          ' Subscribe to my YouTube channel', icon_size)
st_button('hashnode', 'https://townee.hashnode.dev/',
          ' Read my blogs', icon_size)
st_button('twitter', 'https://twitter.com/_townee/',
          ' Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/tonykipkemboi/',
          ' Follow me on LinkedIn', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/tonykip',
          ' Buy me a coffee', icon_size)

# Credits to Chanin a.k.a. "The Data Professor" for the Linktree --> Streamlit version tutorial
st.caption(
    '*Thanks to Chanin for the [tutorial](https://www.youtube.com/watch?v=1AiBgm-iZO4)!*')
