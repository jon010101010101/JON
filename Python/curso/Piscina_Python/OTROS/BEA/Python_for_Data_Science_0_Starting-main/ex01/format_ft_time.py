
from datetime import datetime

# To get current_date
current_date = datetime.now()

# To get seconds from 1970 January first
Seconds_from_1970 = current_date.timestamp()

# Print output in required format.
print(f"Seconds since January 1, 1970: {Seconds_from_1970:,.4f} or {Seconds_from_1970:.2e} in scientific notation")
print(f"{current_date.strftime('%b %d %Y')}")
