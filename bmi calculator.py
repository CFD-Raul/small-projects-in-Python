# Function responsible for collecting and validating the patient's body mass
def getting_body_mass():
    while True:
        try:
            # Collecting body mass input and converting to float
            body_mass = float(input("Please enter your weight in kg (use a dot for decimals if needed): "))
            # Validating that body mass is greater than zero
            if body_mass <= 0:
                raise ValueError("Weight cannot be less than or equal to zero. Please try again!")
            return body_mass
        except ValueError as e:
            # Handling non-numeric input
            if "could not convert string to float:" in str(e):
                print("Invalid input. Please enter a positive numeric value!")
            # Handling custom validation errors
            else:
                print(f"Invalid input! {e}")

# Function responsible for collecting and validating the patient's height
def getting_height():
    while True:
        try:
            # Collecting height input and converting to float
            height = float(input("Please enter your height in meters (use a dot for decimals if needed): "))
            # Validating that height is within acceptable range
            if height <= 0 or height >= 3:
                raise ValueError("Height cannot be less than or equal to zero, nor greater than or equal to 3 meters. Please try again!")
            return height
        except ValueError as e:
            # Handling non-numeric input
            if "could not convert string to float:" in str(e):
                print("Invalid input. Please enter a positive numeric value!")
            # Handling custom validation errors
            else:
                print(f"Invalid input! {e}")

# Function responsible for calculating the patient's BMI
def calculating_patients_bmi():
    # Collecting validated inputs
    body_mass = getting_body_mass()
    height = getting_height()
    # Calculating BMI
    bmi_height = height * height
    # Checking for zero division before operating
    if bmi_height == 0:
        raise ZeroDivisionError("Cannot divide by zero. Please review your height input.")
    bmi = body_mass / bmi_height
    return bmi

# Function responsible for classifying the BMI and displaying the result
def classifying_bmi():
    # Calculating BMI
    bmi = calculating_patients_bmi()
    # Classifying BMI according to standard ranges
    if bmi < 18.5:
        bmi_class = "Underweight"
    elif bmi < 25:
        bmi_class = "Normal weight"
    elif bmi < 30:
        bmi_class = "Overweight"
    elif bmi < 35:
        bmi_class = "Obesity grade I (Risk of health complications)"
    elif bmi < 40:
        bmi_class = "Obesity grade II (High risk of health complications)"
    else:
        bmi_class = "Obesity grade III (Morbid obesity - Imminent risk of cardiorespiratory, motor and neurological damage)"
    # Displaying result
    print(f"Your Body Mass Index is {bmi:.2f}, and your BMI status is: {bmi_class}!")

# Running the program
classifying_bmi()