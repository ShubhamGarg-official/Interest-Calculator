import streamlit as st
from datetime import datetime

st.set_page_config(page_title="TDS Interest Calculator", page_icon="💼")
st.title("💼 TDS Interest Calculator")
st.write("Choose the applicable delay type:")

# Select interest type
option = st.selectbox(
    "Type of Delay",
    ("Late Deduction of TDS (1% per month)", "Late Payment of TDS (1.5% per month)")
)

# Set interest rate
interest_rate = 0.01 if "Deduction" in option else 0.015

# Input Section
amount = st.number_input("Enter the amount (₹)", value=10000.0)
due_date = st.date_input("Enter the due date")
payment_date = st.date_input("Enter the payment date")

# Accurate month calculation function
def calculate_months(due, pay):
    months = (pay.year - due.year) * 12 + (pay.month - due.month)
    
    if pay.day > due.day:
        months += 1
    elif pay.day <= due.day:
        if months > 0:
            months += 0
        else:
            months = 1  # Same month, just few days late
    return months

# Calculation & Output
if payment_date > due_date:
    months = calculate_months(due_date, payment_date)
    interest = amount * interest_rate * months

    st.subheader("📊 Result")
    st.success(f"📅 Delay Counted: {months} month(s)")
    st.success(f"💸 Interest @ {interest_rate*100:.1f}%: ₹{interest:.2f}")
elif payment_date == due_date:
    st.info("✅ Paid on due date. No interest applicable.")
else:
    st.info("✅ Paid before due date. No interest applicable.")
