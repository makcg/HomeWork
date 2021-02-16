file_with_numbers = open("111.txt", 'r')  # открываем файл для чтения
write_file = open("112.txt", 'w')  # открываем файл для записи
count = 0

for line in file_with_numbers:
    count += 1
    if not line:
        break

    w = line.split()
    a = int(w[0])
    b = int(w[1])
    c = int(w[2])
    for i in list(range(1, c, +1)):
        if (i % a == 0) and not (i % b == 0):
            print("F", end=" ", file=write_file)
        elif (i % b == 0) and not (i % a == 0):
            print('B', end=" ", file=write_file)
        elif (i % a == 0) and (i % b == 0):
            print('FB', end=" ", file=write_file)
        else:
            print(i, end=" ", file=write_file)
    print("\n", end="", file=write_file)

file_with_numbers.close()
write_file.close()

# Написать fizzbuzz для 20 троек чисел, которые '\n'
# записаны в файл. Читаете из файла первую строку,'\n'
# берете из нее числа, считаете для них fizzbuzz, выводите.
