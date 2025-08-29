# CrewAI Agents Demo

## Быстрый старт

1. Создайте и активируйте виртуальное окружение:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. Скопируйте `.env.example` в `.env` и вставьте ваш OpenAI API ключ:
```bash
cp .env.example .env
# Откройте .env и вставьте значение в OPENAI_API_KEY
```
4. Запустите пример:
```bash
python main.py
```

## Что делает пример
- Создаёт двух агентов (Исследователь и Писатель) на базе CrewAI
- Выполняет две последовательные задачи: сбор фактов и финальный отчёт
- Использует модель OpenAI (через `langchain-openai`) и переменную окружения `OPENAI_API_KEY`

## Переменные окружения
- `OPENAI_API_KEY` — ключ OpenAI. Храните его только локально, не коммитьте в git.
