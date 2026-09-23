import random
import string


def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4.")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("\n===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    try:
        password = generate_password(length)
        print("\nGenerated Password:", password)
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
