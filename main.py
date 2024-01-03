
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

#st.write("This calculator calculates the Return on Investment of a good MBA college vs the Return on investment of :orange[Business Leadership Launchpad by Kraftshala]")

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

st.caption("Source of Fee & Placement data: https://campusutra.com/mba-pgdm-placement/")


basl_salary = 900000
#mba_salary = st.number_input("The average salary you get placed at if you opt for traditional MBA (in 24 months)", value = 1500000)

annual_growth = st.number_input("Annual growth in %age",value = 15)

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

# Calculate ROI
roi = (total_salary / corresponding_value)  * 100

# Print results
print(f"Total salary earned after {month} months: {total_salary:.2f}")
print(f"ROI after {month} months: {roi:.2f}%")



