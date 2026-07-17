#  generating the discount calculation function

def discount_calculator():
    # Operating an infinite loop to automate program resumption in case of error.
    while True:

        try:
            # obtaining gross price
            gross_amount = float(input("Enter the gross amount to pay: "))        
                           
                              

            # validating gross price
            if gross_amount <= 0:
                raise ValueError("The value provided is less than or equal to zero. Please enter a larger value.")
                
            
            # obtaining percentage discount
            discount_percentage = int(input("Enter the percentage of discount: "))

            # validating the discount
            if discount_percentage < 0 or discount_percentage > 100:
                raise ValueError("The discount cannot be less than zero or greater than 100%. Please enter a valid discount.")
                
            
            # calculating the discount
            discount = gross_amount * discount_percentage / 100
            amount_to_pay = gross_amount - discount

            # displaying result
            message1 = f"""
            The regular price is: {gross_amount:.2f}USD;
            The discount ({discount_percentage}%) is {discount:.2f}USD;
            The total to pay is {amount_to_pay:.2f}USD.
            """
            message2 = f"""
            The regular price is: {gross_amount:.2f}USD.
            No discount was applied.
            The total to pay is {amount_to_pay:.2f}USD.
            """
            if discount > 0:
                print(message1)
            elif discount == 0:
                print(message2)

        except ValueError as e:
            if "could not convert string to float:" in str(e):
                print("Invalid input. Please enter a positive numeric value!")
            elif "invalid literal" in str(e):
                print("Invalid input! Please enter only integer numbers.")
            else:
                print(f"Invalid input! {e}")
        else:
            break

discount_calculator()