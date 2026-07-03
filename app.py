import streamlit as st

st.title("Power Calculator")
st.write("Enter a Number to calculate it's squre,cube...")

n = st.number_input("Enter an intiger : ")
n = int(n)

squre = n**2
cube = n**3

st.write(f'squre of {n} the number is {squre}')
st.write(f'cube of {n} the number is : {cube}')
