month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
user_number = int(input("Enter the number: "))

user_number_corrected = user_number - 1
month = month_list[user_number_corrected]

print(f"{month} is month {user_number}")