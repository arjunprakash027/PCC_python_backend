import os
from supabase import create_client, Client
import streamlit as st
import pandas as pd

supabase: Client = create_client("https://ztztpbhzaznljbxzwakt.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp0enRwYmh6YXpubGpieHp3YWt0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NTk1NDE1MTAsImV4cCI6MTk3NTExNzUxMH0.4Dc0rOlrUreHwpI0hK56WwjtNivsUteg5I2Yxu79fQk")


def display_users():
    st.title("Information from Users Database")
    data = data = supabase.table("users").select("*").execute()
    data = dict(data)
    df1 = pd.DataFrame(columns = ["user_name","user_id","user_sex","user_dob","user_email","user_city","user_pincode","user_level"])
    data = data["data"]
    for i in range(len(data)):
        dataz = data[i]
        df1 = df1.append({"user_name":dataz["user_name"],
        "user_id":dataz["user_id"],
        "user_sex":dataz["user_sex"],
        "user_dob":dataz["user_dob"],
        "user_email":dataz["user_email"],
        "user_city":dataz["user_city"],
        "user_pincode":dataz["user_pincode"],
        "user_level":dataz["user_level"]
        },ignore_index=True)
    st.dataframe(df1)

def display_complaints():
    st.title("Information from complaints Database")
    data = supabase.table("complaints").select("*").execute()
    data = dict(data)
    df2 = pd.DataFrame(columns = ["complaint_id","complaint_name","complaint_phone","complaint_content","complaint_created","complaint_status","complaint_email","complaint_attended","complaint_closed","complaint_attendee"])
    data = data["data"]
    for i in range(len(data)):
        dataz = data[i]
        df2 = df1.append({"complaint_id":dataz["complaint_id"],
        "complaint_name":dataz["complaint_name"],
        "complaint_phone":dataz["complaint_phone"],
        "complaint_content":dataz["complaint_content"],
        "complaint_created":dataz["complaint_created"],
        "complaint_status":dataz["complaint_status"],
        "complaint_email":dataz["complaint_email"],
        "complaint_attended":dataz["complaint_attended"],
        "complaint_closed":dataz["complaint_closed"],
        "complaint_attendee":dataz["complaint_attendee"]
        },ignore_index=True)
    st.dataframe(df2)


