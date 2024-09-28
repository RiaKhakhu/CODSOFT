"""
A random password generator that generates a password for a user with a specified length and complexity

Author: Khakhu Ria
Version: 23/09/2024

"""

import random
import string


def generate_password(length, difficulty):
    # Character pool: letters, digits, and special characters
    if difficulty == "easy":
        char_pool = string.digits
    elif difficulty == "medium":
        char_pool = string.ascii_letters + string.digits
    else:
        char_pool = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the pool to form the password
    password = ''.join(random.choice(char_pool) for i in range(length))

    return password


# User input for desired length of password
password_length = int(input("Enter the desired length of the password: "))
difficulty = input("How complex should it be? easy(digits), medium(digits+letters) or "
                   "hard(digits+letters+special characters): ")

# Generate and display the password
generated_password = generate_password(password_length, difficulty)
print(f"Here's your Password: {generated_password}")
print("Keep those hackers at bay.")
