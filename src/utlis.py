def get_password_input() -> str:
    return input('Please Enter a password to check strength: ')

def display_result(result: str):
    print(f'Password strength: {result}')
    