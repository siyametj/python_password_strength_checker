# main.py

import sys
from utils.helper import clear_screen, wait_for_enter
from src.input_handler import InputHandler
from src.password_checker import PasswordChecker

def show_menu() -> None:
    print("=" * 55)
    print("  WELCOME TO PYTHON PASSWORD STRENGTH CHECKER  ")
    print("=" * 55)
    print("1. Check Password Strength ")
    print("2. Exit Program ")
    print("-" * 55)

def run_checker() -> None:
    clear_screen()
    print("--- Password Strength Analyzer ---\n")

    while True:
        password = input("Enter the password to check: ").strip()
        if password:
            break
        print("Password cannot be empty! Please try again.")

    result = PasswordChecker.check_strength(password)

    print("\n" + "=" * 40)
    print(f"ANALYSIS REPORT")
    print("=" * 40)
    print(f"Password Length : {result['length']}")
    print(f"Score           : {result['score']}/5")
    print(f"Strength        : {result['strength']}")
    print("-" * 40)
    print("Feedback:")

    for item in result['feedback']:
        print(f"  - {item}")
    print("=" * 40)

def main():
    while True:
        clear_screen()
        show_menu()

        choice = InputHandler.take_string_input("Choose an option", ["1", "2"])

        if choice == "1":
            run_checker()
            if not wait_for_enter():
                break
        elif choice == "2":
            print("\nThank you for using Password Checker! Goodbye")
            break

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram interrupted! Goodbye.")
        sys.exit(0)
