# utils/helper.py

import os
import sys

def clear_screen() -> None:
    os.system("clear" if os.name == "posix" else "cls")

def wait_for_enter() -> bool:
    try:
        input("\nPress Enter to continue...")
        return True

    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram interrupted by user! Goodbye")
        return False

    except Exception as e:
        print(f"Somthing went wrong {e}")
        return False
