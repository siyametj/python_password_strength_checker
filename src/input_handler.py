# src/input_handler.py

import sys

class InputHandler:
    def take_string_input(self, prompt: str, option: list) -> str:
        while True:
            try:
                user_input = input(f"{prompt}: ").strip()

                if not user_input:
                    print("Input can't be empty! Please try again")
                    continue

                if user_input not in option:
                    print("Invalid input! Please try again!")
                    continue

                return user_input
            except (KeyboardInterrupt, EOFError):
                print("\n\nProgram interrupted by user! Goodbye")
                sys.exit(0)

            except Exception as e:
                print(f"Somthing went wrong {e}")
                sys.exit(0)

    def take_integer_input(self, prompt: str, min_value: int = None, max_value: int = None) -> int:
        while True:
            try:
                user_input = input(f"{prompt}: ").strip()
                if not user_input:
                    print("Input can't be empty! Please try again")
                    continue

                user_input = int(user_input)

                if min_value is not None and user_input < min_value:
                    print(f"Input must be at least {min_val}!")
                    continue

                if max_val is not None and user_input > max_val:
                    print(f"Input cannot be greater than {max_val}!")
                    continue

                return user_input

            except ValueError:
                print("Input not a valid number! Please enter a valid number")
                continue

            except (KeyboardInterrupt, EOFError):
                print("\n\nProgram interrupted by user! Goodbye")
                sys.exit(0)

            except Exception as e:
                print(f"Somthing went wrong {e}")
                sys.exit(0)
