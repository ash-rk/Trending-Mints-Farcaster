import pandas as pd
import json

# Load JSON data from file
def load_json_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

# Convert JSON data to pandas DataFrame
def json_to_dataframe(json_data):
    trending_mints = json_data['data']['TrendingMints']['TrendingMint']
    df = pd.json_normalize(trending_mints)
    return df

# Rename and rearrange columns in the DataFrame
def customize_dataframe(df):
    # Rename columns
    df.rename(columns={
        'address': 'Token Address',
        'token.name': 'NFT',
        'token.symbol': 'Symbol',
        'token.type': 'Token Type',
        'criteriaCount': 'Unique Mints',
        'timeFrom': 'Start Time',
        'timeTo': 'End Time'
    }, inplace=True)
    
    # Rearrange columns
    column_order = ['Token Address', 'NFT', 'Unique Mints', 'Symbol', 'Token Type', 'Start Time', 'End Time']
    df = df[column_order]
    return df

# Save DataFrame to CSV
def save_dataframe_to_csv(df, csv_file_name):
    df.to_csv(csv_file_name, index=False)

# Main process
json_file = 'data.json'  # Replace with the path to your JSON file
json_data = load_json_data(json_file)
df = json_to_dataframe(json_data)

# Customize DataFrame (rename and rearrange columns)
df_customized = customize_dataframe(df)

# Specify your desired CSV file name
csv_file_name = 'trending_mints.csv'
save_dataframe_to_csv(df_customized, csv_file_name)

print(f"Data has been saved to {csv_file_name}.")
