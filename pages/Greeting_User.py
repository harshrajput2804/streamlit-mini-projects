import streamlit as st

# st.write("Hello World")
print_name = st.text_input("Enter Your Name")
is_clicked = st.button("Click me")

if is_clicked:
    greet = f"# Hello {print_name}"
    st.write(greet)
    
