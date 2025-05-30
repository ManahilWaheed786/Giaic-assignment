import streamlit as st
import hashlib
import json
import os
from cryptography.fernet import Fernet

# Constants
DATA_FILE = "secure_data.json"
KEY_FILE = "secret.key"
MASTER_PASSWORD = "admin123"  # In production, use a safer method
MAX_ATTEMPTS = 3

# Generate or load encryption key
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as f:
        f.write(Fernet.generate_key())
with open(KEY_FILE, "rb") as f:
    KEY = f.read()
cipher = Fernet(KEY)

# Load/Save JSON data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt/Decrypt
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = load_data()
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "authorized" not in st.session_state:
    st.session_state.authorized = True

# Streamlit App
st.title("🔐 Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome")
    st.write("Securely store and retrieve data using unique passkeys.")

elif choice == "Store Data":
    st.subheader("📂 Store Data")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_pass = hash_passkey(passkey)
            encrypted = encrypt_data(user_data)
            st.session_state.data[encrypted] = {
                "encrypted_text": encrypted,
                "passkey": hashed_pass
            }
            save_data(st.session_state.data)
            st.success("✅ Data stored securely!")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    if not st.session_state.authorized:
        st.warning("🔒 You must login again.")
        st.stop()

    st.subheader("🔍 Retrieve Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            hashed_pass = hash_passkey(passkey)
            entry = st.session_state.data.get(encrypted_text)

            if entry and entry["passkey"] == hashed_pass:
                decrypted = decrypt_data(encrypted_text)
                st.success(f"✅ Decrypted Data: {decrypted}")
                st.session_state.failed_attempts = 0
            else:
                st.session_state.failed_attempts += 1
                remaining = MAX_ATTEMPTS - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts remaining: {remaining}")

                if st.session_state.failed_attempts >= MAX_ATTEMPTS:
                    st.warning("🔒 Too many failed attempts! Redirecting to login...")
                    st.session_state.authorized = False
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == MASTER_PASSWORD:
            st.session_state.failed_attempts = 0
            st.session_state.authorized = True
            st.success("✅ Reauthorized! You can now retrieve data.")
        else:
            st.error("❌ Incorrect password!")

