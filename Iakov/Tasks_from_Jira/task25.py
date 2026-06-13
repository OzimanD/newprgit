
def check_access(role):
    if role == "admin" and "moderator":
        return "Доступ дозволено"
    else:
        return "Відмовлено в доступі"
print(check_access("guest")) # Виводить: "Доступ дозволено" — Ой!
