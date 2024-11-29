import random
from datetime import datetime, timedelta
import heapq

# ОСНОВНАЯ ФУНКЦИЯ 
def query(events: list, assets: list) -> list:
    # Чтобы найти название актива по asset_id, стоит сделать asset_dict[asset_id]. \
    # Это быстрее, чем каждый раз перебирать весь список assets.
    asset_dict = {asset[0]: asset[1] for asset in assets}
    
    result = []
    for event in events:
        event_id, _, event_name, asset_id = event
        if asset_id is not None and asset_id in asset_dict:
            asset_name = asset_dict[asset_id]
            result.append([event_id, event_name, asset_id, asset_name])
        else:
            result.append([event_id, event_name, None, None])
    
    # Сортировка и ограничение
    return heapq.nsmallest(1000, result, key=lambda x: x[0])

# Пример использования из презентации
events = [
    [4, '2024-03-28', 'Event 4', 1],
    [1, '2024-03-26', 'Event 1', 1],
    [6, '2024-03-29', 'Event 6', 3],
    [3, '2024-03-28', 'Event 3', 2],
    [5, '2024-03-29', 'Event 5', None],
    [2, '2024-03-27', 'Event 2', None],
]

assets = [
    [4, 'Asset 4'],
    [1, 'Asset 1'],
    [3, 'Asset 3'],
    [2, 'Asset 2'],
]


# Запуск функции
result = query(events, assets)

# Печать первых 100 строк результата
for row in result[:1000]:
    print(row)
