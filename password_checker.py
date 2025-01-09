import re

def password_complexity_checker(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assess password strength
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if criteria_met == 5:
        strength = "Strong"
    elif criteria_met >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Include at least one number.")
    if not special_char_criteria:
        feedback.append("Include at least one special character (!@#$%^&*(),.?\":{}|<>).")

    return {
        "strength": strength,
        "feedback": feedback
    }

# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = password_complexity_checker(user_password)
    print(f"Password Strength: {result['strength']}")
    if result['feedback']:
        print("Suggestions:")
        for suggestion in result['feedback']:
            print(f"- {suggestion}")
