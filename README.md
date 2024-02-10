### Hexlet tests and linter status:
[![Actions Status](https://github.com/Demidb/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Demidb/python-project-49/actions)
<a href="https://codeclimate.com/github/Demidb/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/522cd74e06f4ba19bd53/maintainability" /></a> 

### Brain games
Проект направлен на оттачивание навыков, полученных разработчиком во время прохождения модулей перед 1-м проектом. Проект закрепляет знания в pip, poetry, а также навыков создания виртуального окружения. 

### Содержание
- [Технологии](#технологии)
- [Начало работы](10-10-2023)
- [Тестирование](05-01-2023)
- [Команда проекта/Автор](Demid Alexeev)

### Технологии
- [Python 3.10](https://www.python.org/)
- [Prompt](https://pypi.org/project/prompt/)
- [flake8] (https://flake8.pycqa.org/en/latest/)

### Разработка и Использование
Для начала необходимо установить poetry и создать вирутальную среду
Установка poetry:
pip install

Создание вирт. среды:

python3 -m venv .venv

Активация вирт. среды:

source .venv/bin/activate

Установите пакет с помощью команды:

python3 -m pip install --user git+https://github.com/<user_name>/<repo_name>.git


Установка зависимостей:

pip3 install prompt flake8

Повторная проверка зависимостей:
Проверка зависимостей:

pip3 list

### Запуск
Чтобы запустить утилиту в режиме разработки, выполните команду:

make brain-games


Чтобы запустить brain_calc, выполните команду:

brain-calc


Чтобы запустить brain_even, выполните команду:

brain-even


Чтобы запустить brain_gcd, выполните команду:

brain-gcd


Чтобы запустить brain_prime, выполните команду:

brain-prime


Чтобы запустить brain_progression, выполните команду:

brain-progression

### Создание билда
Чтобы выполнить сборку, выполните команду: 

make build

### Добавление зависимостей
Можно использовать команду:
poetry add prompt

Что сразу же добавит данную зависимость в:
[tool.poetry.dependencies]
python = "^3.11"
prompt = "^0.4.1"  # сюда

### Установка
Чтобы выполнить установку пакета, выполните команду: 

make package-install

### FAQ
Как проверить работают ли игры? poetry run(впишите сюда название игры из папки games)  
Можно ли в brain-calc ввести два операнда, например * и + ? Я вам запрещаю вводить более 1-го операнда  
Как понять праймовое ли число? Прайм число делится только на само себя и на единицу (можете проверить свои силы введя в терминале brain-prime)

### To do
1. Добавить крутое README  
2.Всё переписать  
3. ...  
4. Проработать логику игр и сократить код  
5. Создать файл-скрипт для запуска игр по форме "одна за одной"

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

brain-gcd test: [![asciicast](https://asciinema.org/a/uZKjLWawlnemQAryBoj1A5tbS.svg)](https://asciinema.org/a/uZKjLWawlnemQAryBoj1A5tbS)

brain-progression test: [![asciicast](https://asciinema.org/a/yJqAKB9m7DJ2cQB0oZSgGgz4k.svg)](https://asciinema.org/a/yJqAKB9m7DJ2cQB0oZSgGgz4k)

brain-prime test: [![asciicast](https://asciinema.org/a/yJqAKB9m7DJ2cQB0oZSgGgz4k.svg)](https://asciinema.org/a/yJqAKB9m7DJ2cQB0oZSgGgz4k)
