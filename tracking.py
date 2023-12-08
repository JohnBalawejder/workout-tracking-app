import streamlit as st
import pandas as pd
from config import conn, pushExisting, pullExisting, legsExisting, pushData, pullData, legsData

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

    submit_form(selected_sheet)

    st.dataframe(selected_data, width=1150, hide_index=True)

def submit_form(selected_sheet):
    with st.form(key="vendor_form"):
        date = st.date_input(label="Workout Date")

        form_fields = get_form_fields(selected_sheet)
        field_values = {field: st.text_input(label) for field, label in form_fields.items()}

        note = st.text_input("Notes")

        submitted = st.form_submit_button("Submit")

        if submitted:
            # Prepare data for the Google Sheet
            data = {
                "Date": [date],
                **field_values,
                "Notes": [note],
            }

            # Upload data to the appropriate Google Sheet
            upload_to_google_sheet(selected_sheet, data)



def get_form_fields(selected_sheet):
    if selected_sheet == "Push":
        return {
            "Flat DB Press": "Flat DB Press",
            "Incline DB Press": "Incline DB Press",
            "Cable Lateral Raises": "Cable Lateral Raises",
            "Chest Flys": "Chest Flys",
            "Tricep Extensions": "Tricep Extensions",
        }
    elif selected_sheet == "Pull":
        return {
            "Chest Supported Row (Upper)": "Chest Supported Row (Upper)",
            "Chest Supported Row (Lats)": "Chest Supported Row (Lats)",
            "JPG Lat Pulldowns": "JPG Lat Pulldowns",
            "Shrugs": "Shrugs",
            "Cable Curls": "Cable Curls",
            "Bicep Curl Machine": "Bicep Curl Machine",
        }
    elif selected_sheet == "Legs":
        return {
            "Cable Lateral Raises": "Cable Lateral Raises",
            "Smith Machine Squat": "Smith Machine Squat",
            "Quad Extensions": "Quad Extensions",
            "Hamstring Curls": "Hamstring Curls",
            "Ab Crunch Machine": "Ab Crunch Machine",
        }
    else:
        return {}
    
def upload_to_google_sheet(selected_sheet, data):
    # Get the corresponding worksheet

    df = pd.DataFrame(data)
    if selected_sheet == "Push":
        updated_df = pd.concat([pushData, df], ignore_index=True)
        conn.update(worksheet="Push", data=updated_df)
    elif selected_sheet == "Pull":
        updated_df = pd.concat([pullData, df], ignore_index=True)
        conn.update(worksheet="Pull", data=updated_df)
    elif selected_sheet == "Legs":
        updated_df = pd.concat([legsData, df], ignore_index=True)
        conn.update(worksheet="Legs", data=updated_df)
    else:
        return
    
    st.success("Workout session successfully recorded!")
