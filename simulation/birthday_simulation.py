"""
Simulation plenty of generations of birthdays
"""

from generator.birthday_generator import BirthdayGenerator


class BirthdaySimulation:
    """Класс для симуляции парадокса дней рождения."""

    def __init__(self):
        self.generator = BirthdayGenerator()

    @staticmethod
    def get_match(birthdays):
        """Проверяем, есть ли совпадающие дни рождения."""
        if len(birthdays) == len(set(birthdays)):
            return None  # Все дни рождения различны.

        for a, birthday_a in enumerate(birthdays):
            for birthday_b in birthdays[a + 1:]:
                if birthday_a == birthday_b:
                    return birthday_a  # Найдены совпадающие дни рождения.
        return None

    def run_simulation(self):
        """Основная функция для запуска симуляции."""
        print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
        The Birthday Paradox shows us that in a group of N people, the odds
        that two of them have matching birthdays is surprisingly large.
        This program does a Monte Carlo simulation (that is, repeated random
        simulations) to explore this concept.
        (It's not actually a paradox, it's just a surprising result.)
        ''')

        months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

        while True:
            print('How many birthdays shall I generate? (Max 100)')
            response = input('> ')
            if response.isdecimal() and (0 < int(response) <= 100):
                num_birthdays = int(response)
                break
        print()

        # Генерация и вывод дней рождения
        print('Here are', num_birthdays, 'birthdays:')
        birthdays = self.generator.get_birthdays(num_birthdays)
        for i, birthday in enumerate(birthdays):
            if i != 0:
                print(', ', end='')
            month_name = months[birthday.month - 1]
            date_text = f'{month_name} {birthday.day}'
            print(date_text, end='')
        print()
        print()

        # Проверка совпадений
        match = self.get_match(birthdays)
        print('In this simulation, ', end='')
        if match is not None:
            month_name = months[match.month - 1]
            date_text = f'{month_name} {match.day}'
            print('multiple people have a birthday on', date_text)
        else:
            print('there are no matching birthdays.')
        print()

        # Симуляция 100,000 раз
        print('Generating', num_birthdays, 'random birthdays 100,000 times...')
        input('Press Enter to begin...')
        sim_match = 0
        for i in range(100_000):
            if i % 10_000 == 0:
                print(i, 'simulations run...')
            birthdays = self.generator.get_birthdays(num_birthdays)
            if self.get_match(birthdays) is not None:
                sim_match += 1

        print('100,000 simulations run.')
        probability = round(sim_match / 100_000 * 100, 2)
        print(f'Out of 100.000 simulations of {num_birthdays} people, there was a')
        print(f'matching birthday in that group {sim_match} times. This means')
        print(f'that {num_birthdays} people have a {probability}% chance of')
        print('having a matching birthday in their group.')
        print('That\'s probably more than you would think!')
