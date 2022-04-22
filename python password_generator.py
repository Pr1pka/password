import string
import random


def password_generator():
    min_len = 14
    max_len = 50
    length = random.randint(min_len, max_len)
    password = [random.choice(string.ascii_lowercase),
                random.choice(string.ascii_uppercase),
                random.choice(string.digits),
                random.choice(string.punctuation)]

    for i in range(length - len(password)):
        password.append(random.choice(''.join([string.ascii_letters, string.digits,
                                               string.punctuation])))

    random.shuffle(password)
    password = ''.join(password)

    return password


print(password_generator())
