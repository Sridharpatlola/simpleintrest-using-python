import streamlit as st
from streamlit_option_menu import option_menu
options = option_menu(menu_title="",options=["Simple Interest calculator"],orientation="horizontal")
if options == "Simple Interest calculator":
    st.title("Simple interest calculator")
    P = st.number_input("Enter the principal amount")
    T = st.number_input("Enter the time in years")
    R = st.number_input("Enter the rate of interest")
    I = (P * T * R) / 100
    if st.button("Calculate interest"):
        st.success("The simple interest is {}".format(I))
#import streamlit pkg to view in Localhost





