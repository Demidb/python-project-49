### Hexlet tests and linter status:
[![Actions Status](https://github.com/Demidb/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Demidb/python-project-49/actions)
<a href="https://codeclimate.com/github/Demidb/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/522cd74e06f4ba19bd53/maintainability" /></a> 

Python-project-49
Проект направлен на оттачивание навыков, полученных разработчиком во время прохождения модулей перед 1-м проектом. Проект закрепляет знания в pip, poetry, а также навыков создания виртуального окружения.
Статус проекта: завершен
Статус билда: завершен

## Содержание
- [Технологии](#технологии)
- [Начало работы](10-10-2023)
- [Тестирование](05-01-2023)
- [Команда проекта/Автор](Demid Alexeev)

## Технологии
- [Python 3.10](https://www.python.org/)
- [Prompt](https://pypi.org/project/prompt/)
- [flake8] (https://flake8.pycqa.org/en/latest/)

## Разработка и Использование
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


### Установка
Чтобы выполнить установку пакета, выполните команду: 

make package-install

## Команда проекта
Автор:

- [Имя фамилия](https://<ссылка на любой контакт>) — Python developer

## Источники


| Название источника | Значение/пояснение |
|--------------------|--------------------|
| 1  Марк Лутц       | В его книге  "Изучаем Python "  были продемонстрированы интересные функции, 
                         которые мотировали встать с дивана и идти тестировать их    |     |

Тесты

brain-even test:  https://asciinema.org/a/uN4r5k0adWDkM8Pd7zdLTC465

brain-calc test: https://asciinema.org/a/0Q41SHJZqXHSDSG8kYbl6aNwk

brain-gcd test: https://asciinema.org/a/iUxAaPbKWFHfF1B5NnuQ8gmcd

brain-progression test: https://asciinema.org/a/P1Hg9MHKbXULw3h7h6X5GZuKc

brain-prime test: https://asciinema.org/a/19JJpE6UrRleI4VQnVPLO8UPU