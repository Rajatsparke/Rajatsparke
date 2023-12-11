import streamlit as st
import numpy as np
import pandas as pd

# Title
st.title('ROI Calculator - BASL vs Trad MBA')

# Sliders
basl_investment = st.number_input('BASL-Investment/Fee in Rupees', value = 160000)
mba_fee = st.number_input('Traditional MBA Fee in Rupees', value = 1000000)

# Input
basl_salary = st.number_input('BASL minimum salary after placement (6 months)', value=900000)
# commit by Varun
mba_salary = st.number_input("MBA Salary after placement (2 years)", value = 1500000)

annual_growth = st.number_input("Annual growth in %age",value = 15)

# Calculations
basl_monthly_salary = basl_salary/12
#st.write('BASL Minimum monthly salary after 6 months is Rs.',basl_monthly_salary)

#n = st.slider("Years from today",0,5,1)
a = st.slider("Months since placement",-6,23,1)

#if n == 0:
 #   st.write("Your approx. salary per month will be", basl_salary/12)
 #   st.write("Therefore, ROI after 6 months from today will be",round(((basl_salary/12)/basl_investment)*100),'%')
b = 0
c = basl_salary/12*(12)
e = (c+((basl_salary*(1+annual_growth/100))/12*(a%12)))
roi_basl = 0
roi_mba = 0
if 1<=a<13:
    b = basl_salary/12*(a%13)
    st.write("Congratulations on your placement. Your have approx. earned", basl_salary/12*(a%13))
    st.write("Therefore, your ROI in BASL is",(round((b/basl_investment)*100)),'%')
    roi_basl = (round((b/basl_investment)*100))
    st.write("ROI of MBA is 0 because it is of 2 years")
elif a <  1:
    st.write("You are still under training")
    roi = 0
elif 13<=a<=18:
    d = (basl_salary*(1+annual_growth/100))/12
    st.write("You received a",annual_growth,"% increment and hence your new monthly salary is now Rs.",basl_monthly_salary*(1+annual_growth/100))
    st.write("Your total earnings after",a ,'months via BASL is',(c+(d*(a%12))))
    e = (c+(d*(a%12)))
    st.write("Therefore, your ROI in BASL is",(round(((c+(d*(a%12)))/basl_investment)*100)),'%')
    roi_basl = (round(((c+(d*(a%12)))/basl_investment)*100))
    st.write("ROI of MBA is 0 because it is of 2 years")
elif 18<a<24:
    d = (basl_salary*(1+annual_growth/100))/12
    st.write("You received a",annual_growth,"% increment and hence your new monthly salary is now Rs.",basl_monthly_salary*(1+annual_growth/100))
    st.write("Your total earnings after",a ,'months is',(c+(d*(a%12))))
    e = (c+(d*(a%12)))
    st.write("Therefore, your ROI in BASL is",(round(((c+(d*(a%12)))/basl_investment)*100)),'%')
    roi_basl = (round(((c+(d*(a%12)))/basl_investment)*100))
    st.write("You got placed via MBA and your monthly salary is",mba_salary/12)
    st.write("You total earnings till now via an MBA are",(mba_salary/12)*(a%18))
    roi_mba = round((((mba_salary/12)*(a%18))/mba_fee)*100)
    st.write("Your ROI in MBA is",roi_mba,"% vs",roi_basl,"% in BASL")

