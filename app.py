import pandas as pd

# List of phones to filter
phones_to_remove = [
    5544984267207
]

# Read the spreadsheet
df = pd.read_excel('xlsx_files/excel.xlsx', engine='openpyxl')

# Filters lines that do not contain phones in the list
df = df[~df['phone'].isin(phones_to_remove)]

# Save the spreadsheet again
df.to_excel('resul.xlsx', index=False, engine='openpyxl')
