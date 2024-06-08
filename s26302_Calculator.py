import math
from collections import deque
from pynput import keyboard
import re
import sys


class Calculator:
    def __init__(self):
        self.history = History()
        self.current_result = 0
        self.invalid_characters = set("|,`~@#%^&")

    def calculate(self, expression):
        try:
            #przygotowanie wyrażenia z inputu uzytkownika
            if any(char in self.invalid_characters for char in expression):
                raise ValueError(f"Nieznany znak w wyrażeniu: {expression}")


            if 'x' in expression:
                expression = expression.replace('x', str(self.current_result))

            expression = self.factorial_finder(expression)
            expression = expression.replace('\\', '/').replace(':', '/')


            result = ExpressionCalculator.evaluate(expression)
            self.history.add(expression, result)
            self.current_result = result
            print(f"Wynik: {result}")
        except Exception as e:
            print(f"Błąd: {e}")

    def factorial_finder(self, expression):

        potential_factorials = re.findall(r'(\d+)!', expression)
        for match in potential_factorials:
            number = int(match)
            factorial_result = math.factorial(number)
            expression = expression.replace(f"{number}!", str(factorial_result))
        return expression

    def show_history(self):
        print("Historia ostatnich 5 operacji:")
        for i, entry in enumerate(self.history.get_last(5), 1):
            print(f"{i}: {entry}")

    def select_from_history(self, index):
        try:
            selected_entry = self.history.get_last(5)[index]


            expression, result = selected_entry.split(' = ')
            result = result.strip()
            print(f"Wybrane wyrażenie: {expression}, wynik: {result}")
            self.current_result = float(result)
            print(f"Nowy x = {self.current_result}")
        except IndexError:
            print("Nieprawidłowy wybór historii")
        except ValueError:
            print("Błąd pobierania wyniku z historii")


class History:
    def __init__(self):
        self.history = []

    def add(self, expression, result):
        self.history.append(f"{expression} = {result}")
        if len(self.history) > 5:
            self.history.pop(0)

    def get_last(self, n):
        return self.history[-n:]


class ExpressionCalculator:
    @staticmethod
    def evaluate(expression):


        if not expression.strip():
            return 0


        try:
            result = eval(expression, {"__builtins__": None}, {
                "pi": math.pi,
                "e": math.e,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "ctg": lambda x: 1 / math.tan(x),
                "sqrt": math.sqrt,
                "factorial": math.factorial

            })

            return result
        except Exception as e:
            raise ValueError(f"Niepoprawne wyrażenie: {e}")


class HandlerInput:
    def __init__(self, calculator):
        self.calculator = calculator
        self.history_index = -1
        self.current_line_length = 0

    def keyboard_action(self, key):
        try:
            if key == keyboard.Key.up:
                self.history_index -= 1
                if self.history_index < -len(self.calculator.history.history):
                    self.history_index = -len(self.calculator.history.history)
                self.show_selected_history()
            elif key == keyboard.Key.down:
                self.history_index += 1
                if self.history_index > -1:
                    self.history_index = -1
                self.show_selected_history()
            elif key == keyboard.Key.enter:
                if self.history_index != -1:
                    self.calculator.select_from_history(self.history_index + len(self.calculator.history.history))
                    self.history_index = -1
                    self.clear_line()
        except AttributeError:
            pass

    def clear_line(self):
        sys.stdout.write('\r' + ' ' * self.current_line_length + '\r')
        sys.stdout.flush()

    def show_selected_history(self):
        if self.history_index == -1:
            display_text = "Aktualna operacja"
        else:
            selected_index = self.history_index + len(self.calculator.history.history)
            display_text = f"Wybrana historia: {self.calculator.history.history[selected_index]}"


        self.clear_line()


        sys.stdout.write(display_text)
        sys.stdout.flush()


        self.current_line_length = len(display_text)

    def run(self):
        print("Aby wyświetlić historię ostatnich operacji, użyj strzałek w góra dół.")
        with keyboard.Listener(on_press=self.keyboard_action) as listener:
            while True:
                user_input = input("\nWprowadź wyrażenie lub 'historia': ").strip().lower()
                if user_input == "historia":
                    self.calculator.show_history()
                else:
                    if user_input:
                        self.calculator.calculate(user_input)
                        self.history_index = -1


if __name__ == "__main__":
    calc = Calculator()
    handler = HandlerInput(calc)
    handler.run()
