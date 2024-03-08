import json

# Function to load and parse JSON data from a file
def parse_trending_mints(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        trending_mints = data['data']['TrendingMints']['TrendingMint']

        for mint in trending_mints:
            address = mint['address']
            token_type = mint['token']['type']
            token_name = mint['token']['name']
            symbol = mint['token']['symbol']
            criteria_count = mint['criteriaCount']
            time_from = mint['timeFrom']
            time_to = mint['timeTo']
            
            # Print the parsed information
            print(f"Address: {address}")
            print(f"Token Type: {token_type}")
            print(f"Token Name: {token_name}")
            print(f"Symbol: {symbol}")
            print(f"Criteria Count: {criteria_count}")
            print(f"Timeframe: {time_from} to {time_to}")
            print("-------------------------------")

# Assuming the JSON file is named 'data-3.json'
parse_trending_mints('data.json')
