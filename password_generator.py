import random
from string import digits, ascii_letters, punctuation

def pg(length):
    code = digits + ascii_letters + punctuation
    results = "".join(random.choice(code) for _ in range(length))
    return results

try:
    user_input = input("Enter Length of password:")
    if user_input.strip() == "":
        raise ValueError("Input cannot be blank")
    else:
      print(pg(user_input))

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Error:", e)
