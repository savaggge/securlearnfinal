#!/bin/bash
# Скрипт для запуска образовательной платформы "Security Learning" в режиме разработки

# ANSI цвета для красивого вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${MAGENTA}========================================================${NC}"
echo -e "${MAGENTA}      Запуск Security Learning в режиме разработки      ${NC}"
echo -e "${MAGENTA}========================================================${NC}"

# Проверяем наличие виртуального окружения
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Виртуальное окружение не найдено. Создание...${NC}"
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo -e "${RED}Ошибка при создании виртуального окружения.${NC}"
        exit 1
    fi
    echo -e "${GREEN}Виртуальное окружение успешно создано.${NC}"
fi

# Активируем виртуальное окружение
echo -e "${BLUE}Активация виртуального окружения...${NC}"
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo -e "${RED}Ошибка при активации виртуального окружения.${NC}"
    exit 1
fi

# Экспорт переменных окружения
echo -e "${BLUE}Настройка переменных окружения...${NC}"
export FLASK_APP=main.py
export FLASK_ENV=development
export FLASK_DEBUG=1

# Если SECRET_KEY не установлен, генерируем случайный
if [ -z "$SESSION_SECRET" ]; then
    export SESSION_SECRET=$(python -c 'import secrets; print(secrets.token_hex(16))')
    echo -e "${YELLOW}SESSION_SECRET не был установлен. Сгенерирован временный ключ.${NC}"
fi

# Если DATABASE_URL не установлен, используем SQLite
if [ -z "$DATABASE_URL" ]; then
    export DATABASE_URL="sqlite:///instance/cybersecurity.db"
    echo -e "${YELLOW}DATABASE_URL не был установлен. Используется SQLite.${NC}"
fi

# Проверяем наличие директории instance
if [ ! -d "instance" ]; then
    mkdir -p instance
    echo -e "${BLUE}Создана директория instance для базы данных.${NC}"
fi

# Запуск сервера разработки
echo -e "${MAGENTA}========================================================${NC}"
echo -e "${GREEN}Запуск сервера разработки...${NC}"
echo -e "${CYAN}Сервер будет доступен по адресу: http://localhost:5000${NC}"
echo -e "${YELLOW}Для остановки нажмите Ctrl+C${NC}"
echo -e "${MAGENTA}========================================================${NC}"

python main.py

# Деактивация виртуального окружения при выходе
deactivate
