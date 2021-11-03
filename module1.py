import pandas as pd
import streamlit as st
from PIL import Image
df = pd.read_csv('startup_funding.csv')
df.columns = [c.replace(' ', '_') for c in df.columns]
image = Image.open('Dashboard_1.png')



# Cleaning Data
dff= df[['Startup_Name','Industry_Vertical','Amount_in_USD', 'City__Location', 'Investors_Name']]

# CD for Startup Name
dff['Startup_Name'] = dff['Startup_Name'].str.replace('xc2','', regex = True)
dff['Startup_Name'] = dff['Startup_Name'].str.replace('\\','', regex = True)
dff['Startup_Name'] = dff['Startup_Name'].str.replace('xa0','', regex = True)
dff['Startup_Name'] = dff['Startup_Name'].str.replace('xe2','', regex = True)
dff['Startup_Name'] = dff['Startup_Name'].str.replace('x80','', regex = True)
dff['Startup_Name'] = dff['Startup_Name'].str.replace('x99s','', regex = True)

#CD for Investors Name
dff['Investors_Name'] = dff['Investors_Name'].str.replace('xc2','', regex = True)
dff['Investors_Name'] = dff['Investors_Name'].str.replace('\\','', regex = True)
dff['Investors_Name'] = dff['Investors_Name'].str.replace('xa0','', regex = True)
dff['Investors_Name'] = dff['Investors_Name'].str.replace('xe2','', regex = True)
dff['Investors_Name'] = dff['Investors_Name'].str.replace('x80','', regex = True)
dff['Investors_Name'] = dff['Investors_Name'].str.replace('x99s','', regex = True)

#CD for Industry Vertical
dff['Industry_Vertical'] = dff['Industry_Vertical'].str.replace('xc2','', regex = True)
dff['Industry_Vertical'] = dff['Industry_Vertical'].str.replace('\\','', regex = True)
dff['Industry_Vertical'] = dff['Industry_Vertical'].str.replace('xa0','', regex = True)
dff['Industry_Vertical'] = dff['Industry_Vertical'].str.replace('xe2','', regex = True)
dff['Industry_Vertical'] = dff['Industry_Vertical'].str.replace('x80','', regex = True)
dff['Industry_Vertical'] = dff['Industry_Vertical'].str.replace('x99s','', regex = True)

#CD for Amount
dff['Amount_in_USD'] = [str(i).replace(',', '') for i in dff.Amount_in_USD]
dff['Amount_in_USD'] = [str(i).replace('Undisclosed', 'NaN') for i in dff.Amount_in_USD]
dff['Amount_in_USD'] = [str(i).replace('nan', 'NaN') for i in dff.Amount_in_USD]
dff['Amount_in_USD'] = [str(i).replace('N/A', 'NaN') for i in dff.Amount_in_USD]
dff['Amount_in_USD'] = [str(i).replace('undisclosed', 'NaN') for i in dff.Amount_in_USD]
dff['Amount_in_USD'] = [str(i).replace('NaN', str(0)) for i in dff.Amount_in_USD]
dff['Amount_in_USD'] = [str(i).replace('unknown', str(0)) for i in dff.Amount_in_USD]
dff['Amount_in_USD'] = dff['Amount_in_USD'].replace(r'[<.]', '', regex=True)
dff['Amount_in_USD'] = dff['Amount_in_USD'].replace(r'[<+]', '', regex=True)
dff['Amount_in_USD'] = dff['Amount_in_USD'].replace(r'[<\\xc\\xa]', '', regex=True)

#CD for City
dff['City__Location'] = dff['City__Location'].str.replace('xc2','', regex = True)
dff['City__Location'] = dff['City__Location'].str.replace('\\','', regex = True)
dff['City__Location'] = dff['City__Location'].str.replace('xa0','', regex = True)
dff['City__Location'] = dff['City__Location'].str.replace('xe2','', regex = True)
dff['City__Location'] = dff['City__Location'].str.replace('x80','', regex = True)
dff['City__Location'] = dff['City__Location'].str.replace('x99s','', regex = True)


# DROP NULL
dff = dff.dropna()



st.write(df)
st.write(dff)
st.image(image)

dff['Amount_in_USD'] = dff['Amount_in_USD'].astype('int64')
dff.dtypes

