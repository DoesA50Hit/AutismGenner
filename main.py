import random
import streamlit as st

st.set_page_config(page_title="Power Generator", layout="centered")
st.title("Power Generator")

st.markdown("Welcome to the Power Generator! Click the button below to generate random power details.")

def main():
    """
    Main function to handle the entire process of:
    1. Rolling for levej.
    2. Get main stats for that level
    3. Displaying the final power details.
    """
    if st.button("Generate Classes 📃"):
        abundance_roll = random.randint(1, 9)
    if st.button("Generate Level and word"):
        abundance_roll = random.randint(1, 9)
