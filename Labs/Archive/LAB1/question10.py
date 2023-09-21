loan_amount = 650000
annual_interest_rate = 5
loan_length_years = 20
months_per_year = 12

number_of_months = loan_length_years * months_per_year
monthly_interest_rate = annual_interest_rate / 12




monthly_payment = round(loan_amount * ((monthly_interest_rate / 100) * (1 + monthly_interest_rate / 100) ** number_of_months) / ((1 + monthly_interest_rate / 100) ** number_of_months - 1))



print("You will need to pay $", monthly_payment, "monthly.")
