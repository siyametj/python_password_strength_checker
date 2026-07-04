# 🔒 Python Password Strength Checker

<p align="center">
  <strong>A simple, fast, and professional Password Strength Checker built with Python.</strong><br>
  Analyze password security using a point-based scoring system and receive detailed improvement suggestions.
</p>

---

## ✨ Overview

**Python Password Strength Checker** is a lightweight CLI application that evaluates the strength of a password based on commonly accepted security standards.

Instead of simply labeling a password as **Weak** or **Strong**, the application analyzes multiple security factors and provides meaningful feedback to help users create stronger passwords.

---

## 🚀 Features

- 🔐 **Point-Based Scoring System**
  - Evaluates passwords using a **0–5 score**
  - Classifies passwords as:
    - ❌ Weak
    - ⚠️ Medium
    - ✅ Strong

- 🔍 **Regex-Based Validation**
  - Checks for:
    - Uppercase letters (`A-Z`)
    - Lowercase letters (`a-z`)
    - Numbers (`0-9`)
    - Special characters (`!@#$%^&*...`)

- 💡 **Smart Feedback**
  - Provides personalized suggestions for improving weak passwords.
  - Explains which security requirements are missing.

- 🛡️ **Robust Input Handling**
  - Handles empty input gracefully.
  - Prevents invalid menu selections.
  - Safely catches keyboard interruptions (`Ctrl+C` / `Ctrl+D`).

- 🧼 **Clean Terminal Experience**
  - Automatically clears the terminal between operations.
  - Keeps the CLI interface organized and user-friendly.

---

## 📂 Project Structure

```text
.
├── main.py                  # 🚀 Application entry point
├── README.md                # 📖 Project documentation
├── requirements.txt         # 📦 Dependencies
│
├── src/
│   ├── __init__.py
│   ├── input_handler.py     # 📥 User input handling
│   └── password_checker.py  # 🔒 Password strength logic
│
├── tests/
│   ├── __init__.py
│   └── test.py              # 🧪 Test cases
│
└── utils/
    ├── __init__.py
    └── helper.py            # ⚙️ Utility functions
```

---

## 📊 Password Evaluation Criteria

| Requirement | Points |
|------------|:------:|
| Minimum length | ✅ |
| Uppercase letter | ✅ |
| Lowercase letter | ✅ |
| Number | ✅ |
| Special character | ✅ |

### Score Guide

| Score | Strength |
|:-----:|----------|
| 0–2 | ❌ Weak |
| 3–4 | ⚠️ Medium |
| 5 | ✅ Strong |

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/python_password_strength_checker.git
```

### Navigate into the project

```bash
cd python_password_strength_checker
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application using:

```bash
python main.py
```

Then enter a password when prompted, and the program will:

- Analyze password strength
- Calculate a security score
- Display the strength level
- Suggest improvements (if needed)

---

## 🧪 Running Tests

```bash
python tests/test.py
```

---

## 🎯 Example

```text
Enter Password:
Hello123

Password Strength: Medium (4/5)

Suggestions:
✔ Add at least one special character.
```

---

## 🛠️ Built With

- 🐍 Python 3
- 🔍 Regular Expressions (Regex)
- 💻 Command Line Interface (CLI)

---

## 📌 Future Improvements

- Password entropy calculation
- Common password detection
- Dictionary attack protection
- Password generation
- Colorized terminal output
- Export analysis report

---

## 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

Feel free to fork the repository, open an issue, or submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

<p align="center">
Made with ❤️ using Python
</p>
