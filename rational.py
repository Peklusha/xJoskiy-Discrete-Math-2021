import natural as nat
import integer as integer


def INT_Q_B(Q):
    if nat.MOD_NN_N(integer.ABS_Z_N(Q[0]), Q[1]) == [0]:
        return True
    else:
        return False
    # Гурьянов Савелий Функция возвращает отрицание результата остатка от деления числителя, преобразованного к
    # натуральному числу, на натуральный знаменатель, если остаток равен нулю, то дробь преобразуется к натуральному
    # числу, иначе не преобразуется и вернётся 0


def RED_Q_Q(Q):
    # Гурьянов Савелий
    # Сокращение дроби
    result = [[0], [0]]
    nod = nat.GCF_NN_N(nat.ABS_Z_N(Q[0]), nat.ABS_Z_N(Q[1]))
    result[0] = integer.DIV_ZZ_Z(Q[0], nod)
    result[1] = integer.DIV_ZZ_Z(Q[1], nod)
    if integer.POZ_Z_D(result[0]) == '-' and integer.POZ_Z_D(result[1]) == '-':
        result[0] = result[0][1:]
        result[1] = result[1][1:]
    return result


def ADD_QQ_Q(list1, list2):
    # Пекло Елизавета
    # Сложение дробей
    numerator = integer.ADD_ZZ_Z(list1[0], list2[0])
    denominator = nat.LCM_NN_N(list1[1], list2[1])
    # Возвращаем новые числитель и знаменатель
    return TRANS_Q_Z(RED_Q_Q([numerator, denominator]))


def DIV_QQ_Q(rational1, rational2):
    # Деление дробей
    # Кривоконь Максим
    result = [[0], [0]]
    result[0] = integer.MUL_ZZ_Z(rational1[0], rational2[1])  # умножение числителя на знаменатель
    result[1] = integer.MUL_ZZ_Z(rational2[1], rational2[0])  # умножение знаменателя на числитель
    if POZ_Z_D(result[0]) == '' and POZ_Z_D(result[1]) == '-':
        result[0] = MUL_ZM_Z(result[0])
        result[1] = MUL_ZM_Z(result[1])
    res = RED_Q_Q(result)  # сокращение дроби
    return res


def MUL_QQ_Q(rational1, rational2):  # на вход функция получает 2 рациональных числа
    # Семёнов Михаил
    # Умножение дробей
    result = [[0], [0]]  # результат умножения
    result[0] = integer.MUL_ZZ_Z(rational1[0], rational2[0]) # умножение числителей
    result[1] = integer.MUL_ZZ_Z(rational1[1], rational2[1]) # умножение знаменателей
    rez = RED_Q_Q(result)  # сокращение дроби


def TRANS_Z_Q(x):
    # Артамонов Артур, гр.0306
    # Преобразование целого в дробное
    x.append('/')
    x.append(1)
    return x


def TRANS_Q_Z(x):
    # Артамонов Артур, гр.0306
    # Преобразование дробного в целое, если знам. = 1
    if x[1][0] == 1:
        return x[0]
    else:
        return x


def SUB_QQ_Q(list1, list2):
    # Дашкин Дамир
    # Вычитание дробей
    k1 = list1[0]
    k2 = list2[0]
    znam = nat.LCM_NN_N(k1, k2)
    add1 = nat.DIV_NN_N(znam, k1)
    add2 = nat.DIV_NN_N(znam, k2)
    chisl1 = integer.MUL_ZZ_Z(add1, list1[1])
    chisl2 = integer.MUL_ZZ_Z(add2, list2[1])
    result = integer.SUB_ZZ_Z(chisl1, chisl2)
    res = [0]*2
    res[0] = result
    res[1] = znam
    return res


def INT_Q_B(A):
    # Аносов Павел
    # Проверка на целое
    if nat.MOD_NN_N(A[0], A[1]) == [0]:
        return True
    else:
        return False






