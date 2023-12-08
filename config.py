import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Connection to google sheet
conn = st.connection("gsheets", type=GSheetsConnection)

def load_workout_data(worksheet, columns_range):
    return conn.read(worksheet=worksheet, usecols=columns_range, ttl=5)

def load_tracking_data(worksheet, columns_range):
    return conn.read(worksheet=worksheet, usecols=columns_range, ttl=5)

# Loading data for each day
pushSplit = load_workout_data("Push", list(range(4))).dropna(how="all")
pullSplit = load_workout_data("Pull", list(range(4))).dropna(how="all")
legsSplit = load_workout_data("Legs", list(range(4))).dropna(how="all")

# Loading tracking data
pushExisting = load_tracking_data("Push", list(range(4, 11))).dropna(how="all")
pullExisting = load_tracking_data("Pull", list(range(4, 12))).dropna(how="all")
legsExisting = load_tracking_data("Legs", list(range(4, 11))).dropna(how="all")

pushData = pd.concat([pushSplit, pushExisting], ignore_index=True)
pullData = pd.concat([pullSplit, pullExisting], ignore_index=True)
legsData = pd.concat([legsSplit, legsExisting], ignore_index=True)