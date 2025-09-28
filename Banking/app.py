# https://emojipedia.org/
# https://banking-atm.streamlit.app/
# https://docs.streamlit.io/
# Eg: https://bankingapp.streamlit.app/ (Done by teacher)
# https://banking-atm.streamlit.app/ 
# ------------------------------------------------------------------------------------------------------------------------------------- 

       
import streamlit as st
st.title("Welcome to the Banking App 🎈")

# Login section
st.header("Login")
acc_no = st.text_input("Account Number")
pin = st.text_input("PIN", type="password")
login_btn = st.button("Login")

if login_btn:
    # Here you would check credentials
    st.success("Logged in successfully!")

    # Banking actions
    st.header("Banking Actions")
    action = st.selectbox("Choose Action", ["Deposit", "Withdraw", "Transfer"])
    amount = st.number_input("Amount", min_value=1)

    if action == "Deposit":
        if st.button("Deposit"):
            st.success(f"Deposited {amount}")
    elif action == "Withdraw":
        if st.button("Withdraw"):
            st.success(f"Withdrew {amount}")
    elif action == "Transfer":
        recipient = st.text_input("Recipient Account Number")
        if st.button("Transfer"):
            st.success(f"Transferred {amount} to {recipient}")
