from datetime import datetime

# Get the current time (timestamp) in seconds since January 1, 1970
current_timestamp = datetime.timestamp(datetime.now())

# Display the time in seconds in decimal and scientific notation
print(f"Seconds since January 1, 1970: {current_timestamp:.4f} or {current_timestamp:.2e}")

# Get the current date and format it as 'Month Day Year'
formatted_date = datetime.now().strftime("%b %d %Y")
print(formatted_date)





