import numpy as np

# 1. Create an array of daily messages sent by your bot for 7 days
daily_messages = np.array([45, 52, 60, 58, 72, 85, 90])

# 2. Basic Math with one command
total_messages = np.sum(daily_messages)
average_per_day = np.mean(daily_messages)
max_messages = np.max(daily_messages)

# 3. The "AI" logic: What if your bot becomes 20% more efficient?
efficient_messages = daily_messages * 1.2

print(f"--- Felix's Bot Report ---")
print(f"Total messages this week: {total_messages}")
print(f"Average daily: {average_per_day:.2f}")
print(f"Busiest day: {max_messages} messages")
print(f"Projected 20% growth: {efficient_messages.round(1)}")
