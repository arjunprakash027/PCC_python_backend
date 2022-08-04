import streamlit as st
from supabase_connect import display_users,display_complaints

page = st.sidebar.selectbox("choose table",("complaints", "User"))

if page == "complaints":
    display_complaints()

else:
    display_users()




    