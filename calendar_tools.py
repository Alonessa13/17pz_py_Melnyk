# calendar_tools.py
import datetime

# Клас, який працює з українським календарем
class UkrainianCalendar:
    def get_holiday_list(self):
        # Повертає список основних свят України
        holidays = [
            "2025-01-01",  # Новий рік
            "2025-01-07",  # Різдво
            "2025-03-08",  # Міжнародний жіночий день
            "2025-04-20",  # Великдень (припустимо)
            "2025-05-01",  # День праці
            "2025-05-09",  # День перемоги
            "2025-06-28",  # День Конституції
            "2025-08-24",  # День Незалежності
        ]
        return holidays

    def is_working_day(self, date):
        # Перевіряє, чи дата є робочим днем
        holidays = self.get_holiday_list()
        weekday = date.weekday()  # 0 = Понеділок, 6 = Неділя

        # Якщо вихідний або свято — повертаємо False
        if weekday >= 5 or date.strftime("%Y-%m-%d") in holidays:
            return False
        else:
            return True
