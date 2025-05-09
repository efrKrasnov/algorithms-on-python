from math import ceil
from typing import Any


def max_tournament_algo(in_list: list) -> None | Any:
    # Для кейсов, при которых ничего не надо высчитывать
    if not in_list:
        return None
    
    # Создаем массив определенной длинны
    comparsion_count: int = ceil(len(in_list) / 2)
    winners: list[None]  = [None for i in range(comparsion_count)]
    
    # На каждом цикле алгоритма у нас длина списка для проверкаи будет уменьшаться
    # В связи с чем мы каждый раз будем пересчитывать длину списка для проверки
    in_list_len = len(in_list)
    
    while in_list_len != 1:
        w_pos = 0       # индексатор для winners
        c_pos = 0       # индексатор для in_list
        cmps = in_list_len // 2     # высчитываем количество сравнений
        
        while cmps:
            # Ищем максимальный элемент в паре сравнений
            if in_list[c_pos] > in_list[c_pos + 1]:
                winners[w_pos] = in_list[c_pos]
            else:
                winners[w_pos] = in_list[c_pos + 1]
            
            # Меняем индексы
            w_pos += 1
            c_pos += 2
            
            # Уменьшаем количество сравнений
            cmps -= 1
            
        # Пограничный случай - это когда у нас в последнем раунде сравнений только 1 элемент
        # В этом случае выбираем сам элемент и модифицируем индексатор для winners
        if c_pos != in_list_len:
            winners[w_pos] = in_list[c_pos]
            w_pos += 1
            
        # Подготавливаем переменные к следующему циклу
        in_list_len = w_pos
        in_list = winners
        
    return in_list[0]

