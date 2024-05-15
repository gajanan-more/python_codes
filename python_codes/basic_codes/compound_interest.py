p_amount = int(input("Please enter principle amount: "))
years = int(input("Please enter time is years: "))
rate_interest = float(input("Please enter rate of interest: "))

total_amount = p_amount * ( 1 + rate_interest/100) ** years

interest = total_amount - p_amount

print("Total interest will be: ", interest)
