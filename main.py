import asyncio
from airstack.execute_query import AirstackClient
import os
from dotenv import load_dotenv
import json

load_dotenv()  # Load variables from .env file
secret_key = os.environ.get('SECRET_KEY')
api_client = AirstackClient(api_key=secret_key)  

query = """
query MyQuery($timeFrame: TimeFrame!, $audience: Audience!, $blockchain: TrendingBlockchain!, $criteria: TrendingMintsCriteria!, $limit: Int = 200) {
  TrendingMints(
    input: {timeFrame: $timeFrame, audience: $audience, blockchain: $blockchain, criteria: $criteria, limit: $limit}
  ) {
    TrendingMint {
      address
      erc1155TokenID
      criteriaCount
      timeFrom
      timeTo
      token {
        name
        symbol
        type
      }
    }
  }
}
"""

variables = {
  "timeFrame": "seven_days",
  "blockchain": "base",
  "limit": 200,
  "criteria": "unique_wallets",
  "audience": "farcaster"
}

async def main():
    execute_query_client = api_client.create_execute_query_object(query=query, variables=variables)
    query_response = await execute_query_client.execute_paginated_query()
    # print(query_response.data)
    with open('data.json', 'w') as file:
        json.dump(query_response.data, file, indent=4)

asyncio.run(main())