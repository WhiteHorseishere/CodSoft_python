# Password Generator
import random
import string
print("=== Password Generator ===")
# User input
length = int(input("Enter the desired password length: "))
# Characters to use in password
characters = string.ascii_letters + string.digits + string.punctuation
# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

# Display password
print("\nGenerated Password:")
print(password)