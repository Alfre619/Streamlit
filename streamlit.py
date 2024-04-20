import streamlit as st
import pandas as pd  # Import pandas to fix the unresolved reference

st.title('My First Streamlit App')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
