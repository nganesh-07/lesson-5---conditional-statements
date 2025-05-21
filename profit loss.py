actual_cost = float(input("Enter the cost here:"))
sale_amount = float(input("Enter how much it was sold for here:"))

if sale_amount > actual_cost:
    profit = sale_amount - actual_cost
    print(profit)

else:
    print("No profit made.")