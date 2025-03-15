import re
import streamlit as st

def check_password_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        suggestions.append("Include at least one number.")

    if re.search(r'[\W_]', password):
        strength += 1
    else:
        suggestions.append("Use at least one special character (e.g., @, #, $).")

    strength_levels = ["Very Weak 😔", "Weak 😕", "Moderate 🙂", "Strong 💪", "Very Strong 🔥"]

    return strength_levels[strength], suggestions

# Streamlit UI
st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password:", type="password")

if password:
    strength, suggestions = check_password_strength(password)
    st.subheader(f"Password Strength: {strength}")

    if suggestions:
        st.write("### Suggestions to Improve:")
        for s in suggestions:
            st.write(f"- {s}")
