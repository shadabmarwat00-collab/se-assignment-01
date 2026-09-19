import streamlit as st
import calculator

st.title("Simple Calculator Web App")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)
operation = st.selectbox("Choose operation", ["Add", "Subtract"])

if st.button("Calculate"):
    if operation == "Add":
        result = calculator.add(num1, num2)
        st.success(f"Result: {result}")
    elif operation == "Subtract":
        result = calculator.subtract(num1, num2)
        st.success(f"Result: {result}")