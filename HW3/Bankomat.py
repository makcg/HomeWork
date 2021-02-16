def GiveOutMoney(V):

    money = [1, 2, 5, 10, 20, 50,  # Все номиналы валюты
             100, 500, 1000]
    n = len(money)
    ans = []  # Результат инициализации
    i = n - 1
    while i >= 0:  # Проход всех номиналов

        while V >= money[i]:  # Нахождение номиналов
            V -= money[i]
            ans.append(money[i])
        i -= 1
    for i in range(len(ans)):
        print(ans[i], )

if __name__ == '__main__':
    n = int(input('Your money '))
    print(n, ": ", )
    GiveOutMoney(n)