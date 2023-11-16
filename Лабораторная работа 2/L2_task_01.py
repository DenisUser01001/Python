money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

budget = money_capital + salary - spend
mounths_of_prosperity = 0

while budget >= 0:
    mounths_of_prosperity += 1
    spend *= 1 + increase   # Расчёт методом умножения на коэффициент больше 1 (так как increase задан в виде "0,05")
    budget = budget + salary - spend

print("Количество месяцев, которое можно протянуть без долгов:", mounths_of_prosperity)
