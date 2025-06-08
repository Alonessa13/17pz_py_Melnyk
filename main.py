# main.py

# Імпортуємо всі потрібні модулі
from calendar_tools import UkrainianCalendar
from math_utils import Calculator
from text_analysis import TextStats
import datetime

# ===============================
# Демонстрація UkrainianCalendar
# ===============================
print("== МОДУЛЬ КАЛЕНДАРЯ ==")
calendar = UkrainianCalendar()

# Виводимо список свят
print("Свята України:")
for holiday in calendar.get_holiday_list():
    print("-", holiday)

# Перевіримо дату
date_str = input("Введіть дату у форматі YYYY-MM-DD: ")
date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

if calendar.is_working_day(date):
    print(f"{date} — це робочий день")
else:
    print(f"{date} — це вихідний або свято")

# ===============================
# Демонстрація Calculator
# ===============================
print("\n== МОДУЛЬ КАЛЬКУЛЯТОРА ==")
calc = Calculator()

print("Оберіть операцію:")
print("1 — Додавання")
print("2 — Віднімання")
print("3 — Множення")
print("4 — Ділення")

choice = input("Ваш вибір: ")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

if choice == "1":
    print("Результат:", calc.add(a, b))
elif choice == "2":
    print("Результат:", calc.subtract(a, b))
elif choice == "3":
    print("Результат:", calc.multiply(a, b))
elif choice == "4":
    print("Результат:", calc.divide(a, b))
else:
    print("Невірний вибір!")

# ===============================
# Демонстрація TextStats
# ===============================
print("\n== МОДУЛЬ АНАЛІЗУ ТЕКСТУ ==")
user_text = input("Введіть будь-який текст: ")
stats = TextStats(user_text)

print("Кількість слів у тексті:", stats.count_words())
print("Найпоширеніша літера:", stats.most_common_letter())
