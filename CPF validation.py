# CPF (Cadastro de Pessoas Físicas) is a Brazilian individual taxpayer
# identification number composed of 11 digits. It is commonly used
# for identification in financial and legal processes in Brazil.
#
# You need to validate whether a given CPF has the correct format
# before proceeding with further processing.
#
# A valid CPF must:
# - contain exactly 11 digits
# - include only numeric characters (no letters or symbols)
#
# Create a program that asks the user to enter a CPF number and
# checks whether it meets these requirements.
#
# Example input:
# Enter your CPF: 12345678901
#
# Expected output:
# Valid CPF.
#
# If the input contains non-numeric characters:
# Enter your CPF: 1234abc567
# Error: The CPF must contain only numbers.
#
# If the CPF does not have exactly 11 digits:
# Enter your CPF: 1234567
# Error: The CPF must have exactly 11 digits.
# \


def cpf_validation():
    while True:
        
        user_cpf = input("Enter your CPF: ").strip()

        if not user_cpf.isdigit():
            print("Error: The CPF must contain only numbers.")
            continue

        if len(user_cpf) != 11:
            print("Error: The CPF must have exactly 11 digits.")
            continue

        if len(set(user_cpf)) == 1:
            print("Error: The CPF cannot have all digits the same.")
            continue
        
        print("CPF validated successfully!")
        return user_cpf       


cpf_validation()