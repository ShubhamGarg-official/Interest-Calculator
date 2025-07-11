import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Interest Calculator", page_icon="📊")
st.title("💰 Income Tax Interest Calculator")
st.write("1% per month or part thereof")

# Input Section
amount = st.number_input("Enter the amount (₹)", value=10000.0)
due_date = st.date_input("Enter the due date")
payment_date = st.date_input("Enter the payment date")

# Calculation
if payment_date > due_date:
    months = (payment_date.year - due_date.year) * 12 + (payment_date.month - due_date.month)
    if payment_date.day > due_date.day:
        months += 1
    else:
        months += 1  # Even 1 day late = full month

    interest = amount * 0.01 * months
    st.success(f"📅 Delay: {months} month(s)")
    st.success(f"💸 Interest Payable: ₹{interest:.2f}")
elif payment_date == due_date:
    st.info("✅ Paid on time. No interest.")
else:
    st.info("✅ Advance payment. No interest.")
