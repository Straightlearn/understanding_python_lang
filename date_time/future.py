from datetime import datetime, timedelta

# Set the target date
target_date = datetime(2025, 12, 31)

# Calculate the number of days from now to the target date
days_until_target = target_date - datetime.now()

# Print the number of days
print(f'Number of days until {target_date}: {days_until_target.days}')

