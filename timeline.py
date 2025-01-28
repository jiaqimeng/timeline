import streamlit as st
import pandas as pd
import json
from streamlit_timeline import timeline

# Make the Streamlit app use the entire browser width
st.set_page_config(layout="wide")

def main():
    st.markdown("# 500 years of glory human history")
    st.markdown("## build by ROE AI + DeepSeek R1")

    # Upload CSV file
    # Read the CSV file into a pandas DataFrame

    df = pd.read_csv('./tl.csv')
    # Drop rows that don't have the required columns
    df.dropna(subset=["year", "biggest_event", "darkest_joke"], inplace=True)

    # Build the timeline events list
    events_list = []
    for _, row in df.iterrows():
        start_year = str(row["year"])
        events_list.append({
            "start_date": {"year": start_year},
            "text": {
                "headline": str(row["biggest_event"]),
                "text": row["darkest_joke"].strip('"')
            }
        })

    # Create the base timeline JSON structure
    timeline_data = {
        "title": {
            "text": {
                "headline": "Events Timeline"
            }
        },
        "events": events_list
    }

    # Add a selectbox to let the user jump directly to a year
    unique_years = sorted(df["year"].unique())
    # Convert the data structure to JSON
    timeline_json = json.dumps(timeline_data)

    # Render the timeline with increased height (and wide layout via set_page_config)
    timeline(timeline_json, height=800)


if __name__ == "__main__":
    main()
