def count_premium(exp, salary):
    if 2 <= exp <= 5:
        return (salary * 0.02) + salary
    elif   5 < exp <= 10:
        return (salary * 0.05) + salary


print(count_premium(exp, salary))