# src/password_checker.py

import re

class PasswordChecker:
    @staticmethod
    def check_strength(password: str) -> dict:
        score = 0
        feedback = []
        strength = ""

        if len(password) >= 8:
            score += 1
        else:
            feedback.append("The password must be at least eight characters.")

        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Must have at least one uppercase letter (A-Z)")

        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Must have at least one lowercase letter (a-z)")

        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Must have at least one number (0-9).")

        if re.search(r'[@$!%*?&#.]', password):
            score += 1
        else:
            feedback.append("Must have at least one special character (e.g.:@, #, $, %)")

        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        else:
            strength = "Strong"

        return {
            "length": len(password),
            "score": score,
            "strength": strength,
            "feedback": feedback if feedback else ['Your password is perfect']
        }
