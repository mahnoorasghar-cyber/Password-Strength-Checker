# Write a function to check password strength
from getpass import getpass
from zxcvbn import zxcvbn


def check_password_strength(password: str) -> dict:
    result = zxcvbn(password)
    labels = ["Very weak", "Weak", "Fair", "Strong", "Very strong"]

    return {
        "score": result["score"],  # 0 to 4
        "label": labels[result["score"]],
        "warning": result["feedback"]["warning"],
        "suggestions": result["feedback"]["suggestions"],
    }


if __name__ == "__main__":
    password = input("Password to check: ")
    report = check_password_strength(password)

    print(f"Strength: {report['label']}")
    if report["warning"]:
        print(report["warning"])
    for suggestion in report["suggestions"]:
        print(f"- {suggestion}")

