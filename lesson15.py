import random
import string

def generate_password(length, use_numbers, use_symbols):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    characters = letters

    if use_numbers:
        characters += numbers

    if use_symbols:
        characters += symbols

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

def check_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    length = len(password)

    score = 0

    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_number:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        return "WEAK ❌"
    elif score <= 4:
        return "MEDIUM ⚠️"
    else:
        return "STRONG 💪"

def main():
    print("================================")
    print("   Welcome to Password Generator")
    print("================================")

    name = input("Enter your name: ")

    while True:
        try:
            length = int(input("How long should the password be? "))
            if length < 4:
                print("Please enter a length of at least 4!")
                continue
        except ValueError:
            print("Error: Please enter a valid number!")
            continue

        use_numbers_input = input("Include numbers? (yes/no): ").lower()
        use_numbers = use_numbers_input == "yes"

        use_symbols_input = input("Include symbols? (yes/no): ").lower()
        use_symbols = use_symbols_input == "yes"

        print(f"\nGenerating password for {name}...")
        password = generate_password(length, use_numbers, use_symbols)
        strength = check_strength(password)

        print(f"Your password is: {password}")
        print(f"Password strength: {strength}")

        again = input("\nWant to generate another? (yes/no): ").lower()
        if again != "yes":
            print(f"\nGoodbye {name}! Keep your passwords safe! 🔐")
            break

main()