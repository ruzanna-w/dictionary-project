from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse('Hello')

# # utilities
# def is_cyrillic(rus):
#     return bool(re.match(r'^[а-яёА-ЯЁ]+$', rus))

# def is_latin(eng):
#     return bool(re.match(r'^[a-zA-Z]+$', eng))

# def is_word_correct(word):
#     if word.isalpha() and word != "":
#         return True
#     return False

# def add_word():
#     eng = input('введите слово на английском или "exit", чтобы выйти: ').lower()
#     if eng == "exit":
#         return 
#     result = is_word_correct(eng)
#     if result and is_latin(eng):
#         rus = input('введите перевод слова: ').lower()
#         if is_word_correct(rus) and is_cyrillic(rus):
#             if db.check_exist_word(eng, rus):
#                 print('слово уже есть в базе данных')
#             db.add_word(eng,rus)
#             print('слово добавлено')
#         else: print('"Напишите перевод кириллицей"')
#     else: print('"Напишите слово корректно"')

# def delete_word():
#     eng = input('введите слово на английском или "exit", чтобы выйти: ').lower()
#     if eng == "exit":
#         return
#     if is_word_correct(eng):
#         word = db.check_word_to_delete(eng)
#         if word is None:
#             print("такого слова нет в базе данных")
#         else:
#             count_words = len(word)
#             if count_words > 1:
#                 choose_word = input(f"У вас {count_words} слов(а). Какое вы хотите удалить? Введите перевод слова: ")
#                 for row in word:
#                     if row[2] == choose_word:
#                         word_index = row[0]
#                         db.delete_word(word_index)
#             else:
#                 word_index = word[0][0]
#                 db.delete_word(word_index)
#                 print('слово удалено')


# def show_words_list():
#     result = db.show_words_list()
#     if not result :
#         print("ваш словарь пуст")
#     else: print(result)

# def test_knowledge():
#     while True:
#         word = db.random_word()
#         if word is None:
#             return
#         else: 
#             print(f'переведите слово: {word[1]}')
#         translate_word = input('Введите перевод или слово "exit" если хотите выйти: ').lower()
#         if translate_word == 'exit':
#             break
#         elif translate_word == word[2]:
#             db.is_correct_answer(word[0])
#             print('Верно!')
#         else:
#             db.is_wrong_answers(word[0])
#             print('неверно')

# # Отсортировать слова
# def word_order():
#     alphabet_order = db.word_order()
#     if not alphabet_order:
#         print("ваш словарь пуст")
#     else:
#         print(alphabet_order)

# # И поиск слова по частям
# def search_part_word():
#     eng = input('введите слово на английском или "exit", чтобы выйти: ').lower()
#     if eng == "exit":
#         return
#     else:
#         show_words = db.search_by_part(eng)
#         if not show_words:
#             print("ваш словарь пуст")
#         else:
#             print(show_words)

# def close():
#     db.close()


