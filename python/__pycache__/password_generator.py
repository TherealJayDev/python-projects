import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if length <= 0:
        raise ValueError("Password length must be a positive integer.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the password length: "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
