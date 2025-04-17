import random
import streamlit as st
from gen import generate_random_class
from lib import CLASSES  # Import CLASSES from lib.py

st.set_page_config(page_title="Power Generator", layout="centered")
st.title("Power Generator")

st.markdown("Welcome to the Power Generator! Click the button below to generate random power details.")

def main():
    """
    Main function to handle the entire process of:
    1. Generating unique classes
    2. Displaying the class name and description
    """
    if st.button("Generate Classes 📃"):
        # Clear previous results
        st.session_state.generated_classes = []
        used_classes = set()
        
        # Generate 3 unique random classes
        while len(st.session_state.generated_classes) < 3:
            random_class = generate_random_class()
            if random_class not in used_classes:
                used_classes.add(random_class)
                st.session_state.generated_classes.append(random_class)
        
        # Display the results in a list
        st.subheader("Generated Classes:")
        for i, class_name in enumerate(st.session_state.generated_classes, 1):
            class_description = CLASSES.get(class_name, "No description available")
            st.markdown(f"### {i}. {class_name}")
            st.write(class_description)
            st.write("---")  # Add a separator between classes

if __name__ == "__main__":
    main()
