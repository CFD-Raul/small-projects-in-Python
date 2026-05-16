# You work as a waiter in a restaurant and need to calculate
# the tip that customers leave when paying the bill.
# The restaurant suggests a 10% tip, but some customers
# may choose to give more or less.
#
# To speed up the process, you want a program that receives
# the total bill amount and the desired tip percentage,
# then displays the final amount the customer should pay.
#
# Create a program that asks the user for the bill amount
# and the tip percentage. The program should calculate
# and display the tip amount and the total to be paid.
#
# Example input:
# Enter the bill amount: 120.00
# Enter the tip percentage: 10
#
# Expected output:
# Tip amount: $12.00
# Total to pay: $132.00

def percentage_calculator():
    gross_value = float(input("Enter the bill gross amount: "))
    tip_rate = float(input("Enter the tip percentage: ")) /100
    tip_amount = gross_value * tip_rate
    net_value = gross_value + tip_amount
    message = (f"""
    The bill gross amount is U${gross_value:.2f}
    The Tip amount is U${tip_amount:.2f}
    Total to pay: U${net_value:.2f}
    """)
    return message

print(percentage_calculator())