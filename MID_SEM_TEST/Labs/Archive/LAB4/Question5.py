age = int(input("Enter the age: "))
enrollment_status = str(input("Is the patient enrolled? (yes/no): "))

if enrollment_status == "yes":
    if age < 13:
        print("Fee: $0")
    elif 13 <= age <= 17:
        print("Fee: $40")
    elif 18 <= age <= 44:
        print("Fee: $60")
    elif 45 <= age <= 64:
        print("Fee: $50")
    elif age <= 65:
        print("Fee: $43")
elif enrollment_status == "no":
    if age < 5:
        print("Fee: $30")
    elif 5 <= age <= 12:
        print("Fee: $40")
    elif 13 <= age:
        print("Fee: $70")