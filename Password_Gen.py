import random
import string

def generate_password(length):
    if length < 1:
        return "Error: Password length must be at least 1."

    # Define the character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a positive integer for the password length.")
                continue
            
            password = generate_password(length)
            print(f"Generated password: {password}")

            another = input("Do you want to generate another password? (yes/no): ").lower()
            if another != 'yes':
                print("Thanks for using the password generator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

