def collapsible_section(title, content_func):
    import streamlit as st
    with st.expander(title):
        content_func()
    return st.empty() # Placeholder for a return value
