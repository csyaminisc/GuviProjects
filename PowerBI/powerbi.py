# importing modules
import json
import requests
import pandas as pd

# storing the url in the form of string
url = "https://api.covid19india.org/state_district_wise.json"
data = ((requests.get(url)).json())

# Initialize lists to store the extracted data
states = []
districts = []
active_cases = []
deceased_cases = []
recovered_cases = []
confirmed_cases = []

# Iterate through the JSON data
for state, state_data in data.items():
    for district, district_data in state_data['districtData'].items():
        states.append(state)
        districts.append(district)
        active_cases.append(district_data.get('active', 0))  # Handle missing data with .get()
        deceased_cases.append(district_data.get('deceased', 0))
        recovered_cases.append(district_data.get('recovered', 0))
        confirmed_cases.append(district_data.get('confirmed', 0))

# Create a Pandas DataFrame
df = pd.DataFrame({
    'state': states,
    'district': districts,
    'active': active_cases,
    'deceased': deceased_cases,
    'recovered': recovered_cases,
    'confirmed': confirmed_cases
})
# saving the dataframe
df.to_csv('powerbicoviddata.csv')
print(df)
