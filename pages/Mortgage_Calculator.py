import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import math



# ✅ Indian Currency Formatter
def format_inr(amount):
    s = str(int(round(amount)))
    if len(s) <= 3:
        return s
    last3 = s[-3:]
    rest = s[:-3][::-1]
    rest = ",".join(rest[i:i+2] for i in range(0, len(rest), 2))
    return rest[::-1] + "," + last3


st.title("🏠 Mortgage Loan Calculator (INR)")

st.write("### 🔢 Input Data")
col1, col2 = st.columns(2)

home_value = col1.number_input("Home Value (₹)", min_value=0, value=500000, step=50000)
deposit = col1.number_input("Deposit (₹)", min_value=0, value=100000, step=10000)

interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)

# ✅ Loan Calculations
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12

monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

# ✅ INR Display Metrics
st.write("### 💰 Repayments")

col1, col2, col3 = st.columns(3)

col1.metric("Monthly EMI", f"₹ {format_inr(monthly_payment)}")
col2.metric("Total Repayment", f"₹ {format_inr(total_payments)}")
col3.metric("Total Interest", f"₹ {format_inr(total_interest)}")


# ✅ Payment Schedule Table
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)

    schedule.append(
        [
            i,
            round(monthly_payment),
            round(principal_payment),
            round(interest_payment),
            max(0, round(remaining_balance)),
            year,
        ]
    )

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

# ✅ Convert all currency columns to INR format
for col in ["Payment", "Principal", "Interest", "Remaining Balance"]:
    df[col] = df[col].apply(lambda x: f"₹ {format_inr(x)}")

st.write("### 📊 Payment Schedule (Yearly Balance)")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()

st.line_chart(
    df.groupby("Year")["Month"].count()
)

st.dataframe(df)
