import random
import streamlit as st
from gen import generate_random_class

st.set_page_config(page_title="Power Generator", layout="centered")
st.title("Power Generator")

st.markdown("Welcome to the Power Generator! Click the button below to generate random power details.")

def main():
    """
    Main function to handle the entire process of:
    1. Rolling for level.
    2. Get main stats for that level
    3. Displaying the final power details.
    """
    if st.button("Generate Classes 📃"):
        # Clear previous results
        st.session_state.generated_classes = []
        
        # Generate 3 random classes
        for i in range(3):
            random_class = generate_random_class()
            st.session_state.generated_classes.append(random_class)
        
        # Display the results in a list
        st.subheader("Generated Classes:")
        for i, class_details in enumerate(st.session_state.generated_classes, 1):
            st.markdown(f"### Class {i}")
            st.write(class_details)  # Assuming generate_random_class() returns a string or dict
            st.write("---")  # Add a separator between classes

if __name__ == "__main__":
    main()
