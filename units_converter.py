volml = float(input('Введите объем напитка в миллилитрах: '))

drink = str(input('Выберите напиток: 1 - пиво, 2 - вино '))
country = str(input('Выберите страну: 1- США, 2 - Великобритания '))

vol = volml/1000

if drink == '1' and country == '1':
    usa_bar = vol / 117.3
    usa_pint = vol / 0.47
    print(volml, ' мл пива в США равняется:\n', round(usa_bar, 3), ' пивного барреля\n', round(usa_pint,3), ' американской жидкой пинты')
elif drink == '2' and country == '1':
    usa_winebar = vol / 3.78
    usa_quart = vol / 0.9081
    print(volml, ' мл вина в США равняется:\n', round(usa_winebar,3), ' малого барреля\n', round(usa_quart,3), ' квартам')
elif drink == '1' and country == '2':
    uk_pint = vol / 0.568
    uk_quartpint = vol / 0.142
    print(volml, ' мл пива в Британии равняется:\n', round(uk_pint,3), ' пинты\n', round(uk_quartpint,3), ' четвертьпинты')
elif drink == '2' and country == '2':
    uk_gallon = vol / 4.546
    print(volml, ' мл вина в Британии равняется:\n', round(uk_gallon,3), ' галлона\n')
else:
    print('Ошибочное значение')
