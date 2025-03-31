from app import app
from models import User
from datetime import datetime

# Вывод пользователей в консоль
with app.app_context():
    users = User.query.all()
    print("\n=== Зарегистрированные пользователи ===")
    print("ID | Имя пользователя | Email | Дата регистрации | Последний вход")
    print("-" * 80)
    
    if not users:
        print("Нет зарегистрированных пользователей.")
    else:
        for user in users:
            reg_date = user.registration_date.strftime("%Y-%m-%d %H:%M") if user.registration_date else "N/A"
            last_login = user.last_login.strftime("%Y-%m-%d %H:%M") if user.last_login else "N/A"
            print(f"{user.id} | {user.username} | {user.email} | {reg_date} | {last_login}")
    
    print("-" * 80)
    print(f"Всего пользователей: {len(users)}")