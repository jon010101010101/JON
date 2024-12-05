from datetime import datetime

# Get the current time (timestamp) in seconds since January 1, 1970
current_timestamp = datetime.timestamp(datetime.now())

# Display the time in seconds in decimal and scientific notation
print(f"Seconds since January 1, 1970: {current_timestamp:.4f} or {current_timestamp:.2e}")

# .: Specifies that we want to include decimals in the number.
# 4: Indicates that we want to display 4 decimal places.
# f: Specifies that we want to format the number as a floating-point
# number (decimal).

# :: Indicates the beginning of the format specification.

# .2: Means that we want two decimal places after the decimal point.

# e: Indicates that we want to format the number in scientific or exponential notation. In scientific notation, numbers are expressed as a coefficient multiplied by a power of ten, in the form:
# a x 10 raised to b

# Get the current date and format it as 'Month Day Year'
formatted_date = datetime.now().strftime("%b %d %Y")
print(formatted_date)

# strftime means "string format time." 
# It converts the datetime object into a string using the specified format.

# %b: abbreviated month (e.g., "Jan", "Feb", "Mar", etc.).
# %d: day of the month as a decimal number, with zero padding if necessary (e.g., "01", "02", ..., "31").
# %Y: year as a four-digit decimal number (e.g., "2024").
# strftime: A Python function to format dates. It comes from the time
# or datetime module.



