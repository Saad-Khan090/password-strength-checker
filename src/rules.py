def rule_length(password: str) -> bool:
    return len(password) >= 8

def rule_uppercase(password: str) -> bool:
    return any(char.isupper() for char in password)

def rule_digit(password: str) -> bool:
    return any(char.isdigit() for char in password)

def rule_islower(password: str) -> bool:
    return any(char.islower() for char in password)

def rule_symbol(password: str) -> bool:
    return any(not char.isalnum() for char in password)

def rule_not_repeat(password: str) ->bool:
    for i in range(len(password)-2):
        if password[i] == password[i+1] == password[i+2]:
            return False
    return True

def rule_get_missing(password: str) -> list[str]:
    """Return a list of human-readable messages for rules the password fails."""
    missing: list[str] = []
    if not rule_length(password):
        missing.append('Password length must be at least 8.')
    if not rule_uppercase(password):
        missing.append('Uppercase letter missing.')
    if not rule_symbol(password):
        missing.append('Password must contain a special character.')
    if not rule_digit(password):
        missing.append('Password must contain at least one digit.')
    if not rule_islower(password):
        missing.append('Lowercase letter missing.')
    if not rule_not_repeat(password):
        missing.append('Password has repeated characters.')
    return missing

def rule_get_missing(password: str) -> list[str]:
    missing = list()
    if not rule_length(password):
        missing.append('Password Length must be 8. ')
    if not rule_uppercase(password):
        missing.append("Uppercase later missing. ")
    if not rule_symbol(password):
        missing.append('Password must contain alphabet and spacial character. ')
    if not rule_digit(password):
        missing.append('Password must have some digits. ')
    if not rule_islower(password):
        missing.append('Lowecase latter missing. ')
    if not rule_not_repeat(password):
        missing.append('Password have repeated charactors')
    return missing