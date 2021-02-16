
a = int(input('Enter the fizz: '))
b = int(input('Enter the buzz: '))
i = int(input('Enter any number: '))
for i in list(range(1, i +1)):
    if(i % a == 0) and not(i % b == 0):
        print("F", end = " ")
    elif(i % b == 0) and not (i % a == 0):
        print('B', end = " ")
    elif(i % a == 0) and (i % b == 0):
        print('FB', end = " ")
    else:
        print (i, end = " ")

#Пример условия и результата:
#Введены числа 2, 5, 18
#Вывод должен быть таким:
#1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F