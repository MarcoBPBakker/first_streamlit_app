import streamlit
import pandas

streamlit.title('Pablo & Pedro\'s Kattenbak')

streamlit.header('Ontbijt Menu')
streamlit.text('🥗 brokjes met kattemelk')
streamlit.text('🐔 gekookte kip op kattengras')
streamlit.text('🥣 haring gemarineerd in zalmsaus')

streamlit.header('🍌🥭 Smoothie\'s voor de baasjes? 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
