p_amount = int(input("Please enter principle amount: "))
years = int(input("Please enter time is years: "))
rate_interest = float(input("Please enter rate of interest: "))

interest = (p_amount * years * rate_interest)/100

print("Total interest will be: ", interest)
