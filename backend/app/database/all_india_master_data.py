"""
All-India Master Districts & Tourist Places Catalog
Aggregates all 36 States and Union Territories covering all ~780 official districts of India.
Every single district includes accurate geo-coordinates, safety index, regional culinary highlights,
and rich tourist attractions with categories, entry fees, visiting hours, and descriptions.
"""

import sys
from pathlib import Path

# Ensure backend root is on sys.path
backend_dir = str(Path(__file__).resolve().parent.parent.parent)
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.database.states_south import SOUTH_STATES
from app.database.states_west import WEST_STATES
from app.database.states_north import NORTH_STATES
from app.database.states_east_central import EAST_CENTRAL_STATES
from app.database.states_northeast_islands import NORTHEAST_ISLANDS_STATES

MASTER_DISTRICTS_DATA = {}

# Merge all regions in order
for region_dict in [
    SOUTH_STATES,
    WEST_STATES,
    NORTH_STATES,
    EAST_CENTRAL_STATES,
    NORTHEAST_ISLANDS_STATES
]:
    for state_name, districts_list in region_dict.items():
        MASTER_DISTRICTS_DATA[state_name] = districts_list

if __name__ == "__main__":
    total_states = len(MASTER_DISTRICTS_DATA)
    total_districts = sum(len(d) for d in MASTER_DISTRICTS_DATA.values())
    total_places = sum(
        sum(len(dist.get("places", [])) for dist in dist_list)
        for dist_list in MASTER_DISTRICTS_DATA.values()
    )
    print(f"Master Catalog Loaded Successfully:")
    print(f" - States/UTs: {total_states}")
    print(f" - Districts: {total_districts}")
    print(f" - Tourist Places: {total_places}")
