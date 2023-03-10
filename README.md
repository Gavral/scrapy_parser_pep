# Проект «Scrapy_parser_pep - асинхронный парсер PEP» 

## Стек технологий:
- [Python](https://www.python.org/); 
- [Scrapy](https://scrapy.org/).

## Как установить и запустить
1. Клонировать репозиторий к себе на компьютер:

```bash
git clone git@github.com:Gavral/scrapy_parser_pep.git
```
2. Cоздать и активировать виртуальное окружение:

```
python -m venv venv
source venv/Scripts/activate
```
3. Установить зависимости из файла requirements.txt, который лежит в корне проекта:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Запуск парсера:
```
scrapy crawl pep
```

## Результаты работы парсера:
Парсер выводит собранную информацию в два файла .csv:

- В первом файле - список всех PEP: номер, название и статус.
  
- Во втором файле - содержится сводка по статусам PEP — 
  сколько найдено документов в каждом статусе (статус, количество) и общее количество всех документов.

## Автор
Гаврилов Александр

gavrilov-al@mail.ru