
import streamlit as st
import numpy as np
import pandas as pd
import gspread
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title='ROI Calculator',page_icon="bar_chart")
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()



# Title
#st.title('Calculate your ROI \n **Kraftshala\'s Business and Sales Launchpad (BASL) or Traditional MBA**')

st.title('Choosing the Business-program that delivers the best ROI for you')
st.caption('Business education should be about making better decisions. Let us help you make a decision in 2024 that could impact the long term returns on your investment in a business program.')
st.caption('The tool below is an ROI calculator that enables you to select a B-school and understand the difference between the ROI of the Kraftshala BLP program and a Business-program from the selected school.')
#st.write("This calculator calculates the Return on Investment of a good MBA college vs the Return on investment of :orange[Business Leadership Launchpad by Kraftshala]")

basl_investment = 175000
#mba_fee = st.number_input('Traditional MBA Fee in Rupees', value = 1000000)
#mba_institute = st.selectbox("Select your Institute",options=institutes)
#mba_fee = float(st.selectbox('Your Institute\'s fee ',options=fee))
column1_options = df['Institute'].tolist()
selected_option = st.selectbox("Please select a B-School", column1_options)

#corresponding value = institute's fees
corresponding_value1 = df.loc[df['Institute'] == selected_option, 'Total Fees (Rs)'].values
if len(corresponding_value1) > 0:
     st.success(f"Fee for {selected_option} is: Rs {corresponding_value1[0]} Lacs")
else:
     st.warning("No corresponding value found.")
corresponding_value = corresponding_value1 * 100000
salary1 = df.loc[df['Institute'] == selected_option, 'Average Salary'].values
if len(salary1) > 0:
     st.success(f"Average CTC of {selected_option} student is: Rs {salary1[0]} Lacs")
else:
     st.warning("No corresponding value found.")

salary = (salary1 * 100000)/12
#st.write(corresponding_value/12)

st.caption("Source of Fee & Placement data: https://campusutra.com/mba-pgdm-placement/")


basl_salary = round(float(900000/12))
#mba_salary = st.number_input("The average salary you get placed at if you opt for traditional MBA (in 24 months)", value = 1500000)

annual_growth = 15

# Calculations
basl_monthly_salary = basl_salary/12
#st.write('BASL Minimum monthly salary after 6 months is Rs.',basl_monthly_salary)
mba_salary = round(float(salary))
#n = st.slider("Years from today",0,5,1)
month = st.slider(f"Months since placement from {selected_option}",1,60,1)
#a = st.slider("Months since placement",-6,30,1)


# Validate month input
if not 1 <= month <= 60:
  print("Invalid month. Please enter a value between 1 and 60.")
  exit()

# Initialize variables
total_salary = 0
current_salary = salary
previous_year_salary = current_salary

# Calculate salary and apply growth based on month
for i in range(1, month + 1):
  total_salary += current_salary

  # Apply annual growth every 12 months starting from month 13
  if i % 12 == 0 and i >= 12:
    previous_year_salary *= (1 + annual_growth / 100)
    current_salary = previous_year_salary

total_salary_float = float(total_salary)
# Calculate ROI
roiii_mba = round(float(total_salary_float/corresponding_value)*100)

# Print results
#st.write(f"Total salary earned after {month} months: {total_salary:.2f}")
#st.write(f"ROI after {month} months: {roi:.2f}%")

st.write("Your earnings in",month,"month(s) (in INR) post 24 months training-period: ",int(total_salary_float))
st.write("ROI of studying at",selected_option,":",(round(float(total_salary_float/corresponding_value)*100)),"%")


month_basl = month + 18
total_salary_basl = 0
current_salary_basl = basl_salary
previous_year_salary_basl = current_salary_basl

# Calculate salary and apply growth based on month
for i in range(1, month_basl + 1):
  total_salary_basl += current_salary_basl

  # Apply annual growth every 12 months starting from month 13
  if i % 12 == 0 and i >= 12:
    previous_year_salary_basl *= (1 + annual_growth / 100)
    current_salary_basl = previous_year_salary_basl

total_salary_float_basl = float(total_salary_basl)
# Calculate ROI
roiii_basl = int(total_salary_float_basl/basl_investment)*100

# Print results
#st.write(f"Total salary earned after {month} months: {total_salary:.2f}")
#st.write(f"ROI after {month} months: {roi:.2f}%")

#st.write("Total earnings BASL",total_salary_float_basl)
#st.write("ROI BASL",round(float(total_salary_float_basl/basl_investment)*100),"%")
st.markdown("***When you enroll yourself into the BLP program instead, here's how your earnings & ROI (over the same duration) would look like:***")
st.write("Earnings in",month_basl,"months (in INR) post :orange[BLP Program's Placement]:",int(total_salary_float_basl))
st.write("ROI of the BLP Program:",int(total_salary_float_basl/basl_investment)*100,'%')
#(int(total_salary_float_basl/basl_investment)*100)-(int(total_salary_float/corresponding_value)*100)
st.write('Over',month,'months, the ROI of the BLP program is',(roiii_basl - roiii_mba) ,'% more than the ROI of',selected_option)

st.link_button("Know more about the BLP Program","https://www.kraftshala.com/business-management-course/")