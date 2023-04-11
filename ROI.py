# Asking for input from user
purchase_price = float(input("What was the purchase price of the property? "))
rental_income = float(input("What is the monthly rental income? "))
operating_expenses = float(input("What are the monthly operating expenses? "))
total_investment = float(input("What is the total investment? "))

# Calculating ROI
cashflow = rental_income - operating_expenses
annual_cashflow = cashflow * 12
cash_on_cash_roi = float(annual_cashflow / total_investment)

print(f"The ROI for the rental property is {cash_on_cash_roi * 100}%.")