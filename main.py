
import streamlit as st
import numpy as np
import pandas as pd
import gspread
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title='Calculate your ROI ',page_icon="bar_chart")
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()



# Title
#st.title('Calculate your ROI \n **Kraftshala\'s Business and Sales Launchpad (BASL) or Traditional MBA**')

st.title('Calculate your ROI \n **Kraftshala\'s Business and Sales Launchpad (BASL) or Traditional MBA**')

basl_investment = 175000
#mba_fee = st.number_input('Traditional MBA Fee in Rupees', value = 1000000)
#mba_institute = st.selectbox("Select your Institute",options=institutes)
#mba_fee = float(st.selectbox('Your Institute\'s fee ',options=fee))
column1_options = df['Institute'].tolist()
selected_option = st.selectbox("Please select your dream college", column1_options)

#corresponding value = institute's fees
corresponding_value1 = df.loc[df['Institute'] == selected_option, 'Total Fees (Rs)'].values
if len(corresponding_value1) > 0:
     st.success(f"Fee for {selected_option} is : Rs {corresponding_value1[0]} Lacs")
else:
     st.warning("No corresponding value found.")
corresponding_value = corresponding_value1 * 100000
salary1 = df.loc[df['Institute'] == selected_option, 'Average Salary'].values
if len(salary1) > 0:
     st.success(f"Average CTC of {selected_option} is : Rs {salary1[0]} Lacs")
else:
     st.warning("No corresponding value found.")

salary = salary1 * 100000
#st.write(corresponding_value/12)


basl_salary = 900000
#mba_salary = st.number_input("The average salary you get placed at if you opt for traditional MBA (in 24 months)", value = 1500000)

annual_growth = st.number_input("Annual growth in %age",value = 15)

# Calculations
basl_monthly_salary = basl_salary/12
#st.write('BASL Minimum monthly salary after 6 months is Rs.',basl_monthly_salary)
mba_salary = round(float(salary))
#n = st.slider("Years from today",0,5,1)
slider = st.slider(f"Months since placement from {selected_option}",1,60,1)
#a = st.slider("Months since placement",-6,30,1)
a = slider + 18

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
    st.write(" *Opted for BASL:* Congratulations on your placement! \n Your have approx. earned Rs.", basl_salary/12*(a%13))
    
    roi_basl = (round((b/basl_investment)*100))
    st.write(" *Opted for MBA :* You're still in training")
    st.write(" **ROI of BASL vs ROI of MBA upto month** ",a,':',(round((b/basl_investment)*100)),'% vs 0')
elif a <  1:
    st.write("You are in training")
    roi = 0
elif 13<=a<=18:
    d = (basl_salary*(1+annual_growth/100))/12
    st.write("You received a",annual_growth,"% increment and hence your new monthly salary is Rs.",round(basl_monthly_salary*(1+annual_growth/100)))
    st.write("Your total earnings after",a ,'months via BASL is',(c+(d*(a%12))))
    e = (c+(d*(a%12)))
    st.write(" *Opted for MBA :* You're still in training")
    st.write(" **ROI of BASL vs ROI of MBA upto month** ",a,':',(round(((c+(d*(a%12)))/basl_investment)*100)),'% vs 0')
    roi_basl = (round(((c+(d*(a%12)))/basl_investment)*100))
   
elif 18<a<24:
    d = (basl_salary*(1+annual_growth/100))/12
    st.write("You received a",annual_growth,"% increment and hence your new monthly salary is Rs.",round(basl_monthly_salary*(1+annual_growth/100)))
    st.write("Your total earnings after",a ,'months via BASL is',round(c+(d*(a%12))))
    e = (c+(d*(a%12)))
    roi_basl = (round(((c+(d*(a%12)))/basl_investment)*100))
    st.write("You got placed via MBA and your monthly salary is", round(mba_salary/12))
    st.write("You total earnings till now via an MBA are",round((mba_salary/12)*(a%18)))
    roi_mba = ((((mba_salary/12)*(a%18))/corresponding_value)*100)
    roii_mba = round(float(roi_mba))
    st.write(" **ROI of BASL vs ROI of MBA upto month** ",a,':',(round(((c+(d*(a%12)))/basl_investment)*100)),'% vs',roii_mba,'%')
    comparison = round(roi_basl/roii_mba)
    st.write(f"BASL ROI is {comparison} times {selected_option}'s")
elif a==24:
    d = (basl_salary*(1+annual_growth/100))/12
    st.write("You received a",annual_growth,"% increment and hence your new monthly salary is Rs.",round(basl_monthly_salary*(1+annual_growth/100)))
    st.write("Your total earnings after",a ,'months via BASL is',round((c+(d*(12)))))
    
    roi_basl = (round(((c+(d*(12)))/basl_investment)*100))
    st.write("You got placed via MBA and your monthly salary is",round(mba_salary/12))
    st.write("You total earnings till now via an MBA are", round((mba_salary/12)*(a%18)))
    roi_mba = ((((mba_salary/12)*(a%18))/corresponding_value)*100)
    roii_mba = round(float(roi_mba))
    st.write(" **ROI of BASL vs ROI of MBA upto month** ",a,':',(round(((c+(d*(12)))/basl_investment)*100)),'% vs',roii_mba,'%')
elif 25<=a<=30:
    d = (basl_salary*(1+annual_growth/100))/12
    st.write("You received a",annual_growth,"% increment again and hence your new monthly salary is Rs.",round(d*(1+annual_growth/100)))
    f = (d*(1+annual_growth/100))
    x = round((c+(d*(12))))
    st.write("Your total earnings after",a ,'months via BASL is',round(x+(f*(a%12))))
    
    roi_basl = ((x+(f*(a%12))/basl_investment)*100)
    st.write("You got placed via MBA and your monthly salary is", round(mba_salary/12))
    st.write("You total earnings till now via an MBA are",round((mba_salary/12)*(a%18)))
    roi_mba = ((((mba_salary/12)*(a%18))/corresponding_value)*100)
    roii_mba = round(float(roi_mba))
    st.write(" **ROI of BASL vs ROI of MBA upto month** ",a,':',round(((x+(f*(a%12)))/basl_investment)*100),'% vs',roii_mba,'%')



    

