import random
from datetime import datetime, timedelta
import heapq

# Функция для генерации данных
def generate_large_datasets(num_events: int, num_assets: int):
    assets = [[i, f"Asset {i}"] for i in range(1, num_assets + 1)]
    
    events = []
    start_date = datetime(2024, 1, 1)
    for i in range(1, num_events + 1):
        date = start_date + timedelta(days=random.randint(0, 365)) 
        asset_id = random.choice([random.randint(1, num_assets), None])  
        events.append([i, date.strftime('%Y-%m-%d'), f"Event {i}", asset_id])
    
    return events, assets

# ОСНОВНАЯ ФУНКЦИЯ 
def query(events: list, assets: list) -> list:
    # Чтобы найти название актива по asset_id, стоит сделать asset_dict[asset_id].
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

# Генерация данных 
num_events = 1_000_000  
num_assets = 10_000 
events, assets = generate_large_datasets(num_events, num_assets)

# Запуск функции
result = query(events, assets)

# Печать первых 100 строк результата
for row in result[:1000]:
    print(row)
