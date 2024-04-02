vehicles = {
    'ford': 'Fiesta',
    'volkswagen': 'Passat',
    'suzuki': 'Swift',
    'kia': 'Seltos',
    'hyundai': 'Verna',
    'toyota': 'Fortuner'
}

# suv = vehicles['toyota']
# print(suv)
#
# hatchback = vehicles.get('suzuki')
# print(hatchback)
#
# print(vehicles.get('volkswagen'))
result = vehicles.pop('kia')
print(result)
print()
vehicles['tata'] = 'Safari'
vehicles['suzuki'] = 'Alto'
for keys, value in vehicles.items():
    print(keys, value, sep=", ")

