import streamlit as st
import random
import string

def generate_password(length , use_digit , use_characters):
    characters = string.ascii_letters

    if use_digit:
        characters += string.digits
    if use_characters:
        characters += string.punctuation
        
    return''.join(random.choice(characters)for _ in range(length))
    
# streamlit
st.title("Genrate Password")
length = st.slider("Select Password Legth", min_value=6 , max_value=20 , value=12)

use_digit = st.checkbox('include digits')
use_characters = st.checkbox("include symbol")

if st.button("Generate Password"):
    password = generate_password(length , use_digit , use_characters)
    st.write(f"Generated Pssword: `{password}`")