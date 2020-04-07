INCH = 25400

while True:
    print('Калькулятор вычисления размеров точек по значению DPI')
    print()
    choose = int(input("""1. Ввести увеличение
2. Вычислить увеличение
3. Закончить работу

Выберите пункт: """))
    if choose == 1:
        magnif = int(input('Введите увеличение: '))
    elif choose == 2:
        oculus = int(input('Введите увеличение окуляра: '))
        glass = int(input('Введите увеличение объектива: '))
        magnif = oculus*glass
    elif choose == 3:
        break
    scale = round(1/magnif*1000, 2)
    dpi = int(input('Введите разрешение изображения в dpi: '))
    overall = round(INCH/dpi, 2)
    size = round(overall/scale, 2)
    print()
    print(""'Увеличение составляет: {}x'.format(magnif),
'\nЦена деления в окуляре: {}мкм'.format(scale),
'\nРеальный размер одной точки: {}мкм'.format(overall),
'\nСоотношение размера одной точки и одного деления: {} делений(-ия)'.format(size),
'\n{:_^40}'.format('_'))