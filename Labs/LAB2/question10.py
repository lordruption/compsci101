days = int(input("Enter the total number of days: "))

years = days // 365
year_remainer = days % 365
weeks = year_remainer // 7
weeks_remainder = year_remainer % 7






print(f"{days} days is equal to {years} years, {weeks} weeks, and {weeks_remainder} days.")