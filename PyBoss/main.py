

import os
import csv
import datetime


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

name = []
first_name = []
last_name = []
dob = []
ssn = []
state =[]
emp_id = []
with open("employee_data1.csv", 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        emp_id.append(row[0])
        name = row[1].split(" ")
        first_name.append(name[0])
        last_name.append(name[1])
        dob.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
        ssn.append('*' * 3 + "-" + '*' * 2 + "-" + row[3][-4:])
        state.append(us_state_abbrev[row[4]])
output_data = zip(emp_id, first_name, last_name, dob, ssn, state)

for rows in output_data:
    print(rows)


with open("converted_employee_data.csv", 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    
    writer.writerows(zip(emp_id, first_name, last_name, dob, ssn, state))
    

