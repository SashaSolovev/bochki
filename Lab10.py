import random
import logging

logging.basicConfig(filename="log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(funcName)s: "
                                                                   "%(lineno)d - %(message)s")

log = logging.getLogger()


def Shuffle_List(my_list):  # Рандомизация порядка чисел в списке
    random.shuffle(my_list)
    return my_list


try:
    n = int(input("Введите число бочонков: "))  # Ввод кол-ва бочонков
    if n < 1:
        log.error("Введено число %s, которое меньше единицы" % n)
        quit("Ошибка! Число меньше единицы! Перезапустите программу!")
    log.info("Введено кол-во бочонков - %s" % n)
    Random_Numbers = list(range(1, n + 1))  # Создание списка от 1 до n
    Shuffle_List(Random_Numbers)  # рименение функции рандомизации на созданный список
    log.info("Создан список от 1 до %s, с рандомным расположением чисел - %s" % (n, Random_Numbers))
    for i in range(1, n + 1):  # Вывод значений через цикл
        print(Random_Numbers[i - 1])
        log.info("Вытянут бочонок с числом %s" % Random_Numbers[i - 1])
        input("Нажмите Enter, чтобы продолжить")
    print("Бочонки закончились!")
    log.info("Бочонки закончились!")
except ValueError:
    log.error("Ошибка неверного типа данных!")
    quit("Ошибка! Вы ввели не число! Перезапустите программу!")
