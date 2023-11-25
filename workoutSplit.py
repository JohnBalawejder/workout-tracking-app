import streamlit as st
from config import pushSplit, pullSplit, legsSplit

def display_workout_split():
    # Add your workout split functionality here
    sheet_data = {
        "Push": pushSplit,
        "Pull": pullSplit,
        "Legs": legsSplit
    }

    sheet_names = list(sheet_data.keys())

    selected_sheet = st.selectbox("Select Workout Day", sheet_names)
    selected_data = sheet_data[selected_sheet]

    st.dataframe(selected_data, width=500, hide_index=True)