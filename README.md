# Selenium Pytest Demo

Автоматизированные тесты с использованием Selenium WebDriver и pytest.

---

## Требования

- Python 3.9+ (у тебя 3.9.6 — отлично)
- Google Chrome (совместимая версия с ChromeDriver)
- Интернет для скачивания зависимостей и драйвера ChromeDriver

---

## Быстрый старт

### 1. Клонируем репозиторий

```bash
git clone https://github.com/ibulygin/pytest-selenium-example.git
cd selenium-pytest-demo
```

### 2. Создаем и активируем виртуальное окружение

#### На macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### На Windows (PowerShell):

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Устанавливаем зависимости вручную

```bash
pip install selenium pytest webdriver-manager

```

### 4. Запускаем тесты

```bash
pytest -v tests/
```
