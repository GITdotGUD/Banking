# https://emojipedia.org/
# https://banking-atm.streamlit.app/
# https://docs.streamlit.io/
# Eg: https://bankingapp.streamlit.app/ (Done by teacher)
# https://banking-atm.streamlit.app/ 

import streamlit as st
from bank import BANK, accounts

st.title("Welcome to the Banking App 🎈")

# Session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

st.header("Login")
acc_no = st.text_input("Account Number")
pin = st.text_input("PIN", type="password")
login_btn = st.button("Login")

if login_btn:
    user = accounts.get(acc_no)
    if user and str(user.pin) == pin:
        st.session_state.logged_in = True
        st.session_state.user = user
        st.success("Logged in successfully!")
    else:
        st.error("Invalid account number or PIN.")

if st.session_state.logged_in and st.session_state.user:
    user = st.session_state.user
    st.header(f"Welcome, {user.AccName}")
    st.info(f"**Account Number:** {user.AccNo}")
    st.info(f"**Bank:** {user.bank}")
    st.success(f"**Current Balance:** {user.starting_Balance}")

    st.header("Banking Actions")
    action = st.selectbox("Choose Action", ["Deposit", "Withdraw", "Transfer"])
    amount = st.number_input("Amount", min_value=1, step=1)

    if action == "Deposit":
        if st.button("Deposit"):
            user.starting_Balance += amount
            st.success(f"Deposited {amount}. New balance: {user.starting_Balance}")
    elif action == "Withdraw":
        if st.button("Withdraw"):
            if amount > user.starting_Balance:
                st.error("Insufficient funds.")
            else:
                user.starting_Balance -= amount
                st.success(f"Withdrew {amount}. New balance: {user.starting_Balance}")
    elif action == "Transfer":
        recipient = st.text_input("Recipient Account Number")
        if st.button("Transfer"):
            if recipient == user.AccNo:
                st.error("You cannot transfer to your own account.")
            elif recipient not in accounts:
                st.error("Recipient account not found.")
            elif amount > user.starting_Balance:
                st.error("Insufficient funds.")
            else:
                user.starting_Balance -= amount
                accounts[recipient].starting_Balance += amount
                st.success(f"Transferred {amount} to {accounts[recipient].AccName}. New balance: {user.starting_Balance}")