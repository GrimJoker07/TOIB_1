import random
import string

def generate_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

try:
    length = int(input("Введите длину пароля (по умолчанию 8 символов): ") or 8)
except ValueError:
    print("Некорректный ввод. Будет использована длина по умолчанию (8 символов).")
    length = 8

print(generate_password(length))
