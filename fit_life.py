# Проект FitLife - MVP версия 1.0

WATER_NORM_PER_KG_ML = 30  # Норма воды: 30 мл на 1 кг веса
ML_IN_LITER = 1000         # Количество миллилитров в одном л.

# Пороговые значения нормы ИМТ по ВОЗ
BMI_LOW_NORM = 18.5
BMI_HIGH_NORM = 25.0

# Пороговые значения возраста для рекомендаций ВОЗ
AGE_MIN_NORM = 18
AGE_MAX_NORM = 60

# Пороговые значения для веса (в кг) и роста (в м.)
WEIGHT_MIN_NORM = 10.0
WEIGHT_MAX_NORM = 300.0

HEIGHT_MIN_NORM = 0.5
HEIGHT_MAX_NORM = 2.5


# ОСНОВНОЙ БЛОК СБОРА ДАННЫХ

# Ввод Имени
while True:
    user_name = input('Как вас зовут? ').strip()
    if user_name:
        break
    print(
        'Ошибка: имя не может быть пустым. '
        'Пожалуйста, повторите ввод еще раз.',
    )


ERROR_RANGE_MSG = (
    'Ошибка: введите число в разумных пределах '
    '(от {} до {}).'
)
ERROR_TYPE_MSG = 'Ошибка: пожалуйста, введите корректное число.'

# Ввод Возраста
while True:
    try:
        user_age = int(input('Сколько вам лет? '))
        if AGE_MIN_NORM <= user_age <= AGE_MAX_NORM:
            break
        print(ERROR_RANGE_MSG.format(AGE_MIN_NORM, AGE_MAX_NORM))
    except ValueError:
        print(ERROR_TYPE_MSG)

# Ввод Веса
while True:
    try:
        user_weight = float(input('Какой у вас вес in кг? '))
        if WEIGHT_MIN_NORM <= user_weight <= WEIGHT_MAX_NORM:
            break
        print(ERROR_RANGE_MSG.format(WEIGHT_MIN_NORM, WEIGHT_MAX_NORM))
    except ValueError:
        print(ERROR_TYPE_MSG)

# Ввод Роста
while True:
    try:
        user_height = float(
            input('Какой у вас рост в метрах (например, 1.75)? '),
        )
        if HEIGHT_MIN_NORM <= user_height <= HEIGHT_MAX_NORM:
            break
        print(ERROR_RANGE_MSG.format(HEIGHT_MIN_NORM, HEIGHT_MAX_NORM))
    except ValueError:
        print(ERROR_TYPE_MSG)


# РАСЧЕТЫ
# Расчет Индекса Массы Тела (ИМТ). Рост в м.
user_bmi = round(
    user_weight / (user_height ** 2),
    1
)

# Расчет суточной нормы воды в л.
water_needed_liters = round(
    (user_weight * WATER_NORM_PER_KG_ML) / ML_IN_LITER,
    2
)


# ОПРЕДЕЛЕНИЕ СКЛОНЕНИЯ СЛОВА "ЛЕТ"
last_digit = user_age % 10
last_two_digits = user_age % 100

age_word = 'лет'
if not (11 <= last_two_digits <= 14):
    if last_digit == 1:
        age_word = 'год'
    elif 2 <= last_digit <= 4:
        age_word = 'года'


# ИНТЕРПРЕТАЦИЯ ИМТ ПО СТАНДАРТАМ ВОЗ
bmi_recommendation = (
    'Ешьте!' if user_bmi < BMI_LOW_NORM else
    'Поститесь!' if user_bmi >= BMI_HIGH_NORM else
    'Так держать!'
)


# ВЫВОД РЕЗУЛЬТАТА
print(f'\nВозраст: {user_age} {age_word}')
print(f'ИМТ: {user_bmi}')
print(f'Статус: {bmi_recommendation}')
print(f'Норма воды: {water_needed_liters} л')

print(
    f'Рекомендация ВОЗ: для поддержания водного баланса '
    f'вам необходимо выпивать {water_needed_liters} л воды в сутки.',
)
print('Расчет окончен. Будьте здоровы!')
