salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
emergency_fund = 0
dnt_apply_first_mounth_incr_rate = 0  # Переменная вводится для условия неначисления процентов в первый месяц.

for i in range(1, months+1):
    spend *= 1 + increase * dnt_apply_first_mounth_incr_rate  # Начисление процентов, в первом месяце без %.
    dnt_apply_first_mounth_incr_rate = 1
    # print(f"Траты в {i} месяц составляют: {spend}")

    needed_additional_money_in_current_mounth = spend - salary
    # print(f'В {i} месяц, чтобы не уйти в долги нужно иметь запас {needed_additional_money_in_current_mounth}')

    emergency_fund += needed_additional_money_in_current_mounth

emergency_fund = round(emergency_fund, 2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", emergency_fund)
