# Вспоминаем работу с файлом. Есть файл, '\n'
# в котором много англоязычных текстовых строк.'\n'
# Считаем частоту встретившихся слов в файле, '\n'
# но через функции и map, без единого цикла!
import re
import string

frequency = {}
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])