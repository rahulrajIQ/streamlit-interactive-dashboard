import streamlit as st

def intro():

    st.write("# Welcome to Options Trading World! 👋")
    st.sidebar.success("Select a service above.")

    st.markdown(
        """
        This is a Options Trading app built to ease the calculations related
        to options and its greeks.

        **👈 Select a service from the dropdown on the left** 

        ### Want to learn more?

        - Check out Zerodha Varsity
        - Read books
        
    """
    )
intro()