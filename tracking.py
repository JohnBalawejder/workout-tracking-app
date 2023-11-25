import streamlit as st
import pandas as pd
from config import pushExisting, pullExisting, legsExisting

def display_tracking():
    # Use pushExisting, pullExisting, legsExisting data as needed
    # Add more tracking functionality here
    sheet_data = {
        "Push": pushExisting,
        "Pull": pullExisting,
        "Legs": legsExisting
    }

    sheet_names = list(sheet_data.keys())

    selected_sheet = st.selectbox("Select Workout Day", sheet_names)
    selected_data = sheet_data[selected_sheet]

    st.dataframe(selected_data, width=1150, hide_index=True)