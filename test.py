# # res = tavily_search("Best Hotels in India")
# # print(res)


# res = search_flights("Plan a 7 days Germany trip from India")

# print(res)




# import os
# from dotenv import load_dotenv
# import requests

# load_dotenv()

# API_KEY = os.getenv("AVIATIONSTACK_API_KEY")
# print(f"API Key exists: {bool(API_KEY)}")
# print(f"API Key: {API_KEY}")
# print(f"Length: {len(API_KEY) if API_KEY else 0}")

# # Direct API call
# response = requests.get(
#     "https://api.aviationstack.com/v1/flights",
#     params={
#         "access_key": API_KEY,
#         "limit": 1,
#         "dep_iata": "DEL",
#         "arr_iata": "NRT"
#     }
# )

# print("\nStatus Code:", response.status_code)
# print("Response:", response.json())

# from backend import run_travel_agent

# user_input = input("Enter travel request: ")

# response = run_travel_agent(
#     user_input=user_input,
#     thread_id="test_user"
# )

# print("]n FIINAL RESPONSE: \n")
# print(response["answer"])
import os 
from dotenv import load_dotenv
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

import asyncio
from mcp_client_test import get_all_tools,tavily_mcp_search

if __name__ == "__main__":
    query = "Latest news about AI"
    print(bool(TAVILY_API_KEY))
    asyncio.run(tavily_mcp_search(query))