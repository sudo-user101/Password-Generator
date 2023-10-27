import random
from string import digits, ascii_letters, punctuation

def generate_password(length):
    all_chars = digits + ascii_letters + punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

user_input = int(input("Enter Length of password: "))
print("Generated password:", generate_password(user_input))
