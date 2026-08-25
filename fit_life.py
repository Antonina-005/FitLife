# Проект FitLife - MVP версия 1.0

# Константы модуля
WATER_NORM_PER_KG_ML = 30  # Норма воды: 30 мл на 1 кг веса
ML_IN_LITER = 1000         # Количество миллилитров в одном литре

# Пороговые значения нормы ИМТ по ВОЗ
BMI_LOW_NORM = 18.5
BMI_HIGH_NORM = 25.0


# Функции для точного расчета данных
# 1. Ввод Имени
while True:
    user_name = input('Как тебя зовут? ').strip()
    if not user_name:
        print(
            'Ошибка: имя не может быть пустым. '
            'Пожалуйста, повторите ввод еще раз.',
        )
        continue
    break

# 2. Ввод Возраста
while True:
    try:
        user_age = int(input('Сколько тебе лет? '))
        if 1.0 <= user_age <= 120.0:
            break
        print(
            'Ошибка: введите число в разумных пределах '
            '(от 1.0 до 120.0).',
        )
    except ValueError:
        print('Ошибка: пожалуйста, введите корректное число.')

# 3. Ввод Веса
while True:
    try:
        user_weight = float(input('Какой у тебя вес в кг? '))
        if 10.0 <= user_weight <= 300.0:
            break
        print(
            'Ошибка: введите число в разумных пределах '
            '(от 10.0 до 300.0).',
        )
    except ValueError:
        print('Ошибка: пожалуйста, введите корректное число.')

# 4. Ввод Роста
while True:
    try:
        user_height = float(
            input('Какой у тебя рост в метрах (например, 1.75)? '),
        )
        if 0.5 <= user_height <= 2.5:
            break
        print(
            'Ошибка: введите число в разумных пределах '
            '(от 0.5 до 2.5).',
        )
    except ValueError:
        print('Ошибка: пожалуйста, введите корректное число.')


# Расчета
# Расчет Индекса Массы Тела (ИМТ). Рост в метрах.
user_bmi = round(
    user_weight / (user_height ** 2),
    1
)

# Расчет суточной нормы воды в литрах
water_needed_liters = round(
    (user_weight * WATER_NORM_PER_KG_ML) / ML_IN_LITER,
    2
)


# Определение склонения слова лет
last_digit = user_age % 10
last_two_digits = user_age % 100

if 11 <= last_two_digits <= 14:
    age_word = 'лет'
elif last_digit == 1:
    age_word = 'год'
elif 2 <= last_digit <= 4:
    age_word = 'года'
else:
    age_word = 'лет'


# ИМТ по стандартам ВОЗ
if user_bmi < BMI_LOW_NORM:
    bmi_recommendation = 'Ешьте!'
elif user_bmi >= BMI_HIGH_NORM:
    bmi_recommendation = 'Поститесь!'
else:
    bmi_recommendation = 'Так держать!'


# Вывод данных
print(f'\nПривет, {user_name}!')
print(f'Возраст: {user_age} {age_word}')
print(f'ИМТ: {user_bmi}')
print(f'Статус: {bmi_recommendation}')
print(f'Норма воды: {water_needed_liters} л')

print(
    f'Рекомендация ВОЗ: для поддержания водного баланса '
    f'вам необходимо выпивать {water_needed_liters} л воды в сутки.',
)
print('Расчет окончен. Будьте здоровы!')
