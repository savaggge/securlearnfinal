@echo off
:: Скрипт для запуска образовательной платформы "Security Learning" в режиме разработки в Windows

echo ========================================================
echo       Запуск Security Learning в режиме разработки
echo ========================================================

:: Проверяем наличие виртуального окружения
if not exist venv (
    echo Виртуальное окружение не найдено. Создание...
    python -m venv venv
    if errorlevel 1 (
        echo Ошибка при создании виртуального окружения.
        exit /b 1
    )
    echo Виртуальное окружение успешно создано.
)

:: Активируем виртуальное окружение
echo Активация виртуального окружения...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo Ошибка при активации виртуального окружения.
    exit /b 1
)

:: Экспорт переменных окружения
echo Настройка переменных окружения...
set FLASK_APP=main.py
set FLASK_ENV=development
set FLASK_DEBUG=1

:: Если SESSION_SECRET не установлен, генерируем случайный
if "%SESSION_SECRET%"=="" (
    for /f "tokens=*" %%a in ('python -c "import secrets; print(secrets.token_hex(16))"') do (
        set SESSION_SECRET=%%a
    )
    echo SESSION_SECRET не был установлен. Сгенерирован временный ключ.
)

:: Если DATABASE_URL не установлен, используем SQLite
if "%DATABASE_URL%"=="" (
    set DATABASE_URL=sqlite:///instance/cybersecurity.db
    echo DATABASE_URL не был установлен. Используется SQLite.
)

:: Проверяем наличие директории instance
if not exist instance (
    mkdir instance
    echo Создана директория instance для базы данных.
)

:: Запуск сервера разработки
echo ========================================================
echo Запуск сервера разработки...
echo Сервер будет доступен по адресу: http://localhost:5000
echo Для остановки нажмите Ctrl+C
echo ========================================================

python main.py

:: Деактивация виртуального окружения при выходе
call venv\Scripts\deactivate.bat
