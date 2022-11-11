import streamlit as st
import pandas

data = {
  'Series_1':[1, 3, 4, 6, 7],
  'Series 2':[10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)

st.title('Our first Streamlit app')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write('''This is our first Web App''')
st.write(df)