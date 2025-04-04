#!/usr/bin/env python3
"""
Скрипт для запуска образовательной платформы "Security Learning" в режиме разработки.
Этот скрипт настраивает необходимые переменные окружения и запускает приложение
с активированным режимом отладки.
"""

import os
import platform
import subprocess
import sys
from pathlib import Path

# Определение цветов для вывода в терминал
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_colored(text, color):
    """Выводит текст заданным цветом."""
    print(f"{color}{text}{Colors.ENDC}")

def check_requirements():
    """Проверяет наличие всех необходимых зависимостей."""
    try:
        import flask
        import flask_login
        import flask_sqlalchemy
        import flask_wtf
        import werkzeug
        return True
    except ImportError as e:
        print_colored(f"Ошибка: Отсутствует пакет {e.name}.", Colors.FAIL)
        print_colored("Установите зависимости с помощью команды:", Colors.WARNING)
        print_colored("pip install -r requirements.txt", Colors.CYAN)
        print_colored("или", Colors.WARNING)
        print_colored("pip install flask flask-login flask-sqlalchemy flask-wtf email-validator gunicorn psycopg2-binary werkzeug", Colors.CYAN)
        return False

def check_database():
    """Проверяет наличие базы данных и создаёт её при необходимости."""
    instance_dir = Path("instance")
    if not instance_dir.exists():
        print_colored("Создание директории для базы данных...", Colors.BLUE)
        instance_dir.mkdir(exist_ok=True)
    
    db_path = instance_dir / "cybersecurity.db"
    if not db_path.exists():
        print_colored("База данных не найдена. Инициализация...", Colors.BLUE)
        try:
            from app import app, db
            with app.app_context():
                db.create_all()
            print_colored("База данных успешно инициализирована.", Colors.GREEN)
        except Exception as e:
            print_colored(f"Ошибка при инициализации базы данных: {e}", Colors.FAIL)
            return False
    return True

def set_environment():
    """Настраивает переменные окружения для режима разработки."""
    os.environ['FLASK_APP'] = 'main.py'
    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_DEBUG'] = '1'
    
    # Установка секретного ключа, если он не задан
    if 'SESSION_SECRET' not in os.environ:
        import secrets
        os.environ['SESSION_SECRET'] = secrets.token_hex(16)
    
    # Установка URL базы данных для SQLite, если не указан другой
    if 'DATABASE_URL' not in os.environ:
        db_path = Path("instance/cybersecurity.db").absolute()
        os.environ['DATABASE_URL'] = f"sqlite:///{db_path}"

def run_development_server():
    """Запускает сервер разработки Flask."""
    try:
        from main import app
        
        host = '0.0.0.0'  # Доступно с любых IP
        port = 5000
        
        print_colored("=" * 50, Colors.HEADER)
        print_colored(" Security Learning - Сервер разработки ", Colors.BOLD + Colors.HEADER)
        print_colored("=" * 50, Colors.HEADER)
        print_colored(f"Сервер запущен по адресу: http://{host}:{port}", Colors.GREEN)
        print_colored("Для доступа с локального компьютера используйте: http://localhost:5000", Colors.GREEN)
        print_colored("Для остановки сервера нажмите Ctrl+C", Colors.WARNING)
        print_colored("=" * 50, Colors.HEADER)
        
        app.run(host=host, port=port, debug=True)
    except Exception as e:
        print_colored(f"Ошибка при запуске сервера: {e}", Colors.FAIL)
        return False
    return True

def main():
    """Основная функция для запуска сервера разработки."""
    print_colored("Подготовка к запуску сервера разработки Security Learning...", Colors.HEADER)
    
    # Проверка наличия зависимостей
    if not check_requirements():
        return 1
    
    # Настройка переменных окружения
    set_environment()
    
    # Проверка базы данных
    if not check_database():
        return 1
    
    # Запуск сервера разработки
    if not run_development_server():
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())