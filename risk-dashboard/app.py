import streamlit as st
import pandas as pd
from pathlib import Path

# Import your custom utilities from the 'utils' package
# Ensure utils/__init__.py exists and utils/streamlit_kpi.py, etc., are created
# from utils.streamlit_kpi import kpi_block
# from utils.streamlit_collapse import collapsible_section

# --- Data Loading ---
# Define the path to your cleaned Parquet file relative to the app.py script.
# If app.py is in 'risk-dashboard/', then Path(__file__).parent refers to 'risk-dashboard/'.
# So, 'data/risk_clean.parquet' refers to 'risk-dashboard/data/risk_clean.parquet'.
DATA_FILE_PATH = Path(__file__).parent / "data/risk_clean.parquet"

@st.cache_data # Cache the data loading to improve performance and avoid re-loading on every rerun
def load_risk_data(file_path):
    """
    Loads the cleaned credit risk dataset from a Parquet file.
    """
    st.info(f"Attempting to load data from: {file_path}") # Informative message for debugging
    try:
        # Check if the file actually exists before trying to read
        if not file_path.exists():
            st.error(f"Error: Data file not found at {file_path}. Please ensure it's in the correct location and pushed to GitHub.")
            st.stop() # Stop the app if the file is missing

        df = pd.read_parquet(file_path)
        st.success("Data loaded successfully!")
        return df
    except Exception as e:
        st.error(f"An unexpected error occurred while loading data: {e}")
        st.stop() # Stop the app on any loading error

# Load the data when the app starts
df_risk = load_risk_data(DATA_FILE_PATH)

# --- Streamlit App Content ---

st.set_page_config(layout="wide", page_title="Risk Dashboard App")

st.title("Risk Dashboard App")

st.markdown("""
This dashboard provides insights into credit risk data.
""")

# Display basic information about the loaded data
if df_risk is not None:
    st.subheader("Dataset Overview")
    st.write(f"Loaded {df_risk.shape[0]} rows and {df_risk.shape[1]} columns.")

    st.write("First 5 rows:")
    st.dataframe(df_risk.head())

    st.write("Dataset Columns:")
    st.write(df_risk.columns.tolist())

    st.write("Descriptive Statistics:")
    st.dataframe(df_risk.describe())

    # Example of using a utility function (uncomment if you've added them)
    # kpi_block("Total Records", df_risk.shape[0], delta=None)

    # with st.container():
    #     collapsible_section("Raw Data Table", lambda: st.dataframe(df_risk))

else:
    st.warning("Data could not be loaded. Please check the file path and ensure the data file is committed to your repository.")

st.markdown("---")
st.caption("Built with Streamlit")
