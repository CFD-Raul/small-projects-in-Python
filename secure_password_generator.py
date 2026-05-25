# You are developing a user registration system and need to generate secure passwords.
# You want to ensure that each password is strong and includes a mix of character types.
#
# Create a program that generates a random password with 12 characters.
# The password must contain at least:
# - one uppercase letter
# - one lowercase letter
# - one number
# - one special character
#
# Display the generated password to the user.
#
# Expected output:
#
# Generated password: A1b@C3d$E5f&
#\

import secrets
import string

# Generates a function with a result of a predetermined size.
def generate_password(length=12):
    # Since there are four sets of characters, the code must generate at least one of each, that is, at least 4.
    if length < 4 : 
        raise ValueError("Password must have at least 4 characters.")

    # Character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Ensure you have at least one of each type.
    password = [
        secrets.choice(upper),
        secrets.choice(lower),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Fill in the rest.
    all_chars = upper + lower + digits + special
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    # To shuffle things up so they don't become predictable.
    secrets.SystemRandom().shuffle(password)

    return "".join(password)

print("Generated password:", generate_password())
