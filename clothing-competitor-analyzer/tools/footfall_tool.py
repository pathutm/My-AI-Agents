from langchain.tools import tool
from typing import List, Dict
import random

# You can later integrate with Google Places API or Tavily
# For now, mock response for demo/testing

MOCK_COMPETITORS = [
    {"name": "Trendy Threads", "address": "Koramangala 5th Block"},
    {"name": "Style Studio", "address": "Koramangala 6th Block"},
    {"name": "Urban Wear", "address": "Sony Signal, Koramangala"},
    {"name": "Fashion Point", "address": "Jyoti Nivas College Road"},
    {"name": "WearHouse", "address": "Koramangala 7th Block"},
]

def generate_mock_footfall() -> Dict:
    return {
        "average_footfall_per_day": random.randint(200, 500),
        "busiest_hours": random.choice(["5 PM - 8 PM", "1 PM - 4 PM", "11 AM - 2 PM"]),
        "weekend_peak": random.choice(["Saturday", "Sunday"]),
    }

@tool
def get_nearby_competitors(location: str = "Koramangala") -> List[Dict]:
    """
    Returns a list of nearby clothing store competitors with mock footfall data and peak hours.
    You can later integrate with real data sources like Tavily or Google Places API.
    """
    competitors_with_data = []
    for store in MOCK_COMPETITORS:
        footfall_data = generate_mock_footfall()
        competitors_with_data.append({
            "store_name": store["name"],
            "address": store["address"],
            "footfall_data": footfall_data
        })
    return competitors_with_data
