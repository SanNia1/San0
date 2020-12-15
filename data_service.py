"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""

"""модуль зчитує первинні файли для обробки
"""

def get_dovidnik():
    """повертає список клієнтів b з файла `dovidnik.txt`

    Returns:
        dovidnik_list: список клієнтів
    """

    with open("./data/dovidnik.txt") as dovidnik_file:
        from_file = dovidnik_file.readlines()

    dovidnik_list = []
    for line in from_file:
        line_list = line.split(';')
        dovidnik_list.append(line_list)

    return dovidnik_list


def get_orders():
    """повертає список накладних

    Returns:
        from_file: список накладних
    """
    
    with open('./data/orders.txt') as orders_file:
        from_file = orders_file.readlines()

    
    # розбити строку на реквізити та перетворити формати (при потребі)
    
    # список-накопичувач
    orders_list = []    
    
    for line in from_file:
        line_list = line.split(';')
        line_list[3] = int(line_list[3])
        line_list[4] = int(line_list[4])
        orders_list.append(line_list)

    return orders_list


def show_dovidnik(dovidnik):
    """виводить список клієнтів по заданому інтервалу кодів

    Args:
        dovidnik (list): список клієнтів
    """

    # задати інтервал виводу
    client_code_from = input("З якого кода клієнта? ")
    client_code_to   = input("По який кода клієнта? ")

    lines_found = 0

    for dovidnik in dovidnik:
        if client_code_from <= client[0] <= client_code_to:
            print ("код: {:5} назва підприємства: {:15}".format(*client))
            lines_found += 1

    if lines_found == 0:
        print("Клієнтів по Вашому запиту не знайдено") 


def show_orders(orders):
    """виводить список накладних на екран

    Args:
        orders (list): список накладних
    """

    for order in orders:
        print("назва: {:3} період: {:4} товарообіг: {:20} Баланс прибуток: {:35} середньорічна вартість основих засобів: {:45}"
            .format(order[0], order[1], order[2], order[3], order[4]))

# dovidnik = get_dovidnik()
# show_dovidnik(dovidnik)

# orders= get_orders()
# show_orders(orders)


