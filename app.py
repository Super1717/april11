import streamlit as st

if 'x' not in st.session_state:
    st.session_state.x =0

increment = st.button("increment")
if increment:
    st.session_state.x += 1
st.write('count' , st.session_state.x)