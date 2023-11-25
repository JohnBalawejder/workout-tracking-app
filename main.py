import streamlit as st
from streamlit_option_menu import option_menu

# Web app config
st.set_page_config(page_title="Workout Volume",
                   page_icon=":fire:",
                   layout="wide")

from workoutSplit import display_workout_split
from analytics import display_analytics
from tracking import display_tracking

# Title 
st.markdown("<h1 style='text-align: center; color: black;'>Workout Tracking App</h1>", unsafe_allow_html=True)

# Menu Bar
selected = option_menu(
    menu_title=None,
    options=["Workout Split", "Analytics", "Tracking"],
    icons=["journal-check", "bar-chart-line-fill", "clipboard2-check"],
    default_index=0,
    orientation="horizontal"
)

# Menu Functionality
if selected == "Workout Split":
    display_workout_split()
elif selected == "Analytics":
    display_analytics()
elif selected == "Tracking":
    display_tracking()