"""
Generate day of the birth
"""
import datetime
import random


class BirthdayGenerator:
    """Класс для генерации дней рождения."""

    @staticmethod
    def get_birthdays(number_of_birthdays):
        """Возвращаем список объектов дат для случайных дней рождения."""
        birthdays = []
        for _ in range(number_of_birthdays):
            start_of_year = datetime.date(2001, 1, 1)
            random_number_of_days = datetime.timedelta(random.randint(0, 364))
            birthday = start_of_year + random_number_of_days
            birthdays.append(birthday)
        return birthdays

    @staticmethod
    def format_birthdays(birthdays):
        """Возвращает список дней рождения в формате строк."""
        return [birthday.strftime("%d %B %Y") for birthday in birthdays]
