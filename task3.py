#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
#Достаточно вернуть один допустимый вариант. 

items = {'Мультитул': 550,
         'Плед': 500,
         'Газовая горелка + плита': 1000,
         'Еда': 2500,
         'Котелок': 1500,
         'Посуда': 800,
         'Палатка': 3000,
         'Спальный мешок': 2000,
         'Вода': 4000,
         }
bag = 10000
result = []
for elements in items:
    if bag > items[elements]:
        result.append(elements)
        bag = bag - int(items[elements])
    else: break
print(result)
