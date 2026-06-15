# Задача 8: Банківський вклад
# Користувач кладе в банк X грошей під 10% річних (кожного року сума збільшується на 10% від поточної).
# Напиши програму, яка порахує, через скільки років сума вкладу подвоїться (стане не меншою ніж 2 * X).

summ_deposit = 1000
profit = 10 # %
print("Deposit: ", summ_deposit)
print("Profit per year: ", profit, '%')

def counter_duble_profit(s_dep:float, profit:float)->float:
    years = 0
    profit_in_year = s_dep
    while profit_in_year < s_dep * 2:
        profit_in_year += (profit_in_year * (profit/100))
        years += 1
    print("In", years, "years - sum Deposit will be duble!!!" )
    print("Sum of Deposit = ", round(profit_in_year, 2))


counter_duble_profit(summ_deposit, profit)