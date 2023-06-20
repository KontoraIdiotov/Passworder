import random
digits =  '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
iscls = "il1Lo0O"
chars = ''
kol = int(input('Сколько паролей хочешь сгенерировать : '))
num = int(input('Длина одного пороля : '))
digit = input('Включить цифры в пароль? да/нет : ')
lowlet = input('Включить строчные буквы  в пароль? да/нет : ')
upplet = input('Включить прописгые буквы  в пароль? да/нет : ')
sim = input('Включить символы " !#$%&*+-=?@^_. " в пароль? да/нет : ')
iscl = input('Включить символы с неоднозначным значением "il1Lo0O"? да/нет : ')
print()
if digit == 'да' or digit == 'д':
    chars += digits
if lowlet == 'да' or lowlet == 'д':
    chars += lowercase_letters
if upplet == 'да' or upplet == 'д':
    chars += uppercase_letters
if sim == 'да' or sim == 'д':
    chars += punctuation
if iscl == 'нет' or iscl == 'н' or iscl == 'не':
    for i in chars:
        if i in iscls:
            chars = chars.replace(i, '')
def generate_password(x, y):
    for i in range(x):
        password = ''
        for j in range(y):
            password += random.choice(chars)
        print(password)
generate_password(kol, num)