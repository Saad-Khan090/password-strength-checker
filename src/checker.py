
import os
import sys
# ensure project root is on sys.path so 'src' package can be imported when
# running this file directly (e.g. `python src/checker.py`).
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.rules import (
    rule_digit, 
    rule_length, 
    rule_uppercase, 
    rule_islower, 
    rule_not_repeat, 
    rule_symbol,
    rule_get_missing,
)
def check_password_strength(password: str) -> str:
    """Return a short strength label for the given password (used by tests).

    For CLI/display purposes the missing requirements can be obtained with
    `rule_get_missing(password)` and passed along to `display_result`.
    """
    checks = [
        rule_uppercase(password),
        rule_digit(password),
        rule_length(password),
        rule_symbol(password),
        rule_not_repeat(password),
        rule_islower(password)
    ]
    score = sum(checks)   # sum the number of true functions
    if score >= 6:
        return "Very Strong"
    elif score >= 4:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"


if __name__ == '__main__':
    from src.utlis import get_password_input, display_result
    password = get_password_input()
    status = check_password_strength(password)
    missing = rule_get_missing(password)
    display_result((status, missing))