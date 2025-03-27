import streamlit as st
import joblib

clf=joblib.load('Loan.joblib')

st.title('LOAN APP RCE')
g=st.number_input('Enter Gender 0:Male,1:Female')
m=st.number_input('Enter Marital Status 0:No,1:Yes')
ai=st.number_input('Enter Applicant Income In Thousands')
la=st.number_input('Enter Loan Amount In Thousands')

if st.button('PREDICT'):
    Predition=clf.predict([[g,m,ai,la]])
    if predition=='Y':
        st.txt('LOAN IS APPROVED')
    else:
        st.txt('LOAN IS REJECTED')
    
