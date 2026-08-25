# Проект FitLife - MVP версия 1.0

# Константы модуля
WATER_NORM_PER_KG_ML = 30  # Норма воды: 30 мл на 1 кг веса
ML_IN_LITER = 1000         # Количество миллилитров в одном литре

# Пороговые значения нормы ИМТ по ВОЗ
BMI_LOW_NORM = 18.5
BMI_HIGH_NORM = 25.0


# Функции для точного расчета данных
def get_clean_name() -> str:
    """Запрашивает имя и проверяет, чтобы оно не было пустым."""
    while True:
        name = input('Как тебя зовут? ').strip()
        if not name:
            print(
                'Ошибка: имя не может быть пустым. '
                'Пожалуйста, повторите ввод еще раз.',
            )
            continue
        return name


def get_float_input(prompt: str) -> float:
    """Запрашивает ввод и гарантирует, что возвращено число."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Ошибка: пожалуйста, введите корректное число.')


def get_valid_number(prompt: str, min_val: float, max_val: float) -> float:
    """Проверяет число на вхождение в заданный диапазон."""
    while True:
        value = get_float_input(prompt)
        if min_val <= value <= max_val:
            return value
        print(
            f'Ошибка: введите число в разумных пределах '
            f'(от {min_val} до {max_val}).',
        )


# Основной блок сбора данных
user_name = get_clean_name()

user_age = int(
    get_valid_number('Сколько тебе лет? ', 1.0, 120.0)
)

user_height = get_valid_number(
    'Какой у тебя рост в метрах (например, 1.75)? ',
    0.5,
    2.5,
)

user_weight = get_valid_number('Какой у тебя вес в кг? ', 10.0, 300.0)


# Расчеты
# Расчет Индекса Массы Тела (ИМТ). Рост изначально в метрах.
user_bmi = round(
    user_weight / (user_height ** 2),
    1
)

# Расчет суточной нормы воды в литрах
water_needed_liters = round(
    (user_weight * WATER_NORM_PER_KG_ML) / ML_IN_LITER,
    2
)


# Определние склонения слова 'лет'
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


# Вывод результата
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
