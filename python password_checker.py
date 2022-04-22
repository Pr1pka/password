import string


def password_rules():
    print('\n*** Password Rules ***\n')
    print('- Password must contain both lowercase and uppercase characters')
    print('- Password must contain digits')
    print(f'- Password must contain at least one punctuation character ({string.punctuation})')
    print('- Password must not contain any other characters')
    print('- Password must be at least 14 characters long\n')


def password_length_checker(password):
    required_len = 14

    if len(password) < required_len:
        print(f'- Password must be at least {required_len} characters long')
        return False
    return True


def char_checker(password):
    digit_flag, upper_flag, lower_flag, punctuation_flag, invalid_char_flag \
        = False, False, False, False, False
    is_valid = True

    for char in password:
        if char.isdigit():
            digit_flag = True
            continue
        if char.isupper():
            upper_flag = True
            continue
        if char.islower():
            lower_flag = True
            continue
        if char in string.punctuation:
            punctuation_flag = True
            continue
        invalid_char_flag = True

    if not upper_flag or not lower_flag:
        print('- Password must contain both lowercase and uppercase characters')
        is_valid = False
    if not digit_flag:
        print('- Password must contain digits')
        is_valid = False
    if not punctuation_flag:
        print(f'- Password must contain at least one punctuation character ({string.punctuation})')
        is_valid = False
    if invalid_char_flag:
        print('- Invalid character')
        is_valid = False

    return is_valid


def password_checker(password):
    is_valid = True
    if not password_length_checker(password):
        is_valid = False
    if not char_checker(password):
        is_valid = False

    if is_valid:
        print('Password is valid')
    return is_valid


password_rules()
while True:
    if password_checker(input('Input password: ')):
        break
