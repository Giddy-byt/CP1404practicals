# 4. Deep Sleep Calculation (Percentage)
total_sleep_seconds = int(input("Total sleep in seconds: "))
deep_sleep_seconds = int(input("Deep sleep in seconds: "))

# Calculate percentage of deep sleep
percentage_deep_sleep = (deep_sleep_seconds / total_sleep_seconds) * 100

# Calculate minutes and seconds for total sleep and deep sleep
total_minutes, total_seconds = divmod(total_sleep_seconds, 60)
deep_minutes, deep_seconds = divmod(deep_sleep_seconds, 60)

print(f"Deep sleep: {deep_minutes}m {deep_seconds}s")
print(f"Total sleep: {total_minutes}m {total_seconds}s")
print(f"Percentage: {percentage_deep_sleep:.2f}%")
