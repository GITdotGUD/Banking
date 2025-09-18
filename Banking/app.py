# https://emojipedia.org/
# https://banking-atm.streamlit.app/
# https://docs.streamlit.io/


import streamlit as st
st.title("Welcome to the Banking App 🎈")

from acc import Account
# Login section
st.header("Login")
acc_no = st.text_input("Account Number")
pin = st.text_input("PIN", type="password")
login_btn = st.button("Login")

if login_btn:
    account = Account("Adam Ibrahim", "123456789", 1000)

    if acc_no == account.AccNo:
        st.success("Logged in successfully!")
        st.write(f"Welcome, {account.AccName}")
        st.write(f"Current Balance: {account.starting_Balance}")

        action = st.selectbox("Choose Action", ["Deposit", "Withdraw"])
        amount = st.number_input("Amount", min_value=1, step=1)

        if action == "Deposit":
            if st.button("Deposit"):
                account.starting_Balance += amount
                st.success(f"Deposited {amount}. New balance: {account.starting_Balance}")
        elif action == "Withdraw":
            if st.button("Withdraw"):
                if amount > account.starting_Balance:
                    st.error("Insufficient funds.")
                else:
                    account.starting_Balance -= amount
                    st.success(f"Withdrew {amount}. New balance: {account.starting_Balance}")
    else:
        st.error("Account not found.")

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