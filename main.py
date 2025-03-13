import streamlit as st
import random
import string

def generate_password(length, use_digit, use_characters):
    characters = string.ascii_letters  # A-Z, a-z

    # Ensure at least one digit & symbol (if selected)
    password = []
    if use_digit:
        characters += string.digits
        password.append(random.choice(string.digits))  # Ensure one digit
    if use_characters:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))  # Ensure one symbol

    # Fill the remaining length with random characters
    password += [random.choice(characters) for _ in range(length - len(password))]
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Streamlit UI
st.title("🔑 Secure Password Generator")

st.write("Customize your password and enhance security!")

length = st.slider("Select Password Length", min_value=6, max_value=20, value=12)

use_digit = st.checkbox('🔢 Include Digits')
use_characters = st.checkbox("🔣 Include Symbols")

if st.button("🚀 Generate Password"):
    password = generate_password(length, use_digit, use_characters)
    
    # Determine Password Strength
    strength = "Weak 🔴" if length < 8 else "Medium 🟡" if length < 12 else "Strong 🟢"
    
    st.success(f"**Generated Password:** `{password}`")
    st.write(f"🔒 Password Strength: **{strength}**")

    # Copy Button (Only works in some browsers)
    st.code(password, language="bash")
