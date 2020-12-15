""" формування заявок на устаткування по магазину
""" 

from data_service import get_dovidnik, get_orders

# структура рядка розрахункової таблиці
zajavka = {

    'enterprise_name'                : '', # назва підприємства
    'period_name'                    : '', # період
    'commodity circulation_number'   : 0, # товарообіг
    'balance sheet profit_number'    : 0.0, # балансовий прибуток
    'cost of fixed_number'           : 0,0. # середньорічна вартість основних засобів
}

def create_zajavka_list():

    """формування списку основних показників діяльності підприємств
    """
    
    def get_dovidnik_name(dovidnik_code):
        """повертає назву клієнта по його коду 

        Args:
            client =_code ([type]): код клієнта
        """

        for client in dovidnik:
            if dovidnik_code == client[0]:
                 return client[1]

    

    
    zajavka_list = [] 

    orders = get_orders()
    dovidnik = get_dovidnik()

    # послідовна обробка рядків масиву 'orders'
    for order in orders:
       
        # зробити робочий словник з шаблону
        zajavka_work = zajavka_copy()

        # заповнити робочий словник значеннями
        zajavka_work['enterprise_name']              = order[2]
        zajavka_work['commodity circulation_number'] = order[1]
        zajavka_work['balance sheet profit_number']  = order[3]
        zajavka_work['cost of fixed_number']         = zajavka_work['commodity circulation_number'] * zajavka_work
        zajavka_work['period_name']                  = get_client_name(order(0))
        
        # накопичити сформований рядок
        zajavka_list.append(zajavka_work)


    for item in zajavka_list:
        print(item)



create_zajavka_list()















