from datetime import datetime
import time
#https://spb.hh.ru/applicant/vacancy_response?vacancyId=67743303
#На языке Python реализовать алгоритм (функцию) определения четности целого числа,
# который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

def myIsEven (value):
    if(type(value) == int and value > 0):
        return value & 1 == 0
    else:
        Exception ("BadType")

def isEven(value):
    return value % 2 == 0

def speedTest(funktion):
    start_time = datetime.now()
    for x in range(10000000):
        funktion(x)

    return datetime.now() - start_time

try:
    print('myIsEven time is', speedTest(myIsEven))
except ValueError:
    "BadData"
try :
    print('isEven time is', speedTest(isEven))
except :
    print("BadData")


# Функция myIsEven менее эффективная по времени, однако, она защищена от неправильных данных