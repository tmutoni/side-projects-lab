def kpi_block(label, value, delta=None, delta_color='normal'):
    import streamlit as st
    st.metric(label=label, value=value, delta=delta, delta_color=delta_color)
    return st.empty() # Placeholder for a return value
