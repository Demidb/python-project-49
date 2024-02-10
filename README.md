### Hexlet Tests and Linter Status
[![Actions Status](https://github.com/Demidb/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Demidb/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/522cd74e06f4ba19bd53/maintainability)](https://codeclimate.com/github/Demidb/python-project-49/maintainability)

### Brain Games
Этот проект предназначен для оттачивания навыков, полученных разработчиком во время прохождения модулей перед первым проектом. Он закрепляет знания в pip, poetry, а также навыки создания виртуального окружения. 

### Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Тестирование](#тестирование)
- [Команда проекта/Автор](#команда-проекта)

### Технологии
- [Python 3.10](https://www.python.org/)
- [Prompt](https://pypi.org/project/prompt/)
- [Flake8](https://flake8.pycqa.org/en/latest/)

### Разработка и Использование
Для начала необходимо установить poetry и создать виртуальное окружение.

#### Установка poetry:
```bash
pip install poetry
```

#### Создание виртуальной среды:
```bash
python3 -m venv .venv
```

#### Активация виртуальной среды:
```bash
source .venv/bin/activate
```

#### Установка пакета:
```bash
python3 -m pip install --user git+https://github.com/<user_name>/<repo_name>.git
```

#### Установка зависимостей:
```bash
pip3 install prompt flake8
```

#### Проверка зависимостей:
```bash
pip3 list
```

### Запуск
Чтобы запустить утилиту в режиме разработки, выполните команду:
```bash
make brain-games
```

Чтобы запустить игру brain_calc, выполните команду:
```bash
brain-calc
```

Чтобы запустить игру brain_even, выполните команду:
```bash
brain-even
```

Чтобы запустить игру brain_gcd, выполните команду:
```bash
brain-gcd
```

Чтобы запустить игру brain_prime, выполните команду:
```bash
brain-prime
```

Чтобы запустить игру brain_progression, выполните команду:
```bash
brain-progression
```

### Создание билда
Чтобы выполнить сборку, выполните команду: 
```bash
make build
```

### Добавление зависимостей
Можно использовать команду:
```bash
poetry add prompt
```
Это сразу добавит данную зависимость в файл `pyproject.toml`.

### Установка
Чтобы выполнить установку пакета, выполните команду: 
```bash
make package-install
```

### FAQ
- Как проверить, работают ли игры? Выполните `poetry run <название игры из папки games>`
- Можно ли в игре brain-calc ввести два оператора, например, * и +? Нет, введите только один оператор.
- Как понять, является ли число простым? Простое число делится только на себя и на единицу.

### To Do
1. Добавить крутое README  
2. Всё переписать  
3. ...  
4. Проработать логику игр и сократить код  
5. Создать файл-скрипт для запуска игр поочередно

### Команда проекта
Автор:

- [Демид Алексеев](vk.com/demidkab) — Python developer


### Источники


| Название источника | Значение/пояснение |
|--------------------|--------------------|
| 1  Марк Лутц       | В его книге  "Изучаем Python "  были продемонстрированы интересные функции, которые мотировали встать с дивана и идти тестировать их|
|2 Видео школьников 10-летней давности | Видео оказали на меня внушительное влияния, показав, как нужно пользоваться VSC и настраивать PATH в Windows, а также помогли с установкой Ubuntu|
|3 Мой брат | Объяснение логики работы некоторых функций, а также разжевывание требований проекта с 3 по 7 шаги| 


### Тестирование

brain-even: [![asciicast](https://asciinema.org/a/PjELBsWhQEPUUTV07nSEnEgQk.svg)](https://asciinema.org/a/PjELBsWhQEPUUTV07nSEnEgQk)

brain-calc: [![asciicast](https://asciinema.org/a/nTcG92bkzQcR64Cn07oCN68dE.svg)](https://asciinema.org/a/nTcG92bkzQcR64Cn07oCN68dE)

brain-gcd : [![asciicast](https://asciinema.org/a/uZKjLWawlnemQAryBoj1A5tbS.svg)](https://asciinema.org/a/uZKjLWawlnemQAryBoj1A5tbS)

brain-progression : [![asciicast](https://asciinema.org/a/yJqAKB9m7DJ2cQB0oZSgGgz4k.svg)](https://asciinema.org/a/yJqAKB9m7DJ2cQB0oZSgGgz4k)

brain-prime : [![asciicast](https://asciinema.org/a/yJqAKB9m7DJ2cQB0oZSgGgz4k.svg)](https://asciinema.org/a/yJqAKB9m7DJ2cQB0oZSgGgz4k)
