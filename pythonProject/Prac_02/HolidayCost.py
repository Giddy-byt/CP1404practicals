# 3. Holiday Cost
daily_food_cost = float(input("Daily food cost: $"))
daily_activities_cost = float(input("Daily activities cost: $"))
number_of_days = int(input("Number of days: "))

hotel_cost_per_day = 75  # Constant for hotel cost per day

total_cost = (daily_food_cost + daily_activities_cost) * number_of_days + hotel_cost_per_day * number_of_days
print("The trip will cost $", total_cost, sep="")
