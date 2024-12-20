import pandas as pd

file_path = r'C:\Users\Daryn Bang\Desktop\database_data\laptop_data.xlsx'
df = pd.read_excel(file_path, sheet_name="Sheet1")

print(df['Price'])
