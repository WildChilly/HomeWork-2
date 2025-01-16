from http.cookiejar import uppercase_escaped_char
from tkinter.font import names


def test_func(*params):
    print(params)
    print('Тип:', type(params))
    print('Аргумент', params)
test_func()
test_func(1,2,3,4)


def summator(txt, *values, types='sum'):
    s = 0
    for i in values:
        s += i
    return f'{txt} {s} {types}'
print(summator('Сумма чисел',2,3,4,5,5, types='Summator'))

def info(values_item, *typeser, name_author='Alexei Burdakov', **values):
    print('Тип:', type(values))
    print('Аргумент', values)
    for key, value in values.items():
        print(key,value)
    print(name_author)
info('Пример использования параметров всех типов',1,3332,3,4,name_author='burdakov', name='Alexei', course='Python')

def my_sum(n, *args, txt='Сумма чисел'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ':', s)

my_sum(1,1,4,5,2,3)
my_sum(3,3,45,6,6, txt='Сумма кубов')

# Самостоятельная работа
def single_root_words(root_word, *other_words): # на наличие начала с одного корня
    same_words = []
    root_word_lower = root_word.lower() # приводим к нижнему регистру проверочное root_word слово
    for word in other_words: # Делаем цикл для проверки наличия похожих слов
        word_lower = word.lower() # приводим к нижнему регистру каждое текущее слово
        # проверяем есть ли проверочное слово в корневом или наоборот согласно условию задачи
        if root_word_lower.startswith(word_lower) or word_lower.startswith(root_word_lower): # этот метод проверяет, начинаются ли слова с однокоренного
            same_words.append(word)
    return same_words

result = single_root_words('cheRRy', 'Cherr', 'Chiabata', 'Cherrep', 'Percherry')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result)
print(result2)

def single_root_words(root_word, *other_words):# на наличие корня в составе слова
    same_words = []
    root_word_lower = root_word.lower() # приводим к нижнему регистру проверочное root_word слово
    for word in other_words: # Делаем цикл для проверки наличия похожих слов
        word_lower = word.lower() # приводим к нижнему регистру каждое текущее слово
        # проверяем есть ли проверочное слово в корневом или наоборот согласно условию задачи
        if root_word_lower.count(word_lower) > 0 or word_lower.count(root_word_lower) > 0:
            same_words.append(word)
    return same_words
result = single_root_words('cheRRy', 'Cherr', 'Chiabata', 'Cherrep', 'Percherry')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result)
print(result2)
# данное задание не слишком раскрывает закрепление навыков по *args **kwargs, больше запутывает и наталкивает на поиск
# информации, а не самостоятельное решение, интуитивно не получится додуматься
