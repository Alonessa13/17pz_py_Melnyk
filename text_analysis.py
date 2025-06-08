# text_analysis.py
from collections import Counter

# Клас для аналізу тексту
class TextStats:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        # Повертає кількість слів у тексті
        words = self.text.split()
        return len(words)

    def most_common_letter(self):
        # Повертає найпоширенішу літеру (ігноруємо пробіли)
        letters = [char.lower() for char in self.text if char.isalpha()]
        counter = Counter(letters)
        most_common = counter.most_common(1)
        if most_common:
            return most_common[0][0]
        else:
            return None
