import io
from pprint import pprint


print()


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):

        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:

                    # Для каждого файла считывайте единые строки,
                    # переводя их в нижний регистр (метод lower()).
                    line = line.lower()

                    # Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - ']
                    # в строке.
                    punctuation = [',', '.', '=', '!', '?', ';', ':']
                    for punct in punctuation:
                        line = line.replace(punct, '')
                    line = line.replace(' - ', ' ')

                    # Разбейте эту строку на элементы списка методом split().
                    # (разбивается по умолчанию по пробелу)

                    # extend() добавляет новые элементы в конец списка, но, в отличие от append(),
                    # принимает в качестве параметров итерируемые объекты: списки, кортежи и строки.
                    # При этом объединяемые списки могут содержать элементы любых типов:
                    # например, вы можете объединить строки с числами или числа с кортежами.
                    words.extend(line.split())

                # В словарь all_words запишите полученные данные,
                # ключ - название файла, значение - список из слов этого файла.
                all_words[file_name] = words
        return all_words

    # В методах find и count пользуйтесь ранее написанным методом get_all_words
    # для получения названия файла и списка его слов.

    # find(self, word) - метод, где word - искомое слово.
    # Возвращает словарь, где ключ - название файла,
    # значение - позиция первого такого слова в списке слов этого файла.
    def find(self, word):
        places = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1

        return places

    # count(self, word) - метод, где word - искомое слово.
    # Возвращает словарь, где ключ - название файла,
    # значение - количество слова word в списке слов этого файла.
    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count

        return counters


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())  # Все слова
# print(finder2.find('TEXT'))  # 3 слово по счёту
# print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
