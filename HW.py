t1 = 0
t2 = int(input("Введите количество необходимых билетов: "))
for i in range(1, t2+1):
    age = int(input("Введите возраст посетителей: "))
    if age < 18:
        t1 = t1 + 0
        print("Стоимость билета: ", 0)
    elif age >= 18 and age < 25:
        t1 = t1 + 990
        print("Стоимость билета: ", 990)
    elif age >= 25:
        t1 = t1 + 1390
        print("Стоимость билета: ", 1390)
allprice = sum([t1])
print("Цена за все билеты: ", allprice)
if t2 >= 3:
    allprice = sum([t1])*0.9
    print("Сумма к оплате с учетом скидки: ", (allprice))
