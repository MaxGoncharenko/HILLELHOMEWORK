#Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.

dict = { "cito": 47.999,
         "BB_studio":42.999,
         "momo": 49.999,
         "main-service": 37.245,
         "buy.now": 38.324,
         "x-store": 37.166,
         "the_partner": 38.988,
         "store": 37.720,
         "rozetka": 38.003,
         }

lower_limit = 35.9
upper_limit = 37.339

for key,values in dict.items():
    if lower_limit < values and upper_limit > values:
        print(f'{key},the price is {values}')

